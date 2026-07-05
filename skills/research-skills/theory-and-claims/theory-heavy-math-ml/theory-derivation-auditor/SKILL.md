---
name: theory-derivation-auditor
description: Check algebra, calculus, probability, linear algebra, and asymptotic steps line by line. Use for appendices, proof details, optimization derivations, mathematical debugging, or whenever a derivation must be trusted, cited, reused, or used as a load-bearing step.
---

# Derivation Auditor

Check each transformation, not just the endpoints.

## Workflow

1. Rewrite the derivation step by step.
2. For each step, justify the rule used.
3. Flag silent assumptions such as differentiability, invertibility, exchange of limits, or independence.
4. Verify dimensions, domains, signs, and constants.
5. Mark the first invalid or unproven step exactly.
6. If the derivation is valid only under added conditions, state the weakest conditions you found.

## Rules

- Do not skip steps that are essential to the argument, even if they seem obvious.
- If a derivation is only heuristic, explicitly label it as heuristic.
- Distinguish algebra mistakes from missing assumptions.
- Do not repair the derivation silently; name the repair.

## Output

Return:
- target derivation;
- checked step list;
- first invalid or unsupported step;
- required assumptions;
- corrected version if small enough;
- verdict: valid / valid with conditions / heuristic / invalid.
