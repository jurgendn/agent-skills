"""Stage 3 of the contract: metric(result, data) -> float.

Metrics read ONLY from the result dict an algorithm returned, never from a fitted
model object. That is what lets a scipy/sklearn baseline and your own class be
scored by the same code: a metric reading `model.coef_` would work on one and crash
on the other.

If a metric genuinely must re-probe a fitted object (evaluating on a third split,
tuning a threshold after fitting), the algorithm may return it under the key
"model" -- documented escape hatch, not the normal path.

Add a metric by adding one line to METRICS.
"""
import numpy as np


def rmse_train(result: dict, data: dict) -> float:
    return float(np.sqrt(np.mean((result["preds_train"] - data["y_train"]) ** 2)))


def rmse_test(result: dict, data: dict) -> float:
    return float(np.sqrt(np.mean((result["preds_test"] - data["y_test"]) ** 2)))


def fit_seconds(result: dict, data: dict) -> float:
    """A diagnostic the algorithm computed and reported. The metric just reads it."""
    return float(result["fit_seconds"])


METRICS = {
    "rmse_train": rmse_train,
    "rmse_test": rmse_test,
    "fit_seconds": fit_seconds,
}

# Every algorithm must return every key any metric reads. run.py checks this and
# fails on the first run rather than leaving a hole in the table after 200 runs.
REQUIRED_RESULT_KEYS = ("preds_train", "preds_test", "fit_seconds")

# Metrics that measure the machine rather than the mathematics: wall-clock, memory,
# throughput. They vary run to run by nature, so the determinism check skips them.
# Keep this list SHORT -- anything listed here is exempt from the strongest check in
# the project, so a metric belongs here only if it is genuinely a hardware timing.
NONDETERMINISTIC_METRICS = ("fit_seconds",)
