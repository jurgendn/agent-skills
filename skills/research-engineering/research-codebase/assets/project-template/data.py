"""Stage 1 of the contract: config + seed -> one problem instance.

Two entry points, because a run is either generated or loaded:

    generate(params, seed)  synthetic instances -- simulations, solver instances,
                            numerical verification of a bound
    load(params, seed)      real datasets from data/raw/ (never modified)

Keep the one your work needs and delete the other. Both must return the same dict
shape so the algorithms and metrics do not care which was used.
"""
from pathlib import Path

import numpy as np


def generate(params: dict, seed: int) -> dict:
    """Return one problem instance. Deterministic given (params, seed)."""
    rng = np.random.default_rng(seed)
    n_train, n_test, d = params["n_train"], 500, 20

    beta = rng.standard_normal(d)
    x = rng.standard_normal((n_train + n_test, d))
    y = x @ beta + params["noise"] * rng.standard_normal(n_train + n_test)

    # Index sets are returned so sanity_check.py can assert they are disjoint.
    idx = rng.permutation(n_train + n_test)
    train_idx, test_idx = idx[:n_train], idx[n_train:]
    return {
        "x_train": x[train_idx],
        "y_train": y[train_idx],
        "x_test": x[test_idx],
        "y_test": y[test_idx],
        "train_idx": train_idx,
        "test_idx": test_idx,
        "beta_true": beta,
    }


def load(params: dict, seed: int) -> dict:
    """Load a real dataset from data/raw/ and split it. Same return shape as generate().

    Expects data/raw/<name>.csv with the target in the last column. data/raw/ is
    read-only -- write any derived version to data/processed/ instead.
    """
    raw = np.loadtxt(Path("data/raw") / f"{params['data']}.csv", delimiter=",", skiprows=1)
    x, y = raw[:, :-1], raw[:, -1]

    # The split is seeded, so the same seed gives the same split on every machine.
    rng = np.random.default_rng(seed)
    idx = rng.permutation(len(y))
    n_train = int(round(params.get("train_frac", 0.8) * len(y)))
    train_idx, test_idx = idx[:n_train], idx[n_train:]
    return {
        "x_train": x[train_idx],
        "y_train": y[train_idx],
        "x_test": x[test_idx],
        "y_test": y[test_idx],
        "train_idx": train_idx,
        "test_idx": test_idx,
    }


# Register each data source here; the "data" key of a config selects one.
LOADERS = {
    "synthetic": generate,
    # "cora": load,      # uncomment per real dataset in data/raw/
}
