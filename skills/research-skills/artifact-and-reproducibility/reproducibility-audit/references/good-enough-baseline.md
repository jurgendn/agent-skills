# Reproducibility baseline: what a "good enough" artifact must contain

A checklist of the minimum ingredients whose *absence* is a reproducibility finding.
Derived from Wilson, Bryan, Cranston, Kitzes, Nederbragt, Teal, *Good Enough
Practices in Scientific Computing*, PLoS Comput. Biol. (2017), arXiv:1609.00037,
scoped here to the audit question: **can this result be regenerated from what's
available, and if not, exactly which piece is missing?**

Use this as the reference set behind step 2 of the workflow ("check for the required
ingredients"). Each row is a thing to look for; if it is missing or ambiguous, that is
a finding, not a minor annoyance.

## Data provenance
- **Raw data is preserved and read-only.** The originating data still exists,
  unmodified, separate from anything derived. If only cleaned/derived data survives,
  the pipeline from raw → analysis-ready cannot be checked. Finding.
- **Every processing step is recorded** — as a script, or (for inherently interactive
  steps) as explicit written instructions. A gap between raw data and the table in the
  paper that no script or note explains is a blocker.
- **Data is deposited and citable** (DOI-issuing repository) or, if access-restricted,
  the access path and any legal constraints are stated. "Data available on request"
  with no responder is effectively missing data.

## Code and dependencies
- **Code that produces each claimed number is present**, not just illustrative
  snippets. Distinguish *code availability* from *result reproducibility* — a public
  repo that can't regenerate Table 2 is available, not reproducible.
- **Dependencies and requirements are explicit and version-pinned**
  (`requirements.txt` / lockfile / environment file). "Install the usual libraries"
  is not pinning; unpinned deps are a silent source of drift.
- **A smoke/example test exists**: something a fresh user can run to confirm the code
  works on a known input before trusting the full pipeline. Its absence means the
  first sign of breakage is a wrong result.
- **The entry point is obvious** — a driver/`runall` script or a README command,
  not a folder of scripts with no stated order.

## Versioning and identity
- **The exact code version is pinned** (commit hash / tag / release) and matches what
  the paper reports. "Latest main" is not a version.
- **A README** states purpose and at least one working run command; a **CITATION**
  and **LICENSE** exist (licensing gaps block legitimate reuse just as hard as
  missing files).

## Determinism and environment
- **Random seeds are set and passed explicitly.** An unseeded result cannot be
  reproduced and cannot be defended to a reviewer — treat a missing seed as a
  first-class finding, not a footnote.
- **Hardware / platform assumptions are stated** where they affect results (GPU vs
  CPU numerics, thread counts, accelerator-specific kernels).

## Mapping to the audit verdict
For each target result, the claim should map to executable steps end to end. When it
doesn't, name the single missing ingredient from the list above rather than a vague
"not reproducible" — the smallest fix is usually one specific row here (deposit the
seed, pin the deps, add the driver command, publish the preprocessing script).
