---
name: flow-deep-understanding
description: >-
  Orchestrate depth-first mastery of ONE specific object the user already partly knows — a paper, method, algorithm, theorem, derivation, or result — until they can re-derive it, criticize it, and find where it breaks. Use when the user says "I want to really understand X", "help me understand this paper deeply", "I get the gist but not the mechanism", "walk me through this method", "defend/criticize this", or "tear this apart so I get it". Routes through singleton skills and verifies gates with graded exercises. Also supports DISCUSSION MODE, where the user masters the object by explaining it to an honest novice, an opinionated lab mate, and a professor; trigger it on "I learn better by discussing", "question me while I explain", "let's discuss instead of lecturing", "run this like a lab meeting", or "grill me on this paper". Use flow-learn-new-topic for breadth-first onboarding into an area; use flow-idea-to-proof to formalize the user's own idea.
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

**Or verify the gate by discussion.** A user who learns by explaining may clear any gate through a *discussion round* on that stage's material instead of an exercise set — see **Discussion Mode** below. The two verifiers are interchangeable per stage: exercises test whether the user can derive, discussion tests whether they can explain without borrowing. Neither is a soft option; both are cleared unaided or not at all.

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
*In discussion mode the playback has been running since stage 1* — this stage is its
summation over the whole object, not first contact with the student.

## Discussion Mode

Some users learn by *being the explainer* rather than by reading and then testing. In discussion mode the user teaches the current stage's material to a cast of three, and the resulting playback clears that stage's gate in place of an exercise checkpoint. This is a gate mechanism, not a new stage: the pipeline above is unchanged, only how each gate gets verified.

**The cast.** STUDENT (`naive-student`) drives with earned questions. PEER (`whiteboard-peer`) challenges the user's answers. MENTOR (`professor-mentor-technical-teaching`) supplies a missing dependency, rarely. MODERATOR is this file — it rules each answer in one line and decides when to move on.

**The professor splits three ways.** Moderating is not teaching, and neither is grading. `professor-critic` must **not** fire during a discussion: it requires a finished artifact, a named reader, and an acceptance bar, none of which a live session has, and a verdict on unfinished thinking only demoralizes.

**What each voice may know.** The STUDENT may use only what has been spoken aloud in this session — never outside domain knowledge, which is its *silent repair* failure mode and would make the playback decorative instead of diagnostic. The STUDENT tags every link it accepts with `[USER]`, `[PEER]`, or `[MENTOR]`. PEER and MENTOR are unrestricted in knowledge but tightly restricted in timing and volume.

**The round.** STUDENT asks one question at the earliest unsupported link → USER answers first, always → PEER may then *challenge* (its default move), or *assist* with one partial move only if the user explicitly passes → MODERATOR rules `CORRECT` / `INCOMPLETE: <what's missing>` / `WRONG: <the error>` / `STALLED` → STUDENT records the source tag and asks the next question.

**The escalation ladder.** Never skip a rung:

```text
USER answers → PEER challenges → USER retries → PEER partial move → MENTOR minimal dependency
```

Jumping straight to the mentor converts the discussion back into the lecture the user chose to avoid. Per round: one student question, one substantive peer move, one moderator line, at most one mentor dependency. If the mentor fires in two consecutive rounds, stop — the material is above the user's current footing, so drop back a stage rather than lecturing through it.

**Passing the gate.** The gate passes when the playback holds **and** every load-bearing link is `[USER]`-owned. A model that holds on borrowed links is a debt, not understanding: route those links to `knowledge-debt-audit` and re-run the round that should have established them.

Because this is mastery of one object, the peer's challenges should escalate with the stages — quibbling definitions early, then attacking assumptions, then hunting the regime where the object breaks. By stage 4 a discussion round that produces no surviving objection has not been adversarial enough to certify mastery.

## Optional Branches

- Notation is the obstacle, or another formalism would clarify → `theory-formalism-translator`.
- The object is a dense paper and step 1 needs its formal core extracted first → `theory-paper-to-theorem-distiller`.
- Understanding has matured into wanting to *improve* the object → hand off to **gap-finder**, then **flow-idea-to-proof**.
- The user has a partial extension and needs a co-solver who will disagree without
  taking over → `whiteboard-peer`.
- The purpose was to *defend* the object (meeting, exam, committee) → after stage 5,
  have the user write the explanation up as a finished piece and hand it to
  `professor-critic` with a named reader and acceptance bar **the user supplies** —
  do not invent either. This is where the critic belongs: on a committed artifact
  after the discussion, never inside it.

## Router Rules

- **Delegate, don't duplicate.** Each stage hands to a singleton; this file owns sequencing and gates only.
- **Enter at the fuzzy edge.** Skip stages the user already passes; depth-first means spending effort where comprehension breaks.
- **One object only.** If scope creeps to a family of methods, that's a **flow-learn-new-topic** job.
- **The re-derivation in stage 5 is the real test.** Passing earlier gates by nodding along doesn't count — make them reproduce it.
- **Loop back, don't bulldoze.** A failed gate sends the user back to the relevant stage, not forward.
- **Verify gates with Tier 3+ checks.** Confirm each gate with a `concept-exercise-generator` checkpoint skewed to analyze/derive/break problems, or with a discussion round; advance only when the user clears it unaided. Generate the exercises there — never inline them here.
- **In discussion mode, the user answers first.** A peer that pre-empts the user destroys the diagnostic — the playback would then be grading the peer, not the user.
