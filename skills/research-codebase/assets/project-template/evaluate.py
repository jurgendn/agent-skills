"""Compute metrics. Kept separate from train.py because it's called by both
the training script and any re-scoring you do later.
"""
import numpy as np


def accuracy(preds: np.ndarray, labels: np.ndarray) -> float:
    """preds, labels: [N]. Returns fraction correct."""
    return float((preds == labels).mean())
