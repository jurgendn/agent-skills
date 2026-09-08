# Vocabulary buckets, contribution roles, and calibration terms

Two things live here: the **concept-kind classification** used in `SKILL.md` step 2, and the
**contributor-role vocabulary** used in step 4. Read the provenance notes — the two halves have
very different evidential standing.

## Why the buckets are ours, and why no catalogue can replace them

The seven buckets (research problem / theory / method / model-algorithm / evaluation / tooling /
outcome-artifact) are this skill's own instrument. They were checked against the standing subject
taxonomies first, and the search returned a clean negative:

| Taxonomy | What it classifies | Concept-kind axis? |
|---|---|---|
| ACM CCS 2012 | computing subject areas; SKOS/XML, free for educational and research use | no |
| arXiv category taxonomy | subject classes (cs.LG, math.PR, …) | no |
| MSC2020 | mathematics subject areas; CC-BY-NC-SA | no |
| IEEE Thesaurus | ~12,420 terms, BT/NT/RT/UF relations; download by access request | no |
| CSO | ~14k CS topics, CC-BY 4.0 | no |

**Every general taxonomy examined classifies by subject area only.** None carries an orthogonal
problem / theory / method / model / evaluation / tool dimension. Two partial precedents exist and
both are domain-scoped: **EDAM** (bioinformatics) splits **Operation / Data / Topic / Format** at
the top level, separating what a thing *does* from what it is *about* — independent evidence that
the method-versus-subject distinction is load-bearing enough to build into an ontology — and
**MeSH** carries a dedicated "Analytical, Diagnostic and Therapeutic Techniques and Equipment"
branch alongside its disease and anatomy branches.

Two consequences, and they are the point of this section:

1. **Do not go looking for a standard to adopt.** This search has been run; the answer is that the
   concept-kind axis does not exist in a general, maintained vocabulary.
2. **Subject taxonomies answer a question this skill never asks.** CCS, CSO, and MSC tell you
   *what field a term belongs to*. A CV review needs *what kind of thing the term is*. Do not
   vendor their term lists here.

Verification caveats from that search, which must not be quietly dropped: `dl.acm.org/ccs`
returned 403, so the CCS top-level names came from Wikipedia rather than the live page;
`arxiv.org/category_taxonomy` was likewise not fetched directly, so its top-level group list is
unconfirmed; IEEE's redistribution terms sit behind an access-request form and are unknown; EDAM's
licence is inferred as CC-BY from OBO Foundry convention, not read from its LICENSE file.

## Contributor roles — CRediT

**This is the one externally standardised instrument in the file.** CRediT, the Contributor Roles
Taxonomy, is published at https://credit.niso.org/contributor-roles-defined/ and formalised as
**ANSI/NISO Z39.104-2022**. Its fourteen roles, verbatim:

Conceptualization · Data curation · Formal analysis · Funding acquisition · Investigation ·
Methodology · Project administration · Resources · Software · Supervision · Validation ·
Visualization · Writing – original draft · Writing – review & editing

Use it in step 4 as the ownership instrument. Rather than asking the vague question "is the
contribution clear", ask **which of these roles the bullet actually claims** — and whether the
CV's evidence supports that claim. This turns ownership from a matter of tone into a checkable
one, and it is the register a committee already reads in, since journals record contributions this
way.

It sharpens three specific findings:

- A bullet claiming **Conceptualization** ("proposed the approach") on work where the evidence
  supports only **Software** and **Investigation** is an ownership inflation, not a wording issue.
- A candidate whose real roles are Investigation + Formal analysis + Software has a precise,
  standard way to say so without escalating to Conceptualization. Recommend that, not a stronger verb.
- Authorship maps to roles, not to independence. A middle author with Software and Validation has
  a legible, respectable contribution; do not let a repair silently upgrade it.

Do **not** require a candidate to use CRediT vocabulary literally on the CV. It is the reviewer's
analytic frame; the repair is a concrete description of what they did.

## Research actions

