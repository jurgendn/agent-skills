---
name: debugging-strategies
description: Apply systematic debugging, profiling, and root cause analysis across codebases and technology stacks. Use when investigating bugs, flaky behavior, crashes, stack traces, production issues, memory leaks, performance regressions, or any unexpected behavior where guessing would waste time.
---

# Debugging Strategies

Turn debugging into a controlled investigation: reproduce, isolate, hypothesize,
test, and only then fix. Do not shotgun changes.

For language/tool-specific commands and advanced patterns, read
`references/debugging-toolbox.md` only when needed.

## Core Process

### 1. Reproduce

Establish:
- exact steps;
- expected vs actual behavior;
- frequency: always / intermittent / environment-specific;
- smallest reproducible case;
- environment: commit, OS, runtime, dependency versions, config.

If it cannot be reproduced, collect more observability before changing code.

### 2. Isolate

Narrow the failing surface:
- remove unrelated inputs;
- reduce concurrency, caching, and external services;
- compare last known good vs current;
- bisect code, config, data, or dependency changes.

### 3. Form Hypotheses

Write 2-5 plausible causes. For each:
- why it explains the symptom;
- what evidence would confirm it;
- what evidence would falsify it;
- cheapest test.

Rank by probability times test cost, not by how interesting the theory is.

### 4. Test One Thing

Change or instrument one variable at a time. Preserve logs and commands. A fix
without a confirmed cause is a risk, not a result.

### 5. Verify and Prevent Regression

After a fix:
- rerun the minimal reproduction;
- rerun relevant tests;
- add a regression test if feasible;
- document the root cause and why the fix addresses it.

## Issue Routing

- Performance bottleneck in Python → `python-performance-optimization`.
- Test design or failing pytest suite → `python-testing-patterns`.
- Structural code problem causing repeated bugs → `python-design-patterns`.
- Prompt/model behavior in Claude-backed code → `prompting-claude-models`.

## Output

Return:
- symptom summary;
- reproduction status;
- narrowed failing surface;
- ranked hypotheses;
- exact next diagnostic;
- fix verification plan;
- regression-prevention step.
