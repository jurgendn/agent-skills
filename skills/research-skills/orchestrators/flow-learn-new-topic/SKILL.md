---
name: flow-learn-new-topic
description: >-
  Orchestrate breadth-first onboarding into an unfamiliar topic, method, subfield, or research area — going from near-zero to a working, usable map. Use whenever the user says "I want to learn X", "help me get up to speed on X", "I'm new to X, where do I start", "give me a learning path for X", "I need to understand this field before I can read its papers", or hands over a topic they have no prior grounding in. Each stage is verified with a graded easy-to-advanced exercise checkpoint (handed off to concept-exercise-generator) so the user can self-test whether they actually understood before moving on, rather than the orchestrator just asserting they did. This is a ROUTER: it sequences existing singleton skills, it does not teach directly. Use flow-deep-understanding instead when the user already knows the basics and wants rigorous mastery of ONE specific thing (a paper, a derivation, a single method). Use flow-idea-to-proof when the goal is to formalize a research idea into a claim and proof, not to learn an existing topic.
---

# Learn a New Topic (Orchestrator)

Breadth-first onboarding. The goal is a **usable map of an unfamiliar area**: the core problems, the main method families, the key papers, and enough working intuition to start reading primary sources without drowning. This skill decides *what to do next and which skill to hand to* — it does not produce the teaching itself.

Contrast with siblings:
- **flow-deep-understanding** — depth-first mastery of one already-familiar object. Use it when breadth is no longer the bottleneck.
- **flow-idea-to-proof** — turning the user's own idea into a formal claim. Different goal entirely.

## Before You Start: Locate the User

Ask only what you can't infer. You need:
- **The target** — what topic/method/field, stated concretely.
- **Starting point** — total novice, adjacent-field transfer, or "I've heard the words but nothing sticks".
- **Purpose & depth** — passing familiarity, ability to read papers, or ability to build. This sets how far down the pipeline to go.
- **Time budget** — a one-hour orientation vs a multi-week ramp changes everything.

If the target is vague ("I want to learn ML"), narrow it before routing — a map of an ocean is useless.

## The Pipeline

Run these stages in order. **Skip forward** to wherever the user already is; not everyone starts at stage 1.

```text
Orient → Map the landscape → Build core intuition → Ground with toy cases → Bridge to primary sources → (handoff)
```

**Gates are verified, not assumed.** Each exit gate is checked with an *exercise checkpoint*: hand off to `concept-exercise-generator` to produce a short, graded easy-to-advanced problem set (with solutions in a separate file) targeting that stage's level. The user attempts it, self-scores against the rubric, and only then advances. A gate is met when the user clears the checkpoint's harder (Tier 3+) problems unaided — passing only the easy recall problems means re-study, not progress. Skip a checkpoint only when the user explicitly opts out or is clearly already past that stage.

### Stage 1 — Orient (you, directly)
Give a one-screen lay of the land: what problem this area exists to solve, the 3–6 sub-areas inside it, and the names they'll keep hearing. This is a sketch to make later stages navigable, not a lecture.
**Exit gate:** the user can name the major sub-areas and say which one they care about.
**Checkpoint:** a Tier 1–2 set (recall the sub-areas, match terms to definitions).

### Stage 2 — Map the landscape → `literature-triangulation`
Hand off to build a source-grounded map of the area: the canonical papers, the method families, the benchmarks, and the genuine disagreements. This prevents you from teaching a hallucinated consensus.
**Exit gate:** there is a concrete reading list and a method-family map, with the user's target sub-area identified.
**Checkpoint:** a Tier 1–2 set (which family solves which problem; which benchmark measures what).

### Stage 3 — Build core intuition → `professor-mentor-technical-teaching`
For each core concept on the map, hand off to teach it properly: motivation → intuition → assumptions → formalism → limitations. Go concept by concept; don't dump the whole field at once.
**Exit gate:** the user can explain *why* each core method exists and what pressure it responds to.
**Checkpoint:** a Tier 3 set (why this method not that; what assumption breaks it) — this is the gate that actually verifies understanding; do not skip it.

### Stage 4 — Ground with toy cases → `theory-to-toy-cases`
Turn the abstractions into the smallest concrete cases the user can compute or picture. Onboarding sticks when it becomes operational.
**Exit gate:** the user has worked (or watched you work) at least one minimal example per core idea.
**Checkpoint:** a Tier 2 + Tier 3 set (compute a fresh toy case unaided; predict what changes when an input is perturbed).

### Stage 5 — Bridge to primary sources
Point back at the stage-2 reading list and have the user read the first canonical paper, now with enough scaffolding to follow it. Optionally hand off to `theory-formalism-translator` if the area's notation collides with a formalism they already know.
**Exit gate:** the user can read a primary paper in the area without getting stuck on prerequisites.
**Checkpoint:** a Tier 4 set on the actual paper (critique the central claim; derive a stated result; design an experiment that would falsify it).

## Handoffs Out

When breadth is no longer the bottleneck, route onward:
- One specific paper/method now needs rigorous mastery → **flow-deep-understanding**.
- They have an idea and want to formalize it → **flow-idea-to-proof**.
- They want to evaluate whether a method is actually good / find gaps → **gap-finder** or `research-idea-stress-test`.

## Router Rules

- **Delegate, don't duplicate.** Each stage hands to a singleton skill; this file never re-teaches what that skill does.
- **Resume, don't restart.** Begin at the user's actual level. A returning user picks up at their last unmet exit gate.
- **One concept at a time in stages 3–4.** Breadth-first does not mean everything-at-once.
- **Honor the depth target.** "Read papers" stops at stage 5; "just curious" may stop at stage 3.
- **Stop when the gate is met.** Don't push the user through stages they don't need.
- **Verify gates, don't assume them.** Confirm each gate with a `concept-exercise-generator` checkpoint; advance only when the user clears its Tier 3+ problems unaided. Generate the exercises there — never inline them here.