Career-office action-verb lists are the only published verb evidence found, and only three were
verifiable verbatim — Yale (https://ocs.yale.edu/resources/resume-action-verbs/), MIT CAPD
(https://capd.mit.edu/resources/resume-action-verbs/), and Purdue OWL
(https://owl.purdue.edu/owl/job_search_writing/preparing_an_application/action_verbs_to_describe_skills_jobs_and_accomplishments_in_employment_documents/action_verbs_list.html).
Berkeley's list would not extract; Harvard, Northeastern, Michigan, Vitae, Oxford, and Cambridge
were not verified.

Appearing in all three research categories:

collected · diagnosed · evaluated · examined · identified · investigated · reviewed · surveyed

**These lists under-serve the CVs this skill reviews, and that is the important finding.** They
are field-generic and skew toward *investigation*. The verbs a computational or mathematical
research CV runs on — formulated, derived, proved, modeled, designed, implemented, developed,
optimized, benchmarked, validated, characterized, deployed — appear in none of the three research
categories. **No source ranks verbs as strong or weak on any stated basis.**

So do not grade a bullet by matching its verb against a list. Ask whether the verb names an action
whose object is recoverable: "optimized" is strong when what was optimized and against what
objective are present, and empty when they are not.

Ownership-weak verbs are the exception worth naming, and they have structural corroboration:
Purdue files **assisted, helped, worked** under "Helping Skills", separate from its accomplishment
categories. Add the CV-idiomatic variants: participated in · involved in · supported ·
contributed to · responsible for. Yale states the underlying principle directly — "go beyond
describing what you were responsible for and instead focus on what you have accomplished,
improved, or changed."

## Instantiating the buckets in any field

The buckets and their defining tests in `SKILL.md` are domain-free. **The term lists below are
one worked instantiation, for computational, ML, and mathematical research**, included because
that is the field this skill is most often pointed at. They are illustrative, not exhaustive, and
not a lookup table: a term absent below is not thereby generic.

For a CV in another field, instantiate the same buckets by applying the defining tests to that
field's own vocabulary. The structure holds everywhere; only the fillers change:

| Field | Problem | Method | Named specific | Evaluation | Tooling |
|---|---|---|---|---|---|
| Economics | wage effect of a policy | instrumental variables | two-stage least squares | placebo test, pre-trend check | Stata, R |
| Chemistry | reaction barrier prediction | density functional theory | B3LYP functional | benchmark against CCSD(T) | Gaussian, VASP |
| Biology | species divergence timing | phylogenetic inference | maximum-likelihood tree search | bootstrap support | RAxML, BEAST |
| Linguistics | dialect contact effects | corpus analysis | mixed-effects regression | held-out speaker validation | Praat, ELAN |
| Psychology | mediation of a treatment effect | structural equation modelling | a named fit index | preregistration, replication | Mplus, jsPsych |

Two things transfer unchanged and matter more than the fillers. **Method outranks named
specific** in every row — naming an estimator, a functional, or a package says less than naming
the approach and the reason for it. And **tooling is the lowest-weight bucket** in every row:
Stata, Gaussian, and Praat carry exactly as little as PyTorch does.

## Calibration terms — computational, ML, and mathematical research

**Research problem** — node classification · link prediction · community detection · graph
matching · subgraph isomorphism · influence maximization · graph partitioning · network alignment ·
anomaly detection · churn prediction · distribution shift · cold-start recommendation ·
multi-objective scheduling · causal effect estimation · sample-efficient control · calibration
under class imbalance

**Theory / mathematics** — graph theory · spectral graph theory · random graph models ·
percolation theory · Markov chains · algebraic connectivity · probability · stochastic processes ·
measure theory · convex optimization · information theory · statistical learning theory ·
numerical linear algebra · combinatorics · PAC-Bayes · concentration inequalities

**Method** — message passing · random walks · graph diffusion · modularity optimization ·
centrality analysis · label propagation · spectral clustering · graph coarsening · negative
sampling · neighbourhood sampling · contrastive learning · metric learning · representation
learning · self-supervised pretraining · active learning · semi-supervised learning · curriculum
learning · knowledge distillation · Bayesian optimization · variational inference · MCMC · Monte
Carlo · importance sampling · conformal prediction

**Model / algorithm** — GCN · GAT · GraphSAGE · GIN · R-GCN · heterogeneous GNN · node2vec ·
DeepWalk · PageRank · HITS · betweenness centrality · eigenvector centrality · Louvain · Leiden ·
Infomap · Dijkstra · Kernighan–Lin · transformer · VAE · diffusion model · Gaussian process · CRF ·
XGBoost · CatBoost · random forest · NSGA-II · particle swarm optimization · simulated annealing ·
ADMM · L-BFGS · beam search

**Evaluation** — ablation study · cross-validation · held-out test set · stratified split ·
temporal split · bootstrap confidence interval · significance test · error analysis · robustness
evaluation · out-of-distribution evaluation · human evaluation · AUC · F1 · precision@k · NDCG ·
calibration error · modularity · perplexity · regret

**Tooling** — PyTorch · JAX · PyTorch Geometric · DGL · NetworkX · igraph · graph-tool · SNAP ·
cuGraph · Neo4j · scikit-learn · Spark · GraphX · Docker · Kubernetes · Airflow · CUDA · MLflow ·
Weights & Biases · SLURM

**Outcome / artifact** — peer-reviewed publication · accepted paper · preprint · conference
presentation · poster · thesis · released dataset · open-source implementation · benchmark suite ·
derived bound · proved convergence · identified failure mode · deployed pipeline · runtime reduction

### Anchored versus declared

Classify a term by **where it sits** before classifying it by kind. Anchored = in a bullet that
also carries a task and a contribution. Declared = in a skills list, interests line, headline, or
course title only.

Build the bucket profile from **anchored terms only**. Anyone working in a field has that field's
vocabulary somewhere in their CV — a graph researcher will name Louvain, PageRank, and a GNN
library whatever they actually did — so presence measures familiarity, not capability. A rich
declared profile over a thin anchored one is its own finding: breadth claimed, not demonstrated.
Report declared-only terms as a separate list, and name the ones a committee would most expect to
see anchored.

### Method is not the named specific

The boundary where miscounting concentrates, in every field — see the instantiation table above
for the economics, chemistry, biology, linguistics, and psychology forms of the same confusion.
Within computational graph work it looks like this:

| Method (why) | Algorithm or measure (what) |
|---|---|
| community detection · modularity optimization | Louvain · Leiden · Infomap |
| centrality analysis | PageRank · betweenness · eigenvector centrality |
| representation learning on graphs | node2vec · DeepWalk · GraphSAGE |
| message passing | GCN · GAT · GIN · R-GCN |

A CV naming three centrality measures with no stated reason for computing any of them has
populated the **model/algorithm** bucket, not the **method** bucket. Read it that way, and say so
— the repair is to name the question the measure was computed to answer.

### Reading the buckets against each other

The distribution is the finding, not the count. Three patterns recur:

- **Tooling-only.** Every concrete noun is a library or platform; problem, theory, and method are
  empty. Reads as engineering support work, however long the list.
- **Model-only.** Named models with no method and no problem. Reads as someone who ran things
  rather than someone who chose them — a model name is only as informative as the method it
  instantiates and the task it addresses.
- **Evaluation-empty.** Problems, methods, and models present, no evaluation vocabulary anywhere.
  Reads as work never tested, and pairs with the missing-outcome finding.

## Generic terms

No institutional source publishes a weak-word list for CVs — career offices publish action-verb
lists only. Everything locatable was content-marketing material (Indeed, Novoresume, Teal), and
LinkedIn's own buzzword page could not be found, so even those claims are secondhand. Nothing
addresses the academic CV. **Therefore this section states a test, not a banned-words list**, and
no banned list should be added later on that evidence base.

The two failure modes are different and take different repairs:

**Imprecise category label** — a real thing named at too coarse a level: model · algorithm ·
system · solution · optimization · data analysis · machine learning · AI · pipeline · framework.
Repair by substitution, **and only where the supplied materials already support the precise
term**. Where they do not, the finding is *missing evidence*, not *weak wording* — never introduce
terminology the candidate has not shown.

| Generic | Precise, when evidenced |
|---|---|
| machine-learning model | gradient-boosted decision tree; heterogeneous GNN |
| graph algorithm | Louvain modularity optimization |
| optimization algorithms | NSGA-II, PSO, and simulated annealing |
| deep-learning model | graph attention network |
| data preprocessing | construction of a heterogeneous graph from transaction records |
| improved performance | +3.1 F1 over the tuned baseline on held-out data |
| large dataset | 4.2M nodes, 18M edges |
| statistical analysis | mixed-effects regression with bootstrap CIs |

**Unsupported self-assessment** — a claim about the candidate that carries no evidence:
innovative · advanced · state-of-the-art · cutting-edge · novel · passionate · results-driven ·
detail-oriented · various · several. These have no precise replacement; the repair is deletion,
or replacement of the adjective with the result that would justify it. Note that the published
(non-institutional) buzzword lists target *this* category almost exclusively, which is why they do
not cover the imprecise-category-label case that matters more on a research CV.
