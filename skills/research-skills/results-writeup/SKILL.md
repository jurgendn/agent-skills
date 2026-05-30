---
name: results-writeup
description: Turn verified research findings into clear, calibrated scientific writing — paper sections (Results, Experiments, Discussion), lab notes, technical reports, and grant progress reports. Use this skill whenever the user has run experiments or analysis and wants help writing them up, including casual phrasings like "draft the results section", "write up these numbers", "turn my notebook into a paper section", or "summarize what we found". Also use when the user shares logs, tables, or a notebook and asks for prose. For reviewer-by-reviewer rebuttal strategy, use reviewer-response-strategist instead. The skill's main job is preventing confident-sounding overclaims and hallucinated numbers in scientific text.
---

# Results Writeup

Write the strongest *honest* version of the result. Calibrated writing wins more arguments with reviewers than confident writing.

## The core problem this skill solves

Two failure modes dominate scientific writeups, and good prose has to avoid both:

1. **Overclaiming.** Treating a correlation as a mechanism, a single dataset as a general law, p < 0.05 as truth, or an absence of effect as proof of no effect. Reviewers catch this and it sinks papers.
2. **Underclaiming / mushiness.** Hedging everything into uselessness ("results may suggest a potential trend"), burying the actual finding under qualifications, or refusing to commit to *any* interpretation. This wastes the reader's time and signals the authors don't believe their own work.

The target is in between: state precisely what was found, precisely what it means, and precisely where it stops — in that order. If you find yourself reaching for "may" or "potentially" twice in one sentence, the claim is either wrong or you haven't figured out what it actually is.

## Workflow

### 1. Gather findings with provenance

Before writing anything, list every quantitative claim the writeup will make and note where each comes from — a specific table, a logged experiment, a notebook cell, a script output. If a number doesn't have a traceable source, it doesn't go in the writeup. This is the single most important step; everything else is downstream of it.

If the user hasn't given you sources for some numbers and you'd need them, ask before drafting. Don't paper over the gap with plausible-looking values.

### 2. Separate observation from interpretation

The most common reviewer complaint is that authors conflate "what we measured" with "what it means". Keep these in different sentences, ideally different paragraphs:

- **Observation**: "Method A achieved 0.84 F1 on the test set, compared to 0.79 for the baseline (n=3 seeds, ±0.01)."
- **Interpretation**: "This is consistent with the hypothesis that <mechanism>, though the gap is small enough that <alternative explanation> remains plausible."

A useful internal test: could a skeptical reader agree with the observation sentence while disagreeing with the interpretation sentence? If not, the two are tangled.

### 3. Calibrate the claim to the evidence

Match the strength of language to the strength of the evidence. Rough scale, from strongest to weakest:

- "X is" / "X causes Y" — reserved for well-established mechanism or theorem
- "X improves Y" / "we find X" — direct, replicated empirical result with clear effect
- "X is consistent with Y" / "the data support Y" — observational evidence aligned with a hypothesis
- "X suggests Y" / "this is suggestive of Y" — weaker signal, exploratory analysis
- "X is preliminary evidence for Y" — single experiment, small n, not yet replicated

If hedging language ("may", "could", "potentially") appears, it should carry information: *why* is the claim hedged? Sample size? Confounders? Single dataset? Make the reason visible at least once in the section.

### 4. State what was *not* tested

Most papers are rejected not for what they claim but for what they fail to acknowledge. Before the limitations section, list:

- Conditions outside the experimental range (other datasets, scales, distributions)
- Ablations not run
- Baselines not compared against (and why)
- Failure modes that weren't probed

This is honest *and* strategically smart: pre-empting reviewer objections is more persuasive than dodging them.

### 5. Surface inconsistencies and weak evidence

If a result didn't replicate across seeds, a metric improved while another degraded, or one dataset disagreed with the others — say so. Burying inconsistencies tends to backfire: reviewers find them, and the cover-up reads worse than the original tension. A short "Result X did not transfer to setting Y; we attribute this to <reason> but cannot rule out <alternative>" is much stronger than silence.

### 6. End with concrete next steps

Vague future work ("we plan to extend this to other domains") is filler. Concrete next steps name the specific experiment, dataset, or analysis that would resolve the open question. Even one or two specific items beats a paragraph of generalities.

## Common epistemic traps to avoid

