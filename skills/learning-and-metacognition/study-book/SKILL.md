---
name: study-book
description: >-
  Write a story-first study book (Typst PDF) to explain and rebuild from, not recite. Modes: exam
  revision from a transcript, syllabus or course list (oral exam, APS/DAAD or PhD/MSc admissions
  interview, qualifying exam); learning a new topic from a source list; or a deep dive into one
  framework, model or method. Each Part teaches its central idea through two worked cases the reader
  compares and ends with an unaided transfer question. Use whenever the user says "make a study book /
  revision book / study guide", "summarise my courses for the interview", "prepare me for the APS
  interview from my transcript", "write me notes to really understand X", "a deep dive into how
  <framework/model> works", or wants a Part added to such a book, even without mentioning Typst. Not
  for live explanation (professor-mentor-technical-teaching), guided questioning
  (flow-learn-new-topic, flow-deep-understanding), exercise sets (concept-exercise-generator), mock
  interviews (apply-interview-prep) or Obsidian vaults (init-workspace).
---

# Study book

A durable book the reader studies from, built so that a second question ("why?", "what if the assumption fails?", "how does this connect?") does not break it. **Read `references/teaching-philosophy.md` before writing**: it is the reason for every structural rule below, and its end-of-Part checklist is the acceptance test.

## 1. Intake (one batch, then proceed)

Ask only what the sources do not already answer:

1. **Mode and goal.** *Exam* (what exam or interview, target programme or panel, language), *topic* (what to learn and what for), or *deep dive* (which framework, model or method, and which version).
2. **Reader.** What they already know well (this is what the *connection* step links to) and the book's default style, Foundation or Depth (§2), with any Part that should differ. In exam mode: degree, institution, grading scale.
3. **Sources.** Exam: transcript with grades, syllabi or lecture notes, thesis if it will be examined. Topic: papers, textbook chapters, lecture notes. Deep dive: the paper, official docs, or repository, at a pinned version.
4. **Scope and output.** What to include or skip; target directory.

Defaults if unstated: English; style as in §2; exam mode treats grades below B as weak; output in `study-book/` of the current project.

## 2. Mode table

Every mode builds Parts from the same pieces (§8). What changes:

| | Exam | Topic | Deep dive |
|---|---|---|---|
| A Part is | one subject (may group several courses) | one subtopic | one component or stage of the system |
| Default style (below) | Depth | Foundation | Foundation |
| Grounded in | syllabus, notes, thesis | the source list | paper, official docs, source at the pinned version |
| Connection points to | another course, the thesis | another Part, the reader's prior knowledge | another Part, the reader's prior knowledge, rival designs |
| The two compared cases (§8) | **close** (same kind of object, alike on the surface) if cases-first; may be far apart if map-first | as exam | as exam; rival designs must do the same job under comparable conditions |
| The transfer question | far: different surface, no hint | far: different surface, no hint | far: a system or setting the Part never mentions |
| Closing questions | `#ask[...]`: likely examiner questions | `#ask(title: "Self-test questions")[...]` | same as topic |
| Weighting | weak grades: more examples and questions; strong grades: depth goes to proof ideas, edge cases and failure modes | load-bearing ideas get depth | the parts the reader will modify or debug get depth |
| Extra closing Parts | Gaps, Strategy (§4) | none | none |

### Part style

Each content Part is **Foundation** (new or weak material) or **Depth** (a solid background to build on). The style is the only switch for the Part's order (§8), figures (§7) and section content.

| | Foundation | Depth |
|---|---|---|
| Order | cases-first; a deep-dive component opens with the question it answers | map-first |
| Figures | drawn by default for a shape, quantity, process or structure | only for what the prose and example do not show |
| Sections | plain explanation, worked example, link to the section before | also proofs, why each assumption is needed, a counterexample, real trade-offs |

Choose it per Part; the first rule that applies wins:

1. The reader's explicit choice for that Part.
2. The reader's current assessment of it: "new to me" means Foundation; "I know this" means Depth.
3. A weak transcript grade: Foundation.
4. The default: Depth for the reader's own thesis or project; for any other Part the book default the reader set, otherwise the mode's row above.

The *Weighting* row sets page budget only: a load-bearing idea or a component the reader will modify does not become Depth because of it.

## 3. Grounding: never invent

