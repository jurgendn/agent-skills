---
name: experiment-design
description: Design a minimal, decision-relevant experiment with fair baselines, explicit controls, and measurable success criteria. Use before large-scale implementation or expensive training — including before benchmarking, hyperparameter sweeps, large-model training, or whenever a research claim requires rigorous empirical validation.
---

# Experiment Design

Design the smallest experiment that can meaningfully reduce uncertainty.

The goal is not to maximize benchmark numbers.  
The goal is to determine whether the claimed mechanism actually works.

---

# Procedure

## 1. State the Hypothesis

Write the claim in falsifiable form.

Bad:
```text
Our method improves graph learning.
```

Better:
```text
Adaptive random-walk length based on spectral gap improves ONMI
over fixed walk-length baselines in dynamic community detection.
```

The hypothesis should specify:
- what changes;
- compared against what;
- under which conditions;
- measured by which metric.

---

## 2. Define the Minimal Experiment

Specify the smallest setup capable of testing the hypothesis.

### Dataset / Environment

State:
- dataset name;
- synthetic or real-world;
- task type;
- graph size or sample size;
- relevant constraints.

Example:
```text
Dataset:
Dynamic LFR benchmark with controlled overlap and fragmentation.
```

### Split Protocol

Explicitly define:
- train / validation / test split;
- temporal split if applicable;
- leakage prevention.

Example:
```text
Train:
first 60% of snapshots

Validation:
next 20%

Test:
final 20%

No future edges visible during training.
```

### Intervention

Describe exactly what changes.

Bad:
```text
Use our method.
```

Better:
```text
Replace fixed walk length t=5 with adaptive
t selected from estimated mixing time.
```

### Compute Budget

Record:
- GPU/CPU budget;
- wall-clock limit;
- number of seeds;
- search budget.

Example:
```text
3 random seeds
Single RTX 4090
Maximum training time: 6 hours
```

---

## 3. Define Fair Baselines

Baselines must be:
- competitive;
- properly tuned;
- compute-matched where possible.

Weak baseline selection invalidates conclusions.

Example:
```text
Baselines:
- Static Louvain
- DF-Louvain
- RW refinement with fixed t
- Spectral clustering
```

Also define:
- which hyperparameters are tuned;
- whether all methods receive equal search budget.

---

## 4. Define Metrics

Separate:
- primary metric;
- secondary diagnostics.

Example:
```text
Primary:
ONMI

Secondary:
Modularity
Runtime
Community fragmentation rate
```

If metrics can disagree, state this explicitly.

---

## 5. Identify Confounders

List alternative explanations for the result.

Common confounders:
- data leakage;
- larger parameter count;
- longer training;
- larger receptive field;
- preprocessing artifacts;
- seed sensitivity;
- prompt contamination;
- hidden filtering effects.

Example:
```text
Potential confounder:
Adaptive walk length may simply increase effective neighborhood size,
not improve mixing-time alignment.
```

---

## 6. Add Mandatory Sanity Checks

Before scaling, verify correctness.

### Overfit-Small-Batch Test

The model should overfit a tiny subset.

Failure here usually indicates:
- implementation bug;
- metric issue;
- optimization failure.

### Metric Verification

Manually verify:
- metric direction;
- normalization;
- averaging logic;
- edge-case behavior.

### Seed Stability

Run at least 3 seeds for unstable systems.

Large variance may invalidate small gains.

---

## 7. Define Decision Criteria

Specify what outcome changes the conclusion.

| Result | Interpretation |
|---|---|
| Large, stable improvement across seeds | Supports hypothesis |
| Small gain within variance | Likely null result |
| Gain disappears under fair tuning | Baseline unfairness |
| Improvement only on one dataset | Weak generalization |
| Higher accuracy but extreme runtime | Tradeoff, not clear win |
| Regression on controlled benchmarks | Evidence against hypothesis |

Avoid post-hoc reinterpretation.

---

## 8. Recommend Run Order

Run cheapest experiments first.

Example:
```text
1. Verify data pipeline
2. Overfit 1 batch
3. Run baseline sanity benchmark
4. Run toy synthetic dataset
5. Run ablation study
6. Run full benchmark
7. Run multi-seed evaluation
```

Do not scale before correctness is verified.

---

# Rules

- Prefer toy experiments before large-scale sweeps.
- Every experiment should answer a decision-relevant question.
- Baselines must receive fair tuning effort.
- Record what is intentionally not tested.
- Avoid benchmark inflation through hidden compute advantages.
- Small reproducible experiments are more valuable than large noisy ones.

---

# Output Format

## Hypothesis

State the falsifiable claim.

## Minimal Experiment

- Dataset:
- Split protocol:
- Intervention:
- Compute budget:

## Baselines

- Baseline 1:
- Baseline 2:
- Baseline 3:

## Metrics

### Primary
- ...

### Secondary
- ...

## Risks / Confounders

- ...
- ...
- ...

## Sanity Checks

- ...
- ...
- ...

## Run Order

1. ...
2. ...
3. ...

## Decision Criteria

| Outcome | Interpretation |
|---|---|
| ... | ... |

## Scope Limits

Explicitly state:
- what is not being tested;
- assumptions held fixed;
- conclusions that cannot yet be made.