# Slide design principles (reference)

Workspace-local crib of the rules the `deck-*` builder skills apply in depth. Use this while filling `_dashboard/slide-plan.md`; each builder carries the full spec schema in its own `references/slide-spec-and-design.md`.

## One signal per slide

- Each slide delivers exactly **one** point. If a slide has two messages, it's two slides.
- The **title is a claim, not a label.** "Our method cuts error 40%", not "Results".

## Visual hierarchy

- The eye should land on the one thing that matters first. Use size, weight, colour, and position to rank — don't make everything bold.
- One accent colour for emphasis; the rest neutral. Colour means something.
- Generous whitespace. Crowding hides the signal.

## Density limits

- Few words per line, few lines per slide. Slides are not documents — detail goes in `script.md` (what you say) or a backup slide.
- One chart per slide, pre-digested: highlight the part that supports the claim; strip gridlines/legends that don't earn their place.

## Figures

- Adapt figures for projection: larger fonts, fewer series, high contrast. A paper figure rarely works verbatim on a slide.
- Label the takeaway directly on the figure where possible.

## Accessibility

- High contrast; don't rely on colour alone to distinguish series.
- Readable from the back row: large type, thick lines.

For the per-slide spec schema and detailed critique, defer to the `deck-*` builder you are rendering with; for narrative/pacing, to `research-talk-planner`.
