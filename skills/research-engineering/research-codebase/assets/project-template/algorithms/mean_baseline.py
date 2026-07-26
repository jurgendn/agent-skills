"""The baseline. Keep it as a separate file with no shared parent class.

Two methods that share no real behavior stay two independent files. An abstract base
class introduced only to share a signature is indirection you pay for at every read.
"""
import time

import numpy as np


def mean_baseline(data: dict, params: dict) -> dict:
    """Predict the training mean everywhere. If your method cannot beat this, stop."""
    start = time.perf_counter()

    mean = float(np.mean(data["y_train"]))
    return {
        "preds_train": np.full_like(data["y_train"], mean),
        "preds_test": np.full_like(data["y_test"], mean),
        "fit_seconds": time.perf_counter() - start,
    }
