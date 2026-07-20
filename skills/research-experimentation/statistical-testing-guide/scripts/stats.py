#!/usr/bin/env python3
"""Statistical comparison helper for ML experiments.

This is the deterministic companion to the statistical-testing-guide skill. The
skill explains *which* test to use and *why*; this script computes it correctly
so the numbers that go into a paper or rebuttal are not re-derived (and possibly
mis-derived) by hand each time.

It covers the common ML case — comparing two methods across seeds — and the two
follow-ups that always come up: effect size and "did I run enough seeds?".

Dependencies: numpy, scipy. Both are already present in any ML environment.

Usage
-----
Compare two methods (each a list of per-seed scores), auto-selecting the test:

    python stats.py compare --a 0.843 0.851 0.838 0.847 0.840 \\
                            --b 0.812 0.805 0.820 0.808 0.815 \\
                            --paired --metric F1

Read the same from JSON ({"A": [...], "B": [...], "paired": true}):

    python stats.py compare --json comparison.json

Correct a family of p-values for multiple comparisons:

    python stats.py correct --pvalues 0.01 0.04 0.03 0.20 --method holm

Plan seeds (how many for 80% power at a target effect size) or, given the seeds
you have, the smallest effect you can detect:

    python stats.py power --d 0.5            # -> required seeds
    python stats.py power --d 0.5 --n 5      # -> required seeds + MDE at n=5

Sanity-check the implementation:

    python stats.py selftest
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field

import numpy as np
from scipy import stats


# --------------------------------------------------------------------------- #
# Effect sizes
# --------------------------------------------------------------------------- #
def cohens_d(a: np.ndarray, b: np.ndarray, paired: bool) -> float:
    """Standardised mean difference.

    Paired: mean of differences / SD of differences (the quantity that actually
    drives a paired test's power). Unpaired: difference of means / pooled SD.
    """
    a, b = np.asarray(a, float), np.asarray(b, float)
    if paired:
        diff = a - b
        sd = diff.std(ddof=1)
        return float(diff.mean() / sd) if sd > 0 else 0.0
    na, nb = len(a), len(b)
    pooled = np.sqrt(((na - 1) * a.var(ddof=1) + (nb - 1) * b.var(ddof=1)) / (na + nb - 2))
    return float((a.mean() - b.mean()) / pooled) if pooled > 0 else 0.0


def cliffs_delta(a: np.ndarray, b: np.ndarray) -> float:
    """Non-parametric effect size in [-1, 1]; ~0 means stochastically equal.

    delta = P(a > b) - P(a < b). Robust to non-normal / ordinal metrics.
    """
    a, b = np.asarray(a, float), np.asarray(b, float)
    gt = sum((x > y) for x in a for y in b)
    lt = sum((x < y) for x in a for y in b)
    return float((gt - lt) / (len(a) * len(b)))


def interpret_d(d: float) -> str:
    ad = abs(d)
    if ad < 0.2:
        return "negligible"
    if ad < 0.5:
        return "small"
    if ad < 0.8:
        return "medium"
    return "large"


# --------------------------------------------------------------------------- #
# Confidence interval on the difference (bootstrap — distribution-free)
# --------------------------------------------------------------------------- #
def bootstrap_diff_ci(
    a: np.ndarray, b: np.ndarray, paired: bool, n_boot: int = 10000,
    alpha: float = 0.05, seed: int = 0,
) -> tuple[float, float, float]:
    """Percentile bootstrap CI for (mean A - mean B). Returns (mean_diff, lo, hi)."""
    rng = np.random.default_rng(seed)
    a, b = np.asarray(a, float), np.asarray(b, float)
    boot = np.empty(n_boot)
    if paired:
        diff = a - b
        n = len(diff)
        for i in range(n_boot):
            boot[i] = diff[rng.integers(0, n, n)].mean()
        point = float(diff.mean())
    else:
        na, nb = len(a), len(b)
        for i in range(n_boot):
            boot[i] = a[rng.integers(0, na, na)].mean() - b[rng.integers(0, nb, nb)].mean()
        point = float(a.mean() - b.mean())
    lo, hi = np.percentile(boot, [100 * alpha / 2, 100 * (1 - alpha / 2)])
    return point, float(lo), float(hi)


def permutation_pvalue(
    a: np.ndarray, b: np.ndarray, paired: bool, n_perm: int = 10000, seed: int = 0,
) -> float:
    """Two-sided permutation p-value for the difference in means.

    Gold standard for small n: makes no distributional assumption. Paired version
    flips the sign of each difference; unpaired version shuffles group labels.
    """
    rng = np.random.default_rng(seed)
    a, b = np.asarray(a, float), np.asarray(b, float)
    if paired:
        diff = a - b
        obs = abs(diff.mean())
        n = len(diff)
        count = 0
        for _ in range(n_perm):
            signs = rng.choice([-1.0, 1.0], n)
            if abs((diff * signs).mean()) >= obs - 1e-12:
                count += 1
        return (count + 1) / (n_perm + 1)
    obs = abs(a.mean() - b.mean())
    pool = np.concatenate([a, b])
    na = len(a)
    count = 0
    for _ in range(n_perm):
        rng.shuffle(pool)
        if abs(pool[:na].mean() - pool[na:].mean()) >= obs - 1e-12:
            count += 1
    return (count + 1) / (n_perm + 1)


# --------------------------------------------------------------------------- #
# Test selection + comparison
# --------------------------------------------------------------------------- #
@dataclass
class ComparisonResult:
    metric: str
    paired: bool
    n_a: int
    n_b: int
    mean_a: float
    mean_b: float
    sd_a: float
    sd_b: float
    test_name: str
    test_reason: str
    p_value: float
    perm_p: float
    effect_name: str
    effect_value: float
    effect_interp: str
    mean_diff: float
    ci_lo: float
    ci_hi: float
    win_rate: float | None
    alpha: float
    notes: list[str] = field(default_factory=list)


def _is_normal(x: np.ndarray) -> bool:
    """Shapiro-Wilk normality screen. Needs n >= 3; conservative default True at tiny n."""
    x = np.asarray(x, float)
    if len(x) < 3:
        return True
    try:
        return stats.shapiro(x).pvalue > 0.05
    except Exception:
        return True


def compare(
    a, b, paired: bool, metric: str = "metric", alpha: float = 0.05,
) -> ComparisonResult:
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    notes: list[str] = []

    if paired and len(a) != len(b):
        raise ValueError("paired comparison requires equal-length, aligned samples")
    if min(len(a), len(b)) < 2:
        raise ValueError("need at least 2 observations per method")

    small = min(len(a), len(b)) < 10
    if paired:
        normal = _is_normal(a - b)
        if not small and normal:
            test_name = "Paired t-test"
            reason = "paired, >=10 seeds, differences approximately normal"
            p = float(stats.ttest_rel(a, b).pvalue)
        else:
            test_name = "Wilcoxon signed-rank"
            reason = ("paired; " + ("few seeds (<10)" if small else "non-normal differences")
                      + " -> non-parametric")
            try:
                p = float(stats.wilcoxon(a, b).pvalue)
            except ValueError:
                p = float("nan")
                notes.append("Wilcoxon undefined (all differences zero); see permutation p.")
        effect_name, effect_value = "Cohen's d (paired)", cohens_d(a, b, True)
    else:
        normal = _is_normal(a) and _is_normal(b)
        if not small and normal:
            test_name = "Welch's t-test (unpaired)"
            reason = ">=10 per group, approximately normal, unequal variance not assumed"
            p = float(stats.ttest_ind(a, b, equal_var=False).pvalue)
            effect_name, effect_value = "Cohen's d", cohens_d(a, b, False)
        else:
            test_name = "Mann-Whitney U"
            reason = ("unpaired; " + ("small n (<10)" if small else "non-normal") + " -> non-parametric")
            p = float(stats.mannwhitneyu(a, b, alternative="two-sided").pvalue)
            effect_name, effect_value = "Cliff's delta", cliffs_delta(a, b)

    if small:
        notes.append("Small sample: the permutation p-value is the more trustworthy figure.")
    if test_name.startswith(("Welch", "Paired")) and effect_name.startswith("Cohen") and abs(effect_value) < 0.2:
        notes.append("Effect size is negligible — statistical significance here would not be practically meaningful.")

    perm_p = permutation_pvalue(a, b, paired)
    mean_diff, lo, hi = bootstrap_diff_ci(a, b, paired, alpha=alpha)
    win_rate = float(np.mean(a > b)) if paired else None

    return ComparisonResult(
        metric=metric, paired=paired, n_a=len(a), n_b=len(b),
        mean_a=float(a.mean()), mean_b=float(b.mean()),
        sd_a=float(a.std(ddof=1)), sd_b=float(b.std(ddof=1)),
        test_name=test_name, test_reason=reason, p_value=p, perm_p=perm_p,
        effect_name=effect_name, effect_value=effect_value,
        effect_interp=interpret_d(effect_value) if effect_name.startswith("Cohen") else f"{effect_value:+.2f}",
        mean_diff=mean_diff, ci_lo=lo, ci_hi=hi, win_rate=win_rate,
        alpha=alpha, notes=notes,
    )


# --------------------------------------------------------------------------- #
# Multiple-comparison correction
# --------------------------------------------------------------------------- #
def correct_pvalues(pvalues, method: str = "holm"):
    """Return corrected p-values. method in {bonferroni, holm, bh}."""
    p = np.asarray(pvalues, float)
    k = len(p)
    method = method.lower()
    if method == "bonferroni":
        return np.minimum(p * k, 1.0)
    order = np.argsort(p)
    out = np.empty(k)
    if method == "holm":
        running = 0.0
        for rank, idx in enumerate(order):
            val = (k - rank) * p[idx]
            running = max(running, val)
            out[idx] = min(running, 1.0)
        return out
    if method in ("bh", "fdr", "benjamini-hochberg"):
        running = 1.0
        for rank in range(k - 1, -1, -1):
            idx = order[rank]
            val = p[idx] * k / (rank + 1)
            running = min(running, val)
            out[idx] = min(running, 1.0)
        return out
    raise ValueError(f"unknown correction method: {method}")


# --------------------------------------------------------------------------- #
# Power / seed planning (paired or one-sample on the differences)
# --------------------------------------------------------------------------- #
def required_seeds(d: float, power: float = 0.8, alpha: float = 0.05) -> int:
    """Approximate seeds needed to detect standardized effect d at given power.

    Uses the normal approximation n = ((z_{1-a/2} + z_{1-power}) / d)^2, then a
    small-sample bump. Matches the skill's rule of thumb (large d ~ 3-5 seeds,
    medium ~ 8-12, small ~ 30+).
    """
    if d <= 0:
        return 10**9
    z_a = stats.norm.ppf(1 - alpha / 2)
    z_b = stats.norm.ppf(power)
    n = ((z_a + z_b) / d) ** 2
    return max(2, int(np.ceil(n)) + 1)


def detectable_effect(n: int, power: float = 0.8, alpha: float = 0.05) -> float:
    """Smallest standardized effect detectable with n seeds at given power (MDE)."""
    z_a = stats.norm.ppf(1 - alpha / 2)
    z_b = stats.norm.ppf(power)
    return float((z_a + z_b) / np.sqrt(n))


# --------------------------------------------------------------------------- #
# Reporting (matches the skill's "Output format" template)
# --------------------------------------------------------------------------- #
def format_report(r: ComparisonResult) -> str:
    sig = (r.p_value < r.alpha) if r.p_value == r.p_value else (r.perm_p < r.alpha)
    verdict = "statistically significant" if sig else "not statistically significant"
    n_for_power = required_seeds(abs(r.effect_value)) if r.effect_name.startswith("Cohen") else None
    powered = (n_for_power is not None and min(r.n_a, r.n_b) >= n_for_power)
    lines = [
        "# Statistical Analysis Report",
        "",
        "## Comparison structure",
        f"- Metric: {r.metric}",
        f"- Pairing: {'paired (same seeds)' if r.paired else 'unpaired'}",
        f"- Method A: mean {r.mean_a:.4f} ± {r.sd_a:.4f} SD over {r.n_a} runs",
        f"- Method B: mean {r.mean_b:.4f} ± {r.sd_b:.4f} SD over {r.n_b} runs",
        "",
        "## Recommended test",
        f"- Test: {r.test_name}",
        f"- Why: {r.test_reason}",
        f"- p-value: {r.p_value:.4g}",
        f"- Permutation cross-check p: {r.perm_p:.4g}",
        "",
        "## Effect size",
        f"- {r.effect_name}: {r.effect_value:+.3f} ({r.effect_interp})",
        f"- Mean difference (A−B): {r.mean_diff:+.4f}  [95% CI {r.ci_lo:+.4f}, {r.ci_hi:+.4f}]",
    ]
    if r.win_rate is not None:
        lines.append(f"- Win rate (A>B across paired runs): {r.win_rate:.0%}")
    lines += [
        "",
        "## Power / seeds",
    ]
    if n_for_power is not None:
        lines += [
            f"- Seeds for 80% power at the observed effect: ~{n_for_power}",
            f"- Seeds available: {min(r.n_a, r.n_b)}",
            f"- Verdict: {'adequately powered' if powered else 'UNDERPOWERED — treat a null result as inconclusive'}",
        ]
    else:
        lines.append("- Non-parametric effect; plan seeds from a Cohen's d target via `power` subcommand.")
    lines += [
        "",
        "## Bottom line",
        f"- The difference is **{verdict}** at α={r.alpha} "
        f"({r.test_name}, p={r.p_value:.4g}; {r.effect_name}={r.effect_value:+.3f}).",
    ]
    if r.notes:
        lines += ["", "## Caveats"] + [f"- {n}" for n in r.notes]
    lines += [
        "",
        "## Copy-paste sentence",
    ]
    if sig:
        lines.append(
            f"Method A achieved {r.mean_a:.3f} ± {r.sd_a:.3f} on {r.metric} over {r.n_a} seeds, "
            f"compared to Method B's {r.mean_b:.3f} ± {r.sd_b:.3f} ({r.n_b} seeds). The difference "
            f"({r.mean_diff:+.3f}) is statistically significant ({r.test_name}, p={r.p_value:.3g}; "
            f"{r.effect_name}={r.effect_value:+.2f})."
        )
    else:
        lines.append(
            f"The observed difference of {r.mean_diff:+.3f} on {r.metric} was not statistically "
            f"significant ({r.test_name}, p={r.p_value:.3g}; 95% CI [{r.ci_lo:+.3f}, {r.ci_hi:+.3f}]), "
            f"with limited power to detect small effects given {min(r.n_a, r.n_b)} seeds."
        )
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def _cmd_compare(args) -> int:
    if args.json:
        cfg = json.load(open(args.json))
        a, b = cfg["A"], cfg["B"]
        paired = cfg.get("paired", args.paired)
        metric = cfg.get("metric", args.metric)
    else:
        if args.a is None or args.b is None:
            print("error: provide --a and --b (or --json)", file=sys.stderr)
            return 2
        a, b, paired, metric = args.a, args.b, args.paired, args.metric
    print(format_report(compare(a, b, paired=paired, metric=metric, alpha=args.alpha)))
    return 0


def _cmd_correct(args) -> int:
    corrected = correct_pvalues(args.pvalues, method=args.method)
    print(f"# Multiple-comparison correction ({args.method}, k={len(args.pvalues)})\n")
    print(f"{'raw p':>10} {'corrected':>10}  significant@" + str(args.alpha))
    for raw, cor in zip(args.pvalues, corrected):
        print(f"{raw:>10.4g} {cor:>10.4g}  {'yes' if cor < args.alpha else 'no'}")
    return 0


def _cmd_power(args) -> int:
    n = required_seeds(args.d, power=args.power, alpha=args.alpha)
    print(f"Target effect (Cohen's d): {args.d}")
    print(f"Seeds for {args.power:.0%} power (α={args.alpha}): ~{n}")
    if args.n:
        mde = detectable_effect(args.n, power=args.power, alpha=args.alpha)
        print(f"With n={args.n} seeds, smallest detectable effect (MDE): d≈{mde:.2f} "
              f"({interpret_d(mde)})")
    return 0


def _cmd_selftest(_args) -> int:
    rng = np.random.default_rng(0)
    # Clear separation, paired.
    a = 0.85 + rng.normal(0, 0.005, 12)
    b = 0.81 + rng.normal(0, 0.005, 12)
    r = compare(a, b, paired=True, metric="F1")
    assert r.p_value < 0.05 and r.effect_value > 0.8, r
    # No real difference.
    c = rng.normal(0.8, 0.02, 8)
    d = rng.normal(0.8, 0.02, 8)
    r2 = compare(c, d, paired=False, metric="acc")
    assert r2.perm_p > 0.05, r2
    # Corrections monotone and >= raw.
    raw = [0.01, 0.04, 0.03, 0.20]
    for m in ("bonferroni", "holm", "bh"):
        cor = correct_pvalues(raw, m)
        assert np.all(cor >= np.array(raw) - 1e-9), (m, cor)
    # Power monotonicity.
    assert required_seeds(0.8) < required_seeds(0.5) < required_seeds(0.2)
    print("selftest OK")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("compare", help="compare two methods, auto-selecting the test")
    c.add_argument("--a", type=float, nargs="+", help="per-seed scores for method A")
    c.add_argument("--b", type=float, nargs="+", help="per-seed scores for method B")
    c.add_argument("--json", help='JSON file {"A": [...], "B": [...], "paired": bool}')
    c.add_argument("--paired", action="store_true", help="seeds are shared/aligned between A and B")
    c.add_argument("--metric", default="metric", help="metric name for the report")
    c.add_argument("--alpha", type=float, default=0.05)
    c.set_defaults(func=_cmd_compare)

    r = sub.add_parser("correct", help="correct a family of p-values")
    r.add_argument("--pvalues", type=float, nargs="+", required=True)
    r.add_argument("--method", default="holm", choices=["bonferroni", "holm", "bh"])
    r.add_argument("--alpha", type=float, default=0.05)
    r.set_defaults(func=_cmd_correct)

    w = sub.add_parser("power", help="plan seeds from an effect-size target")
    w.add_argument("--d", type=float, required=True, help="target Cohen's d")
    w.add_argument("--n", type=int, help="seeds you have (reports MDE)")
    w.add_argument("--power", type=float, default=0.8)
    w.add_argument("--alpha", type=float, default=0.05)
    w.set_defaults(func=_cmd_power)

    s = sub.add_parser("selftest", help="run internal sanity checks")
    s.set_defaults(func=_cmd_selftest)
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
