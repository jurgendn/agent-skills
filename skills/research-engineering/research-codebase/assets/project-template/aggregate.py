"""Turn finished runs into the paper's table.

    python aggregate.py

Reads outputs/*/metrics.json, groups by configuration across seeds, and writes
results/table.csv and results/table.tex. The .tex rows paste into a booktabs table,
so no number is ever transcribed by hand.

Two rules that are not stylistic:
  * every run matching a config is aggregated -- never the maximum, never the best
    few seeds. Selecting top-N of several trials is a known source of results that
    do not survive replication.
  * a bootstrap confidence interval is reported alongside the mean. If the interval
    overlaps your baseline, the honest response is more seeds, not a bolder claim.

Train and test quantities stay in separate columns. Do not fold them into a single
composite "overfitting score": the published composites are not identifiable (the
same value is consistent with overfitting or underfitting) and their sign convention
silently inverts between error-type and accuracy-type metrics.
"""
import csv
import json
from collections import defaultdict
from pathlib import Path

import numpy as np

OUTPUTS, RESULTS = Path("outputs"), Path("results")
N_BOOTSTRAP = 10_000


def bootstrap_ci(values: np.ndarray, level: float = 0.95, seed: int = 0) -> tuple:
    """Percentile bootstrap CI of the mean. Wide interval == you need more seeds."""
    if len(values) < 2:
        return (float("nan"), float("nan"))
    rng = np.random.default_rng(seed)
    draws = rng.choice(values, size=(N_BOOTSTRAP, len(values)), replace=True).mean(axis=1)
    lo, hi = (1 - level) / 2 * 100, (1 + level) / 2 * 100
    return (float(np.percentile(draws, lo)), float(np.percentile(draws, hi)))


def collect() -> dict:
    """Group every finished run by its configuration, ignoring the seed."""
    groups = defaultdict(lambda: defaultdict(list))
    key_sets = set()
    for metrics_file in sorted(OUTPUTS.glob("*/metrics.json")):
        config = json.loads((metrics_file.parent / "config.json").read_text())["config"]
        key_sets.add(frozenset(config))
        key = tuple(sorted(config.items()))
        for name, value in json.loads(metrics_file.read_text()).items():
            groups[key][name].append(value)

    # Adding a key to configs.py mid-project puts old and new runs in different
    # groups, silently halving the n_seeds behind every number. Warn loudly: a table
    # reporting 5 seeds where you believe there are 10 is the worst failure here.
    if len(key_sets) > 1:
        fields = sorted(set().union(*key_sets) - set.intersection(*map(set, key_sets)))
        print(
            f"WARNING: runs in outputs/ have different config fields (differing: {fields}).\n"
            "         They will NOT be grouped together, so n_seeds per row is lower than\n"
            "         you expect. Delete outputs/ and re-run, or exclude the stale runs.\n"
        )
    return groups


def main() -> None:
    groups = collect()
    if not groups:
        print("no finished runs in outputs/ -- run `python run.py` first")
        return

    metric_names = sorted({m for per_metric in groups.values() for m in per_metric})
    config_keys = sorted({k for key in groups for k, _ in key})

    rows = []
    for key, per_metric in sorted(groups.items()):
        config = dict(key)
        row = {k: config.get(k, "") for k in config_keys}
        row["n_seeds"] = len(next(iter(per_metric.values())))
        for name in metric_names:
            values = np.asarray(per_metric.get(name, []), dtype=float)
            if values.size == 0:
                row[f"{name}_mean"] = row[f"{name}_std"] = row[f"{name}_ci"] = ""
                continue
            lo, hi = bootstrap_ci(values)
            row[f"{name}_mean"] = f"{values.mean():.4f}"
            row[f"{name}_std"] = f"{values.std(ddof=1) if values.size > 1 else 0.0:.4f}"
            row[f"{name}_ci"] = f"[{lo:.4f}, {hi:.4f}]"
        rows.append(row)

    RESULTS.mkdir(exist_ok=True)
    fieldnames = list(rows[0])
    with (RESULTS / "table.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    # booktabs rows: \begin{tabular} ... \toprule <header> \midrule <rows> \bottomrule
    # Underscores must be escaped or the row will not compile in text mode.
    def tex_cell(value) -> str:
        return str(value).replace("_", r"\_")

    tex = [" & ".join(f.replace("_", " ") for f in fieldnames) + r" \\"]
    tex += [" & ".join(tex_cell(row.get(f, "")) for f in fieldnames) + r" \\" for row in rows]
    (RESULTS / "table.tex").write_text("\n".join(tex) + "\n")

    print(f"{len(rows)} configuration(s) -> results/table.csv and results/table.tex")


if __name__ == "__main__":
    main()
