---
name: abstract-and-intro-writer
description: Draft or revise the abstract and introduction of a research paper. Use whenever the user needs to write or improve these sections — including phrasings like "write my abstract", "improve my intro", "draft the introduction", "my abstract is weak", "how should I open the paper", "the intro is too long", "I need a hook", "write a one-paragraph summary", or "my introduction doesn't sell the contribution". Also use when the user has a paper plan or results but no prose yet for the opening. The abstract and introduction have distinct structures and reviewer conventions that differ from the rest of the paper; this skill handles both as a pair since the intro must match and extend the abstract's promises. If the contribution or paper spine is not yet stable, use paper-argument-planner first.
---

# Abstract and Introduction Writer

The abstract and introduction are the only parts of a paper most reviewers read carefully before deciding how to score it. Write them as a pair: the abstract makes promises; the introduction keeps them.

## The core failure modes

**1. Claiming without grounding.** "We propose a novel method that significantly outperforms..." without telling the reader what specifically is novel or what the number is. Reviewers read this as empty.

**2. Motivation without gap.** Two paragraphs on why the problem matters, then jumping straight to the method. The reader has no idea why existing work doesn't already solve it.

**3. Contribution list that doesn't match the paper.** Bullet points that list things the paper vaguely does rather than claims the experiments support. Every bullet should be checkable against a section or table.

**4. Abstract that buries the result.** A 200-word abstract where the result appears in the last sentence and the finding is "X improves performance." What performance, by how much, under what conditions?

**5. Introduction that repeats the abstract.** The introduction should extend and deepen, not summarize.

---

## Abstract

### What it must do in order

1. Name the problem and why it matters (1–2 sentences).
2. State what existing work fails to do — the specific gap (1–2 sentences).
3. State what this paper does — the method or contribution in one concrete sentence.
4. Give the key result with a number, if the paper is empirical (1 sentence).
5. State the broader implication or takeaway (1 sentence, optional).

### Length norms

- ML/NLP conference (NeurIPS, ICLR, ICML, ACL): 150–250 words.
- Systems/applied (OSDI, SOSP, EuroSys): 150–200 words.
- Theory (STOC, FOCS, COLT): 150–250 words; emphasize problem formulation and result statement.
- Journals: up to 300 words; structured abstracts (Background / Methods / Results / Conclusions) required by many venues.

### Structured vs. narrative

Narrative (most ML/NLP venues):
```
[Problem sentence]. [Existing work limitation]. We propose [method], which [core idea].
Experiments on [benchmarks] show [key result]. [Implication sentence].
```

Structured (many medical/science journals):
```
Background: ...
Methods: ...
Results: ...
Conclusions: ...
```

Use structured only if the venue requires it.

### Calibration

- Name the benchmark and give the number. "We improve F1 by 4.2 points on CoNLL-2003" beats "we show improvements across standard benchmarks."
- Bound the claim. If the method works in one setting, don't write "we solve X."
- Don't use "novel," "significant," or "state-of-the-art" as adjectives without evidence anchoring them. Let the result speak.

---

## Introduction

The introduction has four jobs. Each should have its own paragraph or paragraph cluster.

### 1. Motivation (why does the problem matter?)

Open with the concrete problem, not a sweeping claim about AI. Give the reader a reason to care in 2–3 sentences. A failing system, a real constraint, a theoretical gap — something tangible.

Avoid:
```
Deep learning has revolutionized many areas of machine learning.
```

Prefer:
```
Annotating temporal events in clinical notes requires resolving coreferences across paragraphs,
yet current systems fail on 30% of cross-sentence cases even with large pretrained models.
```

### 2. Gap analysis (why doesn't existing work solve it?)

This is the most important paragraph. State what prior work does and precisely where it falls short. Do not say "no prior work has addressed X" unless you are sure — say "prior work on X assumes Y, which does not hold when Z."

One crisp gap sentence is worth three vague ones. The gap sentence should make the contribution feel necessary, not just interesting.

### 3. Contribution statement

This should be specific enough that a reader could falsify each claim.

Template for an empirical paper:
```
This paper introduces [method name], which [core technical idea]. The key insight is that [mechanism].
We evaluate on [datasets/settings] and find [headline result].
Our contributions are:
(1) [specific technical contribution],
(2) [specific empirical finding or benchmark],
(3) [secondary contribution — analysis, dataset, or theoretical result, if any].
```

Rules for the contribution list:
- Each bullet maps to a specific section, table, or theorem.
- Use past tense for things done, future tense for nothing.
- Avoid "we show that our method is effective." That is a result, not a contribution.

### 4. Paper organization (optional but useful for long papers)

One short paragraph. "Section 2 defines the problem. Section 3 presents the method. Section 4 reports experiments. Section 5 discusses limitations and future work." Skip if the structure is obvious.

---

## Writing the pair as a unit

Before finalizing, check these consistency requirements:

| Abstract promise | Introduction must... |
|---|---|
| Claims method X does Y | Describe X in the contribution paragraph |
| Cites a specific metric/number | Map that number to a table in contributions |
| Names the gap | Give 1–2 citations justifying the gap claim |
| States a broader implication | Restate it (briefly) in the contribution paragraph |

The introduction should never introduce a major claim the abstract didn't prepare the reader for, and the abstract should never make a promise the introduction doesn't support.

---

## Process

### If the user has a paper plan (from paper-argument-planner or similar)

1. Extract: one-sentence thesis, key gap, method, main result, contributions.
2. Draft the abstract first — compress everything to 200 words.
3. Draft the introduction — expand each element, add motivation and related-work context.
4. Check the pair for consistency.
5. Return both with a short note on any claims that need more evidence or citations.

### If the user has a partial draft

1. Read what exists.
2. Identify which of the four introduction jobs are missing or weak.
3. Revise or draft the missing parts; don't rewrite what already works.

### If the user only has results

1. Ask for: the problem, the main result with a number, and the strongest baseline comparison.
2. Draft a minimal abstract and intro skeleton with `[TODO]` placeholders where missing information is needed.
3. Do not invent numbers or gap claims.

---

## Output format

```markdown
# Abstract

[Draft, ~200 words]

---

# Introduction

[Draft, organized into the four jobs above]

---

## Notes

**Claims needing citations:** [list]
**Numbers or facts to verify:** [list]
**Weaker sections:** [list with specific suggestions]
```

If revising an existing draft, also include:
```markdown
## What works

## Specific changes made and why
```

---

## Quality bar

A reviewer should finish the abstract knowing: what problem, what gap, what method, what result. They should finish the introduction knowing: why the problem matters, exactly why existing work falls short, and what specifically this paper contributes — each contribution tied to something checkable.
