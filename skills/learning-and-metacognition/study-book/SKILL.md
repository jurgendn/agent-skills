---
name: study-book
description: >-
  Write a story-first study book (compiled to PDF with Typst) whose reader must explain and rebuild the
  material, not recite it. Three modes chosen at intake: exam revision from a transcript, syllabus or
  course list (oral exam, APS/DAAD or PhD/MSc admissions interview, qualifying exam); learning a new
  topic from a source list; or a deep dive into one framework, model or method. Every Part follows
  story, statement, small checked example, connection, with a spine diagram, concept graph, decision
  table, seven-stage story flow and questions. Use whenever the user says "make a study book / revision book / study
  guide", "summarise my courses for the interview", "prepare me for the APS interview from my
  transcript", "write me notes to really understand X", "a deep dive into how <framework/model> works",
  or wants a Part added to an existing book of this kind, even without mentioning Typst. Not live
  explanation in chat (professor-mentor-technical-teaching), not interactive guided mastery
  (flow-learn-new-topic, flow-deep-understanding: use those when the user wants to be taught or
  questioned rather than handed a written book), not an exercise set
  (concept-exercise-generator, which this skill hands off to), not mock interviews (apply-interview-prep),
  and not an Obsidian notes vault (init-workspace).
---

# Study book

A durable book the reader studies from, built so that a second question ("why?", "what if the assumption fails?", "how does this connect?") does not break it. **Read `references/teaching-philosophy.md` before writing**: it is the reason for every structural rule below, and its end-of-Part checklist is the acceptance test.

## 1. Intake (one batch, then proceed)

Ask only what the sources do not already answer:

1. **Mode and goal.** *Exam* (what exam or interview, target programme or panel, language), *topic* (what to learn and what for), or *deep dive* (which framework, model or method, and which version).
2. **Reader.** What they already know well; this is what the *connection* step links to. In exam mode: degree, institution, grading scale.
3. **Sources.** Exam: transcript with grades, syllabi or lecture notes, thesis if it will be examined. Topic: papers, textbook chapters, lecture notes. Deep dive: the paper, official docs, or repository, at a pinned version.
4. **Scope and output.** What to include or skip; target directory.

Defaults if unstated: English; exam mode treats grades below B as weak; output in `study-book/` of the current project.

## 2. Mode table

The Part skeleton (§8) is the same in every mode. What changes:

| | Exam | Topic | Deep dive |
|---|---|---|---|
| A Part is | one subject (may group several courses) | one subtopic | one component or stage of the system |
| Grounded in | syllabus, notes, thesis | the source list | paper, official docs, source at the pinned version |
| Connection points to | another course, the thesis | another Part, the reader's prior knowledge | another Part, the reader's prior knowledge, rival designs |
| Closing questions | `#ask[...]`: likely examiner questions | `#ask(title: "Self-test questions")[...]` | same as topic |
| Weighting | weak grades: more examples and questions; strong grades: more depth | load-bearing ideas get depth | the parts the reader will modify or debug get depth |
| Extra closing Parts | Gaps, Strategy (§4) | none | none |

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
  - **Strategy**: a connection map (one idea → where it appears in each Part); how to handle weak grades honestly (one sentence of context, then demonstrate the knowledge, then point to later evidence of growth); the four-step answer (intuition, statement, small example, connection; if memory fails, rebuild aloud from the story); a final checklist.
- Show the plan as a table (Part, title, sources, planned sections) and wait for confirmation.

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

Build: first regenerate figures, `for f in figures/[0-9]*.py; do python3 "$f"; done` (needs `plotly` and `kaleido`; without a local install, `uv run --with plotly --with kaleido --with numpy python3 "$f"`; kaleido 1.x drives a local Chrome), then `typst compile --root . study-book/main.typ study-book.pdf`. `--root .` is required because imports are root-relative (`/lib/helpers.typ`). Tested with Typst 0.15.1; `@preview/fletcher:0.5.8` downloads on first build. The heading fonts are macOS fonts; elsewhere Typst falls back with a warning, which is harmless.

## 6. The Typst API (use these, do not redefine them)

Every Part file starts with `#import "/lib/helpers.typ": *`, which re-exports `template.typ`.

**Cross-references are labels, never hand-typed numbers.** Put `<part:slug>` on every `=` heading and `<sec:slug>` on every `==` heading; cite with `@sec:slug` (prints "§ 1.3") or `@part:slug` (prints "Part 1"). A label that does not exist fails the build, and inserting a Part renumbers everything automatically.

**Set-up.** `#show: book.with(title:, subtitle:, author:, doc-title:, header-title:, kicker:, blurb:)`, then `#show: inline-display` (inline maths at full size). Headings number themselves: the first `=` heading (`= Overview`) is Part 0; each `=` starts a new page.

