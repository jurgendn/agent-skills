---
name: slide-design-principles
description: >-
  Shared reference for building any slide deck — the slide-spec schema and the design rules (one-signal-per-slide, claim-titles, visual hierarchy, density limits, figure adaptation, color/contrast) that the format-specific deck builders reuse. Use this skill when the user wants general slide-design feedback not tied to a tool ("is this slide too busy", "how do I make this slide clearer", "what should go on this slide", "fix the visual hierarchy"), or load it as the foundation before beamer-academic-deck, beamer-proposal-report-deck, or business-report-deck. This skill defines the per-slide spec those builders fill in; it does not emit .tex or .pptx itself.
---

# Slide Design Principles

This is the shared foundation for every deck builder in this category. It defines two things:

1. The **slide-spec** — a tool-agnostic, per-slide intermediate the builders produce *before* generating any `.tex` or `.pptx`. The spec is where structure is decided and corrected; the artifact is a mechanical render of an approved spec.
2. The **design rules** that apply regardless of format.

Use this skill directly for tool-agnostic slide feedback. Otherwise it is loaded as a dependency by:

- `beamer-academic-deck` — seminar, conference, lecture (LaTeX Beamer)
- `beamer-proposal-report-deck` — proposal, progress/final report (LaTeX Beamer)
- `business-report-deck` — industrial / executive report (PowerPoint via python-pptx, or Canva)

Planning a talk's *narrative and pacing* (what the one takeaway is, what to cut) is a separate, upstream job owned by `research-talk-planner`. This skill and the builders assume that planning is done — or do a lightweight version of it inline when no plan exists.

---

## The slide-spec

Every builder produces this before any code. One block per slide. Keep it in markdown so the user can edit it directly.

```markdown
### Slide N — <one-line working title that is a claim, not a label>
- **Role**: title | agenda | problem | gap | method | result | ablation | timeline | budget | risk | summary | backup
- **Message**: the single sentence this slide must land. If you can't write one, the slide is doing two jobs — split it.
- **Body**: the bullets / equation / statement. Max ~5 lines, ~7 words each. Use "—" for sub-points sparingly.
- **Visual**: figure | diagram | table | none. Describe what it shows and where it comes from (paper Fig. 3, new TikZ, screenshot, generated chart).
- **Build**: (optional) staged reveals — "1) baseline, 2) overlay ours". Only when sequence aids understanding.
- **Notes**: speaker notes / talking points the slide body should NOT contain.
```

Rules for the spec:

- **One message per slide.** The `Message` field is a forcing function. "And also…" means a second slide.
- The **title is the message compressed**, phrased as a claim. `Results` is a label; `Adaptive walks win on all 5 benchmarks` is a claim.
- **Body is evidence for the title, not a transcript.** Anything you'd *say* but not *show* goes in `Notes`.
- Mark every visual's **provenance** so the artifact step knows whether to reuse a file, draw TikZ, or generate a chart.

Confirm the spec with the user before generating the artifact. Correcting structure in markdown is cheap; correcting it in `.tex`/`.pptx` is not.

---

## Design rules (format-independent)

### 1. One signal per slide
A slide answers one question. If a listener can't say what the slide was about in five words, it carried too much. Density is the most common failure; when in doubt, split.

### 2. Claim-titles
The title is the most-read line on every slide. Spend it on the takeaway, not a category name.

| Weak (label) | Strong (claim) |
|---|---|
| Experimental Results | Our method cuts error 23% with half the compute |
| System Overview | Three stages, one bottleneck: retrieval |
| Background | Prior work assumes static graphs — ours don't |

### 3. Visual hierarchy
Largest element = most important element. The eye should land on the message, then the evidence, then the detail. If everything is the same size, nothing is emphasized. Use position (top-left first in LTR), size, weight, and color — in that order of strength.

### 4. Density limits
- Prose: never a paragraph on a slide. Bullets are compressed speech, not sentences.
- ~6 bullets max, ~7 words each (the "6×7" heuristic — a ceiling, not a target).
- One table per slide; ≤ 6 rows / 5 columns visible. Bigger tables are appendix/backup.
- One primary figure per slide. Two only if they're a direct comparison.

### 5. Figure adaptation
Paper figures are built for a reader who can zoom and reread; slides are seen once from across a room. Adapt:
- Strip multi-panel figures to the one panel that makes the point.
- Increase font sizes; a label readable in a PDF is invisible projected.
- Remove gridlines, legends, and annotations the audience won't parse live.
- Add one highlight (arrow, circle, color) that points at the takeaway.

### 6. Color and contrast
- Pick one accent color and use it only for emphasis; everything else neutral.
- Ensure text/background contrast survives a washed-out projector (dark on light is safest).
- Never encode meaning by color alone — pair with shape, label, or position (colorblind-safe).
- Consistency across the deck: the same concept gets the same color throughout.

### 7. Consistency and chrome
- Fixed layout grid: titles, page numbers, and logos in the same place every slide.
- Footers/logos are chrome — make them quiet. The content is the message.
- One font family, ≤ 2 weights. Math in the body font's companion math font.

### 8. Progressive disclosure
Reveal complex content in steps (builds) so attention follows the explanation. Build equations piece by piece; overlay results onto baselines. Builds should *reveal logic*, never decorate.

---

## When to push back

Tell the user to fix structure (not styling) when you see:
- A slide whose `Message` you cannot write in one sentence.
- More than ~7 slides per 10 minutes of talk (too fast to follow).
- A wall-of-text slide that is really speaker notes pasted onto the canvas.
- A figure copied from the paper at paper resolution and density.
- Titles that are all labels — a sign the deck has no argument, just sections.

---

## Output

When invoked directly: return the corrected slide-spec block(s) and a short list of the rules each change applies. When invoked as a dependency: hand the agreed slide-spec to the calling builder, which renders it to the target format.
