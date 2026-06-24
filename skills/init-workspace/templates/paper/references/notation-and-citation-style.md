# Notation and citation style (reference)

Keep notation and citation usage consistent across every file in `drafts/`.
Drift between sections is one of the most common reviewer irritations. Fill in
the project-specific choices below once, then follow them everywhere.

## Notation conventions

- **Scalars** lowercase italic ($x$), **vectors** bold lowercase ($\mathbf{x}$),
  **matrices** bold uppercase ($\mathbf{X}$), **sets** calligraphic
  ($\mathcal{D}$). Pick one scheme and keep it.
- Define every symbol **at first use**; maintain a symbol table in `ideas/` if
  the method is notation-heavy.
- Don't overload symbols across sections (e.g. $n$ as both sample count and
  dimension). Reserve letters once.
- Functions vs values: be explicit ($f(\cdot)$ vs $f(x)$).
- Use `method-section-writer` to keep the method section's notation aligned with
  the rest of the paper.

### Project symbol decisions (fill in)

| Symbol | Meaning |
|---|---|
| | |

## Citation style

- **Parenthetical** vs **textual**: use `\citep{}` when the citation is an aside
  ("prior work shows X (Smith, 2020)") and `\citet{}` when the authors are the
  sentence subject ("Smith (2020) shows X"). Don't mix them up.
- Cite the **original** source for a claim, not a survey that repeats it, unless
  you are explicitly crediting the survey. `citation-auditor` checks for this.
- Every non-obvious factual/empirical claim gets a citation; every citation
  actually says what you claim it says.
- Consistent author/year vs numeric style per the venue template.

## Figures and tables

- Reference every figure/table in the text ("Figure 3 shows…"); never leave one
  unreferenced.
- Caption is self-contained: a reader should understand the figure from the
  caption alone. Plan these with `figure-table-planner`.
- Consistent capitalisation ("Figure 3", "Table 1") and `\autoref`/`\cref` usage.
