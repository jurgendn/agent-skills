---
name: business-report-deck
description: >-
  Build a business / industrial report deck in PowerPoint or Canva — executive summaries, stakeholder updates, project/pilot results, quarterly business reviews, R&D-to-business reports, client deliverables, and internal decision decks for a non-academic audience. Use when the user wants PowerPoint or Canva (not LaTeX/Beamer) slides aimed at executives, managers, or clients, organized around situation/recommendation/impact rather than a paper's contribution: "make a PowerPoint report", "build a .pptx for the leadership review", "executive deck for our pilot results", "industrial report slides", "QBR deck", "Canva slides for the client". Two phases — slide-spec, then a real .pptx via the python-pptx builder (or import-ready content + a design spec for Canva). For academic talks/lectures use beamer-academic-deck; for proposal/report decks in LaTeX use beamer-proposal-report-deck.
---

# Business / Industrial Report Deck

Produces decks for a **business audience** — executives, managers, clients, cross-functional stakeholders — in **PowerPoint** (generated as a real `.pptx`) or **Canva** (import-ready content plus a design spec, since Canva files can't be generated programmatically). The audience cares about decisions, impact, risk, and next steps, not methodological novelty.

This is the render step for non-LaTeX decks. It reuses the slide-spec and design rules from `slide-design-principles`. For academic LaTeX decks use the `beamer-*` skills instead.

---

## What a business deck is for

A business deck answers, in order: **What's the situation? What should we do? What happens if we do (or don't)?** Lead with the answer; supporting detail follows. This is the opposite of a paper's build-up-to-the-result structure — executives read top-down and may stop after slide 3.

Two framings that work; pick one and keep it:

- **SCQA** — Situation → Complication → Question → Answer. Good for problem/recommendation decks.
- **Pyramid (answer-first)** — Recommendation up front, then grouped supporting arguments, then evidence. Good for decision and QBR decks.

---

## Common genres & spines

| Genre | Spine |
|---|---|
| Executive summary / decision deck | Recommendation → why → impact → risks → ask |
| Pilot / project results report | Goal → what we did → results vs. target → what it means → next step |
| Quarterly business review (QBR) | Headline metrics → wins → misses → drivers → plan |
| R&D-to-business report | Problem & opportunity → approach (plain language) → evidence → business impact → roadmap/ask |
| Client deliverable | Objectives → findings → recommendations → implementation plan → appendix |

Every spine opens with a **single executive-summary slide** that stands alone — if that's all someone reads, they get the decision and the why.

---

## Workflow

### 1. Gather inputs
- Target tool: **PowerPoint** (`.pptx`) or **Canva**.
- Genre, audience seniority, and the **one decision/action** the deck should drive.
- The numbers: metrics, targets, results, costs/benefits, timeline.
- Branding: template/theme colors, logo, fonts (a corporate `.pptx` template to start from?).

### 2. Build the slide-spec
Use the genre spine, then per-slide spec blocks (`slide-design-principles`), with business-specific emphasis:

- **Slide 1 after title = executive summary**: the recommendation + 2–3 reasons + the ask. Self-contained.
- **Claim-titles as business outcomes**: "Pilot cut handling time 31% — recommend full rollout", not "Pilot Results".
- **One chart per slide**, the chart *is* the argument (bar/line/waterfall), labeled with the takeaway, minimal chrome.
- **Quantify impact in business units**: time, cost, revenue, risk, satisfaction — not just model metrics. Translate accuracy/F1 into dollars/hours when possible.
- **Risks & next steps** are mandatory closing slides; executives want the downside and the ask.
- Detailed methodology, full tables, and technical depth go to an **appendix**.

Confirm the spec before generating the artifact.

### 3a. Emit the .pptx (PowerPoint)
Render the approved spec to a real PowerPoint file with `scripts/build_pptx.py`:

- Write the spec to a `slides.json` (schema documented in the script header).
- Run the builder; it produces `deck.pptx` with title, section, bullet, chart-placeholder, and table layouts, claim-titles, consistent theme colors, page numbers, and speaker notes.
- If a corporate `.pptx` template is supplied, pass it as the base so brand fonts/colors/master are inherited.
- Charts: the builder inserts native PowerPoint charts when given data, or a labeled placeholder otherwise (so the user can paste a branded chart).

### 3b. Canva path
Canva has no file-generation API, so deliver:
- **Import-ready content**: a clean, per-slide text outline (title + body + notes) the user can paste into Canva, plus the exact chart data.
- **A design spec**: recommended Canva template style, color hex codes, font pairing, layout per slide type, and where each visual goes.
- Optionally, generate the same deck as `.pptx` (step 3a) — Canva can import a `.pptx` and apply a template, which is usually the fastest route to a branded Canva deck. Offer this.

### 4. Hand off
PowerPoint: how to open, where to swap in branded charts/logo, where notes live, what's in the appendix. Canva: the import/paste steps and the design spec.

---

## Business-deck rules that differ from academic decks

- **Answer first.** Never make an executive sit through motivation to reach the recommendation.
- **Speak business, not model.** "94% precision" means nothing to a VP; "cuts false alerts by ~2,000/month, freeing ~3 FTE" does.
- **One message, one chart, one number per slide.** Density reads as "not yet decision-ready".
- **Make the ask explicit.** End with the decision, resource, or approval you need.
- **Appendix is your friend.** Depth lives there; the main line stays at decision altitude.

---

## Anti-patterns to refuse

- Burying the recommendation on slide 12.
- Reporting model metrics with no business translation.
- A title slide followed by methodology before any result or recommendation.
- Dense multi-chart slides copied from an analysis notebook.
- No risks slide, no explicit ask.

---

## Output

1. The confirmed slide-spec (markdown), on a business spine, answer-first.
2. **PowerPoint**: `slides.json` + a generated `deck.pptx` (via `scripts/build_pptx.py`), with marked placeholders and speaker notes.
   **Canva**: import-ready per-slide content + chart data + a design spec (and optionally the `.pptx` for import).
3. Hand-off instructions (branding swap-in, appendix contents, Canva import steps).
