"""The four checks that stand between fast publishing and a retraction.

    python sanity_check.py

Not a test suite. Each check is one you can verify is MATHEMATICALLY the right check
even if you would not have written the code -- which is the point. Run it after any
change to data.py, an algorithm, or metrics.py, and before launching a full sweep.
"""
import numpy as np

from algorithms import ALGORITHMS
from data import LOADERS
from metrics import METRICS, NONDETERMINISTIC_METRICS, REQUIRED_RESULT_KEYS
from run import run_one

# The method the correctness check exercises. Change this when you replace the
# placeholder method -- if it names an algorithm you deleted, the checks fail with a
# KeyError that looks like the checker is broken rather than your code.
PRIMARY = next(iter(ALGORITHMS))

TINY = {"data": "synthetic", "algorithm": PRIMARY, "n_train": 50, "noise": 0.5}


def check_determinism() -> None:
    """Same seed twice must give bit-identical metrics. Catches unseeded randomness.

    Timing metrics are exempt (see metrics.NONDETERMINISTIC_METRICS) -- they measure
    the machine, not the mathematics.
    """
    first, second = run_one(TINY, seed=0), run_one(TINY, seed=0)
    for name in METRICS:
        if name in NONDETERMINISTIC_METRICS:
            continue
        assert first[name] == second[name], (
            f"{name} changed between two runs with seed 0 "
            f"({first[name]} vs {second[name]}): some RNG is not seeded."
        )


def check_required_keys() -> None:
    """Every algorithm reports every key a metric reads. Catches holes in the table."""
    data = LOADERS[TINY["data"]](TINY, 0)
    for name, algorithm in ALGORITHMS.items():
        result = algorithm(data, TINY)
        missing = [k for k in REQUIRED_RESULT_KEYS if k not in result]
        assert not missing, f"{name} does not report {missing}"


def check_no_leakage() -> None:
    """Train and test index sets must be disjoint. Delete if your runs are generated
    fresh per split and no held-out set exists."""
    data = LOADERS[TINY["data"]](TINY, 0)
    overlap = set(data["train_idx"].tolist()) & set(data["test_idx"].tolist())
    assert not overlap, f"{len(overlap)} index/indices appear in both train and test"


def check_recovers_known_answer() -> None:
    """With little noise and plenty of data, ridge must approach the true beta.

    This is the correctness check: for a learning setup, substitute 'loss goes to ~0
    when overfitting a tiny batch'; for a numerical method, 'agrees with the closed
    form on a case that has one'.
    """
    config = {"data": "synthetic", "algorithm": PRIMARY, "n_train": 2000, "noise": 0.01}
    data = LOADERS[config["data"]](config, 0)
    result = ALGORITHMS[PRIMARY](data, config)
    rmse = float(np.sqrt(np.mean((result["preds_test"] - data["y_test"]) ** 2)))
    assert rmse < 0.1, f"{PRIMARY} did not recover a near-noiseless signal (rmse={rmse:.3f})"


if __name__ == "__main__":
    for check in (check_determinism, check_required_keys,
                  check_no_leakage, check_recovers_known_answer):
        check()
        print(f"ok  {check.__name__}")
    print("\nall sanity checks passed")
