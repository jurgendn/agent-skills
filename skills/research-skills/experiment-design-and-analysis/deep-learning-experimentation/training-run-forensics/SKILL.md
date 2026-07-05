---
name: training-run-forensics
description: Diagnose unstable or underperforming training runs from logs, curves, configs, and samples. Use when a run diverges, plateaus, collapses, overfits, underfits, behaves strangely, or needs debugging across optimization, regularization, and data pathologies.
---

# Training Run Forensics

Treat the run as evidence.

## Intake

Ask for:
- loss/metric curves;
- optimizer, learning rate schedule, batch size, precision, regularization;
- train/validation samples or predictions;
- recent code/data changes;
- hardware/distributed setup if relevant.

## Workflow

1. Gather curves, configs, sample outputs, and recent code changes.
2. Classify the symptom: divergence, overfitting, underfitting, collapse, dead training, noisy validation.
3. Generate a shortlist of likely causes.
4. Identify the smallest discriminating checks.
5. Prioritize fixes by probability and cost.
6. State which checks should run before any new sweep.

## Rules

- Do not shotgun hyperparameters blindly.
- Separate symptom from cause.
- A curve shape is not a diagnosis until matched against config and data evidence.
- If the symptom points to leakage or split mismatch, route to `data-pipeline-auditor`.

## Output

Return:
- symptom classification;
- likely causes;
- discriminating checks;
- fix order;
- what evidence would falsify the diagnosis.
