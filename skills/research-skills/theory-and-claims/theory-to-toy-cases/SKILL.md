---
name: theory-to-toy-cases
description: Turn abstract math or ML ideas into minimal examples, counterexamples, sanity checks, and tiny simulations. Use when a concept is too abstract or a claim needs intuition or falsification.
when_to_use: Use for theorem intuition, debugging derivations, constructing stress tests, or converting a research idea into small checkable cases.
---

# Theory to Toy Cases

Make the idea concrete before scaling it up.

## Workflow

1. Restate the abstract claim in the smallest possible setting.
2. Build 2-5 minimal cases:
   - a friendly case where the idea should work
   - a boundary case
   - a failure case
   - a misleading case that appears to work for the wrong reason
3. If useful, write a tiny simulation or symbolic example.
4. Compare predicted behavior vs actual behavior.
5. Extract what the toy case teaches about the full problem.

## Good toy cases

Prefer cases that are:
- low-dimensional
- analytically tractable
- numerically checkable
- likely to expose hidden assumptions

## Rules

- Do not use toy cases as proof.
- Say what scales and what does not.
- If a toy case fails, treat that as signal, not annoyance.

## Output shape

Return:
- Abstract idea
- Minimal setup
- Cases
- What each case shows
- Implication for the full research question
