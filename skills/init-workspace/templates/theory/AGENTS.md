# AGENTS.md — Theory: <PROJECT TITLE>

Orientation for any agent operating on this theory/proof vault. This file is the
map and the rules; the proof craft lives in the installed `theory-*` skills this
file routes to. The vault tracks claims from informal idea to proved (or
refuted) statement, with a paper trail of assumptions, counterexamples, and toy
cases.

## What this vault is

A workspace for developing mathematical/theoretical results. Each claim is a
note that moves through `conjecture → sketched → proved` (or `refuted`). The
vault optimises for *knowing exactly what is assumed, what is proved, and where
it breaks* — the things that decide whether a theory result survives review.

## Layout

```text
claims/           # informal → formal statements being developed
definitions/      # precise definitions and the notation setup
proofs/           # proof sketches → full proofs, one per claim
counterexamples/  # constructions that break or bound a claim
toy-cases/        # minimal examples, simulations, sanity checks
references/       # proof-techniques, common-pitfalls, notation
_dashboard/       # claims-status
```

## Filename conventions

```text
claims/           claim-{NNN}-{shortname}.md       # claim-001-uniform-bound.md
proofs/           proof-{NNN}-{shortname}.md       # mirrors the claim id
counterexamples/  cex-{NNN}-{shortname}.md
toy-cases/        toy-{NNN}-{shortname}.md
```

Zero-pad numbers. A proof mirrors its claim's id so `claim-001` ↔ `proof-001`.

## Claim note format

Every file in `claims/` opens with YAML frontmatter so `_dashboard/` can track
status and assumptions:

```markdown
---
claim: claim-001
status: sketched          # conjecture | sketched | proved | refuted
statement: under <assumptions>, the estimator achieves a uniform O(1/n) bound
assumptions: [bounded-loss, iid-data, convexity]
proof: proof-001
date: 2026-06-24
---

## Statement (formal)
...

## Why it should be true (intuition)
...

## Status notes
What's proved, what's hand-wavy, what would refute it.
```

## Routing

| Folder / task | Skill to use |
|---|---|
| formalising an idea | `theory-proof-sketcher`, `theory-formalism-translator` |
| `definitions/`, assumptions | `theory-assumption-extractor` |
| `proofs/` | `theory-proof-sketcher`; `theory-derivation-auditor` to check steps |
| `counterexamples/` | `theory-counterexample-hunter` |
| `toy-cases/` | `theory-to-toy-cases` |
| auditing a finished claim | `theorem-and-claim-audit`, `gap-finder` |

Use `flow-idea-to-proof` to orchestrate the sequence (idea → claim → assumptions
→ sketch → audit) when unsure what comes next.

## Default actions

- **New idea:** create `claims/claim-{NNN}-…md` (`conjecture`), state it
  formally, list explicit + hidden assumptions (`theory-assumption-extractor`).
- **Developing a proof:** sketch in `proofs/proof-{NNN}…md`; audit every
  non-trivial step with `theory-derivation-auditor` before trusting it.
- **Before claiming `proved`:** stress-test with `theory-counterexample-hunter`
  and a `toy-cases/` sanity check; run `theorem-and-claim-audit`.
- **Update `_dashboard/claims-status.md`** whenever a claim's status changes.

## Rules

- **Assumptions are explicit.** Every claim lists what it assumes, including the
  conveniences a proof quietly relies on (`theory-assumption-extractor`). A
  weaker-than-stated assumption is a bug.
- **Stress-test before trusting.** A claim is `conjecture` until a counterexample
  hunt and a toy case have failed to break it. Don't mark `proved` on intuition.
- **Check the algebra.** Run `theory-derivation-auditor` on derivation-heavy
  steps; off-by-epsilon and non-uniform bounds are the usual culprits
  (`common-pitfalls.md`).
- **Notation is fixed once** in `definitions/` and `references/notation.md`; don't
  let symbols drift between claims.
