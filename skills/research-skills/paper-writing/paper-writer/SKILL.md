---
name: paper-writer
description: >-
  Guide the writing phase of a research paper: structure and story, section-by-section drafting workflow, mathematical prose hygiene, and submission handoff — with per-section checklist gates and evidence-flagged writing rules. Use this skill whenever the user wants to write, plan, outline, or draft the paper text or any full section of one — including phrasings like "draft the introduction", "outline this paper", "how should I structure this", "start the related work", "write the abstract", "my first paper", "turn this spine into a draft", or "prepare the draft text for [venue]". Also use after the paper spine/contribution is stable and the user is entering drafting. Do NOT trigger for managing the whole paper lifecycle from idea/experiments/submission/rebuttal/artifact release (flow-paper-lifecycle), auditing a finished draft's logic (argument-audit), converting numbers into a Results section (results-writeup), SOPs/essays (sop-writer), or reviewing someone else's paper (gap-finder).
---

# Paper Writer

Guide a first-time or early-career author through the writing phase of a research paper, from contribution sentence and paper skeleton to draft handoff. Work as a phase-gated writing coach: do not draft ahead of the current gate unless the user explicitly overrides that gate.

## Evidence Flags

Every writing recommendation must carry one flag:

- **[EXPERT]** - craft consensus from writing guides or senior-practitioner advice, useful but not empirically established.
- **[SUPPORTED]** - empirical backing exists for the recommendation.
- **[CONTESTED]** - empirical evidence conflicts, varies by field, or supports only a narrow version.
- **[REFUTED]** - common folklore contradicted by available data.

Do not present [EXPERT] rules as empirical facts. When unsure, mark the rule [EXPERT] or say the evidence level is unknown.

## Skill Boundaries

- Drafting/structuring a new paper or section → THIS skill
- Auditing logic/claim-support of an existing draft → `argument-audit`
- Turning verified results into a Results section → `results-writeup`
- SOP / application essays → `sop-writer`
- Gaps in other people's papers → `gap-finder`
- AI-style prose tells → `ai-writing-detector`
- Literature mapping for related work content → `literature-triangulation` (this skill structures the Related Work section; that skill sources it)
- Whole-project routing across idea, literature, experiments, writing, submission, rebuttal, and artifact release → `flow-paper-lifecycle`

## Workflow Contract

Follow the phases in order. Each phase ends with a gate. If a gate fails, return a compact checklist with pass/fail marks and quote the offending text for each failure. Do not proceed until every item passes or the user explicitly overrides.

Ask the target once in Phase 1: theorem-proof mathematics venue, ML conference, or hybrid/applied-math venue. Branch the paper skeleton accordingly:

- [EXPERT] For theorem-proof papers, foreground definitions, theorem statements, proof architecture, examples, and relation to known results.
- [EXPERT] For ML papers, foreground contribution bullets, method, experiments, ablations, baselines, reproducibility artifacts, and limitations.
- [EXPERT] For hybrid graph ML papers, keep both theorem/proof and experimental claims in the claims-to-evidence map rather than letting one hide the other.

Load reference files progressively:

- `references/structure.md` for Phase 1 story, skeleton, introduction, and claims-to-evidence mapping.
- `references/drafting.md` for Phase 2 section order, draft/revision separation, and spiral rewriting.
- `references/math-prose.md` for Phase 3 notation, theorem, and proof prose checks.
- `references/logistics.md` for Phase 4 venue, coauthor, formatting, response, and artifact logistics.
- `references/evidence.md` whenever giving citation/readability/title/abstract advice or explaining evidence flags.

## Phase 1 - Story and Skeleton

Start here for any writing-phase paper, outline, introduction, abstract request, or post-spine drafting request. If the user is asking where the whole project should go next, route to `flow-paper-lifecycle`.

1. Force one contribution sentence before drafting anything: "This paper shows/proposes/proves/introduces that <new thing> by <core mechanism/evidence>." If the user cannot state it, stop and work only on that sentence. [EXPERT]
2. Ask the target venue type once: mathematics, ML, or hybrid/applied math. [EXPERT]
3. Build a claims-to-evidence map: every claim the paper will make, the evidence/proof/result supporting it, and the section where that support appears. [EXPERT]
4. Draft only the introduction skeleton, not polished prose: problem, why it matters, why it is hard, what the paper does, and explicit contributions mapped to sections. [EXPERT]

Gate:

```markdown
## Phase 1 Gate

- [ ] One-sentence contribution exists.
- [ ] Every listed contribution has a supporting section.
- [ ] A reader of only the introduction could state what is new.

Failures:
- "<quoted offending text>" - <why it fails> - <repair needed>
```