- **Mark what is not sourced.** If a Part's content is not backed by a supplied source (in exam mode a transcript gives only course *names*), open it with `#box-note("Unverified scope")[Standard curriculum for this subject; check against your syllabus.]`. The final report lists these Parts.
- **Reader's own work** (thesis, projects): only facts in the document. Note every uncertain fact; never invent numbers, datasets or results.
- **Frameworks and models change between versions.** Record the version on the title page and cite the doc page, paper section or source file for each interface or behaviour claim. A claim you cannot cite is marked unverified, not stated.
- **Programme and exam facts** (what a programme expects, whether the APS interview exists for the reader's country, its language and format) are looked up live on the official page, with URL and access date, never recalled. No page found means `link needed`, not a guess.
- Scanned PDFs: if `pdftotext` returns nothing, render pages (`pdftoppm -r 80 -png`) and read the images.

## 4. Plan the Parts and confirm before writing

- One Part per subject / subtopic / component. Foundations first, applications after; the thesis or the reader's own project last among content Parts.
- **Exam mode only**, two closing Parts:
  - **Gaps**: short primers for topics the target programme expects but the transcript lacks, each with *why it is expected* (citing the live programme page) and a priority.
  - **Strategy**: the recurring patterns table (§8); how to handle weak grades honestly (one sentence of context, then demonstrate the knowledge, then point to later evidence of growth); the four-step answer (intuition, statement, small example, connection; if memory fails, rebuild aloud from the story); a final checklist.
- **Choose each Part's style** by the rules in §2.
- **Find the recurring patterns.** A pattern is a method, relation or operation that appears in at least two Parts, where you can name the correspondences and a result or procedure from one tells you something checkable about the other. For each Part note *introduces X*, *reuses X*, or none. Do not force one: similar notation is not a pattern.
- Show the plan as a table (Part, title, needs, after it you can, style, pattern, sources, planned sections), with the book's 3–5 overall outcomes under it, and wait for confirmation.

## 5. Project layout and build

```
<project>/
├── lib/template.typ               copy unchanged from this skill's assets/lib/
├── lib/helpers.typ                copy unchanged from this skill's assets/lib/
├── figures/
│   ├── book_style.py              copy unchanged from this skill's assets/figures/
│   ├── NN-slug.py                 one Plotly script per Part that has figures
│   └── NN-slug-name.svg           generated; referenced as image("/figures/NN-slug-name.svg")
└── study-book/
    ├── main.typ
    └── parts/NN-slug.typ          file number = Part number
```

**If `lib/` already exists, never overwrite it.** Older books use an earlier API (`course()`, `course-story`, `story-flow` with a section base, string section numbers); swapping in the bundled lib breaks every existing Part. Read the existing `helpers.typ` and write new Parts against its API; migrate to the bundled lib only if the user agrees.

Build from the project root with one command, so Typst runs only after every figure has regenerated (otherwise it can compile a stale SVG from an earlier build):

```bash
sh -ec 'for f in figures/[0-9]*.py; do [ -e "$f" ] || continue; python3 "$f"; done' &&
  typst compile --root . study-book/main.typ study-book.pdf
```

Figures need `plotly` and `kaleido`; without a local install, replace `python3` with `uv run --with plotly --with kaleido --with numpy python3`. Kaleido 1.x drives a local Chrome. `--root .` is required because imports are root-relative (`/lib/helpers.typ`). Tested with Typst 0.15.1; `@preview/fletcher:0.5.8` downloads on first build. The heading fonts are macOS fonts; elsewhere Typst falls back with a warning, which is harmless.

## 6. The Typst API (use these, do not redefine them)

Every Part file starts with `#import "/lib/helpers.typ": *`, which re-exports `template.typ`.

**Cross-references are labels, never hand-typed numbers.** Put `<part:slug>` on every `=` heading and `<sec:slug>` on every `==` heading; cite with `@sec:slug` (prints "§ 1.3") or `@part:slug` (prints "Part 1"). A label that does not exist fails the build, and inserting a Part renumbers everything automatically.

**Set-up.** `#show: book.with(title:, subtitle:, author:, doc-title:, header-title:, kicker:, blurb:)`, then `#show: inline-display` (inline maths at full size). Headings number themselves: the first `=` heading (`= Overview`) is Part 0; each `=` starts a new page.

| Helper | Use for |
|---|---|
| `#part-story[core principle][body]` | The Part's core idea: opens a map-first Part, or the summary of a cases-first one (§8). Body ends with `_One-liner:_ "..."`. |
| `#concept-map([Title], nodes: (...), edges: "...", own: false)[reading]` | Dependency graph of the Part (below). |
| `#framework([a … problem], [Step], [Ask], [Tool (@sec:x)], ...)` | Decision table, rows of three cells. |
| `#story-flow([Title], t1, …, t7)` | The seven stages: problem, approaches, limits + motivation, idea, assumptions, theory, summary + ELI5. Exactly 7 texts. Stage 3 ends with "*So: …*", the turn. It cannot split across pages: keep each text under about 80 words; a flow taller than a page fails the build. |
| `#idea[...]` | "The story" at the start of each section. |
| `#ex[...]`, `#ex(title: "...")[...]` | Worked example. |
| `#ask[...]`, `#ask(title: "Self-test questions")[...]` | Closing questions of a Part. |
| `#box-note("Title")[...]` | Neutral box: overview, source facts, unverified-scope notice, "Compare before reading on" or "Check the principle against two cases", "Predict before reading on" (§9), "Seen before". |
| `#story(title: "...")[...]`, `#takeaway[...]`, `#pitfall[...]`, `#eli5[...]`, `#defn("Term")[...]`, `#derivation(title: "...")[...]` | General boxes. |
| `#fig(image("/figures/NN-slug-name.svg", width: 80%), [caption])` | Figure (Plotly SVG, §7). Pass `image(...)` with a root-absolute path, not a path string. |
| `#part[Label]` | Divider inside one long section. |

Colours: `c-blue c-orange c-aqua c-yellow c-violet c-red c-ink c-muted`; mark weak grades with `#text(fill: c-red)[...]`. Maths operators defined: `argmin argmax Var Cov tr diag sign softmax KL`; write `bb(E)`, `RR` for blackboard letters.

**`concept-map`.** Node tuple: `(key, x, y, kind, [label], <sec:slug>)`, or `none` as the last field for no section. `x` roughly −0.2 to 3.7, `y` integer rows; one cell ≈ 3 cm × 1.45 cm. Kinds: `"t"` term, `"c"` concept/theorem, `"m"` method, `"x"` from another Part (dashed). Edges: space-separated `"a>b"` or `"a>b~30"` (bend 30°), prerequisite → what builds on it. `own: false` prints "Follows the story:" (retell the Part story as a path); `own: true` prints "The graph's own story:" (something the prose does not say); `own: none` prints nothing. `kicker:` replaces the "Concept graph" prefix, e.g. "Learning map". Keep 8–12 nodes, placed so arrows do not cross boxes. A map wider than the paper fails the build; one that only spills into the margins builds, so keep `x` in range.

**Typst maths pitfalls.** Multi-letter text needs quotes (`"rank"`); escape `/` as `\/` where it should not become a fraction; angle brackets are `chevron.l … chevron.r`; `tilde.equiv` for ≅; `divides.not`; `plus.minus`.

## 7. Figures (Plotly)

Figures, charts and diagrams are drawn with **Plotly** by default (a function plot, vectors in the plane, a loss curve, a probability density, an attention heat map, a geometric picture, the Part's spine diagram), exported as SVG and embedded with `#fig`. **Two exceptions stay in Typst**: the `concept-map` and `story-flow` helpers, because their boxes carry live `@sec:` references, and any tiny inline flow of two or three boxes inside prose (fletcher's `diagram`/`node`/`edge`, which `helpers.typ` already imports).

- Each figure script starts `from book_style import go, save, ROLE, DASH, label_ends` and ends `save(fig, "NN-slug-name")`. `book_style` sets the book's palette and fonts and a fixed export size, so all figures look the same; do not restyle per figure.
- **Plot computed values, never hand-placed shapes** (the exceptions are the spine diagram below and process or structure figures, drawn with its `diagram()`: their geometry is conceptual). The script computes what it draws (eigenvectors, densities, iterates) with `numpy`, so the figure is checked the same way as a worked example. Fix random seeds.
- No Plotly title: the Typst caption carries it. Axis titles in words plus units or symbols.
- One figure answers one question from the section's story. Whether to draw it depends on the Part's style (§2):
  - **Foundation**: a section about a shape, a quantity, a process or a structure gets a figure; leaving it out needs a reason in the final report (§10). It counts only if you can say what the figure shows that the reader would otherwise have to picture: a curve, a geometric relation, values changing, steps in order, parts and their connections. A section that only names or defines things does not count and needs no reason.
  - **Depth**: only what the prose and worked example do not show, such as a boundary, a failure or a comparison of methods.
  - Both: no quota and nothing decorative; a section with nothing to show gets no figure. Nor does a figure that only repeats what a nearby table or sentence already makes plain: draw what they cannot show (a shape, a longer run, a boundary) or skip it, giving that as the reason in a Foundation Part. The caption, compare-box (§8) and transfer-question rules still apply.

**Colour is a role, not an order.** Use `ROLE[...]`, never hex codes or Plotly's default cycle. Only `main` (blue), `second` (orange) and `third` (aqua) are data-series colours: they are the only three of the palette that stay apart for colour-blind readers (red and orange, violet and blue do not, even for normal vision). Give each series its matching dash, `DASH[...]`, so lines stay apart in grayscale print. A fourth series goes to small multiples, never a new colour. `breaks` (red) is only for where an idea fails, always with a text label; `context` (grey) is only for the true solution, reference lines and baselines; `highlight` (violet) marks the one point or region the caption is about, never a series. The same role keeps the same colour in every Part.

**Pick the form from the question the caption answers.**

| The question | Form |
|---|---|
| *Convergence and error* | |
| How fast does it converge? | log error against step: a straight line suggests a linear rate (slope = log of the factor), a sustained downward bend faster than linear; the order itself comes from the error ratio or a proof, not the picture |
| How does error scale with h or n? | log–log error against h or n: the slope is the order |
| Where does it stop improving? | log–log error against h with the floor marked (e.g. rounding), the optimal h annotated |
| *Functions and shape* | |
| What does it look like, and how good is the approximation? | line plot: the true function in `context`, the approximation in `main`; add an error panel below on a shared x-axis if the gap is small |
| How does a parameter change the shape? | 2–3 labelled lines, one per parameter value, or small multiples for more; never an animation |
| Where is the optimum, and how does the method get there? | contour plot of the objective with the iterates as a marked path; equal x/y scale |
| *Distributions and uncertainty* | |
| What does the distribution look like? | histogram or density, mean or median as a `context` line |
| How do two or three distributions differ? | overlaid densities on one axis; more groups: box or violin plots side by side |
| How uncertain is the estimate? | line with a shaded band for a curve; error bars for a few points |
| Does the sample match the theory? | QQ plot, or the empirical density with the theoretical one in `context` |
| *Relationships* | |
| Do two quantities relate? | scatter with the fitted line, residuals in a panel below |
| Are the classes separable? | scatter by class (at most 3) with the decision boundary |
| What trades off against what? | scatter of the options with the Pareto frontier as a line |
| Is there a sweet spot (bias–variance, h, learning rate)? | U-shaped curve with the minimum annotated |
| *Magnitudes and ranking* | |
| Which is largest, in what order? | sorted horizontal bars or a dot plot |
| What changed per item, before vs after? | dumbbell or slope chart |
| *Geometry and linear algebra* | |
| What does a linear map do? | unit circle → ellipse with the singular vectors as arrows; equal x/y scale |
| Projection, orthogonality, eigenvectors | vectors as arrows before and after, right angles marked; equal x/y scale |
| How fast does a spectrum decay? | singular values or eigenvalues against index, log y |
| *Matrices and structure* | |
| What are the entries (attention, covariance, a kernel)? | heat map in one hue, light to dark; signed values: two hues with grey at zero |
| Where are the non-zeros? | sparsity (spy) plot |
| *Dynamics and training* | |
| How does it evolve in time? | line against time; a 2-D system as a phase portrait with equal x/y scale |
| How does training go? | train and test loss against steps, log y if it spans orders of magnitude |
| *Conceptual* | |
| What is the Part for? | the spine diagram (below) |
| What are the steps, or how are the parts connected? | boxes and arrows with `diagram()` |
| How do the terms depend on each other? | the concept map (Typst) |
| A single number, or a few exact values | no chart: prose or a table |

Never put two y-axes on one plot: two quantities with different units get two panels sharing the x-axis.

**Choose the labelling from the figure, then check the render:**
- One series: no legend; the caption and axis title name it.
- Two or three lines that are apart at their ends: `label_ends(fig)`, which writes each trace's `name` in ink beside its last point and hides the legend. If they are apart somewhere else, `label_ends(fig, at=x)`.
- Lines that cross or bunch everywhere: keep the legend, or split into panels.
- Scatter by class: one ink label per cluster, placed at its centre.
- Bars: the category names sit on the axis; no legend.
- More than three series: small multiples, each panel titled.
- Heat maps: a colour bar, because colour is a scale there, not an identity.
- Label text is always in ink, never in the series colour. Name every trace anyway; Plotly otherwise prints "trace 0".

**Annotate what the caption asks about**: one or two arrows with short text at the point that answers the question (a slope, a floor, a crossing), arrows in `context` grey. **The caption states the answer, not only the subject**: "The cos iteration's error falls along a near-straight line (linear rate); the √2 iteration's error bends down (faster than linear)", not "Error against step". Claim no more than the picture shows. **Exception:** when the figure is what the reader has to judge in a "Predict before reading on" box (§9), the caption names what is plotted and asks the question, no annotation gives the verdict away, and the interpretation follows in the text.

**The two compared cases (§8) get one figure when they can be drawn**: same axes, same scale, same role colours, so the alignment shows at a glance; it sits next to the alignment table. **The transfer question gets no figure**, or one in a deliberately different form, because a familiar figure is a hint. Reference case, the pair from §8:

```python
# figures/04-fixed-point.py
import math
from book_style import go, save, ROLE, DASH, label_ends

xs, ys = [1.0], [1.0]                       # Case A: x ← (x + 2/x)/2; Case B: x ← cos x
for _ in range(4): xs.append((xs[-1] + 2 / xs[-1]) / 2)
for _ in range(15): ys.append(math.cos(ys[-1]))
star = 1.0
for _ in range(200): star = math.cos(star)
eA = [(t, abs(x - math.sqrt(2))) for t, x in enumerate(xs) if abs(x - math.sqrt(2)) > 1e-15]
eB = [(t, abs(y - star)) for t, y in enumerate(ys)]

fig = go.Figure()
for (name, e, role) in (("Case A: √2", eA, "main"), ("Case B: cos x = x", eB, "second")):
    fig.add_scatter(x=[t for t, _ in e], y=[v for _, v in e], name=name, mode="lines+markers",
                    line=dict(color=ROLE[role], dash=DASH[role], width=2), marker=dict(size=8))
fig.update_yaxes(type="log", title="error |x<sub>t</sub> − x*|", exponentformat="power")
fig.update_xaxes(title="step t")
label_ends(fig)
fig.add_annotation(x=9, y=math.log10(eB[9][1]), text="slope = log 0.67 per step", ax=40, ay=-40,
                   arrowcolor=ROLE["context"])  # annotations on a log axis take log10 positions
fig.add_annotation(x=3, y=math.log10(eA[3][1]), text="e<sub>t+1</sub> = e<sub>t</sub>² / 2x<sub>t</sub>", ax=95, ay=0,
                   arrowcolor=ROLE["context"])
save(fig, "04-fixed-point-rates")
```

### The spine diagram

One picture of what the whole Part is *for*: its objects, the question it asks of them, the recurring move, the theorem that licenses each move, and where the move fails. Build it by answering, in order:

1. **Objects**: what does the subject study?
2. **Central problem**: what does it want to know or compute about them?
3. **Core move**: the recurring strategy; these become the arrows.
4. **Guarantees**: the theorem that justifies each arrow; these become the arrow labels.
5. **Limits**: where the move fails (often the subject's advanced chapters); show it as a dashed arrow, a note on an arrow, or a `#pitfall` under the figure.

Then **place every `==` section that teaches content on a node or arrow** (not the "Putting it together" summary). A section that fits nowhere means the spine is wrong, or the section belongs in another Part; fix the spine, do not drop the section. **Do not force the shape** "transform → solve the easy problem → return" when the subject's spine is classification (objects sorted by an invariant), construction (building up from axioms), or limits (what cannot be done). Draw the shape the subject actually has.

Draw it with `diagram(nodes, edges)` from `book_style`. Boxes size themselves to their text and arrows stop at box edges. Number the arrow labels ①②③…, and put the section mapping in the Typst caption with `@sec:` references, so a missing section fails the build. Any inequality or error decomposition the diagram implies goes under the figure as a displayed Typst equation, not into the plot. Numerical analysis, the reference case:

```python
# figures/03-numerical-analysis.py
from book_style import diagram, save

nodes = {  # (x, y, label); about 4 units between columns; 2–3 between rows, 3 when labels have two lines
    "P":  (0, 2, "P<br><i>integral, ODE, PDE, f(x)=0</i>"),
    "x":  (8, 2, "x  (true solution)"),
    "SP": (0, 0, "SP<sub>h</sub>  (computable)"),
    "S":  (4, 0, "Solver"),
    "xt": (8, 0, "x̃<sub>h</sub> ≈ x<sub>h</sub>"),
}
edges = [  # (from, to, label[, {"dash": True, "side": "above|below|left|right"}])
    ("P", "x", "not computable", {"dash": True}),
    ("P", "SP", "① discretize,<br>parameter h", {"side": "left"}),
    ("SP", "S", "② solve", {"side": "above"}),
    ("S", "xt", "③ stop at tol", {"side": "above"}),
    ("xt", "x", "④ converges as h → 0<br>(consistency + stability)"),
]
save(diagram(nodes, edges), "03-numerical-analysis-spine")
```

```typst
#fig(image("/figures/03-numerical-analysis-spine.svg", width: 100%),
  [The approximately commuting diagram. ① @sec:interpolation @sec:quadrature, ② @sec:direct-solvers,
   ③ @sec:iterative-solvers @sec:newton, ④ @sec:convergence.])
$ norm(x - tilde(x)_h) <= underbrace(norm(x - x_h), "discretization") + underbrace(norm(x_h - tilde(x)_h), "solver + rounding") $
```

It commutes only approximately, in the limit h → 0. In floating point, rounding error grows as h shrinks, giving an accuracy floor (the limit). Newton applied to f(x) = 0 directly is the special case SP<sub>h</sub> = P, where only the bottom path's error remains.

Use HTML for labels (`<sub>`, `<i>`, `<br>`), not Unicode subscripts, which the font may lack. If labels collide, spread the columns or pass a larger `pad`; then check the render (§10).

## 8. `main.typ` and the Parts

```typst
#import "/lib/helpers.typ": *
#show: book.with(title: [...], subtitle: [...], author: [...], doc-title: "...",
  header-title: [...], kicker: "...", blurb: [...])
#show: inline-display
#outline(title: [Contents], depth: 1, indent: auto)

= Overview <part:overview>
== How to read this book <sec:how-to-read>
+ Find where to start in the learning map (@sec:map). Read a Part after the ones it needs.
+ Where a Part opens with two cases, work them first. At "Compare before reading on", write down what
  corresponds and one thing that differs, then read on. The Part's summary is at its end.
+ Where a Part opens with its summary, read it, then come back later and rebuild it from memory. At
  "Check the principle against two cases", find the principle in both before reading the table.
+ At "Predict before reading on", commit to an answer, with your reason, before reading further.
+ Try each Part's last question first. Turn to the hint only if stuck, then check yourself against
  "You have it if".
+ Practise, don't reread: cover the right column of each story flow and retell the seven stages,
  redraw each concept graph from memory, say each Part's core idea aloud in 60 seconds.
#concept-map([how to read one], nodes: (("t", 0, 0, "t", [Term], none), ("c", 1, 0, "c", [Concept], none),
  ("m", 2, 0, "m", [Method], none), ("x", 3, 0, "x", [From another Part], none)), edges: "t>c c>m", own: none)[
  Arrows run from what you need first to what is built on it.]

== Why it is built this way <sec:design>
- *The aim is to explain and rebuild, not recite.* A "why?" or "what if?" should not break what you know.
- *The reason comes before the rule.* Each idea answers a limit of what came before, to give you
  something to rebuild it from.
- *You do the comparing.* In lab studies, two examples helped people solve a new problem more than one
  did (Gick & Holyoak, 1983), and comparing two examples helped more than studying them separately
  (Gentner, Loewenstein & Thompson, 2003). Neither used mathematics or study books, and many people
  still did not succeed, so a missed transfer question shows what to revisit.
- *An idea is built in a loop.* Compare cases, name what they share, say when it holds, try it
  somewhere new, and revise it if it fails.
- *Memory is the test.* Rereading feels like knowing; retelling without the page shows whether you do.
- *Gaps are marked.* "Unverified scope" means no supplied source backs that content: check it.

Everything else here (reason first, the loop, the Foundation and Depth styles, page order, boxes, the
seven-stage story flow) is a design choice, not a research finding.

== Learning map <sec:map>
#concept-map([order of the Parts], kicker: "Learning map",
  nodes: (("a", 0, 0, "c", [Functions], <part:functions>), ("b", 1, 0, "c", [Limits], <part:limits>)),
  edges: "a>b", own: none)[Arrows run from a Part to the Parts that need it.]
#table(columns: 4,        // exam mode: sources are courses with grades, weak ones in c-red
  [*Part*], [*Needs*], [*After it you can*], [*Sources*],
  [@part:functions], [school algebra], [...], [...])

== What you will be able to do <sec:outcomes>
#table(columns: 2,
  [*By the end you can*], [*Check yourself, without the book*],
  [choose a method for a problem you have not seen, and say why], [each Part's last question, then its "You have it if" page],
  [...], [...])

== The big picture <sec:big-picture>   // #story: how the Parts form one loop; #takeaway
== The general framework <sec:framework>  // #framework, 5–7 field-wide steps citing @sec:...

#include "parts/01-....typ"
// topic and deep-dive mode, only if some pattern recurs, uncomment:
// #include "parts/NN-recurring-patterns.typ"
```

**The Overview is the reader's way in** (Part 0, a support Part), in the order above. Fill it for this book:

- **How to read**: describe only what the book contains (if every Part is map-first, drop only the cases-first step; keep the one on checking a stated principle against both cases).
- **Why it is built this way**: half a page at most, in the reader's words, only about what the book contains. State research support no more strongly than `references/teaching-philosophy.md` does, and say what is only a design choice.
- **Learning map**: every content Part once, with an arrow for each prerequisite from the plan; the table gives each Part's own outcome. Past about 10 Parts, draw one map per group. Each *Needs* cell matches that Part's *Before you start* line, where it has one.
- **What you will be able to do**: 3–5 abilities for the whole book, adapted to the reader's goal, each with a check they can run alone. Use observable verbs (explain, compute, choose, predict, design), not "understand". Promise only what the Parts' examples and questions practise, never an exam or admission result. An outcome names the task, not the method that solves it: "estimate a rate from a table of nearby values", not "take the limit of the difference quotient".

**The Overview gives away no Part's principle**, outcomes and design notes included. The map, big picture and framework say what each Part asks and how the Parts depend on each other; the framework's tool column points to sections with `@sec:` and a neutral name, not the mechanism. A deep dive's system diagram shows components and what passes between them, not how a component does its job.

Every content Part is built from these blocks:

- **Title**: `= Title <part:slug>` (exam mode: grades in the title, e.g. `= Calculus (C+ / B+)`).
- **Map**: `#part-story` (the one idea the Part grows from, how its topics follow, a one-liner to say aloud), `#concept-map`, `#framework` (5–8 rows of step → question → tool, citing `@sec:...`) and the Part's `#story-flow`.
- **Central idea**, by comparison: the first `== Section <sec:slug>` (below).
- **Further sections**: 4–9 `== Section <sec:slug>`, each `#idea`, then definitions / theorems / interfaces, then one `#ex` with small numbers. Central concepts open their section with their own `#story-flow`. By style (§2): Foundation explains plainly and says how the section follows from the one before; Depth adds proofs (`#derivation`), why each assumption is needed, a counterexample, and trade-offs, each only where the section really has one and it can be checked or sourced (§3); never invent one to fill the slot. For a system component these are its preconditions and failure cases from the cited source, not mathematical proofs.
- **Questions**: `#ask` for the whole Part. No question repeats one that a worked example, problem or section text already answered; change what the reader has to decide, not only the numbers. Its **last question is a transfer question**: a fresh case that looks different from everything in the Part (§2), worded without naming the Part, its idea or its terms.
- **Hint and check**: last in the Part, each on its own page: `#pagebreak()`, `_Hint (read after trying): ..._`, then `#pagebreak()`, `_You have it if: ..._` giving the answer and what a correct solution must say, followed by `_If you missed this, which correspondence or condition did you overlook?_` The Part must therefore state the conditions under which its principle holds. Before reporting, solve each closing question again from its wording alone, looking for a second correct answer: the hint and check must accept every one, or the question must be tightened to exclude it.

The Part's style (§2) sets the order:

| | Order |
|---|---|
| **Cases-first** (Foundation) | title → *Before you start* line → central idea → further sections → `== Putting it together <sec:slug-summary>` holding the map → questions → hint → check |
| **Map-first** (Depth) | title → map → central idea → further sections → questions → hint → check |

In a cases-first Part nothing printed before the "Compare before reading on" box states the principle: not the Part or section title (word the section title as the question), the *Before you start* line, `#idea`, or a figure caption, and no figure before that box draws what the two cases share. The *Before you start* line (`*Before you start:* ...`) is one sentence naming what the reader needs to know already, never the idea.

**The central-idea section**, in this order:

1. `#idea`: the question and why it matters. In a cases-first Part, no answer yet.
2. **Two worked cases**, `#ex(title: "Case A: ...")` and `#ex(title: "Case B: ...")`: small numbers, recomputed, set out in parallel. In a cases-first Part they look alike on the surface, so lining them up is easy (a design choice); in a map-first Part they may differ widely. The default is two problems solved by the same move. When the idea has another shape, compare: one object in two representations; two objects sorted by the deciding invariant; a familiar construction and its extension; two designs for one job; or a valid case and a matched counterexample that isolates the failed condition.
3. The prompt, by order:
   - **Cases-first**: `#box-note("Compare before reading on")[...]` tells the reader to write down what corresponds to what in the two cases, and one thing that differs. Follow it with `#pagebreak()`, so the table and principle start on a new page.
   - **Map-first**: the principle is already known, so this is a check, not a discovery: `#box-note("Check the principle against two cases")[...]` asks the reader to find each part of the principle in both cases and say where one differs. No page break; claim no transfer benefit for it.
4. **Alignment table**: a plain `#table` with columns *role in the idea | Case A | Case B*, one row per correspondence (at least two), and a last row *does not carry over*.
5. **The principle**: the exact statement (`#defn` or theorem) of what the two cases share.
6. **Seen before**, only if the Part reuses a pattern: `#box-note("Seen before")[...]` linking the earlier section with `@sec:`, giving at least two correspondences and one thing that does not carry over. It goes in the section of this Part that reuses the pattern (one box per pattern, in the first such section), after that section's own idea is stated; in this central-idea section that means after the principle, so that it does not answer the comparison.
7. **Spine diagram** (§7), placed here next to the pair, with its caption mapping arrows to sections and naming the arrows both cases follow ("Case A and Case B both follow ①→②"). If the cases can be drawn, their paired figure (§7) sits beside the alignment table. In deep-dive mode, `@sec:big-picture` holds one diagram of the whole system whose arrows name only what flows between components; each component's guarantees and limits stay in its own Part, which draws a spine diagram here when the component has its own spine.
8. `#pitfall`: where the idea breaks.

**Recurring patterns table.** One per book, at the end, because up front it would give the principles away. Topic and deep-dive mode: a closing Part `= Recurring patterns <part:patterns>`. Exam mode: a section `== Recurring patterns <sec:patterns>` in Strategy. One row per pattern: *pattern | first appears (`@sec:`) | reused in (`@sec:`) | what stays the same | what changes*. If no pattern recurs, omit the table and say so in the final report. Like Gaps and Strategy it is a support Part: the blocks, orders and end-of-Part checklist above are for content Parts (the restatement rule in §9 still applies).

Example of steps 2–4 for a cases-first Part on fixed-point iteration (so the pair is close):

```typst
#ex(title: "Case A: √2 by iteration")[$x_(t+1) = (x_t + 2\/x_t)\/2$, from $x_0 = 1$: 1.5, 1.41667, 1.41422.]
#ex(title: "Case B: cos x = x")[$x_(t+1) = cos x_t$, from $x_0 = 1$: 0.5403, 0.8576, 0.6543, … → 0.7391.]
#box-note("Compare before reading on")[Write down what plays the same role in A and B, and one thing that differs. Then turn the page.]
#pagebreak()
#table(columns: 3,
  [*Role*], [*Case A*], [*Case B*],
  [update map $T$], [$(x + 2\/x)\/2$], [$cos x$],
  [fixed point $x^* = T(x^*)$], [$sqrt(2)$], [$0.7391$],
  [local rate $|T'(x^*)|$], [$0$], [$0.67$],
  [why it converges from $x_0 = 1$], [$T$ maps $[1, 2]$ into itself with $|T'| <= 1\/2$],
  [$cos$ maps $[0, 1]$ into itself with $|T'| <= sin 1 < 1$],
  [does not carry over], [$e_(t+1) = e_t^2 \/ (2 x_t)$], [near $x^*$, error shrinks by about 0.67 a step])
```

The reader's own thesis or project Part defaults to Depth, since they know it (§2 can override), and is built from their document only, plus a first-person section on their contribution and a "two-minute summary".

## 9. Writing rules

The voice and the eleven principles are in `references/teaching-philosophy.md`. The ones agents most often break:

- Every section opens with *why it exists*, before any definition.
- Name the cross-Part connection wherever the mathematics really connects; these links are the content.
- **A connection is a mapping, not a label.** Name at least two correspondences (this Part's *x* is that Part's *y*) and one thing that does not carry over. "This is like X" alone is not a connection.
- **The reader does the comparing.** The prompt box always comes before the alignment table, and in a cases-first Part on an earlier page; a table the reader only reads is weaker than one they first try to fill.
- **Keep an analogy only if a relation carries over**, not only a resemblance, and say where it stops holding.
- Worked examples use small numbers and are **recomputed with `python3 -c`**, not by eye. A worked problem states every value its answer depends on.
- **Let the reader commit before the answer.** Where they already have what they need to predict a result, choose a method or reject an assumption, put `#box-note("Predict before reading on")[...]` there, in either style. It names the decision ("which input voltage sets the minimum inductance?"), never only "think first". The best place is where evidence overturns a plausible verdict (a rule that looks settled and then changes): the row, line or plot that overturns it comes after the box, never above or beside it, so split the table or figure. The text that follows answers it and names one plausible wrong answer and what it should send the reader back to. No quota, and no forced page break, so the answer may sit just below. It does not replace the compare box. Before that box it must not give the principle away (§8): show only the overturning evidence there and explain it after the page turn.
- **A restatement claims no more than what it restates.** Core idea, one-liner, story flow, framework, pattern table, hint, "You have it if" and any answer list keep the conditions of the worked material: a local result stays local, and "agrees at convergence" says what has converged and under which assumptions. This holds in every Part, support Parts included.
- Deep-dive examples are small numerical traces done by hand (two tokens through attention, one step of an optimiser), not code listings, unless the user asks for code.
- **Say where the new idea breaks.** The story flow's stage 3 covers the limits of the *old* approach; every central method also gets a `#pitfall` with its own failure modes and any trade-off it really carries (do not invent one to fill the slot). Required in deep-dive mode and for strong grades in exam mode.
- **An honest turn.** If the limit only *motivates* the idea rather than forcing it, name the extra assumption that makes the idea follow, and state it in stage 5 (Assumptions). "So we must use X" is allowed only when nothing else would fix the limit.
- **Each displayed equation answers a named question**: what is optimised, bounded, approximated, or traded off. Definitions and intermediate derivation steps stay when the argument needs them; an equation that does neither is cut.
- **Check each guarantee, not only the numbers**: its assumptions hold in the example, and a boundary or counterexample case shows what fails without them. A successful run is evidence for that run only; keep a local rate apart from a guarantee over a whole region. Tie each assumption to the step that uses it and drop one that no step uses, rather than checking it. When the two compared cases need different assumptions, say so in the *does not carry over* row (§8).
- **Label how settled a claim is** where it is not textbook-standard: established, the standard account but contested, or uncertain. Never smooth a contested point into a clean story.

## 10. Build in batches and verify before reporting

The Overview links to Parts and sections not yet written, so first create **every** planned file (support Parts included), include them all, and give each its `=` heading and planned `==` headings with their labels, followed by the line `// STUB`:

```typst
= Limits <part:limits>
== What value is a function heading to? <sec:approach>
// STUB
```

Then write Overview + the first 2–3 Parts, compile, and continue 3–4 Parts at a time, compiling after each batch. A Part's `// STUB` line goes when it is written. The book is not finished while `grep -rn "// STUB" study-book/` finds anything.

1. The build finishes with zero errors. A missing label, a story flow without exactly seven texts, a story flow or concept map taller than a page, and a concept map wider than the paper, are errors (an older book's helpers may cut such content off silently, §11).
2. Render each framework, story-flow, concept-graph, spine-diagram and figure page (`pdftoppm -r 70 -png -f P -l P`) and look at it: no missing rows or stages, nothing spilling into the margins, no figure shrunk too small to read, no overlapping boxes, no arrows crossing boxes, figure text readable, no "trace 0" legends, labels beside the lines they name. Render figure pages once more in grayscale (`pdftoppm -gray`): every series must still be told apart.
3. Run the end-of-Part checklist in `references/teaching-philosophy.md`. Then, in every Part, support Parts and answer lists included, read each restatement (§9) against the section it restates. For each cases-first Part, read the rendered pages in order: nothing before the "Compare before reading on" box gives the principle away, its table starts on a later page, and the hint and the check each have their own page.
4. Report: the Part list with each Part's style, any Foundation section left without a figure for a shape, quantity, process or structure (with the reason), whether any pattern recurs, Parts marked unverified scope, facts about the reader's work you could not confirm, and the version and sources used in deep-dive mode.
5. Offer the study-time next steps (the book's job ends where practice begins):
   - **Exercises** → `concept-exercise-generator`, one set per Part, passing this format as the brief: four tiers (1 define and identify; 2 run the method on a small case; 3 explain why, when it fails, what to choose; 4 derive, prove, design); every exercise with a model answer, a "you've got it if" check, and the "common wrong turn" it is designed to catch; one tier-3 exercise asks the reader to state, in their own words, the principle the Part's two compared cases share; the last exercise of each Part is the story-flow drill (retell the seven stages from memory).
   - **Done-check per Part** → `naive-student`: the reader teaches the Part's story flow from memory to an honest novice.
   - **A section that does not click** → `professor-mentor-technical-teaching` for a live explanation, rather than rewriting the book.
   - **Exam mode**: `apply-interview-prep` for mock interviews; `professor-critic` on the reader's own two-minute thesis summary or one-liners, with the named panel as the reader.

## 11. Adding a Part later

Keep the book's existing `lib/` (§5). Write `parts/NN-slug.typ`, add its `#include` in order, rebuild. Choose the new Part's style by §2; do not restyle existing Parts unless the user asks. Add it to the learning map and its table if the Overview has them; do not restructure an older Overview unasked. If it reuses a pattern, add the "Seen before" box and update the book's patterns table (or an older book's connection map); do not create a table in a book that has neither unless the user wants one. If the book predates labels (hand-typed `§N.M`), ask before converting it; otherwise follow its numbering and check the references after it. In a labelled book, every reference renumbers itself. Renaming later part files to keep "file number = Part number" is cosmetic; do it only if the user wants it.

**Overflow protection for an older book (offer it, add it only if the user agrees).** Helpers copied from an earlier version cut off a block that is taller than a page and still build. This rule in `main.typ`, above the first `#include`, makes the build fail instead and leaves `lib/` untouched:

```typst
#show block.where(breakable: false): it => layout(size => {
  assert(measure(it, width: size.width).height <= size.height,
    message: "a block is taller than a page and would be cut off")
  it
})
```

Say what it can change before adding it: a book that builds today may stop building until a block is shortened; page breaks may move slightly; a block of the book's own that is both `sticky` and unbreakable can be left behind on the previous page. It checks height only, so wide diagrams and cropped figures still need the visual check (§10). Compare page counts and look over the pages afterwards.
