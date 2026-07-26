"""Stage 2 of the contract: the algorithm registry.

Add a method with TWO lines here -- an import and a dict entry. run.py never changes.

A plain dict, not an if-chain in run.py: an if-chain means editing the shared entry
point every time you add a method, which is the one edit that breaks every run at
once. And not a decorator-based plugin system: that hides where methods come from.
"""
from algorithms.mean_baseline import mean_baseline
from algorithms.ridge import ridge

ALGORITHMS = {
    "ridge": ridge,
    "mean_baseline": mean_baseline,
}
