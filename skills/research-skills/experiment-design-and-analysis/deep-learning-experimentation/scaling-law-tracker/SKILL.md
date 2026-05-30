---
name: scaling-law-tracker
description: Track how performance changes with data, model size, batch size, or compute to guide resource allocation. Use when deciding where more compute will matter.
when_to_use: Use for planning larger runs and understanding diminishing returns.
---

# Scaling Law Tracker

Measure whether more scale is buying the right thing.

## Workflow

1. Define the scaling axis and metric.
2. Collect comparable runs.
3. Plot performance against resource use.
4. Identify diminishing returns and breakpoints.
5. Recommend whether to scale data, model, or optimization next.

## Rules

- Do not compare incomparable training setups.
- State uncertainty if the run set is sparse.
