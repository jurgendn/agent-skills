---
name: benchmark-and-baseline-selector
description: Given a research proposal, claim, method, or result, recommend the baselines and benchmarks needed to support it — split into a MINIMAL set (necessary for credibility, skipping any risks rejection) and a SUGGESTED set (complementary, strengthens external validity). Use whenever the user proposes something and asks "what should I compare against", "what baselines do I need", "which benchmarks support this claim", "is this enough to be convincing", "what's the minimal experiment set", "what would a reviewer demand", or shares a method/idea and wants the comparison plan. Default to running this on any proposal so claims are backed by the right evidence. Always check first whether the input is sufficient (precise claim, field, the novel component, metric); if not, request the missing context before recommending rather than guessing. Use experiment-design to design the run itself (or to design a measurement when no benchmark exists), and hypothesis-and-ablation-planner for internal ablations.
---

# Benchmark and Baseline Selector

When the user proposes a method, claim, or result, return the **smallest set of baselines and benchmarks that makes the claim credible**, plus a **complementary set that makes it strong**.

The deliverable is always a two-tier comparison plan, not a single list:

- **Minimal** — necessary. If the method ties or loses here, the claim is dead. Omitting any of these invites a desk-reject or "missing baseline" review.
- **Suggested** — complementary. Adds external validity (scale, transfer, robustness), but is not decision-critical for the core claim.

A baseline/benchmark only earns a slot if it can *change the conclusion*. Decorative comparisons that the method obviously wins are noise.

---

# Procedure

## 0. Context intake — gate before recommending

**Do not produce a plan from an underspecified prompt.** First check whether the conversation supplies the context below. Pull what is present; for anything **required** that is missing, *ask the user* — do not guess, and do not hedge about asking. A wrong incumbent or an unowned self-ablation makes the whole plan misleading, so it is always cheaper to ask first.

**Required — ask if absent:**
- **Precise claim** — the property, vs what reference, under what conditions. If only a vague idea is given, ask the user to state it falsifiably.
- **Field / task / domain** — without it, "strong incumbent" and "closest prior method" are unknowable.
- **What is novel** — which component is the contribution. Defines the self-ablation baseline.
- **Metric of record** — what the subfield reports the claim in. If not stated, infer from claim type and **state the assumption explicitly**.

**Helpful — pull if available, otherwise state an assumption:**
- Target venue / audience (calibrates how strict Minimal must be).
- Compute / data / time budget (keeps Minimal runnable; pushes costly comparisons to Suggested).
- What baselines/benchmarks have already been run.
- Data availability + contamination risk.
- Current SOTA numbers / prior art — since this skill carries no baked-in benchmark lists, the *current* incumbent must come from the conversation, the user, or a literature lookup. Ground it before finalizing rather than naming a stale baseline.

Ask the required questions in one batch, concisely. Once answered (or assumptions recorded), proceed. Every assumption you had to make must be surfaced in the final output, not buried.

## 1. Restate the claim and classify it

Rewrite the user's proposal as one falsifiable claim of the form:
*"[Method] achieves [property] compared to [reference] under [conditions], measured by [metric]."*

Then classify the **claim type** — this dictates everything downstream:

| Claim type | The thing that must be controlled / shown |
|------------|-------------------------------------------|
| Accuracy / SOTA | beats the current strong incumbent under the *same* budget and protocol |
| Efficiency (compute / params / latency / cost) | matches quality at lower cost, or better quality at equal cost — needs a cost axis |
| Sample efficiency | better with limited data — needs a learning-curve / data-budget protocol |
| Generalization / transfer | holds on a *different* distribution, domain, or task than it was tuned on |
| Robustness | holds under shift, noise, adversarial, or long-tail conditions |
| Mechanism ("why it works") | the gain comes from the claimed component, not a confound — needs self-ablations |

If the proposal mixes several (e.g. "faster *and* more accurate"), each sub-claim gets its own minimal set.

