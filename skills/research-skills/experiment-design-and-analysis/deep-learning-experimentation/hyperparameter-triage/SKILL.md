---
name: hyperparameter-triage
description: Prioritize which hyperparameters matter most for the current failure mode or objective. Use when sweeping everything would waste compute.
when_to_use: Use for tuning, debugging, and compute-constrained experimentation.
---

# Hyperparameter Triage

Tune the few knobs that are actually plausible culprits.

## Workflow

1. State the objective and failure mode.
2. List high-impact candidate hyperparameters.
3. Rank them by expected leverage.
4. Propose a minimal search plan.
5. Define stop conditions for continuing or abandoning the sweep.

## Rules

- Prefer informed local sweeps over blind grid search.
- Document what was held fixed.
