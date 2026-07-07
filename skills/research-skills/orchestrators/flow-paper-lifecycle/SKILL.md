---
name: flow-paper-lifecycle
description: >-
  Orchestrate a research paper end-to-end — from raw idea through literature grounding, experiment design, implementation, results, writing, submission, rebuttal, and artifact release. Use whenever the user wants to drive a whole paper rather than one stage: "help me write this paper from scratch", "where am I in the paper process", "what should I do next on this project", "take this from idea to submission", "I have results, get me to a draft", "manage my paper workflow", or hands over a project and asks for the path to a venue. This is a ROUTER that sequences existing singleton skills with stage gates; it does not do the ideation, experiments, or writing itself. For a single stage, invoke that stage's skill directly (e.g. abstract-and-intro-writer, experiment-design). For PhD application packages use flow-phd-application. For talks/decks use the presentation skills.
---

# Paper Lifecycle Orchestrator

Drive a paper from idea to released artifact. The job is to know **what stage the project is in, what the next decision is, and which singleton to hand to** — and to gate transitions so the paper doesn't march forward on a weak foundation (no writing before the contribution is stable; no scaling before the claim is isolated). This file owns sequencing and gates only; it never does the ideation, experiments, or prose itself.

For one isolated stage, skip the orchestrator and invoke that skill directly. Use this when the user wants the *whole path* managed.

## Before You Start: Locate the Project

Ask only what you can't infer. You need:
- **Current stage** — idea, lit review, experiments running, results in hand, drafting, under review, accepted. This sets the entry point; most projects don't start at stage 1.
- **The intended contribution** — even one rough sentence. The whole pipeline is in service of making one claim defensible.
- **Target venue / deadline** — shapes scope, baseline bar, and how much to invest at each stage.

If the contribution can't be stated at all yet, start at stage 1. If it's stated but shaky, start at stage 2.

## The Pipeline

Run in order; **enter at the project's actual stage** and resume from the last unmet gate.

```text
1 Frame the idea → 2 Stress-test → 3 Ground in literature → 4 Design experiments
→ 5 Plan evidence (baselines/ablations) → 6 Implement & run → 7 Analyze results
→ 8 Plan figures/tables → 9 Plan the argument → 10 Write sections
→ 11 Audit citations → 12 Submission readiness → 13 Target a venue
→ 14 Rebuttal → 15 Release artifacts
```

### Stage 1 — Frame the idea → `paper-idea-and-scope-brainstormer`
Shape the raw idea into a scoped contribution and candidate paper spine.
**Gate:** a one-sentence contribution and a rough scope exist.

### Stage 2 — Stress-test → `research-idea-stress-test`
Attack the idea cheaply before investing: hidden assumptions, fake novelty, the cheapest decisive experiment.
**Gate:** the idea survives cheap disconfirmation; mechanism / claim / contribution are stated separately. (Drop or reframe here saves months.)

### Stage 3 — Ground in literature → `literature-triangulation`
Build a source-grounded map: nearest prior work, method families, benchmarks, genuine disagreements. Prevents claiming a contribution that already exists.
**Gate:** nearest baselines identified; the contribution is positioned against real, verified prior work.

### Stage 4 — Design experiments → `experiment-design`
Design the minimal decision-relevant experiment with fair controls and explicit success criteria, before expensive runs.
**Gate:** there's a falsifiable experiment plan with measurable success criteria.

### Stage 5 — Plan the evidence → `benchmark-and-baseline-selector` + `hypothesis-and-ablation-planner`
Pin the MINIMAL vs SUGGESTED baselines/benchmarks the claim needs, and design ablations that isolate the causal mechanism rather than decorate the paper. (Per project convention, every proposal gets a baseline/benchmark pass.)
**Gate:** minimal baseline+benchmark set agreed; ablations map to specific alternative explanations.

### Stage 6 — Implement & run → `research-codebase` (+ `pytorch-training-recipe` / `jax-training-recipe` as needed)
Structure the codebase for fast hypothesis testing and implement the runs. Route to data/training/debugging singletons (`data-pipeline-auditor`, `debugging-strategies`, `hyperparameter-triage`) when those bite.
**Gate:** experiments run reproducibly and produce the metrics the plan called for.

### Stage 7 — Analyze results → `model-eval-error-analysis` → `results-writeup`
Inspect where the method wins and fails (slices, failure categories), then turn the runs into a clear results narrative. Use `statistical-testing-guide` when significance claims are involved.
**Gate:** results support (or refute) the claim; significance and failure modes are understood, not just averages.

### Stage 8 — Plan figures & tables → `figure-table-planner`
Decide what's a plot vs table, design ablation tables, make captions self-contained.
**Gate:** every claim has a figure/table that supports it; visual evidence ↔ claims are mapped.

### Stage 9 — Plan the argument → `paper-argument-planner`
Lock the paper spine — the throughline from problem to contribution — before drafting prose.
**Gate:** a stable spine exists; the contribution is fixed. **Do not write sections before this gate.**

### Stage 10 — Write sections → `paper-writer` (+ section singletons as needed)
Use `paper-writer` as the writing-phase coach: structure the full draft, enforce section gates, keep math prose consistent, and coordinate handoffs. Within that phase, delegate narrow section work to `abstract-and-intro-writer`, `method-section-writer`, `related-work-writer`, and `results-writeup` as needed. Abstract+intro remain a pair; Related Work must come from the stage-3 map.
**Gate:** a complete draft whose sections all serve the spine.

### Stage 11 — Audit citations → `citation-auditor`
Verify references exist, claims match sources, nothing is hallucinated or misattributed.
**Gate:** bibliography and inline citations are verified.

### Stage 12 — Submission readiness → `submission-readiness-audit`
Check completeness, formatting, claims-vs-evidence, reproducibility statements against venue requirements.
**Gate:** the draft passes a pre-submission audit.

### Stage 13 — Target a venue → `venue-targeting`
Match the paper to a venue and tune framing/scope to its norms (can also inform earlier stages if run sooner).
**Gate:** a target venue chosen and the paper framed for it.

### Stage 14 — Rebuttal → `reviewer-response-strategist`
After reviews, plan the response strategy and any additional experiments.
**Gate:** a response plan addressing each reviewer's load-bearing concern.

### Stage 15 — Release artifacts → `artifact-release-packager` (+ `reproducibility-audit`)
Decide what to release and package it; audit that results actually reproduce.
**Gate:** an artifact release that supports the paper's claims and reproduces its key results.

## Router Rules

- **Delegate, don't duplicate.** Each stage hands to a singleton; this file owns sequencing and gates.
- **Resume, don't restart.** Enter at the project's real stage; pick up at the last unmet gate.
- **Hard gate before stage 10.** No section-writing until the argument/spine (stage 9) is stable — drafting on an unstable contribution wastes the most time.
- **Loop backward freely.** Weak results (7) can send the project back to design (4) or even reframe (2). Going backward is normal, not failure.
- **Venue can move earlier.** If the deadline is fixed, run stage 13 up front so its norms shape scope and baselines.
- **Stop at the user's goal.** Not every project needs stages 13–15 in one pass.
