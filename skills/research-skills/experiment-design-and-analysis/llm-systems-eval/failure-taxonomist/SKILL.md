---
name: failure-taxonomist
description: Cluster model failures into actionable categories such as retrieval miss, reasoning slip, calibration failure, or formatting brittleness. Use after running evaluations.
when_to_use: Use when average metrics hide qualitatively different errors.
---

# Failure Taxonomist

Turn messy errors into a useful map.

## Workflow

1. Inspect failures directly.
2. Group them into a small taxonomy.
3. Separate model failures, tool failures, data issues, and evaluator bugs.
4. Estimate frequency and severity for each category.
5. Recommend the highest-leverage fix per category.

## Rules

- Keep categories causal and actionable.
- Merge redundant buckets.
