# Debt Taxonomy — knowledge-debt-audit

Ground truth for the strategic-vs-toxic classifier. The classifier drifts in one
direction — toward over-flagging, toward nagging — and these examples are the anchor
that keeps it from probing things it should leave alone. If the skill wants to
interrogate a *strategic* borrow, it is miscalibrated; re-read this file.

The one question that decides the bucket:

> **Will you need to regenerate this, unaided, in an exposure moment?**

No → strategic, stay silent. Yes → toxic, probe now.

---

## Toxic (call the loan)

- **A derivation under your next paper.** You let the AI produce the Schrödinger-bridge
  identity and now you're writing the method section on it. A reviewer asks why it
  holds for *your* cost. Borrowed understanding is worthless collateral here.
  → probe the load-bearing why, or invoke the inversion.
- **A theorem your calibration depends on.** Your $\lambda$-calibration rests on a
  scaling result you didn't derive. If you can't reproduce it on a whiteboard, the
  whole calibration is a black box you can't defend.
- **A concept on your measure-theory / quals track.** Anything you'll be examined on,
  AI-free, by definition. Fluency now ≠ recall under exam conditions.
- **A step you're about to *generalize*.** Extending a result you don't own means the
  extension inherits the debt — and you won't notice where it breaks.

## Strategic (stay silent)

- **The plotting / rendering call** that drew your figure. You will never derive
  matplotlib from scratch and shouldn't. Pure efficiency.
- **API / CLI syntax** (the GitHub trees endpoint, a curl flag). Look-up-able forever;
  internalizing it is waste.
- **A library's internals** you call but don't modify. Borrow the interface, skip the
  guts — until the day you actually need the guts, at which point it reclassifies.
- **Boilerplate** — config scaffolding, a Dockerfile, a CI yaml. Carrying it costs you
  nothing in any exposure moment.

---

## The reclassification rule

Debt is not static. A strategic borrow becomes toxic the moment you move to *build on
its internals*. Calling PyTorch's `eigvalsh` is strategic — until your contribution
*is* a claim about how that eigendecomposition behaves, at which point you now owe the
understanding. The skill should re-check the bucket at each new borrow, not assume the
last classification holds.

## The honest tell

When in doubt, the failure mode to fear is leniency, not strictness — but only on the
*toxic* side. On the strategic side, fear over-strictness. Concretely:

- A *toxic* borrow marked "probed-passed" on a vague answer → false certificate. Worst case.
- A *strategic* borrow that gets probed at all → nag. Second worst, and the one that
  gets the skill turned off.

Two different errors, two different sides. The classifier's whole job is keeping them
straight.