## 2. Build the baseline taxonomy

For the claim, force every relevant slot. Missing the lower bound or the self-ablation is the single most common reviewer complaint.

- **Trivial lower bound** — random / majority / no-op / simplest heuristic. Proves the task and metric are non-degenerate and the method clears the floor.
- **Strong incumbent** — the obvious method a practitioner already uses (well-tuned, not a strawman). Beating a weak baseline proves nothing.
- **Closest prior method** — the most directly competing published approach. This is the comparison reviewers care about most.
- **Self-ablation baseline** — your own method with the claimed component removed/replaced. This is what isolates *your* contribution from the surrounding machinery.

Each baseline gets a one-line rationale: *what conclusion it rules out.*

## 3. Select benchmarks/datasets to match the claim

Pick benchmarks by what they let you *infer*, not by popularity.

- **Minimal benchmark** — the smallest setting that can falsify the claim, with a protocol that matches the claim type (e.g. a learning curve for sample efficiency, a cost axis for efficiency, an OOD split for generalization). One well-chosen benchmark with the right protocol beats five that all measure the same thing.
- **Suggested benchmarks** — add a *different* axis: a second domain (transfer), a larger scale (does the gain survive?), a shifted/long-tail split (robustness), or a harder/contamination-free variant.

Prefer benchmarks where the strong incumbent's number is already public, so the comparison is cheap and uncontestable.

## 4. Match the metric to the claim

Flag any mismatch: an efficiency claim reported only as accuracy, a robustness claim with no worst-case/tail metric, a calibration claim measured by accuracy. State the primary metric and any secondary metric needed to make the claim legible. If the claim implies a trade-off (quality vs cost), require both axes reported together.

## 5. Cut minimal vs suggested

Apply one test to every item:
> *If the method ties or loses on this, is the core claim refuted?*

- **Yes →** Minimal.
- **No, but it broadens the conclusion →** Suggested.

Keep Minimal genuinely small — typically the trivial lower bound, the closest prior method (or strong incumbent), one self-ablation, on one benchmark with the right protocol.

## 6. Flag anti-patterns

Call out, explicitly, any that apply:
- Weak / outdated / untuned baseline (strawman).
- Benchmark cherry-picking — reporting only the splits where the method wins.
- Protocol/metric mismatch — the benchmark can't actually test the claim type.
- Leakage / contamination — train-test overlap, or the benchmark is in pretraining data.
- Unequal budget — comparing your tuned method to an under-tuned baseline.
- Missing self-ablation — gain not attributed to the claimed component.

---

# Output format

```
Claim (falsifiable): <one sentence>
Claim type(s): <from the table>
Primary metric: <metric>  | Secondary: <metric, if the claim needs it>

MINIMAL (necessary — claim dies if it fails here)
  Baselines:
    - <baseline>  — rules out: <what>
    - <self-ablation> — isolates: <your component>
  Benchmark(s):
    - <benchmark> + <protocol>  — can falsify: <which part of the claim>

SUGGESTED (complementary — strengthens, not decision-critical)
  Baselines:  - <stronger SOTA / extra lower bound> — adds: <inference>
  Benchmark(s): - <2nd domain / scale / shift> — adds: <axis of external validity>

Anti-patterns to avoid: <only the ones that apply>
Assumptions made: <any required context that was inferred rather than given — omit if none>
```

Keep it scannable. Lead with the Minimal set — that is the answer to "what do I actually need." Offer the Suggested set as the upgrade path.

---

# When not to use this skill

- Designing the experiment run, controls, or success thresholds → `experiment-design`.
- Internal ablations to isolate a mechanism within one method → `hypothesis-and-ablation-planner`.
- No suitable benchmark exists and a measurement must be designed from scratch → `experiment-design`.
- Interpreting results / error analysis after running → `model-eval-error-analysis`.
- Significance testing of the resulting numbers → `statistical-testing-guide`.
