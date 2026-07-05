---
name: experiment-trace-summarizer
description: Turn messy logs, notebooks, run metadata, and partial conclusions into a clear research update with next actions. Use after intense experimentation, for lab notes, handoff, weekly updates, resuming interrupted work, or when run history needs to become decisions rather than scattered impressions.
---

# Experiment Trace Summarizer

Compress the run history into decisions.

## Intake

Collect the raw trace:
- run ids, commands, configs, seeds, commits;
- metrics and plots;
- notes about anomalies or manual interventions;
- what changed between runs;
- current question the experiment was meant to answer.

## Workflow

1. Gather commands, configs, metrics, and observations.
2. Separate confirmed findings from tentative impressions.
3. Summarize what changed and what mattered.
4. List dead ends and unresolved questions.
5. Identify the current decision state: continue, pivot, debug, rerun, or stop.
6. Recommend exact next runs.

## Rules

- Preserve provenance for every important number.
- Do not tidy away contradictory evidence.
- Do not merge runs with different configs into one conclusion.
- Mark impressions as impressions until backed by a run.

## Output

Return:
- question being tested;
- run timeline;
- confirmed findings;
- contradictions or anomalies;
- current decision;
- next 1-3 runs with exact purpose.
