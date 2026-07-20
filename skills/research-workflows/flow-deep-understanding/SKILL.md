---
name: flow-deep-understanding
description: >-
  Orchestrate depth-first mastery of ONE specific object the user already has basic familiarity with — a single paper, method, algorithm, theorem, derivation, or result — until they can re-derive it, criticize it, and find where it breaks. Use when the user says "I want to really understand X", "help me understand this paper deeply", "I get the gist but not the mechanism", "walk me all the way through this method", "defend/criticize this", or "tear this apart so I actually get it". Routes through singleton skills with graded exercise checkpoints. Use flow-learn-new-topic when the user needs breadth-first onboarding into an area; use flow-idea-to-proof when formalizing the user's own idea.
---

# Deep Understanding (Orchestrator)

Depth-first mastery of a **single object** the user already half-knows. The goal: they can re-derive it from memory, name every assumption it leans on, and say precisely where and why it fails. This skill routes between singletons — it does not produce the teaching, the audit, or the counterexamples itself.

Contrast with siblings:
- **flow-learn-new-topic** — breadth-first onboarding into an unfamiliar *area*. Use it when the user lacks the surrounding map.
- **flow-idea-to-proof** — formalizing the user's own idea. Here the object already exists and is fixed.

## Before You Start: Pin the Object

Ask only what you can't infer. You need:
- **The exact object** — which paper / method / theorem / derivation. One thing, not a family.
- **Current grasp** — what they already understand vs where it goes fuzzy. Mastery is depth-first, so start at the fuzzy edge.
- **The purpose** — implement it, build on it, review it, or defend it in a meeting/exam. This sets how far into critique to push.

If the user names a whole area rather than one object, route to **flow-learn-new-topic** first.

## The Pipeline

Run in order, but **enter at the user's fuzzy edge** — don't re-teach what they already hold.

```text
Reconstruct → Surface assumptions → Verify mechanism → Stress-test → Teach cold
```

**Gates are verified, not assumed.** Each exit gate is checked with an *exercise checkpoint*: hand off to `concept-exercise-generator` to produce a short graded set (solutions in a separate file) for that stage. Because this is mastery, not onboarding, the checkpoints skew to Tier 3–4 (analyze / derive / construct a counterexample) — a stage passes only when the user clears those *unaided*. Skip a checkpoint only when the user is demonstrably already past that stage's fuzzy edge.

### Stage 1 — Reconstruct the reasoning → `professor-mentor-technical-teaching`
Hand off to rebuild the object the way a mentor would: why it exists, the single insight that makes it work, the formalism, the implementation, the limitations. This is the spine of understanding.
**Exit gate:** the user can state *what pressure the object responds to* and the core mechanism in their own words.
**Checkpoint:** a Tier 3 set (why this object exists rather than the obvious alternative; what the core insight buys).

### Stage 2 — Surface assumptions → `theory-assumption-extractor`
Hand off to extract every explicit and hidden premise: which are logically necessary, which are conveniences, and where the argument actually rests. You can't claim to understand something whose load-bearing assumptions you can't list.
**Exit gate:** the user has an explicit assumption inventory, tagged necessary vs convenience.
**Checkpoint:** a Tier 3 set (which assumption is load-bearing; what changes in the conclusion if a given premise is dropped).

### Stage 3 — Verify the mechanism → `theorem-and-claim-audit` (and/or `theory-to-toy-cases`)
If there's a derivation, hand off to check it line by line. If it's a method/algorithm, ground it with `theory-to-toy-cases` so the mechanism becomes something the user can actually compute on a minimal example.
**Exit gate:** the user has either traced the derivation step by step or run the smallest worked example end to end.
**Checkpoint:** a Tier 2 + Tier 4 set (compute a fresh toy case unaided; re-derive one nontrivial step without the reference).

### Stage 4 — Stress-test → `theory-counterexample-hunter`
Hand off to attack the object: edge cases, pathological inputs, the regime where each assumption breaks. Understanding includes knowing the boundaries.
**Exit gate:** the user can name at least one concrete regime where the object fails and *why*.
**Checkpoint:** a Tier 4 set (construct an input/regime that breaks the object and explain which assumption it violates).

### Stage 5 — Re-derive & teach cold → `naive-student`
Have the user re-derive and teach the object cold to an honest novice, then articulate
its fundamental (un-removable) tradeoff. The student's playback localizes any gap
without silently repairing it. If the playback breaks, route back to the stage that
covers the missing dependency.
**Exit gate:** the user can reproduce the object unaided and state its fundamental limitation.
**Checkpoint:** this stage *is* the capstone test — formalize it as a Tier 4 set (re-derive the object cold; state the un-removable tradeoff) via `concept-exercise-generator` if the user wants a scored final check.

## Optional Branches

- Notation is the obstacle, or another formalism would clarify → `theory-formalism-translator`.
- The object is a dense paper and step 1 needs its formal core extracted first → `theory-paper-to-theorem-distiller`.
- Understanding has matured into wanting to *improve* the object → hand off to **gap-finder**, then **flow-idea-to-proof**.
- The user has a partial extension and needs a co-solver who will disagree without
  taking over → `whiteboard-peer`.

## Router Rules

- **Delegate, don't duplicate.** Each stage hands to a singleton; this file owns sequencing and gates only.
- **Enter at the fuzzy edge.** Skip stages the user already passes; depth-first means spending effort where comprehension breaks.
- **One object only.** If scope creeps to a family of methods, that's a **flow-learn-new-topic** job.
- **The re-derivation in stage 5 is the real test.** Passing earlier gates by nodding along doesn't count — make them reproduce it.
- **Loop back, don't bulldoze.** A failed gate sends the user back to the relevant stage, not forward.
- **Verify gates with Tier 3+ checks.** Confirm each gate with a `concept-exercise-generator` checkpoint skewed to analyze/derive/break problems; advance only when the user clears them unaided. Generate the exercises there — never inline them here.
