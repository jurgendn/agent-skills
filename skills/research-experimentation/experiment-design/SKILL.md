---
name: experiment-design
description: >-
  Design a minimal, decision-relevant experiment with fair baselines, explicit controls, and measurable success criteria — and diagnose a training run that has already gone wrong. Use before large-scale implementation or expensive training (benchmarking, hyperparameter sweeps, large-model training, or whenever a research claim requires rigorous empirical validation), and also when a run misbehaves — "my loss diverged", "training collapsed", "the model won't overfit a tiny batch", "these gains look too good", "is this data leakage", "which hyperparameter should I try next", "how do I summarize these runs into a decision", or "is more data/compute still buying anything" (fit that with the bundled scripts/fit_scaling_law.py rather than eyeballing a log-log plot).
---

# Experiment Design

Design the smallest experiment that can meaningfully reduce uncertainty. The
goal is not maximum benchmark performance; it is to decide whether the claimed
mechanism works.

For detailed checklists, read `references/experiment-design-checklist.md`.

## Workflow

1. State the hypothesis in falsifiable form.
2. Define the minimal experiment that can test it.
3. Define fair baselines.
4. Define primary and secondary metrics.
5. Identify confounders and controls.
6. Add mandatory sanity checks.
7. Define decision criteria before running.
8. Recommend run order from cheapest to most expensive.

## Required Design Fields

- **Hypothesis:** what changes, compared to what, under which condition, measured how.
- **Dataset/environment:** source, split, leakage prevention, sample size.
- **Intervention:** what the proposed method changes and what stays fixed.
- **Baselines:** strongest fair comparison plus simple floor.
- **Metrics:** primary metric tied to claim; secondary metrics for tradeoffs.
- **Confounders:** compute, parameters, data leakage, preprocessing, prompt/template effects.
- **Decision criteria:** pursue / revise / stop thresholds.

## Sanity Checks

- Overfit a tiny batch or trivial case.
- Verify metric implementation.
- Check seed stability where stochasticity matters.
- Confirm baseline reproduces known behavior.
- Inspect representative successes and failures.

## When the run goes wrong

Design covers the run you plan; this covers the run that already misbehaved.
The ordering rule matters more than the checklist: **check the data path before
blaming the model, and classify the symptom before touching a hyperparameter.**

1. **Classify the symptom** — divergence, overfitting, underfitting, collapse,
   dead training, or noisy validation. A curve shape is not a diagnosis until
   it is matched against the config and the data.
2. **Audit the data path first.** Splits, duplicates, contamination, label
   semantics, preprocessing, augmentation, train/test mismatch. Suspicious
   *gains* deserve leakage checks more than suspicious losses do — a result
   that looks too good usually is. Separate confirmed leakage from plausible
   leakage.
3. **Only then tune**, and tune by mechanism — optimization, regularization,
   capacity, data/sampling, schedule — changing one mechanism at a time.
   Prefer an informed local sweep to a blind grid.
4. **Record provenance for every number you keep.** Do not merge runs with
   different configs into one conclusion, and mark impressions as impressions
   until a run backs them.

### Scaling questions

When the question is whether *more* (data, parameters, compute) is buying the
right thing, fit it rather than eyeballing a log-log plot.
`scripts/fit_scaling_law.py` fits a power law and the power-law-with-floor
(Kaplan/Chinchilla) form, reports exponent and R², extrapolates, and flags the
diminishing-returns knee:

```bash
python scripts/fit_scaling_law.py \
  --x 1e6 2e6 4e6 8e6 1.6e7 --y 3.10 2.84 2.63 2.48 2.37 \
  --metric "val loss" --lower-better --extrapolate 6.4e7
python scripts/fit_scaling_law.py selftest   # verify the install
```

Vary one axis at a time, keep the architecture family and eval fixed, and treat
any extrapolation beyond ~10× your largest run as a hypothesis to test with one
larger run — not a measured result. Below R² ≈ 0.9, say the power law may not
hold and do not extrapolate far.

## Rules

- A big experiment without a decision rule is not designed.
- A baseline must be strong enough that beating it means something.
- Do not use validation results to define the test claim after the fact.
- If the experiment cannot falsify the hypothesis, redesign it.
- Do not call a model brittle until the data path has been checked.
- Do not shotgun hyperparameters; separate symptom from cause first.

## Output

Return:
- hypothesis;
- minimal experiment;
- baselines;
- metrics;
- risks/confounders;
- sanity checks;
- run order;
- decision criteria;
- scope limits.
