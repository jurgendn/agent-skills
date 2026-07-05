---
name: reproducibility-audit
description: Audit whether a result can actually be reproduced from the available code, data, configs, and documentation. Use before trusting a benchmark claim or releasing your own work. Use for replication, code release checks, paper artifact sanity checks, lab handoffs, catching missing seeds/configs/data before results are cited, or whenever "works on my machine" is a risk. If the user wants to plan what to include in a public artifact package, use artifact-release-packager instead; this skill's job is to test whether reproduction is possible and where it breaks.
---

# Reproducibility Audit

Assume the result is not reproducible until the missing pieces are enumerated.

## Workflow

1. Identify the target result to reproduce.
2. Check for the required ingredients:
   - code
   - commit/version pinning
   - data access
   - config files
   - preprocessing steps
   - hardware assumptions
   - seed handling

   `references/good-enough-baseline.md` expands this into a concrete
   presence/absence checklist (data provenance, pinned dependencies, smoke test,
   version identity, determinism) grounded in *Good Enough Practices in Scientific
   Computing* (Wilson et al., 2017) — a missing item there is a finding, not a
   minor annoyance.
3. Attempt to map paper claims to executable steps.
4. Record ambiguities and blockers explicitly.
5. If running code, log exact commands and outputs.
6. Classify status:
   - reproduced
   - partially reproduced
   - blocked
   - inconsistent with paper
7. Recommend the smallest fixes needed for reproducibility.

## Rules

- Do not say reproduced unless you ran and checked it.
- Missing config details are findings, not minor annoyances.
- Separate code availability from result reproducibility.

## Output shape

Return:
- Target result
- Available artifacts
- Missing artifacts
- Reproduction status
- Commands / evidence
- Recommended fixes
