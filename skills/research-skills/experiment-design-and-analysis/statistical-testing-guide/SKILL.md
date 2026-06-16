---
name: statistical-testing-guide
description: >-
  Choose the right statistical test, compute effect sizes, design power analyses, and report statistics correctly in ML and AI research papers. Use whenever the user asks how to compare two models statistically, whether results are significant, how many seeds to run, how to report variance, which test to use for non-normal data, how to handle multiple comparisons, or how to answer a reviewer challenging statistical validity. Also use when planning an evaluation and needing to decide the number of seeds/trials before running, or when results are borderline and the user needs to know if they can claim significance. Prevents the most common statistical mistakes in ML papers: reporting only means without variance, choosing seeds post-hoc, and conflating statistical significance with practical significance.
---

# Statistical Testing Guide

Statistical validity is not bureaucracy. It is the mechanism by which the reader can trust that a reported improvement is real rather than a lucky seed.

The most common mistake in ML papers is not misapplying a test — it is skipping the test entirely and reporting a mean over 3 seeds as if it were a fact.

---

## Workflow

### 1. Decide what you are comparing

Before choosing a test, be explicit about the comparison structure:

- **Two methods, multiple seeds**: e.g., method A vs. method B, each run with seeds {42, 123, 456}
- **One method, multiple datasets**: e.g., does the improvement hold across 5 benchmarks?
- **One method, multiple hyperparameter settings**: tuning curve, not a significance test
- **Two methods, multiple tasks**: a multi-task comparison

The unit of observation matters. If you run 5 seeds × 3 datasets, you have 15 observations — but they are not independent, and pooling them inflates your effective sample size.

---

### 2. Choose the right test

#### For comparing two methods with multiple seeds (most common ML case)

| Situation | Recommended test |
|---|---|
| ≥10 seeds, metric approximately normal | Paired t-test |
| <10 seeds, or non-normal distribution | Wilcoxon signed-rank test |
| Want to avoid distributional assumptions | Bootstrap permutation test |
| Comparing across multiple datasets | Average-and-test, or mixed-effects model |

**Paired** means each seed is shared between both methods (both run on seed 42, both on seed 123, etc.). Paired tests are more powerful and more appropriate when both methods see the same data/initialization.

**When not to use a t-test**: fewer than 5 seeds, or the metric is bounded (e.g., accuracy near 0 or 1), or the metric is a rank (e.g., position on a leaderboard).

#### For comparing more than two methods

Run pairwise tests, then apply multiple comparison correction (see Step 4). Do not run a single omnibus ANOVA and claim all methods differ — test the specific pairs you care about.

#### For comparing on multiple benchmarks

Do not pool results across benchmarks. Instead:
- Report results per benchmark.
- Note the number of benchmarks where the difference is significant.
- Compute win rate (fraction of benchmarks where method A beats B) as a summary statistic.

#### Non-parametric tests to know

- **Wilcoxon signed-rank**: paired, non-parametric. Use with few seeds or ordinal metrics.
- **Mann-Whitney U**: unpaired, non-parametric. Use when seeds cannot be matched.
- **Bootstrap**: resample the observed runs to estimate the distribution of the difference. Extremely flexible; works well with any metric.
- **Permutation test**: randomly permute labels between methods to build the null distribution. Gold standard for small-n comparisons.

---

### 3. Compute and report effect sizes

Statistical significance answers "is the difference probably not zero?" Effect size answers "is the difference worth caring about?" Both are required.

| Effect size measure | When to use | Interpretation |
|---|---|---|
| Cohen's d | Continuous metric, approximately normal | Small: 0.2, Medium: 0.5, Large: 0.8 |
| Cliff's delta | Ordinal or non-normal | -1 to 1; ~0 means no difference |
| Mean difference ± CI | Always report alongside the above | Most interpretable for readers |
| Win rate | Multiple datasets | Fraction of tasks where A > B |

**Always report the actual numbers, not just p < 0.05.** A difference of 0.1% F1 that is statistically significant (large n) is not practically significant.

---

### 4. Handle multiple comparisons

If you run k tests at significance level α, you expect k × α false positives by chance. With 10 tests at α = 0.05, you expect 0.5 false discoveries — significant even if everything is null.

**When to correct:**
- You are testing the same hypothesis across multiple metrics.
- You are comparing many method pairs in an ablation table.
- You ran many hyperparameter configs and selected the best.

