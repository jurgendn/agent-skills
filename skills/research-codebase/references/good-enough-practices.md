# Good Enough Practices in Scientific Computing

Published grounding for this skill's "add structure only when the pain justifies it"
stance. Source: Wilson, Bryan, Cranston, Kitzes, Nederbragt, Teal, *Good Enough
Practices in Scientific Computing*, PLoS Comput. Biol. (2017), arXiv:1609.00037.

The paper's whole thesis is the same as this skill's: it deliberately recommends a
**minimum viable** set of practices (not "best" practices) that a solo researcher or
a small team will actually keep using months later — and explicitly *defers* the
heavyweight tooling until a project is large enough to pay for it. Use this file as
the citable baseline behind the skill's rules, and as a checklist when a user asks
"what's the least I should be doing to keep this reproducible?"

## The minimum-viable checklist (paper's "Box 1")

**Data management**
- Save the raw data; treat it as read-only.
- Create the data you wish you had (record the steps that get you there).
- Create analysis-friendly ("tidy") data: one variable per column, one observation
  per row, ready to load without manual cleaning.
- Record *all* the steps used to process data — as scripts where feasible, as
  explicit written notes where a step is inherently interactive.
- Anticipate needing multiple tables; give each record a unique, persistent key.
- Submit data to a reputable DOI-issuing repository (Zenodo, Figshare, Dryad) so
  others can find, use, and cite it.

**Software**
- Put a brief explanatory comment at the start of every program.
- Decompose programs into functions; eliminate duplication.
- Reuse well-maintained libraries instead of rewriting; test them before relying.
- Give functions and variables meaningful names.
- Make dependencies and requirements explicit (a `requirements.txt` at the root).
- Don't comment/uncomment blocks to change behavior — use `if/else` or a flag.
- Provide a simple example or test dataset (a "build and smoke test").
- Submit code to a DOI-issuing repository on paper submission, as you do with data.

**Collaboration**
- A `README` overview (title, purpose, contact, an example run command).
- A `CONTRIBUTING` file (dependencies, how to run tests, conventions).
- A shared to-do list (a plain file, or issues).
- An explicit `LICENSE` (CC-0/CC-BY for data & text; MIT/BSD/Apache for code).
- A `CITATION` file so the work is easy to credit.

**Project organization** (the canonical layout)
- One directory per project, named after the project.
- `doc/` for text (manuscript, notes, lab notebook).
- `data/` for raw data + metadata; `results/` for generated/derived files.
- `src/` for project code (analysis "guts" + a `runall` driver script).
- `bin/` for external/compiled programs (omit if none).
- Name files by content/function, never by sequence number or figure position
  (`sightings_analysis.py`, not `result2.csv` or `fig3a.png`).

**Tracking changes**
- Back up (almost) everything a human created, as soon as it's created.
- Keep changes small; share them frequently.
- Keep and use a checklist for what a good commit/change looks like.
- Mirror the project off your machine (remote VCS or sync).
- Either a disciplined manual scheme (a dated `CHANGELOG.txt` + periodic full-copy
  snapshots) **or** a version-control system — pick one and have everyone agree
  before work starts.

**Manuscripts**
- Either an online rich-text tool with change tracking and reference management
  (single master doc, no email merging) **or** plain text (LaTeX/Markdown) under
  version control. The choice matters less than everyone agreeing on it up front.
- Ship supplementary tables/data as reusable text formats (CSV/JSON/YAML), not
  locked inside a PDF.

## What the paper deliberately leaves out (defer until it pays)

This list is the paper's own "What We Left Out" — it is the external backing for this
skill's *Patterns to avoid* and *What to skip* sections. Each is genuinely good, but
only starts paying off past the solo/small-team, single-paper scale:

- **Branches** — add after mastering a basic edit–commit workflow.
- **Build tools (Make)** — a shell script that re-runs everything is fine at small
  scale.
- **Unit tests** — a 20-line smoke/`sanity_check.py` is the good-enough substitute
  for solo exploratory work.
- **Continuous integration** — pays off with many contributors, not a single author.
- **Coverage, profiling/perf tuning** — only once correctness is solved and
  performance is the actual bottleneck.
- **Formal semantic-web metadata, heavyweight documentation** — write the brief
  header comment now; write comprehensive docs when you have users.

The paper's key observation: experienced developers *do* many of these even on small
projects, because they've already paid the learning cost. The danger is prescribing
that full stack to a newcomer, which scares them off the core practices that actually
matter. Recommend the core; name the rest as "later, when it hurts."
