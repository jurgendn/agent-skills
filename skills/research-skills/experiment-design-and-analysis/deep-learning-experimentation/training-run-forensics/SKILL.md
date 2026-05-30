---
name: training-run-forensics
description: Diagnose unstable or underperforming training runs from logs, curves, configs, and samples. Use when a run diverges, plateaus, or behaves strangely.
when_to_use: Use for debugging optimization, regularization, and data pathologies.
---

# Training Run Forensics

Treat the run as evidence.

## Workflow

1. Gather curves, configs, sample outputs, and recent code changes.
2. Classify the symptom: divergence, overfitting, underfitting, collapse, dead training, noisy validation.
3. Generate a shortlist of likely causes.
4. Recommend the smallest discriminating checks.
5. Prioritize fixes by probability and cost.

## Rules

- Do not shotgun hyperparameters blindly.
- Separate symptom from cause.
