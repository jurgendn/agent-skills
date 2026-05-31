---
name: jax-training-recipe
description: Produce an implementable JAX/Flax/Optax training recipe covering functional programming patterns, random key management, jit/vmap/pmap usage, gradient computation, Flax state management, Orbax checkpointing, and debugging. Use when the user is implementing a model in JAX or Flax, porting a PyTorch model to JAX, debugging JAX-specific errors (tracing errors, unexpected NaNs, shape errors from vmap), or writing research code that uses vmap for batching or pmap for multi-device parallelism. Also use when the user is confused by JAX's functional style, immutability, or PRNG key splitting conventions.
---

# JAX Training Recipe

JAX is not PyTorch with a different syntax. The mental model is different: functions are pure, state is explicit, and transformations (jit, vmap, grad) compose. The recipe is only debuggable if you understand what each transformation does to your function.

The goal is a training loop that is:
- **Reproducible**: keys are deterministic and split explicitly.
- **Correct before fast**: verify on CPU before enabling jit or multi-device.
- **Debuggable**: transformations are layered in, not applied from the start.

---

## 1. Specify the experiment

Before writing any JAX code, state:

```text
Task: [supervised classification / self-supervised / generative / RL]
Dataset: [source, format, split]
Model family: [MLP / CNN / Transformer / GNN / custom]
Loss: [cross-entropy / MSE / contrastive / custom]
Evaluation: [metric, frequency, validation protocol]
Target device: [CPU / single GPU / multi-GPU / TPU]
```

---

## 2. Random key management

This is the most common source of bugs for newcomers. JAX's PRNG is explicit and functional — keys must be split before each use.

```python
import jax
import jax.numpy as jnp

# Initialize once from a seed
key = jax.random.PRNGKey(42)

# Split before every operation that consumes randomness
key, subkey = jax.random.split(key)
params = model.init(subkey, dummy_input)

key, subkey = jax.random.split(key)
dropout_key = subkey  # pass to model.apply at each step
```

Rules:
- Never reuse a key. Once consumed, it produces the same values forever.
- Split a key to get two independent subkeys.
- Pass a fresh subkey into every stochastic call (dropout, sampling, noise).
- Keep the "master" key for the loop; split off a subkey per step.

For reproducibility, pass the key from the command line and save it in the run record.

---

## 3. Model definition with Flax

```python
import flax.linen as nn

class MyModel(nn.Module):
    hidden_dim: int
    num_classes: int

    @nn.compact
    def __call__(self, x, training: bool = False):
        x = nn.Dense(self.hidden_dim)(x)
        x = nn.relu(x)
        x = nn.Dropout(rate=0.1, deterministic=not training)(x)
        x = nn.Dense(self.num_classes)(x)
        return x
```

Key Flax concepts:
- `@nn.compact`: define layers inline inside `__call__`. Parameters are created on first call.
- `training` flag: pass explicitly; don't use global state.
- `nn.Module` instances are immutable. Parameters live in `variables`, not in the module.

---

## 4. Initialize model and optimizer

```python
import optax

model = MyModel(hidden_dim=256, num_classes=10)

# Initialize parameters
key, init_key = jax.random.split(key)
dummy_input = jnp.ones((1, input_dim))
variables = model.init(init_key, dummy_input)
params = variables['params']

# Optimizer
optimizer = optax.adamw(learning_rate=1e-3, weight_decay=1e-4)
opt_state = optimizer.init(params)
```

If using batch normalization or other stateful layers:
```python
# variables contains both 'params' and 'batch_stats'
params = variables['params']
batch_stats = variables['batch_stats']
```

---

## 5. Training step (pure function, jit-compiled)

The training step must be a pure function — no side effects, no global mutation.

```python
import functools

@functools.partial(jax.jit, static_argnames=('training',))
def train_step(params, opt_state, batch, key, training=True):
    x, y = batch

    def loss_fn(params):
        key_drop, = jax.random.split(key, 1)  # split for dropout
        logits = model.apply(
            {'params': params},
            x,
            training=training,
            rngs={'dropout': key_drop}
        )
        loss = optax.softmax_cross_entropy_with_integer_labels(logits, y).mean()
        return loss, logits

    (loss, logits), grads = jax.value_and_grad(loss_fn, has_aux=True)(params)
    updates, opt_state = optimizer.update(grads, opt_state, params)
    params = optax.apply_updates(params, updates)

    accuracy = (jnp.argmax(logits, axis=-1) == y).mean()
    return params, opt_state, {'loss': loss, 'accuracy': accuracy}
```

Why `jax.value_and_grad` with `has_aux=True`: compute loss and auxiliary outputs (logits) in one pass without redundant forward calls.

---

## 6. Evaluation step

```python
@jax.jit
def eval_step(params, batch):
    x, y = batch
    logits = model.apply({'params': params}, x, training=False)
    loss = optax.softmax_cross_entropy_with_integer_labels(logits, y).mean()
    accuracy = (jnp.argmax(logits, axis=-1) == y).mean()
    return {'loss': loss, 'accuracy': accuracy}
```

Evaluation is always `training=False`. No key needed if no stochastic operations.

---

## 7. Training loop

```python
import numpy as np

for epoch in range(num_epochs):
    # Training
    train_metrics = []
    for batch in train_loader:
        key, step_key = jax.random.split(key)
        params, opt_state, metrics = train_step(
            params, opt_state, batch, step_key
        )
        train_metrics.append(metrics)

    # Aggregate
    train_loss = np.mean([m['loss'] for m in train_metrics])
    train_acc = np.mean([m['accuracy'] for m in train_metrics])

    # Validation
    val_metrics = []
    for batch in val_loader:
        metrics = eval_step(params, batch)
        val_metrics.append(metrics)

    val_loss = np.mean([m['loss'] for m in val_metrics])
    val_acc = np.mean([m['accuracy'] for m in val_metrics])

    print(f"Epoch {epoch}: train_loss={train_loss:.4f}, val_acc={val_acc:.4f}")
```

