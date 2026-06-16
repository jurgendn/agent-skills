---
name: beamer-academic-deck
description: >-
  Build a compile-ready LaTeX Beamer deck for an academic talk — conference presentation, seminar/colloquium, invited talk, job talk, thesis defense, or a lecture. Use whenever the user wants actual Beamer code for a presentation: "make me Beamer slides", "turn this paper/section into Beamer", "write the .tex for my conference talk", "I need slides for my seminar", "build lecture slides in Beamer", "generate a Beamer deck from these results". Works in two phases — first a per-slide spec, then compile-ready .tex. For deciding the talk's narrative, pacing, and what to cut, use research-talk-planner first (this skill renders that plan into Beamer). For proposals/progress reports in Beamer use beamer-proposal-report-deck; for PowerPoint/Canva business decks use business-report-deck.
---

# Beamer Academic Deck

Produces compile-ready LaTeX Beamer source for academic talks and lectures. This skill is the **render** step — it governs how content lands on slides (the *medium*). Three upstream concerns are handled elsewhere and assumed (or done inline, lightly, when missing):

- **Narrative & pacing** (the one takeaway, the arc, time budget, what to cut) → `research-talk-planner`.
- **Per-slide structure & design rules** (the slide-spec, claim-titles, density) → `slide-design-principles`.
- **Content reasoning** (how to actually explain a method or idea — the pressure it responds to, intuition before formalism, math as justification, the fundamental tradeoff) → `professor-mentor-technical-teaching`.

These compose as layers, they do not compete: `professor-mentor-technical-teaching` decides *what the right explanation is*; this skill *compresses that explanation to the medium*. The professor layer is the source for the substance of teaching-oriented slides (lecture content, the seminar idea/method movement); it is **not** a deck structure — never expand its eight-stage arc onto eight dense slides. Pull its reasoning into a slide's `Message` and `Notes`, then cut to one signal per frame.

If the user has a talk plan, ingest it. If not, do a fast version of the planning questions below before writing any LaTeX.

---

## Genres this skill covers

| Genre | Length | Emphasis | Theme default |
|---|---|---|---|
| Conference talk | 12–20 min | One contribution, clean and fast | `metropolis` or clean `default` |
| Seminar / colloquium | 45–60 min | Build understanding, room for detail | `metropolis` |
| Invited / job talk | 45–60 min | Research program, taste, depth | `metropolis`, custom title |
| Thesis defense | 30–45 min | Mastery of a body of work | institutional theme if required |
| Lecture | 50–90 min | Pedagogy, worked examples, repetition | high-contrast, large fonts |

Lectures differ from talks: they prioritize learning over persuasion. Expect section recaps, worked examples, "check your understanding" slides, and tolerable redundancy. Talks prioritize a single memorable message and ruthless cutting.

**How much to lean on the content-reasoning layer, by genre:**

| Genre | Use of `professor-mentor-technical-teaching` |
|---|---|
| Lecture | Heavily. The lecture *is* teaching — reason about every concept in professor-mode (intuition first, worked examples, critical analysis), then slice onto slides. |
| Seminar / colloquium | On the idea/method movement — name the pressure the method responds to, build intuition before the equations, surface the fundamental tradeoff. |
| Invited / job talk | Lightly, on the method slides only; the deck's job is taste and program, not re-derivation. |
| Conference talk | One compressed insight per the talk arc; the full critical-analysis arc lives in Q&A prep, not on slides. |
| Thesis defense | On the core method(s) the committee will probe; keep depth in backup slides. |

---

## Workflow

### 1. Gather inputs (fast)
- Source material: paper, section, results, or a `research-talk-planner` plan.
- Genre + exact time slot.
- Audience (subfield specialists / broad ML / mixed / students).
- Theme/branding constraints (institutional template? color? logo?).
- Math density (talk-light vs. proof-heavy seminar).

If there's no plan and the talk is non-trivial, state the **one takeaway** in a sentence and a rough time budget before proceeding. Don't silently invent an arc — surface it for confirmation.

