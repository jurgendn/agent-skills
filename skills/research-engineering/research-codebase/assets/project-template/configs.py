"""The whole experiment plan. This is the only file you edit to run more experiments.

Adding an experiment means adding to this list. It never means editing run.py.
"""

# One dict per configuration. Keys are passed through to data generation and to
# the algorithm, so add a key here and read it there -- nothing in between changes.
CONFIGS = [
    {"data": "synthetic", "algorithm": algorithm, "n_train": n_train, "noise": 0.5}
    for algorithm in ("ridge", "mean_baseline")
    for n_train in (50, 500)
]

# Ten is a starting default, not a guarantee. If aggregate.py reports a confidence
# interval wide enough to overlap your baseline, the answer is more seeds -- not a
# bolder claim in the paper.
SEEDS = tuple(range(10))
