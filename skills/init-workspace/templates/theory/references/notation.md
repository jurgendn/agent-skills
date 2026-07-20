# Notation (reference)

Fix the project's notation here **once**, then use it across every `claims/`, `definitions/`, and `proofs/` note. Inconsistent notation between claims is a frequent source of bugs and reviewer confusion. Use `theory-formalism-translator` when moving a result between frameworks.

## Conventions (edit to match this project)

- **Scalars** $x$, **vectors** $\mathbf{x}$, **matrices** $\mathbf{X}$, **sets** $\mathcal{S}$, **random variables** capital $X$.
- **Expectation** $\mathbb{E}$, **probability** $\mathbb{P}$, **variance** $\mathrm{Var}$.
- **Norms**: state which — $\lVert\cdot\rVert_2$, $\lVert\cdot\rVert_\infty$, operator norm — and don't switch silently.
- **Asymptotics**: $O,\Omega,\Theta,o,\omega$; state what the limit is in (n → ∞, with d fixed?) and whether constants are **uniform**.
- **Indexing**: reserve $n$ for sample size, $d$ for dimension, $i,j$ for indices. Don't reuse a letter for two meanings.

## Project symbol table (fill in)

| Symbol | Meaning | First defined in |
|---|---|---|
| | | |

## Definitions index

List the precise definitions in `definitions/` as you add them, so claims can link to them:

- `[[definitions/...]]` — ...