| Helper | Use for |
|---|---|
| `#part-story[core principle][body]` | Opening of every Part. Body ends with `_One-liner:_ "..."`. |
| `#concept-map([Title], nodes: (...), edges: "...", own: false)[reading]` | Dependency graph of the Part (below). |
| `#framework([a … problem], [Step], [Ask], [Tool (@sec:x)], ...)` | Decision table, rows of three cells. |
| `#story-flow([Title], t1, …, t7)` | The seven stages: problem, approaches, limits + motivation, idea, assumptions, theory, summary + ELI5. Exactly 7 texts. Stage 3 ends with "*So: …*", the turn. |
| `#idea[...]` | "The story" at the start of each section. |
| `#ex[...]`, `#ex(title: "...")[...]` | Worked example. |
| `#ask[...]`, `#ask(title: "Self-test questions")[...]` | Closing questions of a Part. |
| `#box-note("Title")[...]` | Neutral box: overview, source facts, unverified-scope notice. |
| `#story(title: "...")[...]`, `#takeaway[...]`, `#pitfall[...]`, `#eli5[...]`, `#defn("Term")[...]`, `#derivation(title: "...")[...]` | General boxes. |
| `#fig(image("/figures/NN-slug-name.svg", width: 80%), [caption])` | Figure (Plotly SVG, §7). Pass `image(...)` with a root-absolute path, not a path string. |
| `#part[Label]` | Divider inside one long section. |

Colours: `c-blue c-orange c-aqua c-yellow c-violet c-red c-ink c-muted`; mark weak grades with `#text(fill: c-red)[...]`. Maths operators defined: `argmin argmax Var Cov tr diag sign softmax KL`; write `bb(E)`, `RR` for blackboard letters.

**`concept-map`.** Node tuple: `(key, x, y, kind, [label], <sec:slug>)`, or `none` as the last field for no section. `x` roughly −0.2 to 3.7, `y` integer rows; one cell ≈ 3 cm × 1.45 cm. Kinds: `"t"` term, `"c"` concept/theorem, `"m"` method, `"x"` from another Part (dashed). Edges: space-separated `"a>b"` or `"a>b~30"` (bend 30°), prerequisite → what builds on it. `own: false` prints "Follows the story:" (retell the Part story as a path); `own: true` prints "The graph's own story:" (something the prose does not say); `own: none` prints nothing. Keep 8–12 nodes, placed so arrows do not cross boxes.

**Typst maths pitfalls.** Multi-letter text needs quotes (`"rank"`); escape `/` as `\/` where it should not become a fraction; angle brackets are `chevron.l … chevron.r`; `tilde.equiv` for ≅; `divides.not`; `plus.minus`.

## 7. Figures (Plotly)

Figures, charts and diagrams are drawn with **Plotly** by default (a function plot, vectors in the plane, a loss curve, a probability density, an attention heat map, a geometric picture, the Part's spine diagram), exported as SVG and embedded with `#fig`. **Two exceptions stay in Typst**: the `concept-map` and `story-flow` helpers, because their boxes carry live `@sec:` references, and any tiny inline flow of two or three boxes inside prose (fletcher's `diagram`/`node`/`edge`, which `helpers.typ` already imports).

- Each figure script starts `from book_style import go, save` and ends `save(fig, "NN-slug-name")`. `book_style` sets the book's palette and fonts and a fixed export size, so all figures look the same; do not restyle per figure.
- **Plot computed values, never hand-placed shapes** (the spine diagram below is the one exception: its geometry is conceptual). The script computes what it draws (eigenvectors, densities, iterates) with `numpy`, so the figure is checked the same way as a worked example. Fix random seeds.
- Name every trace (`name="..."`) or hide the legend; Plotly otherwise prints "trace 0".
- No Plotly title: the Typst caption carries it. Axis titles in words plus units or symbols.
- One figure answers one question from the section's story; skip it if the prose and the worked example already show it.

### The spine diagram

One picture of what the whole Part is *for*: its objects, the question it asks of them, the recurring move, the theorem that licenses each move, and where the move fails. Build it by answering, in order:

