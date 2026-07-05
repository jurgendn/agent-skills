---
name: data-pipeline-auditor
description: Check preprocessing, splits, leakage, augmentation, label noise, and distribution mismatch before blaming the model. Use for new datasets, suspicious gains, brittle generalization, unexplained train-test gaps, or any result that may be caused by data pipeline bugs rather than model behavior.
---

# Data Pipeline Auditor

Assume the data pipeline can break the result.

## Intake

Ask for or infer:
- dataset source and construction process;
- split logic and any filtering;
- preprocessing/tokenization/normalization;
- augmentation and sampling;
- label source and ambiguity;
- train/validation/test metrics and surprising patterns.

## Workflow

1. Inspect dataset creation and splits.
2. Check leakage, duplicates, and contamination.
3. Verify label semantics and preprocessing.
4. Examine augmentation and sampling effects.
5. Identify likely train-test mismatch.
6. Rank suspected bugs by likelihood and impact.
7. Recommend targeted fixes or diagnostics.

## Rules

- Suspicious gains deserve extra leakage checks.
- Data bugs count as findings.
- Do not call a model brittle until the data path has been checked.
- Separate confirmed leakage from plausible leakage.

## Output

Return:
- pipeline map;
- confirmed risks;
- likely risks needing checks;
- highest-value diagnostics;
- fixes that would change the paper's claim or evaluation.
