---
name: concept-exercise-generator
description: >-
  Generate a graded exercise set — easy to advanced — that lets a learner verify whether they actually understand a topic, concept, method, derivation, or paper, with solutions kept in a separate file for honest self-testing. Use whenever the user says "give me exercises", "quiz me on X", "test whether I actually get this", "problems from easy to hard", "practice questions with solutions", "how do I check if I understood this", or wants a self-check after learning something. Produces two artifacts: an `exercises.md` (problems only, tagged by difficulty tier and concept) and a `solutions.md` (worked answers plus a self-check rubric and a pointer to what to revisit on a miss). This skill builds the verification material; it does not teach the concept (use professor-mentor-technical-teaching for that) and it does not sequence a learning path (use flow-learn-new-topic for that). It is the assessment step those flows hand off to at an exit gate.
---

# Concept Exercise Generator

Produce a graded exercise ladder that **verifies understanding** of a specific topic, concept, method, derivation, or paper. The output is two separate files so the learner attempts the problems first and only then checks solutions — peeking is the failure mode this format is built to prevent.

This skill makes the *assessment*, not the lesson. It is the step `flow-learn-new-topic` and `flow-deep-understanding` route to at an exit gate to confirm the learner actually passed, instead of asserting they did.

## When to use / not use

- **Use** when the learner has covered material and wants to test retention, mechanism, reasoning, or generative mastery.
- **Use** as the gate-check inside a learning flow.
- **Don't use** to teach the concept for the first time — that is `professor-mentor-technical-teaching`.
- **Don't use** to design *research* experiments or benchmarks — that is `experiment-design` / `benchmark-and-baseline-selector`.

## Before You Generate: Ground the Exercises

Blind exercises test a hallucinated version of the topic. Gather, or confirm you already have:

- **The concept(s)** to test, stated concretely (not "transformers" but "scaled dot-product attention and why it's scaled").
- **The source material** the learner actually studied — the paper, the lecture, the teaching output, the toy cases. Exercises must be answerable from *that* material, not from a generic textbook the learner never read.
- **Current level** — novice, can-read-papers, or can-build. This sets where the ladder centers.
- **Depth target & budget** — a 15-minute self-check is ~4 problems; a full mastery pass is 8–12 across all tiers.

If the source material is missing, ask for it or pull it from the upstream teaching output before generating. Do not invent facts to build a problem around.

## The Difficulty Ladder

Four tiers, easy → advanced. Full detail, verbs, and per-domain templates are in `references/difficulty-ladder.md` and `references/exercise-templates.md`. For multiple-choice distractors and intuitive-trap problems, use `references/assessment-design-principles.md`. The short form:

| Tier | Name | Tests | Example verbs |
|------|------|-------|---------------|
| 1 | Recall & Recognize | vocabulary, what-is, which-family | define, identify, state, match |
| 2 | Apply & Compute | mechanism on a toy case | compute, trace, predict, plug in |
| 3 | Analyze & Compare | *why*, when it breaks, trade-offs | contrast, diagnose, justify, choose |
| 4 | Build, Derive & Break | generative mastery | derive, construct a counterexample, critique, design a variant |

A learner who only clears Tiers 1–2 can recite and run the method but does not yet understand it; Tiers 3–4 are where real comprehension shows. Always include at least one Tier 3+ problem, even in a short set — that is the one that actually verifies understanding.

## Process

1. **Scope** — confirm concept(s), source material, level, and budget (above).
2. **Pick the spread** — choose how many problems per tier from the budget and depth target. Defaults in `references/difficulty-ladder.md`. Center the ladder on the learner's level but always reach one tier above it.
3. **Write the problems** — one concept per problem, unambiguous, answerable from the source material. Tag each with `[Tier N · concept]`. Use the per-domain templates (conceptual, mathematical/derivation, coding, analysis/critique) in `references/exercise-templates.md`. If you use multiple choice, every distractor must encode a known misconception and diagnose which wrong model the learner holds; never use random wrong answers. When the topic has an attractive intuitive-but-wrong shortcut, include one CRT-style verification problem that forces deliberate checking.
4. **Write the solutions separately** — for each problem: the answer, the worked reasoning, a **self-check rubric** ("you've got it if…", "common wrong turns"), and a **revisit pointer** naming what to restudy on a miss. Format in `references/solution-and-rubric-format.md`.
5. **Emit two files** — never interleave problems and solutions:
   - `exercises.md` — problems only, numbered, tier-tagged, with an instruction header.
   - `solutions.md` — matching numbers, full solutions + rubric + revisit pointers.
6. **State the self-verification protocol** to the learner (below).

## Output: Two Files

`exercises.md` opens with a short header telling the learner how to use it:

```text
# Exercises — <topic>
Attempt every problem before opening solutions.md. Write your answer down; a vague
mental "yeah I know this" is the thing these problems exist to catch. Then score
yourself against the rubric in solutions.md.

1. [Tier 1 · <concept>] <problem>
2. [Tier 2 · <concept>] <problem>
...
```

`solutions.md` mirrors the numbering exactly:

```text
# Solutions — <topic>

1. [Tier 1 · <concept>]
   Answer: ...
   Why: ...
   ✅ You've got it if: ...
   ⚠️ Common wrong turn: ...
   ↩ Revisit if missed: <concept / section / stage to restudy>
```

## Self-Verification Protocol (give this to the learner)

1. Attempt **every** problem and write the answer down before opening `solutions.md`.
2. Score each against its rubric — honestly. A near-miss on a Tier 3–4 problem is a miss.
3. Map every miss to its revisit pointer; restudy those, don't just read the solution.
4. **Gate rule:** understanding is verified only when Tier 3+ problems pass *unaided*. Clearing Tiers 1–2 alone means re-study, not progress.

## Handoffs

- Learner missed problems and needs re-teaching → `professor-mentor-technical-teaching`.
- Misses cluster on computing minimal cases → `theory-to-toy-cases`.
- Tier-4 critique/derivation exposed a real gap in the source itself → `gap-finder` or `theorem-and-claim-audit`.
- Called from a learning flow → return the pass/fail-by-tier result to the orchestrator so it can decide the next stage.
