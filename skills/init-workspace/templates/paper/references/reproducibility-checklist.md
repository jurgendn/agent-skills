# Reproducibility checklist (reference)

Keep this current **as you run experiments**, not as a scramble before the deadline. Each `experiments/` note should leave this checklist answerable. For a real audit run `reproducibility-audit`; to package the release run `artifact-release-packager`.

## Per-experiment

- [ ] Random **seed(s)** recorded; results reported over multiple seeds with variance, not a single run.
- [ ] **Config** captured (hyperparameters, model size, optimizer, schedule) — ideally a committed config file referenced from the experiment note.
- [ ] **Data**: exact dataset version/split, preprocessing, and any filtering; pointer stored in `data/` (not the raw data).
- [ ] **Compute**: hardware, wall-clock, and approximate cost noted.
- [ ] **Code commit** hash that produced the numbers (in the `research-codebase` repo).

## Paper-level

- [ ] Every reported number maps to a specific experiment note + command.
- [ ] Main result table is reproducible from a documented entry point.
- [ ] Statistical claims use an appropriate test and report effect size (`statistical-testing-guide`).
- [ ] Ablations isolate the claimed mechanism (`hypothesis-and-ablation-planner`).
- [ ] Known limitations / failure modes are stated honestly.

## Release-level (if applicable)

- [ ] Code, configs, and scripts released with a licence.
- [ ] README maps paper tables/figures → reproduction commands.
- [ ] Data/model release is safe (licences, PII, model cards) — see `artifact-release-packager`.
