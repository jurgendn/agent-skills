---
name: beamer-proposal-report-deck
description: Build a compile-ready LaTeX Beamer deck for a research proposal or a research report — grant/PhD/project proposal defenses, thesis-proposal talks, progress/milestone reviews, mid-term/final project reports, and committee or funder updates. Use when the user wants Beamer slides organized around objectives, work packages, timeline/Gantt, milestones, deliverables, budget, risks, and progress-vs-plan rather than a single paper's contribution: "Beamer slides for my proposal defense", "progress report deck in LaTeX", "milestone review slides", "PhD proposal presentation", "project final report in Beamer". Two phases: slide-spec, then .tex. For a single paper's results talk use beamer-academic-deck; for PowerPoint/Canva executive reports use business-report-deck; for narrative/pacing of a talk use research-talk-planner.
---

# Beamer Proposal / Report Deck

Produces compile-ready Beamer source for **proposals** (what you intend to do and why it's fundable/approvable) and **reports** (what you did versus what you promised). These genres are structured around a plan-of-work, not a single contribution — they need objectives, work packages, timelines, milestones, deliverables, budget, and risk, and reports add progress-vs-plan.

This is the render step. It reuses the slide-spec and design rules from `slide-design-principles`. It is *not* `beamer-academic-deck` (single-paper results talk) and *not* `business-report-deck` (PPTX/Canva, executive audience).

---

## Two genres, different spines

### Proposal deck
Audience: committee / funder / advisor deciding whether to approve or fund. They evaluate significance, feasibility, and the credibility of the plan.

Spine:
1. **Problem & significance** — why this matters, why now.
2. **Gap / state of the art** — what's missing; what you'll do that others haven't.
3. **Objectives / research questions** — 2–4 crisp, testable aims.
4. **Approach / methodology** — per objective, how you'll attack it.
5. **Preliminary results** — evidence you can pull this off (de-risks the ask).
6. **Work plan & timeline** — work packages mapped to a Gantt.
7. **Milestones & deliverables** — concrete, dated, verifiable.
8. **Risks & mitigations** — name the real ones; show you've thought ahead.
9. **Budget / resources** (if applicable) — what you need and why.
10. **Expected impact & summary** — what success unlocks.

### Report deck (progress / milestone / final)
Audience: same stakeholders, now checking delivery against the promise.

Spine:
1. **Recap of objectives** — what was promised (one slide).
2. **Progress vs. plan** — status per objective/work package (on track / at risk / done).
3. **Key results so far** — the evidence, claim-titled.
4. **Milestones hit / missed** — honest status table.
5. **Deviations & why** — changes from the plan and their justification.
6. **Risks (updated)** — what materialized, what's new.
7. **Remaining work & revised timeline** — what's left, by when.
8. **Budget/resource status** (if applicable) — burn vs. plan.
9. **Summary & ask** — decision or support you need next.

---

## Workflow

### 1. Gather inputs
- Genre (proposal / progress / mid-term / final).
- The plan-of-record: objectives, work packages, original timeline, milestones, deliverables, budget.
- For reports: current status per item, what slipped and why.
- Audience and slot length; institutional/funder Beamer template if mandated.

### 2. Build the slide-spec
Use the relevant spine above as the skeleton, then produce per-slide spec blocks (`slide-design-principles`). Genre-specific guidance:

- **Objectives** get claim-titles framed as outcomes, not topics.
- **Timeline** → one Gantt slide (TikZ `pgfgantt`), not a wall of dates.
- **Milestones/deliverables** → a compact status table (`booktabs`), ≤ 6 rows visible; overflow to backup.
- **Risks** → a 2-column "risk → mitigation" (or likelihood/impact) table, top risks only.
- **Progress (reports)** → a status table with a clear legend (✓ done / ◐ on track / ✗ at risk), color-coded but never color-only.
- **Budget** → summarize categories; full breakdown goes to backup.

Confirm the spec before emitting LaTeX.

### 3. Emit compile-ready .tex
Render the approved spec using `assets/preamble.tex` (adds `pgfgantt`, status macros, and a risk/milestone table style on top of the academic preamble). Requirements:

- Self-contained, compiles with `pdflatex`/`lualatex`; placeholders clearly `% TODO`-marked.
- Gantt chart built with `pgfgantt`; milestone/deliverable/risk tables with `booktabs`.
- Status macros (`\done`, `\ontrack`, `\atrisk`) that pair a symbol with a color (colorblind-safe).
- Speaker notes via `\note{}`; section recap via `\tableofcontents[currentsection]` for longer reviews.
- A backup-slides appendix for detailed budget, full milestone list, and method depth.

### 4. Hand off
Give the compile command, the files to drop in, where to edit dates/numbers, and which detail slides live in the appendix.

---

## What separates good proposal/report decks from paper talks

- **The plan is the product.** A vague timeline or hand-wavy milestones sink a proposal faster than a weak result. Make every milestone dated and verifiable.
- **Feasibility beats novelty here.** Preliminary results exist to show you can execute, not to be a full contribution.
- **Reports must be honest about slippage.** A status table that hides "at risk" items destroys trust; show them with the mitigation.
- **Numbers are checkable.** Budget, timelines, and milestone dates will be scrutinized — keep them consistent across slides.

---

## Anti-patterns to refuse

- Objectives written as topics ("Study X") instead of testable aims with success criteria.
- A timeline slide that's a paragraph of dates instead of a Gantt.
- A report that buries missed milestones or omits the progress-vs-plan view.
- Cramming the full budget/work-package detail onto main slides instead of backup.

---

## Output

1. The confirmed slide-spec (markdown), built on the proposal or report spine.
2. A single compile-ready `.tex` (plus preamble) with Gantt, status tables, and marked placeholders.
3. Compile + edit + appendix instructions.