1. **Objects**: what does the subject study?
2. **Central problem**: what does it want to know or compute about them?
3. **Core move**: the recurring strategy; these become the arrows.
4. **Guarantees**: the theorem that justifies each arrow; these become the arrow labels.
5. **Limits**: where the move fails (often the subject's advanced chapters); show it as a dashed arrow, a note on an arrow, or a `#pitfall` under the figure.

Then **place every `==` section on a node or arrow**. A section that fits nowhere means the spine is wrong, or the section belongs in another Part; fix the spine, do not drop the section. **Do not force the shape** "transform → solve the easy problem → return" when the subject's spine is classification (objects sorted by an invariant), construction (building up from axioms), or limits (what cannot be done). Draw the shape the subject actually has.

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

## 8. `main.typ` and the Part skeleton

```typst
#import "/lib/helpers.typ": *
#show: book.with(title: [...], subtitle: [...], author: [...], doc-title: "...",
  header-title: [...], kicker: "...", blurb: [...])
#show: inline-display
#outline(title: [Contents], depth: 1, indent: auto)

= Overview <part:overview>
#box-note("How to use")[Read each topic as story → statement → example → connection. Practise, don't reread:
  cover the right column of each story flow and retell the seven stages, redraw each concept graph
  from memory, say each Part's core idea aloud in 60 seconds.]
#concept-map([how to read one], nodes: (("t", 0, 0, "t", [Term], none), ("c", 1, 0, "c", [Concept], none),
  ("m", 2, 0, "m", [Method], none), ("x", 3, 0, "x", [From another Part], none)), edges: "t>c c>m", own: none)[legend]
== Map <sec:map>             // table: Part | sources (exam: courses with grades, weak in c-red)
== The big picture <sec:big-picture>   // #story: how the Parts form one loop; #takeaway
== The general framework <sec:framework>  // #framework, 5–7 field-wide steps citing @sec:...

#include "parts/01-....typ"
```

Every content Part, in this order:

1. `= Title <part:slug>` (exam mode: grades in the title, e.g. `= Calculus (C+ / B+)`).
2. `#part-story`: the one idea the Part grows from, how its topics follow, a one-liner to say aloud.
3. Spine diagram (§7) with its caption mapping arrows to sections. In deep-dive mode, draw one for the whole system in `@sec:big-picture` instead, and per Part only when that component has its own spine.
4. `#concept-map`.
5. `#framework`: 5–8 rows of step → question → tool, citing `@sec:...`.
6. `#story-flow` for the Part.
7. 5–10 `== Section <sec:slug>`, each: `#idea`, then definitions / theorems / interfaces, then one `#ex` with small numbers. Central concepts open their section with their own `#story-flow`.
8. `#ask` for the whole Part.

The reader's own thesis or project Part follows the same skeleton from their document only, plus a first-person section on their contribution and a "two-minute summary".

## 9. Writing rules

The voice and the ten principles are in `references/teaching-philosophy.md`. The ones agents most often break:

- Every section opens with *why it exists*, before any definition.
- Name the cross-Part connection wherever the mathematics really connects; these links are the content.
- Worked examples use small numbers and are **recomputed with `python3 -c`**, not by eye.
- Deep-dive examples are small numerical traces done by hand (two tokens through attention, one step of an optimiser), not code listings, unless the user asks for code.
- **Say where the new idea breaks.** The story flow's stage 3 covers the limits of the *old* approach; every central method also gets a `#pitfall` with its own failure modes and the one trade-off it cannot avoid. Required in deep-dive mode and for strong grades in exam mode.
- **An honest turn.** If the limit only *motivates* the idea rather than forcing it, name the extra assumption that makes the idea follow, and state it in stage 5 (Assumptions). "So we must use X" is allowed only when nothing else would fix the limit.
- **Each displayed equation answers a named question**: what is optimised, bounded, approximated, or traded off. An equation that answers none is cut.
- **Label how settled a claim is** where it is not textbook-standard: established, the standard account but contested, or uncertain. Never smooth a contested point into a clean story.

## 10. Build in batches and verify before reporting

Write Overview + the first 2–3 Parts, compile, then 3–4 Parts at a time, compiling after each batch.

1. The build finishes with zero errors (missing labels and wrong story-flow lengths are errors).
2. Render each concept-graph, spine-diagram and figure page (`pdftoppm -r 70 -png -f P -l P`) and look at it: no overlapping boxes, no arrows crossing boxes, figure text readable, no "trace 0" legends.
3. Run the end-of-Part checklist in `references/teaching-philosophy.md`.
4. Report: the Part list, Parts marked unverified scope, facts about the reader's work you could not confirm, and the version and sources used in deep-dive mode.
5. Offer the study-time next steps (the book's job ends where practice begins):
   - **Exercises** → `concept-exercise-generator`, one set per Part, passing this format as the brief: four tiers (1 define and identify; 2 run the method on a small case; 3 explain why, when it fails, what to choose; 4 derive, prove, design); every exercise with a model answer, a "you've got it if" check, and the "common wrong turn" it is designed to catch; the last exercise of each Part is the story-flow drill (retell the seven stages from memory).
   - **Done-check per Part** → `naive-student`: the reader teaches the Part's story flow from memory to an honest novice.
   - **A section that does not click** → `professor-mentor-technical-teaching` for a live explanation, rather than rewriting the book.
   - **Exam mode**: `apply-interview-prep` for mock interviews; `professor-critic` on the reader's own two-minute thesis summary or one-liners, with the named panel as the reader.

## 11. Adding a Part later

Keep the book's existing `lib/` (§5). Write `parts/NN-slug.typ`, add its `#include` in order, rebuild. If the book predates labels (hand-typed `§N.M`), ask before converting it; otherwise follow its numbering and check the references after it. In a labelled book, every reference renumbers itself. Renaming later part files to keep "file number = Part number" is cosmetic; do it only if the user wants it.
