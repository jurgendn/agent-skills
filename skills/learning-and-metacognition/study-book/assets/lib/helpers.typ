// Study-book boxes and diagrams. Re-exports everything from template.typ.
#import "template.typ": *
#import "@preview/fletcher:0.5.8": diagram, node, edge

// Plain information box (overview pages, source facts).
#let box-note(title, body) = teach-box(title, "■", c-muted, body)

// Opening of every Part (violet): the one idea the Part grows from.
#let part-story(principle, body) = story(title: "The core idea")[
  *Core principle: #principle*
  #v(0.3em)
  #body
]

// Opening of every section (orange): why the topic exists and how its pieces connect.
#let idea(body) = teach-box("The story", "→", c-orange, body)

// Worked example (framed).
#let ex(body, title: "Worked example") = derivation(title: title, body)

// Questions at the end of a Part: "Likely questions" (exam) or "Self-test questions" (learning).
#let ask(body, title: "Likely questions") = teach-box(title, "?", c-blue, body)

// Divider inside one long section.
#let part(body) = block(sticky: true, above: 1.6em, below: 0.6em, width: 100%, stroke: (bottom: 0.8pt + c-orange), inset: (bottom: 4pt))[
  #text(font: heading-font, size: 11pt, weight: "bold", fill: c-orange)[#upper(body)]
]

// Display style for inline maths (full-size fractions, sums, integrals). Use: #show: inline-display
#let inline-display(body) = {
  show math.equation.where(block: false): it => {
    if it.body.func() == math.display($x$).func() { it } else { math.equation(math.display(it.body), block: false) }
  }
  body
}

// Concept dependency graph. Arrows run from a prerequisite to what is built on it.
// nodes: (key, x, y, kind, label, sec). kind: "t" term, "c" concept/theorem, "m" method, "x" from another Part.
// sec: a heading label such as <sec:svd>, or none. A label that does not exist fails the build.
// edges: space-separated "a>b", or "a>b~30" to bend by 30 degrees.
// own: true when the graph tells a story the prose does not; false when it retells the Part story; none for no prefix.
#let concept-map(title, nodes: (), edges: "", own: false, reading) = {
  let style = (
    t: (fill: white, stroke: 0.5pt + c-muted, corner-radius: 0pt),
    c: (fill: c-violet.lighten(88%), stroke: 1.1pt + c-violet, corner-radius: 2pt),
    m: (fill: c-orange.lighten(88%), stroke: 0.8pt + c-orange, corner-radius: 11pt),
    x: (fill: luma(245), stroke: (paint: c-muted, thickness: 0.6pt, dash: "dashed"), corner-radius: 2pt),
  )
  block(breakable: false, above: 1em, below: 1.2em, width: 100%)[
    #text(font: heading-font, size: 9pt, weight: "bold", fill: c-violet)[Concept graph: #title]
    #v(0.2em)
    #align(center, diagram(
      cell-size: (3.05cm, 1.45cm),
      spacing: 0pt,
      edge-stroke: 0.6pt + c-muted,
      ..nodes.map(((key, x, y, kind, body, sec)) => node(
        (x, y),
        box(width: 2.55cm, align(center, text(size: 8pt, hyphenate: false)[#set par(justify: false)
          #body#if sec != none [ #text(size: 6.5pt, fill: c-muted, ref(sec))]])),
        name: label(key), inset: 3.5pt, ..style.at(kind),
      )),
      ..edges.split().map(e => {
        let (path, ..bend) = e.split("~")
        let (a, b) = path.split(">")
        assert(nodes.any(n => n.at(0) == a) and nodes.any(n => n.at(0) == b), message: "unknown node in edge " + e)
        edge(label(a), label(b), "-|>", bend: if bend.len() > 0 { float(bend.at(0)) * 1deg } else { 0deg })
      }),
    ))
    #v(0.15em)
    #text(size: 8.5pt)[#if own == true [*The graph's own story:*] else if own == false [*Follows the story:*] #reading]
  ]
}

// Decision table: at each step, what to ask and which tool to pick. rows: step, question, tool (cite with @sec:...).
#let framework(title, ..rows) = block(breakable: false, above: 1em, below: 1.2em, width: 100%)[
  #block(sticky: true, below: 0.5em, text(font: heading-font, size: 9pt, weight: "bold", fill: c-aqua.darken(25%))[Framework: #title])
  #set text(size: 8.5pt)
  #table(
    columns: (0.8fr, 1.1fr, 2.3fr),
    [*Step*], [*Ask*], [*Choose the tool*],
    ..rows.pos(),
  )
]

// Story flow: seven fixed stages, one text each. The turn is stage 3 -> 4 (highlighted).
#let story-flow(title, ..texts) = {
  let stages = ([Problem], [Approaches], [Limits + motivation], [Idea], [Assumptions], [Theory], [Summary + ELI5])
  assert(texts.pos().len() == stages.len(), message: "story-flow needs exactly 7 texts, one per stage")
  block(breakable: false, above: 1em, below: 1.2em, width: 100%)[
    #text(font: heading-font, size: 9pt, weight: "bold", fill: c-violet)[Story flow: #title]
    #v(0.2em)
    #align(center, diagram(
      spacing: (0.3cm, 0.36cm),
      edge-stroke: 0.7pt + c-muted,
      ..stages.enumerate().map(((i, name)) => node(
        (0, i),
        box(width: 2.9cm, align(center, text(size: 8pt, weight: "bold")[#set par(justify: false)
          #name])),
        name: label("s" + str(i)), inset: 3.5pt, corner-radius: 2pt,
        fill: if i == 3 { c-orange.lighten(85%) } else { c-violet.lighten(88%) },
        stroke: (if i == 3 { 1.1pt + c-orange } else { 0.8pt + c-violet }),
      )),
      ..texts.pos().enumerate().map(((i, body)) => node(
        (1, i),
        box(width: 12.6cm, align(left, text(size: 8.5pt)[#set par(justify: false)
          #body])),
        stroke: none, inset: 0pt,
      )),
      ..range(stages.len() - 1).map(i => edge(label("s" + str(i)), label("s" + str(i + 1)), "-|>")),
    ))
  ]
}
