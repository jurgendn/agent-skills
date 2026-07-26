"""One file per method. Replace this with your actual method.

The contract: algorithm(data, params) -> result dict containing every key in
metrics.REQUIRED_RESULT_KEYS. Report any diagnostic only the method can compute
(iterations, rank, wall-clock, whether it converged) as an extra key -- that is how
a "metric that needs the model" is satisfied without a metric ever touching one.
"""
import time

import numpy as np


def ridge(data: dict, params: dict) -> dict:
    """Closed-form ridge regression. Placeholder for your method."""
    start = time.perf_counter()

    x, y = data["x_train"], data["y_train"]
    lam = params.get("lam", 1.0)
    gram = x.T @ x + lam * np.eye(x.shape[1])
    coef = np.linalg.solve(gram, x.T @ y)

    return {
        "preds_train": x @ coef,
        "preds_test": data["x_test"] @ coef,
        "fit_seconds": time.perf_counter() - start,
        # A diagnostic reported by the method, read later by a metric.
        "rank": int(np.linalg.matrix_rank(gram)),
    }
