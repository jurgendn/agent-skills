---
name: flow-paper-lifecycle
description: >-
  Orchestrate a research paper end-to-end — from raw idea through literature grounding, experiment design, implementation, results, writing, submission, rebuttal, and artifact release. Use whenever the user wants to drive a whole paper rather than one stage: "help me write this paper from scratch", "where am I in the paper process", "what should I do next on this project", "take this from idea to submission", "I have results, get me to a draft", "manage my paper workflow", or hands over a project and asks for the path to a venue. Also use it for the writing phase itself — "draft the introduction", "outline this paper", "how should I structure this", "turn this spine into a draft", "my first paper" — which it owns as a phase-gated stage-group (stage 10) rather than delegating. This is otherwise a ROUTER that sequences existing singleton skills with stage gates; it does not do the ideation or experiments itself. For a single narrow section, invoke that section's skill directly (e.g. abstract-and-intro-writer, method-section-writer, results-writeup). For PhD application packages use flow-phd-application. For talks/decks use the presentation skills.
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
Structure the codebase for fast hypothesis testing and implement the runs. When a run misbehaves — divergence, collapse, suspicious gains, a suspected data-path bug, or "which knob next" — go back to `experiment-design`, whose diagnostic pass checks the data path before blaming the model.
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

### Stage 10 — Write sections (the writing stage-group)

This stage is owned here rather than delegated: it is a phase-gated writing
coach in four sub-phases. Do not draft ahead of the current gate unless the user
explicitly overrides it. Delegate narrow section work outward as noted.

Ask the target venue type **once** — theorem-proof mathematics, ML conference,
or hybrid/applied — and branch the skeleton: math papers foreground definitions,
theorem statements, proof architecture and relation to known results; ML papers
foreground contribution bullets, method, experiments, ablations, baselines,
reproducibility and limitations; hybrid papers keep *both* theorem and empirical
claims in the claims-to-evidence map rather than letting one hide the other.

Load reference files progressively: `references/writing-structure.md` (10a),
`references/writing-drafting.md` (10b), `references/writing-math-prose.md`
(10c), `references/writing-logistics.md` (10d), and
`references/writing-evidence.md` whenever giving citation/readability/title/
abstract advice.

**Evidence flags.** Every writing recommendation carries one: **[EXPERT]**
(craft consensus, not empirically established), **[SUPPORTED]** (empirical
backing exists), **[CONTESTED]** (evidence conflicts or is field-specific),
**[REFUTED]** (folklore contradicted by data). Never present an [EXPERT] rule as
an empirical fact; when unsure, mark it [EXPERT] or say the evidence level is
unknown.

**10a — Story and skeleton.** Force one contribution sentence before drafting
anything: *"This paper shows/proposes/proves/introduces that `<new thing>` by
`<core mechanism/evidence>`."* If the user can't state it, stop and work only on
that sentence. Build a claims-to-evidence map (claim → supporting
evidence/proof/result → section). Draft only the introduction *skeleton*, not
polished prose. [EXPERT]
**Gate 10a:** one-sentence contribution exists; every contribution has a
supporting section; a reader of only the intro could state what is new.

**10b — Drafting.** Draft the technical core first, then results, then
introduction, and the abstract last. Separate generation from revision — leave
placeholders rather than polishing or chasing fact-checks mid-draft. After
drafting section N, run the Halmos spiral: rewrite sections 1..N−1 in light of
what N revealed. Delegate to `abstract-and-intro-writer` (abstract+intro stay a
pair), `method-section-writer`, `related-work-writer` (sourced from the stage-3
map, never from memory), and `results-writeup` for verified numeric prose.
[EXPERT]
**Gate 10b (per section):** the section states its purpose in the first
paragraph; it has no forward dependency on unwritten material except an explicit
placeholder; its claims appear in the claims-to-evidence map.

