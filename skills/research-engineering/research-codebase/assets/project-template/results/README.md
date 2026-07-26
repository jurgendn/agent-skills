# Results

`table.csv` and `table.tex` in this directory are **generated** by `python aggregate.py`
from the per-run `metrics.json` files in `outputs/`. Do not edit them by hand — the
next aggregation overwrites your edit, and a hand-edited number no longer traces to a
run.

Each row is one configuration aggregated over all its seeds, reporting `n_seeds`, the
mean, the standard deviation, and a 95% bootstrap confidence interval per metric.

To find what produced a row: the configuration columns identify the group, and
`outputs/<config>__seed=<n>/config.json` holds the exact params, seed, git commit, and
command line for each run in it.

If a paper table needs a subset or a different layout, add the shaping to
`aggregate.py` so it stays reproducible. Do not paste numbers into the manuscript by
hand — `table.tex` is written as booktabs rows for exactly that reason.
