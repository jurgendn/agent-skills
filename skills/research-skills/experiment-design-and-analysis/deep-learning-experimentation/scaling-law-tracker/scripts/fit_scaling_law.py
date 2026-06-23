#!/usr/bin/env python3
"""Fit and extrapolate a scaling law from a set of comparable runs.

The deterministic core the scaling-law-tracker skill needs: given (resource,
metric) pairs — resource = data size / params / compute / batch — fit a power
law, report the exponent and fit quality, extrapolate to a target budget, and
flag where returns diminish below a useful threshold.

Model
-----
Two forms are fit and the better (by R^2 on the chosen scale) is reported:
  - Power law:            y = a * x^b
  - Power law + offset:   y = E + a * x^b   (irreducible-error floor E, the
                          Chinchilla/Kaplan form for losses that plateau)

For a *loss* (lower is better) b is typically negative; for an *accuracy*
(higher is better) b is typically positive and an offset is the ceiling.

Dependencies: numpy, scipy.

Usage
-----
    python fit_scaling_law.py \\
        --x 1e6 2e6 4e6 8e6 1.6e7 \\
        --y 3.10 2.84 2.63 2.48 2.37 \\
        --metric "val loss" --lower-better \\
        --extrapolate 6.4e7

    python fit_scaling_law.py --json runs.json     # {"x":[...],"y":[...], ...}
    python fit_scaling_law.py selftest
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass

import numpy as np
from scipy.optimize import curve_fit


def _power(x, a, b):
    return a * np.power(x, b)


def _power_offset(x, e, a, b):
    return e + a * np.power(x, b)


def _r2(y, yhat) -> float:
    y = np.asarray(y, float)
    ss_res = np.sum((y - yhat) ** 2)
    ss_tot = np.sum((y - y.mean()) ** 2)
    return float(1 - ss_res / ss_tot) if ss_tot > 0 else 0.0


@dataclass
class ScalingFit:
    form: str
    params: dict
    r2: float
    metric: str
    lower_better: bool
    n_points: int
    exponent: float
    notes: list[str]

    def predict(self, x):
        x = np.asarray(x, float)
        if self.form == "power":
            return _power(x, self.params["a"], self.params["b"])
        return _power_offset(x, self.params["E"], self.params["a"], self.params["b"])


def fit(x, y, metric: str = "metric", lower_better: bool = True) -> ScalingFit:
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    notes: list[str] = []
    if len(x) != len(y):
        raise ValueError("x and y must have equal length")
    if len(x) < 3:
        raise ValueError("need >=3 points to fit a scaling law; with 3-4 treat the fit as indicative")
    if len(x) < 5:
        notes.append("Sparse run set (<5 points): exponent has wide uncertainty — state this in the writeup.")
    if np.any(x <= 0):
        raise ValueError("resource values must be positive (log-scale axis)")

    # Plain power law via log-log linear regression (robust starting point).
    pos = y > 0
    if lower_better or np.all(pos):
        logx = np.log(x[pos])
        logy = np.log(y[pos])
        b0, loga0 = np.polyfit(logx, logy, 1)
        a0 = np.exp(loga0)
    else:
        a0, b0 = 1.0, 0.1
    yhat_p = _power(x, a0, b0)
    r2_p = _r2(y, yhat_p)
    best = ScalingFit("power", {"a": float(a0), "b": float(b0)}, r2_p, metric,
                      lower_better, len(x), float(b0), list(notes))

    # Power + offset (needs >=4 points to be identifiable).
    if len(x) >= 4:
        try:
            e_guess = y.min() * 0.9 if lower_better else y.max() * 1.1
            (e, a, b), _ = curve_fit(
                _power_offset, x, y, p0=[e_guess, a0, b0], maxfev=20000,
            )
            r2_o = _r2(y, _power_offset(x, e, a, b))
            if r2_o > best.r2 + 1e-4:
                best = ScalingFit("power+offset", {"E": float(e), "a": float(a), "b": float(b)},
                                  r2_o, metric, lower_better, len(x), float(b), list(notes))
        except (RuntimeError, ValueError):
            notes.append("Offset form did not converge; reporting plain power law.")
            best.notes = list(notes)

    if best.r2 < 0.9:
        best.notes.append(f"Fit quality is modest (R^2={best.r2:.3f}); a clean power law may not hold here.")
    return best


def diminishing_returns(f: ScalingFit, x, rel_gain_threshold: float = 0.02):
    """Find the resource level past which doubling buys < threshold relative gain.

    Returns (knee_x, gain_at_knee) or (None, None) if every doubling in range
    still clears the threshold.
    """
    x = np.sort(np.asarray(x, float))
    grid = np.geomspace(x.min(), x.max(), 64)
    yv = f.predict(grid)
    yv2 = f.predict(grid * 2)
    # Relative improvement from doubling the resource.
    if f.lower_better:
        rel = (yv - yv2) / np.abs(yv)
    else:
        rel = (yv2 - yv) / np.abs(yv)
    below = np.where(rel < rel_gain_threshold)[0]
    if len(below):
        i = below[0]
        return float(grid[i]), float(rel[i])
    return None, None


def format_report(f: ScalingFit, x, extrapolate=None, threshold: float = 0.02) -> str:
    L = [
        f"# Scaling-law fit: {f.metric}",
        "",
        f"- Points: {f.n_points}   ({'lower is better' if f.lower_better else 'higher is better'})",
        f"- Model: {f.form}",
        f"- Exponent b: {f.exponent:+.4f}",
    ]
    if f.form == "power":
        L.append(f"- Form: y = {f.params['a']:.4g} · x^({f.exponent:+.4f})")
    else:
        L.append(f"- Form: y = {f.params['E']:.4g} + {f.params['a']:.4g} · x^({f.exponent:+.4f})")
        L.append(f"- Implied floor/ceiling E: {f.params['E']:.4g}")
    L.append(f"- Fit quality R^2: {f.r2:.4f}")

    knee, gain = diminishing_returns(f, x, threshold)
    L += ["", "## Diminishing returns"]
    if knee is not None:
        L.append(f"- Past resource ≈ {knee:.3g}, doubling buys < {threshold:.0%} relative gain "
                 f"(≈{gain:.1%} at the knee). More scale on this axis is low-value from there.")
    else:
        L.append(f"- Every doubling within the measured range still yields ≥ {threshold:.0%} gain — "
                 "no plateau yet; scaling this axis is still paying off.")

    if extrapolate is not None:
        yhat = float(f.predict(np.array([float(extrapolate)]))[0])
        span = float(extrapolate) / float(np.max(x))
        L += ["", "## Extrapolation",
              f"- Predicted {f.metric} at resource {float(extrapolate):.3g}: {yhat:.4g}"]
        if span > 10:
            L.append(f"- ⚠ This is {span:.0f}× beyond your largest run — extrapolation error grows fast; "
                     "treat as a rough prior, not a guarantee.")
        else:
            L.append(f"- ({span:.1f}× beyond the largest measured run.)")

    L += ["", "## Recommendation"]
    if knee is not None and extrapolate is not None and float(extrapolate) > knee:
        L.append("- The target budget sits past the knee — consider reallocating to a different axis "
                 "(data ↔ model ↔ optimization) rather than pushing this one further.")
    elif knee is None:
        L.append("- This axis has not plateaued; scaling it further is justified by the current fit.")
    else:
        L.append("- Below the knee — scaling this axis still helps; revisit the fit as new runs land.")
    if f.notes:
        L += ["", "## Caveats"] + [f"- {n}" for n in f.notes]
    return "\n".join(L)


def _cmd_fit(args) -> int:
    if args.json:
        cfg = json.load(open(args.json))
        x, y = cfg["x"], cfg["y"]
        metric = cfg.get("metric", args.metric)
        lower = cfg.get("lower_better", args.lower_better)
        extra = cfg.get("extrapolate", args.extrapolate)
        thr = cfg.get("threshold", args.threshold)
    else:
        if args.x is None or args.y is None:
            print("error: provide --x and --y (or --json)", file=sys.stderr)
            return 2
        x, y, metric, lower, extra, thr = (
            args.x, args.y, args.metric, args.lower_better, args.extrapolate, args.threshold)
    f = fit(x, y, metric=metric, lower_better=lower)
    print(format_report(f, x, extrapolate=extra, threshold=thr))
    return 0


def _cmd_selftest(_args) -> int:
    # Synthetic power law with a floor: y = 2.0 + 50 * x^-0.3
    x = np.geomspace(1e6, 2e7, 7)
    y = 2.0 + 50 * x ** -0.3
    f = fit(x, y, metric="loss", lower_better=True)
    assert f.r2 > 0.999, f
    assert abs(f.exponent + 0.3) < 0.1 or f.form == "power+offset", f
    pred = float(f.predict(np.array([4e7]))[0])
    assert 1.9 < pred < 2.6, pred
    knee, _ = diminishing_returns(f, x, 0.05)
    assert knee is not None, "expected a knee at the 5% threshold within range"
    print("selftest OK")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd")

    f = sub.add_parser("fit", help="fit a scaling law (default)")
    f.add_argument("--x", type=float, nargs="+", help="resource values (data/params/compute/batch)")
    f.add_argument("--y", type=float, nargs="+", help="metric at each resource level")
    f.add_argument("--json", help='JSON {"x":[...],"y":[...],"lower_better":bool,"extrapolate":num}')
    f.add_argument("--metric", default="metric")
    f.add_argument("--lower-better", action="store_true", help="metric improves downward (e.g. loss)")
    f.add_argument("--extrapolate", type=float, help="predict the metric at this resource level")
    f.add_argument("--threshold", type=float, default=0.02,
                   help="relative gain per doubling that counts as 'still worth it' (default 0.02)")
    f.set_defaults(func=_cmd_fit)

    s = sub.add_parser("selftest", help="run internal sanity checks")
    s.set_defaults(func=_cmd_selftest)
    return p


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    # `fit` is the default subcommand: allow `fit_scaling_law.py --x ... --y ...`.
    if not argv or argv[0] not in ("fit", "selftest", "-h", "--help"):
        argv = ["fit"] + argv
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
