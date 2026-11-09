// ============================================================
//  Study book: page style, colours, teaching boxes, document set-up
// ============================================================

#let c-blue   = rgb("#2a78d6")
#let c-orange = rgb("#eb6834")
#let c-aqua   = rgb("#1baf7a")
#let c-yellow = rgb("#eda100")
#let c-violet = rgb("#6250d6")
#let c-red    = rgb("#e34948")
#let c-ink    = rgb("#1b1b1a")
#let c-muted  = rgb("#5f5e5a")

// Avenir Next / Helvetica are macOS fonts; elsewhere Typst falls back with a warning.
#let heading-font = ("Avenir Next", "Helvetica Neue", "Helvetica")
#let body-font = ("Libertinus Serif", "New Computer Modern")

// ---- math operators ------------------------------------------------
#let argmin = math.op("arg min", limits: true)
#let argmax = math.op("arg max", limits: true)
#let Var = math.op("Var")
#let Cov = math.op("Cov")
#let sign = math.op("sign")
#let tr = math.op("tr")
#let softmax = math.op("softmax")
#let diag = math.op("diag")
#let KL = math.op("KL")

// ---- generic coloured box ------------------------------------------
#let teach-box(title, icon, accent, body) = block(
  width: 100%,
  breakable: true,
  above: 1.1em,
  below: 1.1em,
  stroke: (left: 3pt + accent),
  fill: accent.lighten(92%),
  inset: (left: 12pt, right: 10pt, top: 9pt, bottom: 9pt),
  radius: (right: 4pt),
)[
  #block(sticky: true, above: 0pt, below: 0.6em, text(font: heading-font, weight: "bold", size: 9.5pt, fill: accent.darken(25%))[#icon #h(3pt) #upper(title)])
  #set text(size: 10.2pt)
  #body
]

#let story(title: "A short story", body) = teach-box(title, "◆", c-violet, body)
#let eli5(body) = teach-box("Explain like I'm 5", "●", c-yellow.darken(10%), body)
#let takeaway(body) = teach-box("Key takeaways", "✓", c-ink, body)
#let pitfall(body) = teach-box("Common pitfall", "!", c-red.darken(10%), body)

#let derivation(title: "Derivation", body) = block(
  width: 100%, breakable: true, above: 1em, below: 1em,
  stroke: 0.6pt + c-muted.lighten(40%), radius: 4pt,
  inset: 11pt,
)[
  #block(sticky: true, above: 0pt, below: 0.6em, text(font: heading-font, weight: "bold", size: 9.5pt, fill: c-muted)[∂ #h(3pt) #upper(title)])
  #body
]

// Takes content, not a path: a path string would resolve relative to this file (lib/).
// Use: #fig(image("/figures/a.png", width: 85%), [caption])  (root-absolute; build with --root .)
#let fig(img, caption) = figure(img, caption: caption)

#let defn(term, body) = block(above: 0.8em, below: 0.8em, inset: (left: 10pt), stroke: (left: 1pt + c-muted.lighten(50%)))[
  *#term.* #body
]

// ---- document set-up --------------------------------------------------
#let book(
  title: "",
  subtitle: "",
  author: "",
  doc-title: "",
  header-title: [],
  kicker: "",
  blurb: [],
  body,
) = {
  set document(title: doc-title)
  set page(
    paper: "a4",
    margin: (x: 2.2cm, top: 2.4cm, bottom: 2.4cm),
    numbering: "1",
    header: context {
      let pg = here().page()
      // Prefer a Part that starts on this page; otherwise the last one before it. None yet: no header.
      let parts = query(heading.where(level: 1)).filter(h => h.numbering != none)
      let on-page = parts.filter(h => h.location().page() == pg)
      let hs = parts.filter(h => h.location().page() < pg)
      if on-page.len() > 0 or hs.len() > 0 {
        let cur = if on-page.len() > 0 { on-page.first().body } else { hs.last().body }
        set text(font: heading-font, size: 8pt, fill: c-muted)
        grid(columns: (1fr, auto), header-title, cur)
        v(-6pt)
        line(length: 100%, stroke: 0.4pt + c-muted.lighten(50%))
      }
    },
  )
  set text(font: body-font, size: 10.8pt, fill: c-ink, lang: "en")
  set par(justify: true, leading: 0.68em, spacing: 1.05em)
  show math.equation: set text(font: "New Computer Modern Math")
  set math.equation(numbering: "(1)")
  // The first level-1 heading (Overview) is Part 0.
  set heading(numbering: (..n) => { let v = n.pos(); numbering("1.1.1", v.first() - 1, ..v.slice(1)) })
  // @sec:x prints "§ 1.3"; @part:x prints "Part 1".
  set heading(supplement: [§])
  show heading.where(level: 1): set heading(supplement: [Part])
  show heading: set text(font: heading-font)
  show heading: set par(justify: false)
  show heading.where(level: 1): it => {
    pagebreak(weak: true)
    v(2.2cm)
    if it.numbering != none {
      text(size: 13pt, fill: c-orange, weight: "bold")[PART #(counter(heading).get().first() - 1)]
      v(-4pt)
    }
    text(size: 24pt, weight: "bold", fill: c-ink, it.body)
    v(4pt)
    line(length: 30%, stroke: 2pt + c-orange)
    v(1.2em)
  }
  show heading.where(level: 2): it => {
    v(1.2em)
    text(size: 15pt, weight: "bold", fill: c-blue.darken(30%), it)
    v(0.4em)
  }
  show heading.where(level: 3): it => {
    v(0.8em)
    text(size: 12pt, weight: "bold", fill: c-ink, it)
    v(0.2em)
  }
  show heading.where(level: 4): it => text(size: 10.8pt, weight: "bold", style: "italic", it.body) + h(0.5em)
  show figure.caption: set text(size: 9pt, fill: c-muted)
  show link: set text(fill: c-blue)
  set list(indent: 0.6em)
  set enum(indent: 0.6em)
  show table: set text(size: 9.5pt)
  show table: set par(justify: false)
  set table(stroke: 0.4pt + c-muted.lighten(50%), inset: 6pt)

  // ---- Title page ----
  page(numbering: none, header: none)[
    #v(4cm)
    #text(font: heading-font, size: 11pt, fill: c-orange, weight: "bold", tracking: 2pt)[#kicker]
    #v(0.4cm)
    #text(font: heading-font, size: 34pt, weight: "bold", fill: c-ink)[#title]
    #v(0.2cm)
    #line(length: 40%, stroke: 3pt + c-orange)
    #v(0.4cm)
    #text(font: heading-font, size: 14pt, fill: c-muted)[#subtitle]
    #v(1fr)
    #text(size: 10.5pt, fill: c-muted)[#blurb]
    #v(1cm)
    #text(font: heading-font, size: 10pt, fill: c-muted)[#author]
  ]
  body
}
