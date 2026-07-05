# Research Idea Stress-Test Checklist

Use this reference when a research idea needs a deeper adversarial pass.

## Core Idea

A strong one-sentence idea specifies:
- mechanism;
- task;
- comparison target;
- expected improvement.

## Contribution Separation

Separate:
- method: what you do;
- hypothesis: why it should work;
- contribution: what the paper adds to the field.

If these collapse into one sentence, the idea may be under-specified.

## What Must Be True

List required assumptions:
- empirical;
- theoretical;
- data-related;
- compute-related;
- evaluation-related.

Mark each as verified, plausible, or untested.

## Novelty Illusions

Watch for:
- new vocabulary for an old method;
- combining two standard tools without a new mechanism;
- applying a known method to a dataset with no scientific reason;
- beating weak or stale baselines;
- "no one has tried it" without checking adjacent fields.

## Cheapest Falsifier

A good falsifier:
- is small;
- can fail clearly;
- targets the core mechanism;
- uses a fair baseline;
- avoids tuning until the mechanism is visible.

## Recommendation Labels

- **Pursue:** meaningful, testable, and cheap evidence supports it.
- **Narrow:** idea is too broad but contains a testable core.
- **Reframe:** current contribution claim is wrong but another framing may work.
- **Drop:** no clear novelty, no decisive test, or core assumption already fails.
