# Evidence base

Only the findings that change an instruction in `SKILL.md` are kept here. Each entry says what it licenses and, where
relevant, what it does *not* license.

## Minimum-viable practice, not best practice

Wilson, Bryan, Cranston, Kitzes, Nederbragt, Teal, *Good Enough Practices in Scientific Computing*, PLoS Comput.
Biol. (2017), arXiv:1609.00037.

Deliberately recommends a **minimum viable** set of practices a solo researcher will still be using months later, and
explicitly defers heavyweight tooling until a project is large enough to pay for it. Licenses: raw data read-only;
record every processing step; dependencies explicit at the root; a smoke test rather than a unit-test suite; name
files by content, never by sequence number. Its own "what we left out" list (branches, build tools, unit tests, CI,
coverage, profiling) is the external backing for this skill's *What to skip*.

Note the paper's own framing of the danger: prescribing the full professional stack to a newcomer scares them off the
core practices that actually matter. That is the audience this skill serves.

## One command, and a table that maps to it

ML Code Completeness Checklist (Stojnic et al., *Tips for Releasing Research Code in ML*, official NeurIPS 2020
recommendations, paperswithcode/releasing-research-code). Five items: specification of dependencies; training code;
evaluation code; pre-trained models; **README includes a table of results accompanied by the precise command to
produce them**.

The fifth item is the external validation of this skill's command-to-number requirement. An auto-generated table
from `aggregate.py` is strictly stronger than the hand-written README the checklist asks for, since it cannot drift
from the runs it summarizes.

## Seeds: no fixed number is defensible

Henderson, Islam, Bachman, Pineau, Precup, Meger, *Deep Reinforcement Learning that Matters*, AAAI 2018,
arXiv:1709.06560.

Ran 10 trials differing **only in random seed**, split them into two groups of 5, and averaged each: the two groups
formed statistically different distributions (2-sample t-test across training, t = −9.09, p = 0.0016). They
explicitly decline to recommend a trial count and point to bootstrap confidence bounds and bootstrap power analysis
instead. They also name averaging over few trials (N < 5), and reporting top-N of several trials, as sources of
misleading results.

Licenses: aggregate every run matching a config, never max or top-N; report a bootstrap CI, not only ±σ; treat a
hardcoded seed count as a starting default that a wide CI overrides. Does **not** license "5 seeds is enough" — that
is precisely the configuration shown to come apart.

## Prototype the pipeline before the sweep

Eimer, Schäpermeier, Biedenkapp, Tornede, Kotthoff, et al. (COSEAL Research Network), *Best Practices For Empirical
Meta-Algorithmic Research*, arXiv:2512.16491 (Dec 2025).

Recommends starting with a small prototype experiment on trimmed or dummy data, whose purpose is not precision but
exercising the evaluation pipeline holistically — logging, plotting, and resource tracking working in tandem — and
using it to extrapolate the full experiment's resource cost before paying it. Also: scripts that run experiments,
gather data, and produce plots are code and deserve the same scrutiny; back up results as soon as they exist.

Directly relevant to a non-programmer working with an agent: the report warns that AI coding tools "can produce
clean-looking, executable, yet wrong code" and that output should always be checked before it is relied on. Hence
the skill's instruction to verify the harness by running it.

## Software engineering: three items adopted, the rest declined

Wolter, Veeramacheneni, Hoyt, *More Rigorous Software Engineering Would Improve Reproducibility in Machine Learning
Research*, arXiv:2502.00902 (Sep 2025). Crawled repositories linked from NeurIPS/ICML/ICLR/AISTATS/TMLR/MLOSS
papers, 2018–2025.

**Adopted:** fix and record every PRNG seed; document dependencies so an environment can be rebuilt; and their final
checklist item — ideally a single file or command that re-runs all of a paper's experiments. The runner is that.

