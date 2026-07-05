---
name: experiment-design
description: Design a minimal, decision-relevant experiment with fair baselines, explicit controls, and measurable success criteria. Use before large-scale implementation or expensive training — including before benchmarking, hyperparameter sweeps, large-model training, or whenever a research claim requires rigorous empirical validation.
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

## Rules

- A big experiment without a decision rule is not designed.
- A baseline must be strong enough that beating it means something.
- Do not use validation results to define the test claim after the fact.
- If the experiment cannot falsify the hypothesis, redesign it.

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
