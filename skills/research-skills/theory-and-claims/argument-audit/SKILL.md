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
- **Make the user construct the counterexample.** This is the load-bearing move, not a nice-to-have. Your own judgment of an argument is the least reliable input in the room; the user testing whether the premises can hold while the claim fails is the actual verification. Push the construction to them whenever they can carry it.
- **A fallacy name is a hypothesis, not a finding.** Naming the flaw ("that's affirming the consequent") is guesswork and often wrong. Do not assert the label. Instead reconstruct the implicit step it depends on and test *that* with a case. The break survives; the name is disposable.

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

There are only **three places to attack any argument** — this is your complete search space, so make sure you've considered each before settling:

1. **A premise is false or unwarranted** — the support itself doesn't hold.
2. **The conclusion fails on external grounds** — even granting the premises, a known fact or case contradicts the claim.
3. **The link doesn't carry** — the premises could all be true and the conclusion still not follow.

The skill privileges (3), because that's the one people miss and the one "the conclusion is correct" can't rescue. But name all three to yourself so you don't tunnel on the link when the real problem is a smuggled premise.

Then classify the inference so you know what "valid" even means here — and note that only **deductive** arguments are graded pass/fail; the other three are graded by *strength of support*, so don't declare a reasonable inductive or causal argument "invalid" just because it isn't a guarantee:

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

The table above catalogs *failure modes*. When the argument fits a recognizable **scheme**, a faster route is to run that scheme's standard critical questions — these are pre-validated and more precise than an improvised probe. Match the argument to one and ask its questions until one bites:

| Argument scheme | Critical questions (ask until one lands) |
|---|---|
| **Expert opinion** ("an authority says X") | Is the source a genuine expert in *this* domain? Did they actually assert X? Are they biased or funded? Do other experts agree? |
| **Cause to effect** ("X produced Y") | Could a third factor cause both? Could the direction run Y→X? Is the correlation strong and consistent? Is there a mechanism? |
| **Analogy** ("A works, and B is like A") | Is the *shared* feature the one doing the work? What's the disanalogy that matters here? |
| **Sign / correlation** ("X, therefore Y — they go together") | Is the association reliable, or could X occur without Y? |
| **Popular opinion** ("everyone accepts X") | Does wide acceptance track truth here, or just familiarity? Who dissents, and why? |
| **Slippery slope** ("X leads to Z") | Is each step actually likely, or just possible? Where does the chain realistically stop? |

The single most useful move across all domains, when the user can carry it: **have them construct the counterexample themselves.** "Can you find a situation where all your premises hold but the claim fails?" If they try honestly and can't, the argument is probably sound. If they find one fast, they just did the audit.

---

## Phase 2 — Converge and land the verdict

Once the weak link is visible (or the user asks for the answer), stop asking and deliver:

```text
CLAIM
  The precise claim, as reconstructed.

INFERENCE TYPE
  Deductive | Inductive | Causal | Analogical (— and what "valid" requires for that type).
  Deductive is graded pass/fail; the other three are graded by strength of support.

VERDICT
  For a DEDUCTIVE argument, one of:
  - Valid / sound — the support establishes the claim.
  - Valid only if you grant X — holds, but leans on an unstated assumption; name X.
  - Invalid — the conclusion does not follow; give the counterexample (premises hold, claim fails).
  For an INDUCTIVE / CAUSAL / ANALOGICAL argument, grade the support instead:
  - Strong / Moderate / Weak support — how much the evidence raises the claim's
    probability, and the specific thing (base rate, confounder, disanalogy) that
    caps it. Reserve "invalid" for a real defeater, not merely "not a guarantee."

WHERE IT BREAKS (if it does)
  Reconstruct the implicit step, don't just name a fallacy:
  "You're treating X as if it implies Y, but that only holds if Z — and here Z
  fails because [counterexample / confound / disanalogy]."
  The reconstruction is checkable; the fallacy label is optional shorthand.

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
- Locate the failure precisely: *which* step, and the counterexample or missing link that breaks it. "This is illogical" is not a finding — and neither is a bare fallacy name, which is a guess to be tested, not the finding itself.
- Grade non-deductive arguments by strength, not by deductive validity. Inductive, causal, and analogical inferences are defeasible by design; judge how much support they confer, and don't call a reasonable one "invalid" for failing to guarantee.
- Prefer narrowing the claim over discarding the argument. Most fixes are a qualifier, not a demolition.
- Don't drag the Socratic loop for its own sake. When the point is made, land it.
- If the user just wants the verdict fast, drop the Socratic mode and go straight to Phase 2 — the interaction serves them, not the ritual.
- If the content is a formal theorem or an ML paper's empirical claim and they want a written audit report rather than a dialogue, hand off to `theorem-and-claim-audit`.
