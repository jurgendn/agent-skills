# TODO

Backlog for the agent-skills ecosystem. Source: learning-to-learn audit handoff
(2026-07-07). Items are independent — pick per session. Status markers: `[ ]` open,
`[~]` in progress / partially done, `[x]` done.

## Done this session (2026-07-20) — skill pruning, 98 → 84

Rationale (recorded in CLAUDE.md at each affected directory): remove skills that
re-order default agent behavior; keep skills that constrain it. The 2026-05-30/31
batch averaged ~250 words and mostly restated what a capable model already does.

- [x] Removed the deep-learning-experimentation/ family (6). Its real content —
  symptom classification, data-path-before-model ordering, mechanism-wise tuning —
  folded into `experiment-design`, whose description now also carries the
  diagnostic triggers. scaling-law-tracker's 257-line `fit_scaling_law.py`
  (selftest passes) was **preserved** into `experiment-design/scripts/`.
- [x] Removed 4× `python-*` + debugging-strategies (5). `coding-support/` now
  holds `prompting-claude-models` only.
- [x] Merged theory-derivation-auditor → `theorem-and-claim-audit` as a
  step-by-step derivation section; 14 references repointed.
- [x] Merged paper-writer → `flow-paper-lifecycle` stage 10 as a four-sub-phase
  writing stage-group (10a–10d) with gates; its 5 reference files moved to
  `references/writing-*.md`.
- [x] Dissolved deck-design-principles into a per-builder
  `references/slide-spec-and-design.md` in all three `deck-*` skills, removing the
  last sibling→sibling hard dependency.
- [x] Fixed dead references found en route: ai-writing-detector (absent from
  repo), a dangling `references/openreview-era-reviewing.md`, and the missing
  `benchmark-and-baseline-selector` README entry — three of PR 1.1's items.

**Open follow-up:** dissolving deck-design-principles dropped its direct-use
entry point ("is this slide too busy", "fix the visual hierarchy") — tool-agnostic
slide feedback now has no triggering home. Decide whether to give that trigger to
`deck-beamer-academic` as the default or leave it out.

## In flight

- [~] **Calibrate `professor-critic`** — skill is authored, registered, and wired in
  (see below); still needs one live run against a *real* artifact to tune harshness,
  verify the FATAL/MAJOR/MINOR ranking, and check the blame-the-artifact line lands.
  Candidates: Wei Jin cold email (reader: busy PI triaging inbox; bar: reply/delete),
  DIAL EDA paragraph (reader: co-author Ngoc Chi Le; bar: sign off/send back),
  RWOT-DCD proof step (reader: Ha Duong at whiteboard; bar: does the line follow).
  Blocked on: user supplying an artifact.

## Done this session (2026-07-09)

- [x] Added spaced, variable-cue re-probes to `knowledge-debt-audit` and old-error
  spacing to `ielts-progress-reporter`.
- [x] Built and registered `naive-student`; wired it into knowledge-debt repayment,
  `flow-learn-new-topic`, and `flow-deep-understanding`.
- [x] Built and registered `whiteboard-peer`; wired it into `flow-idea-to-proof` and
  `flow-deep-understanding`.
- [x] Added the weekly lemma-autopsy mode to `gap-finder`.
- [x] Moved the learning-principles rationale and references into
  `DESIGN-PHILOSOPHY.md`, covering retrieval, spacing, interleaving, and
  productive-failure practice.

## Done previously (2026-07-07)

- [x] Authored `professor-critic` in `skills/research-skills/technical-teaching/` —
  the strict-professor *grading* instrument (finished artifact + named reader +
  acceptance bar → verdict-first FATAL/MAJOR/MINOR teardown). Registered in all three
  registries (CLAUDE.md, README.md, skills.json) and evals seeded.
- [x] Wired `professor-critic` into: `flow-paper-lifecycle` stage 12 (adversarial
  Reviewer-2 pass), the `paper` template AGENTS.md, `flow-phd-application` stages 4 & 6
  (optional reader's-eye pass on SOP / cold email), and the `phd-application` template
  AGENTS.md.

## New skills to build (the role-coverage family)

The metacognitive layer in `technical-teaching/` is a role family. Professor role is
now staffed; these two close the gaps. Both belong in `technical-teaching/`; update
all three registries and keep the CLAUDE.md layer-boundary paragraph in sync.

- [x] **`naive-student`** — learning-by-teaching / protégé effect. User explains a
  concept; the student asks honestly-naive but structurally-pointed questions, gets
  confused precisely where the explanation is underspecified (confusion *earned* from
  the actual words, never scripted), never fakes comprehension (anti-sycophancy), and
  ends with a "what I think you said" playback whose errors localize the gaps. Also the
  debt-repayment route `knowledge-debt-audit` should hand off to ("repay by teaching").
  - [x] After building: wire into `flow-learn-new-topic` / `flow-deep-understanding`
    exits and add the `knowledge-debt-audit` → `naive-student` repayment hand-off.
- [x] **`whiteboard-peer`** — idea-stage co-solver for the unfinished middle.
  Contributes its own partial, possibly-wrong attempts and commits to positions;
  *mandated to disagree* (sociocognitive conflict, not comfort-matching); hard rule
  against sliding into full-solution assistant mode; fires before any artifact exists
  (complement, not overlap, to `professor-critic`).
  - [x] After building: wire into `flow-idea-to-proof` (idea stage) and
    `flow-deep-understanding`.

## Extensions to existing skills

- [x] **Spaced re-probe for `knowledge-debt-audit`** (handoff Item 2 — highest effect
  size). Ledger-level change, not a new skill: add `due_date` + `interval_stage`
  columns to `debt-ledger.yaml`; a debt marked repaid schedules re-probes at expanding
  intervals (~1w → ~1m → ~3m); **variable-cue rule** — never reuse a probe verbatim,
  rotate the angle across re-probes (transfer → boundary → perturbation →
  load-bearing-why); PERIODIC mode surfaces overdue re-probes at session start. Same
  spacing principle applies to `ielts-progress-reporter` (pull old errors back on a
  schedule, not only recent ones).

## Protocols / lighter items

- [x] **Lemma-autopsy habit** (handoff Item 5) — one referee-style teardown per week:
  take a lemma from an in-scope paper (spectral graph theory / community detection /
  GNN theory), find the step that breaks under a weakened hypothesis *before* reading
  the authors' discussion. Trains other-directed diagnosis. Could live as a recurring
  protocol inside `gap-finder` rather than a new skill.
- [x] **Evidence → practice one-pager** (handoff Item 6) — distill Dunlosky 2013 +
  Carpenter 2022 onto two concrete systems: (a) IELTS vault (already retrieval-based;
  add the spacing schedule); (b) measure-theory roadmap (productive-failure protocol:
  attempt each theorem before reading its proof; interleave earlier material — modes
  of convergence are the canonical blocked-study trap).

## Standing constraints (apply to every item above)

- Skill house style: YAML frontmatter with a pushy `description`; verdict-first output
  contracts; named anti-failure-modes; explicit "when NOT to fire"; hand-offs section.
  References: `knowledge-debt-audit`, `professor-critic`.
- Ground every literature claim via `literature-triangulation` before asserting.
- Keep each skill self-contained (no cross-skill file links); orchestrators/templates
  may *name* sibling skills — that is how routing works.
- After any skill add/edit/remove, re-sync CLAUDE.md + README.md + skills.json.
