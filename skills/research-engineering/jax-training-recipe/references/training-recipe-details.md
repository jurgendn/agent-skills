# JAX Training Recipe Details

Use this reference for concrete JAX/Flax/Optax training-plan details.

## Minimal Config Fields

```yaml
seed: 42
dataset:
  name:
  split:
model:
  name:
  hidden_dim:
training:
  optimizer: adamw
  learning_rate:
  batch_size:
  max_steps:
  weight_decay:
  grad_clip:
evaluation:
  metric:
  frequency:
logging:
  output_dir:
  save_every:
```

## First-Run Checks

1. One batch initializes params and state.
2. Loss is finite before `jit`.
3. Gradients are nonzero and finite.
4. Parameters update after one Optax step.
5. Tiny batch can overfit.
6. The same seed reproduces the same run.

## JAX-Specific Checks

- PRNG keys are split before every stochastic operation.
- `params`, `batch_stats`, optimizer state, and RNG state are explicit.
- The un-jitted step works before adding `jit`.
- `vmap` and `pmap` are added only after single-device behavior is correct.
- Checkpoint restore reproduces model, optimizer, and mutable state.

## Staged Rollout

1. CPU/single batch smoke test.
2. Un-jitted tiny subset overfit.
3. Jitted small validation run.
4. Baseline reproduction.
5. Full single-device run.
6. Multi-seed run.
7. `pmap`/multi-device run only after correctness is stable.
