---
name: latency-quality-tradeoff-optimizer
description: Compare model, decoding, caching, and routing choices against quality, latency, and cost. Use when a system must be practical, not just accurate.
when_to_use: Use for deployment decisions and iterative product tuning.
---

# Latency Quality Tradeoff Optimizer

Find the cheapest configuration that still wins where it matters.

## Workflow

1. Define quality floor and latency/cost constraints.
2. Compare candidate configurations fairly.
3. Report Pareto-efficient options.
4. Identify where smaller/faster options fail.
5. Recommend configuration by use case, not one-size-fits-all.

## Rules

- Average quality alone is not enough.
- State the measurement setup clearly.