---

## 8. Checkpointing with Orbax

```python
import orbax.checkpoint as ocp

checkpointer = ocp.StandardCheckpointer()
checkpoint_dir = '/path/to/checkpoints'

# Save
checkpointer.save(
    f'{checkpoint_dir}/epoch_{epoch}',
    {'params': params, 'opt_state': opt_state}
)

# Load
restored = checkpointer.restore(
    f'{checkpoint_dir}/epoch_{epoch}',
    target={'params': params, 'opt_state': opt_state}
)
params = restored['params']
opt_state = restored['opt_state']
```

Save on best validation metric. Save the last checkpoint separately for resumption.

---

## 9. Vectorization with vmap

`vmap` transforms a function that operates on a single example into one that operates on a batch — without writing explicit batch dimensions.

```python
# Single-example forward pass
def forward_single(params, x):
    return model.apply({'params': params}, x[None])[0]  # add/remove batch dim

# Batched forward pass via vmap
forward_batch = jax.vmap(forward_single, in_axes=(None, 0))
logits = forward_batch(params, x_batch)
```

Use vmap for:
- Per-sample gradient computation (useful for influence functions, DP-SGD).
- Batching over tasks (meta-learning).
- Batching over ensemble members.

---

## 10. Multi-device with pmap

```python
# Replicate state across devices
params_rep = jax.device_put_replicated(params, jax.devices())
opt_state_rep = jax.device_put_replicated(opt_state, jax.devices())

@functools.partial(jax.pmap, axis_name='batch')
def train_step_parallel(params, opt_state, batch, key):
    # Same as train_step, but gradients are averaged across devices
    def loss_fn(params):
        logits = model.apply({'params': params}, batch[0], training=True)
        loss = optax.softmax_cross_entropy_with_integer_labels(logits, batch[1]).mean()
        return loss

    loss, grads = jax.value_and_grad(loss_fn)(params)
    grads = jax.lax.pmean(grads, axis_name='batch')  # synchronize gradients
    loss = jax.lax.pmean(loss, axis_name='batch')

    updates, opt_state = optimizer.update(grads, opt_state, params)
    params = optax.apply_updates(params, updates)
    return params, opt_state, loss
```

Don't use pmap until the single-device run is correct. The debugging surface area increases significantly.

---

## 11. First-run safety checks

Before the full training run, verify:

```python
# 1. Shape check
dummy_input = jnp.ones((batch_size, input_dim))
logits = model.apply({'params': params}, dummy_input, training=False)
assert logits.shape == (batch_size, num_classes), f"Got {logits.shape}"

# 2. Loss is finite at init
loss, _ = jax.value_and_grad(loss_fn)(params)
assert jnp.isfinite(loss), "Loss is NaN or inf at initialization"

# 3. Overfit a single batch
single_batch = next(iter(train_loader))
for _ in range(200):
    key, step_key = jax.random.split(key)
    params, opt_state, metrics = train_step(params, opt_state, single_batch, step_key)
assert metrics['accuracy'] > 0.95, "Failed to overfit single batch"
```

---

## 12. Common JAX failure modes

**`jit` tracing errors with Python control flow**
`if x > 0:` inside a jit-compiled function will trace only one branch. Use `jax.lax.cond` for data-dependent branching, or move the condition outside jit.

**Shape errors from vmap**
vmap maps over one axis. If your function expects `(batch, seq, dim)` and you vmap over `(N, batch, seq, dim)`, you get unexpected shapes. Print shapes at each step before applying vmap.

**NaN from unstable initialization**
Use `jax.nn.initializers.lecun_normal()` or `glorot_uniform()`. Check loss at step 0. Gradient clipping: `optax.clip_by_global_norm(1.0)`.

**Slow compilation**
`jax.jit` traces and compiles on the first call. Subsequent calls use the compiled version. Don't time the first call; time the average of subsequent calls.

**Stale keys**
Reusing a key gives identical "random" values. Always split before use.

**pmap axis mismatch**
Batch size must be divisible by number of devices. Add padding if needed.

---

## 13. Staged rollout

```
1. CPU, no jit — verify shapes and loss direction
2. Add jit — check compiled output matches non-jit output
3. Overfit single batch
4. Single-seed full run on one device
5. Add vmap if needed — verify output matches looped version
6. Add pmap for multi-device — verify loss matches single-device
7. Three-seed benchmark
```

---

## Output format

```text
# JAX Training Recipe

Task: [task]
Dataset: [dataset]
Model: [architecture]
Objective: [loss]
Evaluation: [metric]
Target device: [CPU / GPU / TPU / multi-GPU]

# PRNG strategy
[How keys are initialized, split, and passed through the loop]

# Model definition
[Flax module, noting stateful layers]

# Training step
[Pure function signature, jit decoration, grad computation]

# Minimal config
optimizer: adamw
learning_rate: 1e-3
weight_decay: 1e-4
gradient_clip: 1.0
batch_size: 64
max_epochs: 100

# First-run checks
- Shape verification
- Loss finite at init
- Overfit single batch

# Failure modes to watch
[Specific to the model and task]

# Scale-up plan
1. CPU no-jit → 2. jit → 3. overfit → 4. single seed → 5. vmap/pmap → 6. multi-seed
```
