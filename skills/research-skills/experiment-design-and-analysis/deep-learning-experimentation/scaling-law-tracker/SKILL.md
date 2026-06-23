---
name: scaling-law-tracker
description: >-
  Track how performance changes with data size, model size, batch size, or compute, fit a scaling law, and decide where more compute will actually pay off. Use when planning larger runs, deciding whether to scale data vs. model vs. optimization, estimating performance at a bigger budget, or judging whether a curve has hit diminishing returns. Trigger on "is it worth scaling this further", "fit a scaling law", "where are the diminishing returns", "how much better at 10x compute", "should I add data or parameters", or when the user has a set of runs at different scales and wants the trend extrapolated.
---

# Scaling Law Tracker

Measure whether more scale is buying the right thing — and quantify it, rather than eyeballing a log-log plot.

## Workflow

1. **Define the scaling axis and metric.** One axis at a time: data size, parameters, compute (FLOPs), or batch size. State whether the metric improves up (accuracy) or down (loss).
2. **Collect comparable runs.** Same architecture family, same data distribution, same eval. Incomparable setups make the exponent meaningless.
3. **Fit and extrapolate with the bundled script** (below) rather than fitting by hand — log-log regression and the offset form are easy to get subtly wrong.
4. **Read off the exponent, the knee, and the extrapolation.** Is the curve still paying off, or past the point where this axis is worth scaling?
5. **Recommend the next move.** Scale this axis further, reallocate to a different axis (data ↔ model ↔ optimization), or stop.

## Fit it with the bundled script

`scripts/fit_scaling_law.py` fits both a power law (`y = a·x^b`) and a power-law-with-floor (`y = E + a·x^b`, the Kaplan/Chinchilla form for losses that plateau), reports the exponent and R², extrapolates to a target budget, and flags where doubling the resource buys less than a useful relative gain.

```bash
# Fit val-loss vs. tokens, extrapolate to a larger budget:
python scripts/fit_scaling_law.py \
  --x 1e6 2e6 4e6 8e6 1.6e7 \
  --y 3.10 2.84 2.63 2.48 2.37 \
  --metric "val loss" --lower-better --extrapolate 6.4e7

python scripts/fit_scaling_law.py selftest   # verify the install
```

It also accepts `--json '{"x":[...],"y":[...],"lower_better":true,"extrapolate":6.4e7}'`.

## Reading the output

- **Exponent b** — the slope in log-log space. Steeper (larger |b|) means scaling this axis buys more. Compare exponents across axes to decide where to spend.
- **R²** — below ~0.9, a clean power law may not hold; say so and don't extrapolate far.
- **Diminishing-returns knee** — the resource level past which doubling yields less than the threshold (default 2%) relative gain. Past the knee, reallocate.
- **Extrapolation span** — predictions more than ~10× beyond your largest run carry large error; treat them as a prior, not a promise.

## Rules

- Do not compare incomparable training setups — different data, eval, or architecture family invalidate the fit.
- State uncertainty if the run set is sparse (<5 points): the exponent has wide error bars.
- An extrapolation is a hypothesis to test with one larger run, not a result to report as measured.
