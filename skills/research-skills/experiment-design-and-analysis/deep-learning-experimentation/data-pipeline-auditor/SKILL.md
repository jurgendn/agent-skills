---
name: data-pipeline-auditor
description: Check preprocessing, splits, leakage, augmentation, label noise, and distribution mismatch. Use before blaming the model.
when_to_use: Use for new datasets, suspicious gains, and brittle generalization.
---

# Data Pipeline Auditor

Assume the data pipeline can break the result.

## Workflow

1. Inspect dataset creation and splits.
2. Check leakage, duplicates, and contamination.
3. Verify label semantics and preprocessing.
4. Examine augmentation and sampling effects.
5. Identify likely train-test mismatch.
6. Recommend targeted fixes or diagnostics.

## Rules

- Suspicious gains deserve extra leakage checks.
- Data bugs count as findings.