**How to correct:**
- **Bonferroni**: multiply each p-value by k (or set threshold to α/k). Conservative but simple.
- **Holm-Bonferroni**: step-down version of Bonferroni. Less conservative.
- **Benjamini-Hochberg (FDR)**: controls false discovery rate rather than family-wise error. Preferred for exploratory analysis with many tests.

**When not to correct:**
- Pre-specified primary comparison (one method, one metric, one dataset). Correction is unnecessary if the hypothesis was stated before seeing data.
- Exploratory analysis that will feed a follow-up confirmatory study.

Report correction choices explicitly: "We apply Bonferroni correction across 8 ablation variants (α = 0.05/8 = 0.006)."

---

### 5. Plan the number of seeds before running

Power analysis determines how many seeds you need to detect a given effect size with a given probability.

Practical guidance for ML experiments:

| Expected effect size | Minimum seeds for 80% power |
|---|---|
| Large (d > 0.8, e.g., 5+ point improvement) | 3–5 seeds |
| Medium (d ≈ 0.5, e.g., 2–3 point improvement) | 8–12 seeds |
| Small (d < 0.2, e.g., <1 point improvement) | 30+ seeds (often infeasible) |

If a claimed improvement is <1 point and the paper runs only 3 seeds, the result is not interpretable. Say so — and either run more seeds or bound the detectable effect size.

**Rule of thumb for most ML papers**: 5 seeds is the practical minimum; 10 seeds gives reasonable power for medium effects; report variance always.

---

### 6. Report correctly

Minimum reporting requirements for any comparison in a paper:

- Mean (or median for non-normal distributions).
- Standard deviation or standard error (be explicit which).
- Number of seeds / trials.
- Whether seeds were fixed before or after seeing results.
- Test used, p-value, and effect size (when claiming significance).

**Standard deviation vs. standard error**:
- Standard deviation: spread of individual runs. Use for communicating variability.
- Standard error (SD/√n): precision of the mean estimate. Use for confidence intervals on the mean.
- Never report only SE without saying it's SE — it looks like SD and makes results seem more stable than they are.

**Confidence interval format**: "84.3 ± 1.2" should state explicitly "mean ± SD over 5 seeds" or "mean ± 95% CI".

---

### 7. Common mistakes in ML papers

**Reporting only the best seed**: If you ran 10 seeds and reported the maximum, your result is biased. Report mean ± std; mention if you also report max for reference.

**Choosing seeds post-hoc**: Picking seeds after seeing which ones favor your method inflates results. Pre-register seeds (or use all seeds from a fixed range).

**Significance without effect size**: p < 0.05 with d = 0.05 is a meaningless result. Always pair with effect size.

**Comparing means without variance**: Saying "84.3 vs. 83.1" without variance is not evidence. If the SD is 2.0, the difference is invisible.

**Conflating statistical and practical significance**: A 0.1% improvement that is statistically significant at large n is not a contribution if the downstream impact is negligible.

**Testing after adding data**: If you added more seeds after seeing non-significant results, you need to correct for sequential testing (or acknowledge the limitation).

---

## Reporting template for a paper comparison

```
Method A achieved [mean] ± [SD] on [metric] over [n] seeds,
compared to Method B's [mean] ± [SD] ([n] seeds).
The difference ([A−B]) is statistically significant
(Wilcoxon signed-rank, p = [value]; Cohen's d = [value]).
```

If not significant:
```
The observed difference of [A−B] was not statistically significant
(p = [value]; 95% CI [low, high]), with insufficient power to detect
effects smaller than [minimum detectable effect] given [n] seeds.
```

---

## Output format

```markdown
# Statistical Analysis Plan / Report

## Comparison structure
- Unit of observation:
- Number of conditions:
- Pairing:

## Recommended test
- Test: [name and justification]
- Correction for multiple comparisons: [yes/no; method]

## Effect size
- Measure: [Cohen's d / Cliff's delta / mean difference + CI]
- Observed / estimated value:

## Power / seeds
- Effect size target: [what you're trying to detect]
- Seeds required for 80% power: [estimate]
- Seeds you have: [n]
- Verdict: [adequately powered / underpowered / unknown]

## Results
[Formatted comparison with mean ± SD, test statistic, p-value, effect size]

## Reporting text (copy-paste ready)
[Draft sentence for the paper]

## Caveats
[Known limitations of the analysis]
```
