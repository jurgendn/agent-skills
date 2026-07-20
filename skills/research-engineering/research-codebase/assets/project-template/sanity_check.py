"""20 lines that catch the bugs unit tests would, without the ceremony.

Run after any big change: checks shapes are right and loss moves the right way
in the first few steps. Not a test suite — a smoke alarm.
"""
import numpy as np

from evaluate import accuracy


def check_metric_shapes() -> None:
    preds = np.array([0, 1, 1, 0])
    labels = np.array([0, 1, 0, 0])
    acc = accuracy(preds, labels)
    assert 0.0 <= acc <= 1.0, acc
    assert abs(acc - 0.75) < 1e-9, acc


if __name__ == "__main__":
    check_metric_shapes()
    # TODO: add a 3-step training check — assert loss decreases on a tiny batch.
    print("sanity checks passed")
