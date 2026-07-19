#!/usr/bin/env python3
"""Aggregate IELTS Writing feedback files into progress statistics.

Reads the YAML frontmatter of every Markdown file in a vault's ``feedback/``
folder and computes the numbers a progress report needs: band averages and
trends, error-tag frequencies, revision deltas, and coverage counts. It emits
one JSON blob on stdout so the calling agent can turn deterministic numbers
into prose without re-deriving (and risking misreading) any score.

The script intentionally has no third-party dependencies — it ships with a
small frontmatter parser so it runs anywhere Python 3 does.

Usage:
    python aggregate_feedback.py --vault PATH [--mode period|cumulative]
        [--period weekly|monthly] [--since YYYY-MM-DD] [--until YYYY-MM-DD]
        [--task 1|2|all]

The feedback frontmatter schema this expects (see the vault AGENTS.md):
    task, prompt_id, version, date, band_overall, band_cc, band_lr, band_gra,
    band_ta (Task 1) or band_tr (Task 2), errors: [tag, tag, ...]
"""

import argparse
import datetime as dt
import json
import os
import sys
from collections import Counter, defaultdict

# Criterion keys we read. band_ta is Task 1 (Task Achievement); band_tr is
# Task 2 (Task Response). They are mutually exclusive per file but we expose a
# unified "criterion1" so trends can be shown across both tasks.
BAND_KEYS = ["band_overall", "band_cc", "band_lr", "band_gra", "band_ta", "band_tr"]