### 2. Build the slide-spec
Produce the per-slide spec from `slide-design-principles` (one block per frame). Pacing: **~1 slide/minute** as default; fewer slides with more time beats more slides rushed. Use claim-titles. Mark each visual's provenance (reuse paper figure / new TikZ / table / chart).

For any **method / idea / concept** slide — and across a whole **lecture** — reason about the content with `professor-mentor-technical-teaching` *before* compressing it:

- Name the **pressure** the method responds to; that becomes the slide's `Message`, not "Method overview".
- Put **intuition before formalism**: an intuition slide (or build) precedes the equation slide; introduce notation before the symbols appear.
- Earn every equation — it should answer "what is optimized / bounded / approximated / traded off". If it does no argumentative work on the slide, move it to `Notes` or a backup slide.
- Carry the **fundamental tradeoff** and one failure mode into the spec (often a single slide near the close, or Q&A prep) — don't present a method as universally good.
- The full reasoning lives in `Notes` (what you'll *say*); the frame shows only the one signal.

Confirm the spec with the user before emitting LaTeX.

### 3. Emit compile-ready .tex
Render the approved spec to Beamer. Requirements:

- A complete, self-contained document that compiles with `pdflatex`/`lualatex` out of the box (use `assets/preamble.tex` as the base).
- One `frame` per spec block; the spec `title` becomes the `frametitle`.
- `\pause` / overlay specs (`\onslide<>`, `\only<>`) for any `Build` steps.
- Speaker `Notes` become `\note{...}` (with `\setbeameroption{show notes}` commented out for easy toggling), never on-slide text.
- Figures via `\includegraphics` with a clear `\graphicspath`; placeholder boxes (`\fbox`/`tikz`) where a file isn't supplied yet, clearly marked `% TODO: replace placeholder`.
- Tables sized for projection (`\small`/`\footnotesize`, `booktabs`).
- Math built incrementally where the spec calls for it.

### 4. Hand off
Tell the user: the compile command, which figure files to drop in, and where to toggle speaker notes. Offer a backup-slides appendix section for anticipated Q&A.

---

## Beamer specifics that matter

- **Theme**: default to `metropolis` (clean, modern, low-chrome). Fall back to stock `default` + a sober color theme if `metropolis`/`pgfplots` aren't available; note the package dependency.
- **Fonts**: large enough to project. Avoid the default tiny block text; `metropolis` handles this. For lectures bump base size.
- **Overlays**: prefer `\onslide`/`\only` over piling everything with `\pause` when ordering matters. Overlays should reveal logic (baseline → ours), not animate for flair.
- **Figures**: never `\includegraphics` a paper figure at paper density — note in the spec when a figure must be simplified/re-exported for the slide.
- **Sections**: `\section{}` + a `\tableofcontents[currentsection]` recap is good for seminars/lectures, overkill for a 15-min conference talk.
- **Title slide**: title, author, affiliation, venue+date. Job/invited talks may add a one-line research-vision subtitle.
- **Closing**: a take-home claim slide (the one takeaway restated), then leave a "Questions?" / title slide up for Q&A — not a bullet summary.
- **Reproducibility**: the deck must compile with no manual edits beyond dropping in figure files.

See `assets/preamble.tex` for a ready preamble (theme, fonts, math, `booktabs`, `tikz`, notes toggle, claim-title styling).

---

## Anti-patterns to refuse

- Pasting whole paragraphs / paper abstract onto a frame.
- One frame trying to carry the whole method.
- Label-titles (`Results`, `Method`) instead of claim-titles.
- Animations/transitions with no explanatory purpose.
- Importing every paper figure unchanged at paper resolution.
- Expanding the `professor-mentor-technical-teaching` eight-stage arc into eight dense slides — that arc is for prose; on slides it must be compressed to one signal per frame, with the depth in `Notes`/backup.

---

## Output

1. The confirmed slide-spec (markdown).
2. A single compile-ready `.tex` (plus the preamble), with placeholders clearly marked.
3. Compile + figure-drop + notes-toggle instructions.
