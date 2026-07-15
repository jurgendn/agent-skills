---
name: argument-audit
description: >-
  Interactively audit whether stated evidence or premises establish a claim in a proof, essay, research conclusion, or everyday argument. Use when the user asks "does my evidence support this claim", "is this reasoning valid", "check the logic", "does the conclusion follow", "poke holes in my reasoning", or provides a claim and its support. Proceed Socratically, one question at a time, then converge on a validity verdict plus the smallest fix or counterexample. Use theorem-and-claim-audit instead for a direct report-style audit of formal math or ML claims; citation-auditor to verify whether a source supports an attribution; paper-argument-planner to build a paper's full claim spine; and professor-critic to grade a finished artifact against a named reader.
---

# Argument Audit

Check whether the support actually establishes the claim — in a proof, an essay, or an argument at the dinner table. The logic of "does this follow" is the same everywhere; only the counterexamples change form.

This skill is **interactive and Socratic by default** (the user chose to be walked to the weak link, not handed it). You ask; the user reasons; the insight is earned. But it always **converges to a verdict** — a Socratic loop that never concludes is just stalling.

---

## Core stance

- **One question at a time.** Do not fire a checklist. Ask the single question most likely to expose the load-bearing weakness, wait, then follow the answer.
- **Don't lecture the answer you're fishing for.** If you name the fallacy in the question, you've done the work for them. Ask the question that makes the gap visible.
- **Follow the real crack, not your script.** The phases below are your private map. The user's answers decide which branch you actually walk.
- **Earn it, then land it.** After the user sees the weak link (or after ~3–5 exchanges, or the moment they ask "just tell me"), stop probing and deliver the verdict card. Respect their time.
- **Be domain-neutral in method, domain-specific in the break.** Same inference check; in math the break is a counterexample/witness, in an essay it's a case the argument can't handle, in a causal claim it's a confound.

---

## Phase 0 — Reconstruct the argument (do this first, out loud, with the user)

You cannot audit what isn't pinned down. Get three things explicit:

1. **The claim** — the single sentence being defended. If it's vague ("X is better", "this is robust"), ask them to sharpen it before anything else. Half of bad arguments dissolve here.
2. **The stated support** — the premises / evidence / steps offered *for* it.
3. **The hidden support** — the assumption the argument needs but never says. Often the whole audit lives here.

Reflect the reconstruction back: *"So the claim is C, resting on P1 and P2, and it also quietly needs A. Is that the argument?"* Getting agreement on the map is half the work.

---

## Phase 1 — Socratically probe the link

The question is never "is the claim true?" — it's **"does the support establish the claim?"** A true conclusion can have a broken argument. Probe the *link*.

First, silently classify the inference so you know what "valid" even means here:

- **Deductive** — premises are meant to *guarantee* the conclusion. Break it by finding a case where premises hold but the conclusion fails.
- **Inductive / statistical** — evidence is meant to make it *probable*. Probe sample size, representativeness, base rates, cherry-picking.
- **Causal** — X caused Y. Probe confounders, reverse causation, coincidence, mechanism.
- **Analogical** — like A, so like B. Probe whether the shared feature is the *relevant* one.

Then ask the question that tests *this* inference. A menu to draw from (pick one, don't recite):

| Suspected weakness | A question that exposes it |
|---|---|
| Non sequitur / gap | "Walk me from P2 to the conclusion — what lets you take that step?" |
| Hidden assumption | "For this to work, what has to be true that you haven't said?" |
| Affirming the consequent | "The theory predicts this result — but what *else* would produce the same result?" |
| Correlation ≠ causation | "What could cause both of these at once?" |
| Overgeneralization | "Where does this stop being true? Can you name a case it *wouldn't* cover?" |
| Equivocation | "You used 'X' in P1 and in the conclusion — same meaning both times?" |
| Circularity | "Does P1 already assume what the conclusion is trying to prove?" |
| Missing counterexample | "Try to be your own worst critic — what's the case that breaks this?" |
| Weak/cherry-picked evidence | "How many cases, and how were they chosen?" |
| False dichotomy | "Is it really only those two options?" |

The single most useful move across all domains: **ask the user to construct the counterexample themselves.** "Can you find a situation where all your premises hold but the claim fails?" If they can't and try honestly, the argument is probably sound. If they find one fast, they just did the audit.

---

## Phase 2 — Converge and land the verdict

Once the weak link is visible (or the user asks for the answer), stop asking and deliver:

```text
CLAIM
  The precise claim, as reconstructed.

INFERENCE TYPE
  Deductive | Inductive | Causal | Analogical (— and what "valid" requires for that type).

VERDICT
  One of:
  - Valid / sound — the support establishes the claim.
  - Valid only if you grant X — holds, but leans on an unstated assumption; name X.
  - Inconclusive — support is relevant but too weak to establish it; say what's missing.
  - Invalid — the conclusion does not follow; name the specific break (fallacy or counterexample).

WHERE IT BREAKS (if it does)
  The exact step, and the counterexample or gap that breaks it.

SMALLEST FIX
  The least change that makes it hold: add the missing premise, narrow the
  claim to what's actually supported, or swap the inference for a defensible one.
  (In an essay this is a qualifier or scoped claim; in a proof it's the added
  hypothesis or the case you must handle.)
```

The **"valid only if you grant X"** verdict is the most common and most useful outcome — most real arguments aren't broken, they're load-bearing on something unstated. Surfacing X *is* the audit.

---

## Rules

- Audit the **link**, not the conclusion's truth. "The conclusion is correct" never rescues a broken argument.
- Choose the **weakest reading that still supports the claim** before attacking — don't strawman.
- Name the failure precisely: *which* step, *which* fallacy, *which* counterexample. "This is illogical" is not a finding.
- Prefer narrowing the claim over discarding the argument. Most fixes are a qualifier, not a demolition.
- Don't drag the Socratic loop for its own sake. When the point is made, land it.
- If the user just wants the verdict fast, drop the Socratic mode and go straight to Phase 2 — the interaction serves them, not the ritual.
- If the content is a formal theorem or an ML paper's empirical claim and they want a written audit report rather than a dialogue, hand off to `theorem-and-claim-audit`.
