#!/usr/bin/env bash
# One .sh file per experiment. The script IS the configuration — no YAML, no
# config loader. Switch to a config file only past ~10 variants.
python train.py \
  --dataset cora \
  --model rwgp \
  --seed 42 \
  --lr 0.01 \
  --epochs 200