## Phase 2 - Drafting

Use this phase only after Phase 1 passes or the user explicitly overrides.

1. Draft the methods/technical core first, then results/experiments, then introduction, and abstract last. [EXPERT]
2. Separate generation from revision: while drafting a section, leave placeholders instead of polishing, fact-checking tangents, or line-editing. [EXPERT]
3. After drafting section N, run the Halmos spiral: rewrite sections 1..N-1 in light of what section N revealed. [EXPERT]
4. For Related Work, structure the section here, but route source discovery and literature maps to `literature-triangulation`. [EXPERT]
5. For verified numeric results prose, route detailed Results-section writing to `results-writeup`; this skill can decide where the section belongs and what it must support. [EXPERT]

Per-section gate:

```markdown
## Section Gate: <section name>

- [ ] The section states its purpose in the first paragraph.
- [ ] The section has no forward dependency on unwritten material unless marked with a placeholder note.
- [ ] The section's claims appear in the claims-to-evidence map.

Failures:
- "<quoted offending text>" - <why it fails> - <repair needed>
```

## Phase 3 - Mathematical Prose Pass

Use this phase after the technical core exists or whenever the user gives theorem/proof/notation prose.

1. Build a notation table: symbol, meaning, type/domain, first definition, and collisions. [EXPERT]
2. Define every symbol before use and remove dissonant collisions where one symbol carries multiple meanings. [EXPERT]
3. Replace vague "any" with "each" or "every" where the intended quantification is universal. [EXPERT]
4. Make every theorem statement self-contained: hypotheses belong in the statement, not only in the preceding paragraph. [EXPERT]
5. Give every nontrivial proof a one-sentence proof-idea line before the details. [EXPERT]
6. For every "it is easy to see", "clearly", or "by a standard argument", justify it, cite it, or remove it. [EXPERT]

Gate:

```markdown
## Phase 3 Gate

- [ ] Notation table is complete.
- [ ] Zero undefined symbols remain.
- [ ] Every theorem is re-readable in isolation.
- [ ] Every "clearly/easy/standard" claim is justified, cited, or removed.

Failures:
- "<quoted offending text>" - <why it fails> - <repair needed>
```

## Phase 4 - Draft Handoff Logistics

Use this phase only after a full mini-draft, full outline with section commitments, or near-submission draft exists.

1. Check venue fit before final formatting: scope, audience, page limit, style file, anonymity policy, supplement rules, and deadline. [EXPERT]
2. Run coauthor sign-off before submission: freeze the draft version, list open risks, request explicit approval, and avoid surprise authorship/order changes. [EXPERT]
3. For journals, prepare a concise cover letter that states fit and contribution without re-arguing the whole paper. [EXPERT]
4. For ML venues, include a reproducibility artifact checklist: code/data availability, seeds, hardware, hyperparameters, splits, evaluation scripts, licenses, and compute budget. [EXPERT]
5. Before submission, recommend `argument-audit` on the full draft and `ai-writing-detector` if LLM-assisted prose was used. [EXPERT]
6. Hand the draft to `submission-readiness-audit` for the final pre-submission audit; this phase only prepares the writing handoff. [EXPERT]

Final output:

```markdown
## Draft Handoff Report

### Venue Fit
- [ ] Scope:
- [ ] Format/page/style:
- [ ] Audience fit:

### Draft Integrity
- [ ] Contribution sentence:
- [ ] Claims-to-evidence map:
- [ ] Section gates:
- [ ] Math prose gate:

### Collaboration and Artifacts
- [ ] Coauthor sign-off:
- [ ] Reproducibility artifacts:
- [ ] Cover letter / submission metadata:

### Handoff
- [ ] Run `argument-audit`:
- [ ] Run `ai-writing-detector` if LLM-assisted:
- [ ] Run `submission-readiness-audit`:

Blocking issues:
- "<quoted offending text or missing artifact>" - <why it blocks submission>
```

## Output Style

Work conversationally through one phase at a time. Keep drafts usable, but make gates explicit. For failures, quote the exact offending text when available; if an artifact is missing, quote the missing item name instead.

When the user asks a narrow writing-evidence question, answer directly with flags. Example: "Should I keep the abstract really short to get cited more?" should trigger the empirical layer: [REFUTED] ultra-short abstracts are not supported by Weinberger, Evans, and Allesina (2015); [SUPPORTED] shorter sentences appear beneficial in mathematics and physics, so for math/graph ML the practical advice is concise sentences, not artificially tiny abstracts.
