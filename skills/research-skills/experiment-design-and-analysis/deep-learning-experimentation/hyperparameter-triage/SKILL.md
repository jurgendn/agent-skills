---
name: hyperparameter-triage
description: Prioritize which hyperparameters matter most for the current failure mode or objective. Use for tuning, debugging, compute-constrained experimentation, unstable runs, underperformance, or when sweeping everything would waste compute.
---

# Hyperparameter Triage

Tune the few knobs that are actually plausible culprits.

## Intake

Establish:
- target metric and failure mode;
- current config and compute budget;
- training curves and validation behavior;
- known-good baseline settings;
- which knobs have already been tried.

## Workflow

1. State the objective and failure mode.
2. List high-impact candidate hyperparameters.
3. Classify knobs by mechanism: optimization, regularization, capacity, data/sampling, schedule.
4. Rank them by expected leverage and interaction risk.
5. Propose a minimal search plan.
6. Define stop conditions for continuing or abandoning the sweep.

## Rules

- Prefer informed local sweeps over blind grid search.
- Document what was held fixed.
- Change one mechanism at a time unless testing an interaction deliberately.
- If curves imply a data or implementation bug, route to `data-pipeline-auditor` or `training-run-forensics` before tuning.

## Output

Return:
- failure diagnosis;
- ranked hyperparameters with rationale;
- minimal sweep table;
- fixed controls;
- stop/continue criteria.
