---
name: deep-understanding
description: Orchestrate depth-first mastery of ONE specific object the user already has basic familiarity with — a single paper, method, algorithm, theorem, derivation, or result — until they can re-derive it, criticize it, and find where it breaks. Use whenever the user says "I want to really understand X", "help me understand this paper deeply", "I get the gist but not the mechanism", "walk me all the way through this method", "I want to be able to defend/criticize this", or "tear this apart so I actually get it". This is a ROUTER that sequences existing singleton skills; it does not teach directly. Use learn-new-topic instead when the user is new to a whole area and needs breadth-first onboarding. Use idea-to-proof when the goal is to formalize the user's OWN idea into a claim and proof rather than master an existing object.
---

# Deep Understanding (Orchestrator)

Depth-first mastery of a **single object** the user already half-knows. The goal: they can re-derive it from memory, name every assumption it leans on, and say precisely where and why it fails. This skill routes between singletons — it does not produce the teaching, the audit, or the counterexamples itself.

Contrast with siblings:
- **learn-new-topic** — breadth-first onboarding into an unfamiliar *area*. Use it when the user lacks the surrounding map.
- **idea-to-proof** — formalizing the user's own idea. Here the object already exists and is fixed.

## Before You Start: Pin the Object

Ask only what you can't infer. You need:
- **The exact object** — which paper / method / theorem / derivation. One thing, not a family.
- **Current grasp** — what they already understand vs where it goes fuzzy. Mastery is depth-first, so start at the fuzzy edge.
- **The purpose** — implement it, build on it, review it, or defend it in a meeting/exam. This sets how far into critique to push.

If the user names a whole area rather than one object, route to **learn-new-topic** first.

## The Pipeline

Run in order, but **enter at the user's fuzzy edge** — don't re-teach what they already hold.

```text
Reconstruct the reasoning → Surface assumptions → Verify the mechanism → Stress-test → Re-derive & criticize
```

### Stage 1 — Reconstruct the reasoning → `professor-mentor-technical-teaching`
Hand off to rebuild the object the way a mentor would: why it exists, the single insight that makes it work, the formalism, the implementation, the limitations. This is the spine of understanding.
**Exit gate:** the user can state *what pressure the object responds to* and the core mechanism in their own words.

### Stage 2 — Surface assumptions → `assumption-extractor`
Hand off to extract every explicit and hidden premise: which are logically necessary, which are conveniences, and where the argument actually rests. You can't claim to understand something whose load-bearing assumptions you can't list.
**Exit gate:** the user has an explicit assumption inventory, tagged necessary vs convenience.

### Stage 3 — Verify the mechanism → `derivation-auditor` (and/or `theory-to-toy-cases`)
If there's a derivation, hand off to check it line by line. If it's a method/algorithm, ground it with `theory-to-toy-cases` so the mechanism becomes something the user can actually compute on a minimal example.
**Exit gate:** the user has either traced the derivation step by step or run the smallest worked example end to end.

### Stage 4 — Stress-test → `counterexample-hunter`
Hand off to attack the object: edge cases, pathological inputs, the regime where each assumption breaks. Understanding includes knowing the boundaries.
**Exit gate:** the user can name at least one concrete regime where the object fails and *why*.

### Stage 5 — Re-derive & criticize (you, lightly)
Have the user re-derive or re-explain the object cold, then articulate its fundamental (un-removable) tradeoff. This is the test that the previous stages took. If they stumble, route back to the stage that covers the gap.
**Exit gate:** the user can reproduce the object unaided and state its fundamental limitation.

## Optional Branches

- Notation is the obstacle, or another formalism would clarify → `formalism-translator`.
- The object is a dense paper and step 1 needs its formal core extracted first → `paper-to-theorem-distiller`.
- Understanding has matured into wanting to *improve* the object → hand off to **gap-finder**, then **idea-to-proof**.

## Router Rules

- **Delegate, don't duplicate.** Each stage hands to a singleton; this file owns sequencing and gates only.
- **Enter at the fuzzy edge.** Skip stages the user already passes; depth-first means spending effort where comprehension breaks.
- **One object only.** If scope creeps to a family of methods, that's a **learn-new-topic** job.
- **The re-derivation in stage 5 is the real test.** Passing earlier gates by nodding along doesn't count — make them reproduce it.
- **Loop back, don't bulldoze.** A failed gate sends the user back to the relevant stage, not forward.