- **Correlation → mechanism.** "Models with more parameters had lower loss" does not establish that parameters *cause* lower loss in any meaningful sense. State the correlation; flag the unobserved confounders (training compute, data scale, hyperparameter tuning effort).
- **Single dataset → general law.** "Our method outperforms X on CIFAR-10" is not "our method outperforms X". Bound the claim to the conditions tested.
- **Absence of effect → proof of no effect.** "We did not observe a significant difference" is not "there is no difference". State the power / effect size detectable with the sample used.
- **p < 0.05 → truth.** Report effect sizes and confidence intervals alongside (or instead of) p-values. Practical significance ≠ statistical significance.
- **Cherry-picked seeds / metrics.** If only the best seed is reported, say so. If a metric was chosen after seeing results, say so.
- **Best-case framing.** "Up to 30% improvement" usually hides "median 4% improvement". Report the typical case; mention the best case as a separate detail.

## Numbers, units, and figures

- Use numbers only when you can point to the source. If you're tempted to write a number from memory, replace it with a placeholder (`[XX]`) and flag it for the user to fill in.
- Always include uncertainty (standard deviation, confidence interval, IQR — whichever is appropriate) for any aggregate over multiple runs. A point estimate alone is incomplete reporting.
- Match precision to the noise level. Reporting 84.27% when the standard deviation is ±2% is false precision — write 84% ± 2%.
- When referencing a figure or table, briefly describe what it shows in the prose; never assume the reader will look at it.

## Output shape

Default sections, in order:

- **Setup** — what was run, on what data, with what configuration. Enough that the result is reproducible in principle.
- **Main findings** — the headline results, each as a precise claim with its supporting numbers.
- **Interpretation** — what the findings mean, calibrated to evidence strength, with alternative explanations acknowledged.
- **Limitations** — what was not tested, what could undermine the claims, where the results stop applying.
- **Next steps** — specific experiments or analyses that would extend or stress-test the findings.

Adapt the shape to the context:

- **Paper Results section**: Setup + Main findings only; interpretation moves to Discussion.
- **Paper Discussion**: Interpretation + Limitations + a forward-looking close.
- **Conference rebuttal**: lead with the most damaging reviewer point, address it with new evidence or a precise concession, then move to the next. Keep observations and interpretations separated as in #2 — reviewers are especially alert to overclaiming in rebuttals.
- **Lab notes / internal report**: looser, but keep provenance strict — these often become the source of truth for the next paper, so unsourced numbers here cause problems later.
- **Grant / progress report**: emphasize what was *demonstrated* vs. what remains *planned*, since funders are reading specifically for this distinction.

## Examples

### Example 1: tightening a vague claim

Before: *Our model performs significantly better than the baseline, suggesting that attention is crucial for this task.*

After: *Our model achieves 0.84 F1 (±0.01, 3 seeds) compared to the baseline's 0.79 (±0.02), a gap of 5 points. This is consistent with attention contributing to performance on this task, though the ablation in §4.3 shows the gap narrows to 1 point when positional encodings are removed — suggesting the two mechanisms interact rather than attention alone driving the improvement.*

The "after" version is more committed *and* more honest: it gives the actual numbers, narrows the mechanistic claim, and points to the ablation that complicates the simple story.

### Example 2: handling an inconvenient result

Before (omits the failure): *Our method outperforms the baselines across all benchmarks.*

After (acknowledges and contextualizes): *Our method outperforms the baselines on 4 of 5 benchmarks. On the fifth (LongDocQA), it underperforms by 2 points; we trace this to the truncation strategy in §3.2, which discards relevant context for documents longer than 8k tokens. This is a limitation of the current implementation, not a fundamental property of the method.*

The second version is stronger because it both volunteers the failure (good faith) and offers a mechanistic explanation that bounds the damage.

### Example 3: a calibrated negative result

Before: *We found no effect of <intervention> on <outcome>.*

After: *We observed no statistically significant effect of <intervention> on <outcome> (Δ = 0.3%, 95% CI [-1.1%, 1.7%], n=200). The confidence interval rules out effects larger than ~2%, but smaller effects remain possible and would require a larger sample to detect.*

The second version converts a vague null into an informative one: it tells the reader what sizes of effect have been excluded, which is the actually useful information.

## When the user pushes for stronger language

Researchers sometimes ask for punchier claims than the evidence supports — usually under deadline pressure or because a reviewer/advisor pushed back. When this happens:

1. State plainly which specific claim is outrunning the evidence and why.
2. Offer a version that is as strong as the evidence honestly allows.
3. If the user still wants the stronger version, write it — but flag the specific liability so they're choosing with eyes open. The user owns the final claim; the skill's job is to make sure they aren't overclaiming by accident.