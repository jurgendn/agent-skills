"""Run one experiment, top to bottom. Read it without jumping between files.

This is the entry point. Keep the call graph shallow: parse args, load data,
build the model with a plain if-statement, train, evaluate, save. Add a layer
only when you feel the pain of not having it.
"""
import argparse
import random

import numpy as np


def set_seed(seed: int) -> None:
    """Seed every RNG so a result can be reproduced and defended to a reviewer."""
    random.seed(seed)
    np.random.seed(seed)
    try:
        import torch
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
    except ImportError:
        pass


def build_model(name: str):
    """Known at write time, so an if-statement beats a registry/factory."""
    if name == "rwgp":
        from models.rwgp import RWGP
        return RWGP()
    # elif name == "rwgp_overlap":
    #     from models.rwgp_overlap import RWGPOverlap
    #     return RWGPOverlap()
    raise ValueError(f"unknown model: {name}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", required=True)
    parser.add_argument("--model", default="rwgp")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--lr", type=float, default=0.01)
    parser.add_argument("--epochs", type=int, default=200)
    args = parser.parse_args()

    set_seed(args.seed)

    # Name outputs by what produced them — two runs must never overwrite.
    output_dir = f"outputs/{args.dataset}_{args.model}_seed{args.seed}_lr{args.lr}"

    # TODO: load data from data/processed/, train, evaluate, write to output_dir.
    model = build_model(args.model)
    print(f"would train {model.__class__.__name__} on {args.dataset} -> {output_dir}")


if __name__ == "__main__":
    main()
