---
name: theory-paper-to-theorem-distiller
description: Distill a dense theory paper into definitions, main claims, proof strategy, and reusable techniques. Use for theoretical ML or math paper reading, seminar prep, related-work synthesis, extracting reusable lemmas, or deciding what part of a paper is actually load-bearing.
---

# Paper to Theorem Distiller

Extract the reusable mathematical core.

## Workflow

1. Identify the central problem and theorem.
2. List key definitions and notation.
3. Summarize each main claim in plain but precise language.
4. Outline proof strategy without pretending full verification.
5. Note what is novel vs standard machinery.
6. Extract the dependencies between definitions, lemmas, and the main theorem.
7. End with what can be reused in your own work.

## Rules

- Separate paper claims from verified details.
- If a proof was not checked, say so.
- Do not compress away assumptions; they are often the point.
- Separate reusable technique from paper-specific setup.

## Output

Return:
- problem and setting;
- notation and definitions;
- main theorem/claims;
- proof dependency map;
- proof strategy;
- assumptions and limitations;
- reusable techniques;
- unchecked details.
