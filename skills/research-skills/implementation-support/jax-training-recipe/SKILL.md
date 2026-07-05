---
name: jax-training-recipe
description: Produce an implementable JAX, Flax, and Optax training recipe with explicit PRNG management, pure functions, jit/vmap/pmap usage, gradient computation, Flax state handling, checkpointing, and debugging checks. Use when implementing a model in JAX/Flax, porting from PyTorch, debugging tracing/shape/NaN issues, or designing research code that uses JAX transformations.
---

# JAX Training Recipe

JAX is not PyTorch with different syntax. Functions are pure, state is explicit,
and transformations (`jit`, `vmap`, `grad`, `pmap`) compose only when the function
boundaries are clean.

For concrete config/checklist details, read `references/training-recipe-details.md`.

## Intake

Specify:
- task, dataset, loss, and metric;
- target device: CPU, single GPU, multi-GPU, TPU;
- model framework: Flax/Linen, Equinox, or raw JAX;
- randomness needs: dropout, sampling, augmentation;
- state needs: batch norm, optimizer state, EMA, checkpointing.

## Workflow

1. Define the experiment and minimal data batch.
2. Plan PRNG key ownership and splitting.
3. Define model/state boundaries.
4. Initialize model and optimizer.
5. Write a pure `train_step`.
6. Add `jit` only after the un-jitted step works.
7. Add `vmap`/`pmap` only after single-device behavior is correct.
8. Add checkpointing and restore tests.
9. Run first-run safety checks.
10. Stage rollout from tiny batch to full training.

## JAX-Specific Rules

- Never reuse a PRNG key.
- Keep state explicit; do not hide mutable state in closures.
- Avoid Python side effects inside `jit`.
- Treat shape changes under `jit` as design decisions.
- Debug without `jit` first, then re-enable transformations one at a time.
- Replicate state deliberately for multi-device training.

## Common Failure Modes

- Reused PRNG keys causing repeated dropout/sampling.
- Tracer errors from Python control flow or side effects.
- Batch norm/dropout state not separated from params.
- Shape mismatch under `vmap` or `pmap`.
- NaNs hidden by compiled loops.
- Checkpoints missing optimizer or batch-stat state.

## Output

Return:
- experiment summary;
- PRNG strategy;
- model/state design;
- train/eval step plan;
- minimal config;
- first-run checks;
- JAX-specific failure modes;
- scale-up plan.