**10c — Mathematical prose pass.** Build a notation table (symbol, meaning,
type/domain, first definition, collisions). Define every symbol before use.
Replace vague "any" with "each"/"every" where quantification is universal. Make
every theorem statement self-contained — hypotheses belong in the statement, not
only in the preceding paragraph. Give every nontrivial proof a one-sentence
proof-idea line. For every "it is easy to see", "clearly", or "by a standard
argument": justify it, cite it, or delete it. [EXPERT]
**Gate 10c:** notation table complete; zero undefined symbols; every theorem
re-readable in isolation; every clearly/easy/standard claim justified, cited, or
removed.

**10d — Draft handoff.** Check venue fit before final formatting (scope,
audience, page limit, style file, anonymity, supplement rules, deadline). Run
coauthor sign-off: freeze the version, list open risks, request explicit
approval, no surprise authorship changes. For journals, prepare a concise cover
letter stating fit and contribution without re-arguing the paper. For ML venues,
attach a reproducibility checklist (code/data, seeds, hardware,
hyperparameters, splits, eval scripts, licenses, compute). [EXPERT]
**Gate 10d:** a complete draft whose sections all serve the spine, with venue
fit, coauthor sign-off, and reproducibility artifacts recorded.

On gate failure, return a compact pass/fail checklist and **quote the exact
offending text** for each failure; if an artifact is missing, quote the missing
item name instead.

### Stage 11 — Audit citations → `citation-auditor`
Verify references exist, claims match sources, nothing is hallucinated or misattributed.
**Gate:** bibliography and inline citations are verified.

### Stage 12 — Submission readiness → `submission-readiness-audit` (+ `professor-critic`)
Check completeness, formatting, claims-vs-evidence, reproducibility statements against venue requirements. For OpenReview-era ML/NLP/CV/AI venues, make the audit explicitly cover reviewer-visible risks: unsupported claims, vague novelty, missing named baselines, reproducibility gaps, limitations/ethics issues, data attribution, and citation reliability. Then run the *adversarial* pass the checklist can't do: hand the draft to `professor-critic` with the named reader "Reviewer 2 at the target venue who works on the competing method" and the bar "accept / major-revision / reject" — a verdict-first teardown that surfaces the FATAL objection *before* the real reviewer does. (`submission-readiness-audit` checks the paper against requirements; `professor-critic` simulates the hostile reader. Not `peer-review-writer` — that is for reviewing *others'* papers.)
**Gate:** the draft passes the pre-submission audit **and** survives an adversarial reviewer pass with no unaddressed FATAL.

### Stage 13 — Target a venue → `venue-targeting`
Match the paper to a venue and tune framing/scope to its norms (can also inform earlier stages if run sooner).
**Gate:** a target venue chosen and the paper framed for it.

### Stage 14 — Rebuttal → `reviewer-response-strategist`
After reviews, plan the response strategy and any additional experiments. For OpenReview-style discussion periods, answer the load-bearing concerns, acknowledge resolved points, update claims or experiments when evidence changes, and avoid moving the goalposts.
**Gate:** a response plan addressing each reviewer's load-bearing concern.

### Stage 15 — Release artifacts → `artifact-release-packager` (+ `reproducibility-audit`)
Decide what to release and package it; audit that results actually reproduce.
**Gate:** an artifact release that supports the paper's claims and reproduces its key results.

## Router Rules

- **Delegate, don't duplicate.** Each stage hands to a singleton; this file owns sequencing and gates. **Stage 10 is the one exception** — the writing phase is owned here, because its gates and the pipeline's gates are the same gates; it still delegates narrow section work outward.
- **Resume, don't restart.** Enter at the project's real stage; pick up at the last unmet gate.
- **Hard gate before stage 10.** No section-writing until the argument/spine (stage 9) is stable — drafting on an unstable contribution wastes the most time.
- **Loop backward freely.** Weak results (7) can send the project back to design (4) or even reframe (2). Going backward is normal, not failure.
- **Venue can move earlier.** If the deadline is fixed, run stage 13 up front so its norms shape scope and baselines.
- **Reviewing someone else's paper is a different route.** If the user is acting as a reviewer, hand off to `peer-review-writer`.
- **Stop at the user's goal.** Not every project needs stages 13–15 in one pass.
