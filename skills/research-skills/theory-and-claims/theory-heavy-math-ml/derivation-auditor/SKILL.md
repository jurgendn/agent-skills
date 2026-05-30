---
name: derivation-auditor
description: Check algebra, calculus, probability, linear algebra, and asymptotic steps line by line. Use when a derivation must be trusted, cited, or reused.
when_to_use: Use for appendices, proof details, optimization derivations, and mathematical debugging.
---

# Derivation Auditor

Check each transformation, not just the endpoints.

## Workflow

1. Rewrite the derivation step by step.
2. For each step, justify the rule used.
3. Flag silent assumptions such as differentiability, invertibility, exchange of limits, or independence.
4. Verify dimensions, domains, signs, and constants.
5. Mark the first invalid or unproven step exactly.

## Rules

- Do not skip steps that are essential to the argument, even if they seem obvious.
- If a derivation is only heuristic, explicitly label it as heuristic.