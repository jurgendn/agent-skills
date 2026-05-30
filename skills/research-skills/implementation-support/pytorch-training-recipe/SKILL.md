---
name: pytorch-training-recipe
description: Produce an implementable PyTorch or PyTorch Lightning training recipe with dataset handling, optimization, logging, checkpointing, and debugging checks. Use when turning a paper idea into runnable training code.
when_to_use: Use for new experiments, reproductions, fine-tuning, scaling recipes, and debugging unstable training.
---

# PyTorch Training Recipe

Translate the idea into a runnable and debuggable training plan.

The goal is not to mirror a paper blindly.  
The goal is to create a training setup that can fail loudly, debug quickly, and scale only after correctness is verified.

---

# Procedure

## 1. Specify the Experiment

Define the experiment before writing training code.

Include:
- task type;
- dataset;
- model family;
- input and target format;
- loss function;
- evaluation protocol.

Example:
```text
Task:
Node classification on a call graph.

Dataset:
Masked telecom call graph with node labels.

Model:
GraphSAGE / GAT / GCN baseline.

Objective:
Cross-entropy loss over labeled nodes.

Evaluation:
Macro-F1, weighted-F1, confusion matrix, and per-class recall.
```

---

## 2. Define the Data Pipeline

Specify:
- dataset loading;
- preprocessing;
- train/validation/test split;
- batching strategy;
- transforms;
- caching;
- leakage checks.

For graph learning, explicitly define:
- whether the graph is transductive or inductive;
- whether labels are visible only through masks;
- whether edges cross train/test partitions;
- whether negative sampling is needed.

Example:
```text
Data pipeline:
- load graph edges and node labels;
- map raw node IDs to contiguous integer IDs;
- build PyG Data object;
- attach x, edge_index, y, train_mask, val_mask, test_mask;
- verify that every labeled node has a valid mask assignment.
```

---

## 3. Choose the Training Stack

Use the simplest stack that supports the experiment.

Recommended default:
```text
Framework:
PyTorch Lightning for training loop structure.

Core libraries:
PyTorch, PyTorch Geometric, TorchMetrics.

Logging:
CSVLogger or MLflowLogger.

Checkpointing:
save best checkpoint by validation metric.
```

Avoid distributed training until the single-device run is correct.

---

## 4. Set Optimization Choices

State each choice and whether it is justified or uncertain.

Example:
```text
Optimizer:
AdamW

Learning rate:
1e-3 as first default; tune later if unstable.

Weight decay:
1e-4 for regularization.

Scheduler:
ReduceLROnPlateau if validation metric stalls.

Gradient clipping:
1.0 if gradients explode.

Precision:
32-bit for debugging; mixed precision only after correctness is verified.
```

Do not copy paper hyperparameters without saying they are copied defaults.

---

## 5. Add First-Run Safety Checks

Before the real run, require:

```text
Shape checks:
- logits shape matches [num_nodes, num_classes] or [batch_size, num_classes];
- labels are integer class IDs;
- masks are boolean and non-empty.

Loss checks:
- initial loss is finite;
- loss decreases on a tiny subset;
- no NaNs or infs appear.

Data checks:
- class distribution is printed;
- train/validation/test split sizes are printed;
- no unlabeled node is accidentally used for supervised loss.

Overfit test:
- train on a tiny subset until near-perfect training accuracy.
```

Failure to overfit a tiny batch usually means:
- label bug;
- model-output mismatch;
- optimizer issue;
- wrong mask;
- broken loss computation.

---

## 6. Define Metrics

Separate training loss from evaluation metrics.

Example:
```text
Training:
cross-entropy loss.

Validation:
macro-F1 for model selection.

Test:
macro-F1, weighted-F1, accuracy, confusion matrix.
```

For imbalanced data, do not rely only on accuracy.

---

## 7. Define Logging and Checkpointing

Minimum logging:
- train loss;
- validation loss;
- validation primary metric;
- learning rate;
- epoch time;
- seed;
- dataset version;
- config file.

Minimum checkpointing:
```text
Save:
- best validation checkpoint;
- last checkpoint;
- final config;
- test metrics from best checkpoint.
```

---

## 8. Flag Likely Failure Modes

Common PyTorch/PyG failure modes:

```text
NaNs:
Usually caused by too high learning rate, unstable normalization, or bad inputs.

Exploding gradients:
Use gradient clipping and inspect gradient norms.

Dead data loader:
Check num_workers, pinned memory, and dataset __getitem__.

Label bugs:
Verify label range is [0, num_classes - 1].

Metric mismatch:
Confirm logits, probabilities, and class IDs are passed correctly.

Mask bugs:
Check that train_mask, val_mask, and test_mask are disjoint.

Graph leakage:
For inductive tasks, ensure test nodes or future edges are not used during training.
```

---

## 9. Recommend a Staged Rollout

Run in this order:

```text
1. CPU or single-GPU smoke test
2. overfit tiny batch
3. one full epoch on small subset
4. single-seed full run
5. three-seed benchmark
6. hyperparameter tuning
7. mixed precision or distributed training
```

Do not start with a full-scale run.

---

# Rules

- Prefer recipes executable within one week.
- Keep the first implementation simple.
- Distinguish justified choices from uncertain defaults.
- Do not scale before correctness checks pass.
- Do not hide unstable training behind averaged metrics.
- If a hyperparameter is uncertain, mark it as uncertain.
- Use typed configs when possible.
- Save enough metadata to reproduce the run.

---

# Output Format

```text
# Training Recipe

Task:
State the supervised, self-supervised, generative, or RL task.

Dataset:
State source, format, split protocol, and leakage risks.

Model:
State architecture family and minimal variant.

Objective:
State loss function and target format.

Evaluation:
State validation and test metrics.

# Minimal Config

framework:
  pytorch_lightning: true

training:
  max_epochs: 100
  batch_size: 64
  optimizer: AdamW
  learning_rate: 1e-3
  weight_decay: 1e-4
  precision: 32
  gradient_clip_val: 1.0

checkpointing:
  monitor: val_macro_f1
  mode: max
  save_best: true
  save_last: true

logging:
  logger: csv_or_mlflow
  log_every_n_steps: 10

# First-Run Checks

- Verify tensor shapes.
- Verify label range.
- Verify masks or split indices.
- Print class distribution.
- Run overfit-small-batch test.
- Confirm validation metric is computed on validation data only.

# Failure Modes

- NaNs from unstable optimization.
- Exploding gradients.
- Incorrect label encoding.
- Broken masks.
- Data leakage.
- Dead or slow data loader.
- Metric computed with wrong tensor format.

# Scale-Up Plan

1. Smoke test locally.
2. Overfit tiny subset.
3. Run small benchmark.
4. Run full single-seed experiment.
5. Run multi-seed experiment.
6. Tune hyperparameters.
7. Enable mixed precision or distributed training only after stable results.
```