"""The runner. One command executes every experiment in the paper.

    python run.py                 # run everything not already finished
    python run.py --prototype     # tiny version of the sweep, to test the pipeline
    python run.py --force         # re-run even finished runs

Runs already holding a metrics.json are skipped, so a crash costs only the unfinished
work. Nothing here changes when you add a config, a method, or a metric.
"""
import argparse
import hashlib
import json
import random
import subprocess
import sys
from pathlib import Path

import numpy as np

from algorithms import ALGORITHMS
from configs import CONFIGS, SEEDS
from data import LOADERS
from metrics import METRICS, REQUIRED_RESULT_KEYS

OUTPUTS = Path("outputs")


def set_seed(seed: int) -> None:
    """Seed every RNG in use, so a number can be reproduced and defended."""
    random.seed(seed)
    np.random.seed(seed)
    try:
        import torch
    except ImportError:
        return
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.use_deterministic_algorithms(True, warn_only=True)


def git_sha() -> str:
    try:
        out = subprocess.run(
            ["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True
        )
        return out.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"


def run_id(config: dict, seed: int) -> str:
    """Unique, and short enough to stay a legal filename under a wide sweep.

    A readable prefix plus a hash of the full config: joining every key would cross
    the 255-byte filename limit once a sweep has several parameters, and float repr
    (0.0001 vs 1e-05) would make paths unstable. The human-readable version of the
    config lives in config.json inside the directory, so nothing is lost.
    """
    payload = json.dumps(config, sort_keys=True)
    digest = hashlib.sha1(payload.encode()).hexdigest()[:8]
    return f"{config['algorithm']}__seed={seed}__{digest}".replace("/", "-")


def run_one(config: dict, seed: int) -> dict:
    set_seed(seed)
    data = LOADERS[config["data"]](config, seed)
    result = ALGORITHMS[config["algorithm"]](data, config)

    missing = [k for k in REQUIRED_RESULT_KEYS if k not in result]
    if missing:
        raise KeyError(
            f"{config['algorithm']} did not return required key(s) {missing}. "
            "Every algorithm must report every key any metric reads."
        )
    return {name: fn(result, data) for name, fn in METRICS.items()}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prototype", action="store_true",
                        help="one config, two seeds -- exercises the whole pipeline cheaply")
    parser.add_argument("--force", action="store_true", help="re-run finished runs")
    args = parser.parse_args()

    configs, seeds = CONFIGS, SEEDS
    if args.prototype:
        configs, seeds = CONFIGS[:1], SEEDS[:2]

    sha, done, ran = git_sha(), 0, 0
    for config in configs:
        for seed in seeds:
            out_dir = OUTPUTS / run_id(config, seed)
            if (out_dir / "metrics.json").exists() and not args.force:
                done += 1
                continue

            out_dir.mkdir(parents=True, exist_ok=True)
            # Provenance is written by the machine, never maintained by hand.
            (out_dir / "config.json").write_text(json.dumps(
                {"config": config, "seed": seed, "git_sha": sha, "argv": sys.argv},
                indent=2, sort_keys=True,
            ))
            metrics = run_one(config, seed)
            (out_dir / "metrics.json").write_text(json.dumps(metrics, indent=2, sort_keys=True))
            ran += 1
            print(f"ran {out_dir.name}")

    print(f"\n{ran} run(s) executed, {done} skipped as already finished.")
    print("Next: python aggregate.py")


if __name__ == "__main__":
    main()