def parse_frontmatter(text):
    """Return the YAML frontmatter of a Markdown file as a dict.

    Handles the subset of YAML these files actually use: ``key: value`` scalars
    and an ``errors`` list in either inline (``[a, b]``) or block (``- a``)
    form. Keeping the parser tiny avoids a PyYAML dependency that would make the
    skill harder to run in a clean environment.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    out = {}
    i = 1
    while i < len(lines):
        line = lines[i]
        if line.strip() == "---":
            break
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip()
            if val == "":
                # Possibly a block list (errors:\n  - tag) — collect indented
                # "- item" lines that follow.
                items = []
                j = i + 1
                while j < len(lines) and lines[j].lstrip().startswith("- "):
                    items.append(lines[j].lstrip()[2:].strip())
                    j += 1
                if items:
                    out[key] = items
                    i = j
                    continue
                out[key] = ""
            elif val.startswith("[") and val.endswith("]"):
                inner = val[1:-1].strip()
                out[key] = [x.strip() for x in inner.split(",") if x.strip()] if inner else []
            else:
                out[key] = val.strip().strip("'\"")
        i += 1
    return out


def to_float(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def period_key(date_str, granularity):
    """Map an ISO date to a bucket label: ISO week (weekly) or YYYY-MM (monthly)."""
    try:
        d = dt.date.fromisoformat(date_str)
    except (TypeError, ValueError):
        return "undated"
    if granularity == "monthly":
        return d.strftime("%Y-%m")
    iso = d.isocalendar()
    return f"{iso[0]}-W{iso[1]:02d}"


def mean(values):
    vals = [v for v in values if v is not None]
    return round(sum(vals) / len(vals), 2) if vals else None


def collect(feedback_dir):
    records = []
    for fname in sorted(os.listdir(feedback_dir)):
        if not fname.endswith(".md"):
            continue
        path = os.path.join(feedback_dir, fname)
        with open(path, "r", encoding="utf-8") as fh:
            fm = parse_frontmatter(fh.read())
        if not fm:
            continue
        rec = {
            "file": fname,
            "task": str(fm.get("task", "")).strip(),
            "prompt_id": fm.get("prompt_id", fname.rsplit("-v", 1)[0]),
            "version": int(to_float(fm.get("version")) or 0),
            "date": fm.get("date", ""),
            "errors": fm.get("errors") or [],
        }
        for k in BAND_KEYS:
            rec[k] = to_float(fm.get(k))
        # Unified first criterion so Task 1 and Task 2 can share a trend line.
        rec["criterion1"] = rec["band_ta"] if rec["band_ta"] is not None else rec["band_tr"]
        records.append(rec)
    return records


def in_window(rec, since, until):
    if not rec["date"]:
        return since is None and until is None
    try:
        d = dt.date.fromisoformat(rec["date"])
    except ValueError:
        return True
    if since and d < since:
        return False
    if until and d > until:
        return False
    return True


def summarize(records):
    """Band averages, error counts, and coverage over a set of records."""
    crit_keys = ["criterion1", "band_cc", "band_lr", "band_gra", "band_overall"]
    averages = {k: mean([r[k] for r in records]) for k in crit_keys}
    error_counter = Counter()
    for r in records:
        error_counter.update(r["errors"])
    by_task = Counter(r["task"] for r in records)
    prompts = {r["prompt_id"] for r in records}
    return {
        "attempts": len(records),
        "distinct_prompts": len(prompts),
        "by_task": dict(by_task),
        "criterion_averages": averages,
        "error_frequency": error_counter.most_common(),
    }


def revision_deltas(records):
    """For prompts with multiple versions, report the band_overall change from
    the earliest to the latest version — the clearest signal of whether
    revising actually moved the score."""
    by_prompt = defaultdict(list)
    for r in records:
        by_prompt[r["prompt_id"]].append(r)
    deltas = []
    for pid, recs in by_prompt.items():
        if len(recs) < 2:
            continue
        recs = sorted(recs, key=lambda x: x["version"])
        first, last = recs[0], recs[-1]
        if first["band_overall"] is None or last["band_overall"] is None:
            continue
        deltas.append({
            "prompt_id": pid,
            "from_version": first["version"],
            "to_version": last["version"],
            "from_overall": first["band_overall"],
            "to_overall": last["band_overall"],
            "delta": round(last["band_overall"] - first["band_overall"], 2),
        })
    return sorted(deltas, key=lambda x: x["prompt_id"])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--vault", default=".", help="Vault root containing a feedback/ folder")
    ap.add_argument("--feedback-dir", help="Path to feedback dir (overrides --vault/feedback)")
    ap.add_argument("--mode", choices=["period", "cumulative"], default="cumulative")
    ap.add_argument("--period", choices=["weekly", "monthly"], default="monthly")
    ap.add_argument("--since", help="Only include feedback dated on/after YYYY-MM-DD")
    ap.add_argument("--until", help="Only include feedback dated on/before YYYY-MM-DD")
    ap.add_argument("--task", choices=["1", "2", "all"], default="all")
    args = ap.parse_args()

    feedback_dir = args.feedback_dir or os.path.join(args.vault, "feedback")
    if not os.path.isdir(feedback_dir):
        sys.exit(f"error: feedback directory not found: {feedback_dir}")

    since = dt.date.fromisoformat(args.since) if args.since else None
    until = dt.date.fromisoformat(args.until) if args.until else None

    records = collect(feedback_dir)
    records = [r for r in records if in_window(r, since, until)]
    if args.task != "all":
        records = [r for r in records if r["task"] == args.task]

    result = {
        "generated": dt.date.today().isoformat(),
        "feedback_dir": feedback_dir,
        "mode": args.mode,
        "task_filter": args.task,
        "date_range": {
            "since": args.since,
            "until": args.until,
            "earliest": min((r["date"] for r in records if r["date"]), default=None),
            "latest": max((r["date"] for r in records if r["date"]), default=None),
        },
        "overall": summarize(records),
        "revision_deltas": revision_deltas(records),
    }

    if args.mode == "period":
        buckets = defaultdict(list)
        for r in records:
            buckets[period_key(r["date"], args.period)].append(r)
        result["period_granularity"] = args.period
        result["periods"] = [
            {"period": key, **summarize(recs)}
            for key, recs in sorted(buckets.items())
        ]

    json.dump(result, sys.stdout, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
