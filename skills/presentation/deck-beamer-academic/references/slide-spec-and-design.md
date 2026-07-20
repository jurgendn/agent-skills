# Slide-spec and design rules

The tool-agnostic foundation for this deck. Two things: the **slide-spec** (the
per-slide intermediate produced *before* generating any `.tex` or `.pptx`) and
the **design rules** that apply regardless of format.

Structure is decided and corrected in the spec; the artifact is a mechanical
render of an approved spec. Correcting structure in markdown is cheap;
correcting it in `.tex`/`.pptx` is not — so confirm the spec with the user
before generating anything.

Planning a talk's *narrative and pacing* (what the one takeaway is, what to cut)
is a separate, upstream job owned by `research-talk-planner`. This file assumes
that planning is done, or does a lightweight version of it inline when no plan
exists.

---

## The slide-spec

One block per slide. Keep it in markdown so the user can edit it directly.

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

- **One message per slide.** The `Message` field is a forcing function. "And
  also…" means a second slide.
- The **title is the message compressed**, phrased as a claim. `Results` is a
  label; `Adaptive walks win on all 5 benchmarks` is a claim.
- **Body is evidence for the title, not a transcript.** Anything you'd *say* but
  not *show* goes in `Notes`.
- Mark every visual's **provenance** so the artifact step knows whether to reuse
  a file, draw TikZ, or generate a chart.

---

## Design rules (format-independent)

### 1. One signal per slide
A slide answers one question. If a listener can't say what the slide was about
in five words, it carried too much. Density is the most common failure; when in
doubt, split.

### 2. Claim-titles
The title is the most-read line on every slide. Spend it on the takeaway, not a
category name.

| Weak (label) | Strong (claim) |
|---|---|
| Experimental Results | Our method cuts error 23% with half the compute |
| System Overview | Three stages, one bottleneck: retrieval |
| Background | Prior work assumes static graphs — ours don't |

### 3. Visual hierarchy
Largest element = most important element. The eye should land on the message,
then the evidence, then the detail. If everything is the same size, nothing is
emphasized. Use position (top-left first in LTR), size, weight, and color — in
that order of strength.

### 4. Density limits
- Prose: never a paragraph on a slide. Bullets are compressed speech, not
  sentences.
- ~6 bullets max, ~7 words each (the "6×7" heuristic — a ceiling, not a target).
- One table per slide; ≤ 6 rows / 5 columns visible. Bigger tables are
  appendix/backup.
- One primary figure per slide. Two only if they're a direct comparison.

### 5. Figure adaptation
Paper figures are built for a reader who can zoom and reread; slides are seen
once from across a room. Adapt:
- Strip multi-panel figures to the one panel that makes the point.
- Increase font sizes; a label readable in a PDF is invisible projected.
- Remove gridlines, legends, and annotations the audience won't parse live.
- Add one highlight (arrow, circle, color) that points at the takeaway.

### 6. Color and contrast
- Pick one accent color and use it only for emphasis; everything else neutral.
- Ensure text/background contrast survives a washed-out projector (dark on light
  is safest).
- Never encode meaning by color alone — pair with shape, label, or position
  (colorblind-safe).
- Consistency across the deck: the same concept gets the same color throughout.

### 7. Consistency and chrome
- Fixed layout grid: titles, page numbers, and logos in the same place every
  slide.
- Footers/logos are chrome — make them quiet. The content is the message.
- One font family, ≤ 2 weights. Math in the body font's companion math font.

### 8. Progressive disclosure
Reveal complex content in steps (builds) so attention follows the explanation.
Build equations piece by piece; overlay results onto baselines. Builds should
*reveal logic*, never decorate.

---

## When to push back

Tell the user to fix structure (not styling) when you see:
- A slide whose `Message` you cannot write in one sentence.
- More than ~7 slides per 10 minutes of talk (too fast to follow).
- A wall-of-text slide that is really speaker notes pasted onto the canvas.
- A figure copied from the paper at paper resolution and density.
- Titles that are all labels — a sign the deck has no argument, just sections.
