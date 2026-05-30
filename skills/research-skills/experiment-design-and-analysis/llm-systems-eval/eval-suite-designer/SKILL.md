---
name: eval-suite-designer
description: Design a task-specific evaluation suite with clear failure modes, metrics, and decision criteria. Use when generic benchmarks are not enough.
when_to_use: Use for LLM systems, agents, RAG, tool use, and product-facing evaluations.
---

# Eval Suite Designer

Build evaluations that answer the real question.

## Workflow

1. Define the capability to measure.
2. Identify realistic task slices and failure modes.
3. Choose metrics and human checks where needed.
4. Add edge cases, adversarial cases, and abstention cases.
5. Define success criteria and what would invalidate the eval.

## Rules

- Avoid benchmark theater.
- Prefer small decisive evals to giant vague suites.
