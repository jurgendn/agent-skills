---
name: rag-diagnostics-analyst
description: Diagnose whether failures come from retrieval, context selection, grounding, or generation in a RAG system. Use when a retrieval-augmented system underperforms.
when_to_use: Use for search + generation pipelines, knowledge assistants, and grounded QA.
---

# RAG Diagnostics Analyst

Localize the failure before changing the whole stack.

## Workflow

1. Define the end-to-end task.
2. Inspect retrieval quality separately from answer quality.
3. Check whether gold evidence was retrievable.
4. Check whether retrieved evidence was actually used.
5. Separate retrieval miss, selection miss, grounding miss, and generation miss.
6. Recommend the smallest targeted fix.

## Rules

- Retrieval quality alone is not sufficient.
- If the answer is right for the wrong reason, say so.