**Declined, with reason:** the paper also advocates packaging, `pyproject.toml`, `src/` layout, tox/nox, CI, MyPy,
and Sphinx. Its own hedge is that these should be applied "only when appropriate," and it grants that some artifacts
(their example is a theory paper's illustrative notebook) do not need the machinery. Its measurements are of
*released* repositories, and its stated motivation is handover between PhD-student generations — neither is
in-flight experimentation by a non-programmer before a deadline. Their survey found roughly a quarter of repositories
have a test folder and licence adoption stagnant between 50% and 80%, which shows the practices are rare, not that
adopting them mid-project is what makes a paper's numbers trustworthy.

## Reproducibility findings worth quoting accurately

Pineau, Vincent-Lamarre, Sinha, Larivière, Beygelzimer, d'Alché-Buc, Fox, Larochelle, *Improving Reproducibility in
Machine Learning Research (A Report from the NeurIPS 2019 Reproducibility Program)*, JMLR 22(164), arXiv:2003.12206.

- Code submission rose from **<50%** (NeurIPS 2018) to **74.4%** at camera-ready (NeurIPS 2019), under a policy that
  expects but does not require code. Voluntary participation was sufficient.
- **34%** of reviewers found the checklist answers useful.
- 87% of papers said they define their metrics clearly, yet **36%** judged error bars not applicable — the gap this
  skill's aggregator closes mechanically.
- The often-quoted **85% vs 4%** figure (results reproduced with vs without original-author assistance) is **Raff
  (2019)**, cited by Pineau et al., against a baseline of 63.5% of results replicated across 255 manuscripts.
  Pineau et al. flag a likely selection bias in it. Attribute it to Raff, not to the NeurIPS program.

Semmelrock, Ross-Hellauer, Kopeinik, Theiler, Haberl, Thalmann, Kowald, *Reproducibility in Machine Learning-based
Research: Overview, Barriers and Drivers*, arXiv:2406.14325 (Feb 2025). Nine barriers mapped to nine drivers across
four reproducibility types — R1 Description, R2 Code, R3 Data, R4 Experiment (taxonomy due to Gundersen et al., read
here via Semmelrock rather than in the original). Useful framing: the four types trade off against generalizability,
and the barrier this skill actually addresses is R4 Experiment — sources of randomness and nondeterminism. It
concludes that awareness and education underlie all other drivers, which is a cultural finding, not a technical
instruction.

## Not adopted: LOR / COS overfitting scores

Michelucci & Venturini, *Best Practices for Machine Learning Experimentation in Scientific Applications*,
arXiv:2511.21354 (Nov 2025). A 9-page preprint. Its planning table (Exp. ID, Task, Preprocessing, Normalization,
Model instance, Metrics, Dataset, Notes) and results table (the same, plus metric ± σ for train and test) are a
reasonable model for the intake and the aggregator's columns, and its dataset advice matches Wilson (raw data
intact, document every transformation).

Its two proposed diagnostics are **not** carried into this skill, for three reasons:

1. `COS = α·(m_train/m_test) + β·(σ_train/σ_test)` with α=β=½. Its worked examples reproduce the formula (Table 3
   EX1: ½(3.4/3.0)+½(0.2/0.3)=0.90 ✓; EX2: ½(3.5/2.6)+½(0.1/0.4)=0.80 ✓) — but both are same-side cases. Under the
   formula, overfitting (train error below test, σ_test ≫ σ_train) pushes *both* terms below ½, giving COS < 1,
   which the paper's own interpretation text labels **underfitting**. The stated direction is backwards and the
   composite is not identifiable: COS < 1 is consistent with either failure.
2. `LOR = log(m_train/m_test)` has its sign convention fixed by an error-type metric (lower is better). With an
   accuracy-type metric the interpretation inverts — and the paper's planning table uses Accuracy/F1 while its
   results table uses MAE, so the trap is live inside the paper.
3. Overfitting diagnosis is `experiment-design`'s scope, not repo plumbing.

Reporting `metric_train`, `metric_test`, `sigma_train`, `sigma_test` as four separate columns is strictly more
informative than either composite and has no sign convention to get wrong. The paper is also worth citing for one
thing it states plainly: exclude and do not report model instances that failed to learn (constant predictions),
which is a reporting rule rather than a score.
