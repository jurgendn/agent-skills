# PyTorch Training Recipe Details

Use this reference for concrete training-plan details.

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

1. One batch passes through the model.
2. Loss is finite.
3. Backward pass produces nonzero gradients.
4. Parameters update after one optimizer step.
5. Tiny batch can overfit.
6. Metric changes in the expected direction.

## Common Failure Modes

- Wrong labels or masks.
- Metric computed on the wrong split.
- Silent dtype/device mismatch.
- Learning rate too high or too low.
- Baseline under-tuned relative to the proposed method.
- Randomness not controlled.
- Checkpoint restores model but not optimizer/scheduler state.

## Staged Rollout

1. CPU/single batch smoke test.
2. Tiny subset overfit.
3. Small validation run.
4. Baseline reproduction.
5. Full run.
6. Multi-seed run.
7. Distributed run only after correctness is stable.
