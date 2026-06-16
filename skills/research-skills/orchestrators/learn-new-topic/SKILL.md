---
name: learn-new-topic
description: Orchestrate breadth-first onboarding into an unfamiliar topic, method, subfield, or research area — going from near-zero to a working, usable map. Use whenever the user says "I want to learn X", "help me get up to speed on X", "I'm new to X, where do I start", "give me a learning path for X", "I need to understand this field before I can read its papers", or hands over a topic they have no prior grounding in. This is a ROUTER: it sequences existing singleton skills, it does not teach directly. Use deep-understanding instead when the user already knows the basics and wants rigorous mastery of ONE specific thing (a paper, a derivation, a single method). Use idea-to-proof when the goal is to formalize a research idea into a claim and proof, not to learn an existing topic.
---

# Learn a New Topic (Orchestrator)

Breadth-first onboarding. The goal is a **usable map of an unfamiliar area**: the core problems, the main method families, the key papers, and enough working intuition to start reading primary sources without drowning. This skill decides *what to do next and which skill to hand to* — it does not produce the teaching itself.

Contrast with siblings:
- **deep-understanding** — depth-first mastery of one already-familiar object. Use it when breadth is no longer the bottleneck.
- **idea-to-proof** — turning the user's own idea into a formal claim. Different goal entirely.

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

### Stage 1 — Orient (you, directly)
Give a one-screen lay of the land: what problem this area exists to solve, the 3–6 sub-areas inside it, and the names they'll keep hearing. This is a sketch to make later stages navigable, not a lecture.
**Exit gate:** the user can name the major sub-areas and say which one they care about.

### Stage 2 — Map the landscape → `literature-triangulation`
Hand off to build a source-grounded map of the area: the canonical papers, the method families, the benchmarks, and the genuine disagreements. This prevents you from teaching a hallucinated consensus.
**Exit gate:** there is a concrete reading list and a method-family map, with the user's target sub-area identified.

### Stage 3 — Build core intuition → `professor-mentor-technical-teaching`
For each core concept on the map, hand off to teach it properly: motivation → intuition → assumptions → formalism → limitations. Go concept by concept; don't dump the whole field at once.
**Exit gate:** the user can explain *why* each core method exists and what pressure it responds to.

### Stage 4 — Ground with toy cases → `theory-to-toy-cases`
Turn the abstractions into the smallest concrete cases the user can compute or picture. Onboarding sticks when it becomes operational.
**Exit gate:** the user has worked (or watched you work) at least one minimal example per core idea.

### Stage 5 — Bridge to primary sources
Point back at the stage-2 reading list and have the user read the first canonical paper, now with enough scaffolding to follow it. Optionally hand off to `formalism-translator` if the area's notation collides with a formalism they already know.
**Exit gate:** the user can read a primary paper in the area without getting stuck on prerequisites.

## Handoffs Out

When breadth is no longer the bottleneck, route onward:
- One specific paper/method now needs rigorous mastery → **deep-understanding**.
- They have an idea and want to formalize it → **idea-to-proof**.
- They want to evaluate whether a method is actually good / find gaps → **gap-finder** or `research-idea-stress-test`.

## Router Rules

- **Delegate, don't duplicate.** Each stage hands to a singleton skill; this file never re-teaches what that skill does.
- **Resume, don't restart.** Begin at the user's actual level. A returning user picks up at their last unmet exit gate.
- **One concept at a time in stages 3–4.** Breadth-first does not mean everything-at-once.
- **Honor the depth target.** "Read papers" stops at stage 5; "just curious" may stop at stage 3.
- **Stop when the gate is met.** Don't push the user through stages they don't need.
