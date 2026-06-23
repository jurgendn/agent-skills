---
name: artifact-release-packager
description: Plan and audit research artifact releases for papers, including code, data, models, configs, checkpoints, scripts, environment files, licenses, and artifact evaluation instructions. Use this skill whenever the user wants to release a paper codebase, prepare an artifact evaluation package, map paper tables to reproduction commands, write release instructions, check whether a repository supports the paper's claims, or package models/data safely. Use reproducibility-audit to test whether results can be reproduced; use this skill to decide what to include and how to present the release.
---

# Artifact Release Packager

A paper artifact is not just a GitHub repository. It is the set of materials that lets another researcher understand, run, and trust the work at the level the paper claims.

## Use this when

- The user is preparing a code, data, model, or checkpoint release.
- The user needs artifact evaluation instructions.
- The paper's tables or figures need reproduction commands.
- The user wants to know what files, configs, or documentation are missing before release.
- The release may include sensitive, licensed, large, or non-redistributable assets.

## Do not use this when

- The user wants to verify an existing result end-to-end. Use `reproducibility-audit`.
- The user wants to structure, document, or simplify the codebase before release. Use `research-codebase`.

## Workflow

### 1. Define the release promise

State what the artifact is supposed to support:

- reproduce main results exactly
- reproduce trends approximately
- run a small smoke test
- inspect trained models or outputs
- reuse a dataset/preprocessing pipeline
- support artifact evaluation within a time budget

The package should not promise more than it can deliver.

### 2. Map paper claims to artifacts

For each major result, identify:

- paper location: table, figure, or claim
- required code entry point
- config file
- data dependency
- model/checkpoint dependency
- expected output
- expected runtime/hardware
- known variance or nondeterminism

If a result cannot be mapped, mark it as a release gap.

### 3. Build the release inventory

Check for:

- README with quickstart and reproduction map
- environment file or install instructions
- pinned dependency versions where needed
- data download or access instructions
- preprocessing scripts
- training/evaluation scripts
- configs for reported runs
- checkpoints or instructions for obtaining them
- expected outputs or checksums
- license files
- citation file if relevant
- privacy or redistribution notes

### 4. Design the reviewer path

Artifact reviewers and future readers need a short path first:

1. install environment
2. run smoke test
3. reproduce one small result
4. reproduce or inspect main result
5. understand full-run cost

Do not make the first successful run require the full expensive experiment.

### 5. Check release safety

Flag:

- secrets or credentials
- private paths or usernames
- non-redistributable datasets
- model licenses that restrict release
- personally identifiable information
- large files better hosted elsewhere
- generated files that should not be committed

## Output format

```markdown
# Artifact Release Plan

## Release promise

## Claim-to-artifact map
| Paper claim/result | Required artifact | Command/config | Expected output | Status |
|---|---|---|---|---|

## Required package contents

## Smoke test path

## Full reproduction path

## Safety/licensing concerns

## Missing pieces

## Release README outline
```

## Quality bar

A good artifact package lets a skeptical researcher quickly answer: what does this release support, how do I run it, what should I expect, and where are the limits?
