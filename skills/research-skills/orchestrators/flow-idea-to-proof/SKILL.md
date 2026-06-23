---
name: flow-idea-to-proof
description: >-
  Orchestrate the path from a raw research idea to a formal claim with a defensible proof design — drawing the hypothesis out of the idea, stating it as a precise theorem/claim, and designing (and auditing) the proof strategy. Use whenever the user says "help me turn this idea into a theorem", "I have a hunch, can we make it rigorous", "design a proof for this", "what would I need to prove this", "formalize this claim", "is this provable and how", or hands over an informal conjecture they want to develop into a formal result. This is a ROUTER that sequences existing singleton skills; it does not write the proof itself. Use flow-learn-new-topic or flow-deep-understanding when the goal is to understand existing work rather than formalize the user's own idea. Use gap-finder when the starting point is an existing paper's weakness rather than a fresh idea.
---

# Idea → Hypothesis → Proof Design (Orchestrator)

Take a raw idea and walk it to a **formal, defensible claim with a proof strategy**: sharpen the hypothesis, isolate what must be true, state the claim precisely, sketch the proof, and audit it before the user sinks weeks into a full write-up. This skill routes between singletons — it does not produce the stress-test, the proof sketch, or the audit itself.

Contrast with siblings:
- **flow-learn-new-topic / flow-deep-understanding** — understanding *existing* work. Here the object is the user's own idea and doesn't exist yet.
- **gap-finder** — starts from an existing paper's weakness. Use that to *source* an idea; use this to *develop* one you already have.

## Before You Start: Capture the Raw Idea

Ask only what you can't infer. You need:
- **The idea, in one sentence** — even if vague. You'll sharpen it in stage 1.
- **The setting** — what mathematical/empirical objects it concerns (the formalism it lives in).
- **What "true" would mean** — is the user after a theorem, a bound, a guarantee, an impossibility result, or an empirical regularity they want to explain? This sets whether the path is proof-design or experiment-design.

If the user actually wants empirical validation rather than a proof, route to `research-idea-stress-test` → `experiment-design` instead and say so.

## The Pipeline

Run in order. **Enter wherever the idea already is** — a user with a crisp claim skips stage 1.

```text
Stress-test the idea → Extract what must be true → State the formal claim → Sketch the proof → Audit & attack → (handoff to write-up)
```

### Stage 1 — Stress-test the idea → `research-idea-stress-test`
Hand off to expose hidden assumptions, fake novelty, and confounders, and to find the cheapest test of whether the idea is even worth formalizing. Don't design a proof for a claim that dies to a cheap attack.
**Exit gate:** the idea survives cheap disconfirmation and the user can state mechanism + claim + contribution separately.

### Stage 2 — Extract what must be true → `theory-assumption-extractor`
Hand off to list the premises the claim requires, separating logically necessary conditions from conveniences. These become the hypotheses of the theorem.
**Exit gate:** there's an explicit assumption set; the user knows which premises the claim cannot survive without.

### Stage 3 — State the formal claim → `theorem-and-claim-audit`
Hand off to turn the sharpened idea + assumptions into a precisely quantified statement, and to check the claim isn't over-stated, circular, or already implied by something known.
**Exit gate:** there is a formal claim with explicit hypotheses and quantifiers, scoped to what's actually defensible.

### Stage 4 — Sketch the proof → `theory-proof-sketcher`
Hand off to design the proof strategy: the high-level argument, the lemmas needed, the proof technique, and the riskiest step. Optionally ground the strategy on a minimal instance with `theory-to-toy-cases` before committing.
**Exit gate:** there's a proof skeleton with named lemmas and an identified weakest link.

### Stage 5 — Audit & attack → `theory-counterexample-hunter` (+ `theory-derivation-auditor`)
Hand off to attack the claim and the skeleton: hunt counterexamples at the assumption boundaries, and audit any concrete derivation steps line by line. This is where over-broad claims get caught before they reach a referee.
**Exit gate:** no surviving counterexample to the stated claim, and the risky derivation steps check out — or the claim has been narrowed until both hold.

### Stage 6 — Handoff to write-up
A surviving claim + sketch is ready for full proof writing and paper integration. Route to the paper-writing skills (`method-section-writer`, `paper-argument-planner`) and, if relevant, `gap-finder` to position the contribution.

## Router Rules

- **Delegate, don't duplicate.** Each stage hands to a singleton; this file owns sequencing and gates.
- **Enter at the idea's maturity.** A crisp claim skips stages 1–2; a vague hunch starts at stage 1.
- **Loop on failure.** A counterexample in stage 5 sends the user back to stage 2 or 3 to narrow the claim — narrowing is success, not failure.
- **Proof, not experiment.** If "true" means empirical, this is the wrong orchestrator — route to the experiment-design pipeline.
- **Don't formalize a dead idea.** If stage 1 says drop or reframe, stop here; don't proof-design something that isn't worth it.
