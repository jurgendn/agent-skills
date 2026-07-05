# Mixed-methods integration (qual + quant in a pilot)

Many pilots are implicitly mixed-methods: a metric (quantitative) plus interviews,
adoption signals, or human feedback (qualitative). Teams from technical backgrounds
usually run the two strands side by side and then staple the findings together — which
wastes the main advantage of mixing. This reference is for designing the qual/quant
combination *intentionally*, so the integration produces an insight neither strand
could alone.

Source: Storey, Hoda, Milani, Baldassarre, *Guiding Principles for Mixed Methods
Research in Software Engineering*, Empirical Software Engineering (2025),
arXiv:2404.06011. Written for SE research; applies directly to industry pilots that
pair metrics with human/qualitative evidence.

## When mixing is worth it — four guiding principles

Two answer *why* mix; two govern *how*:

1. **Methodological rationale.** Be able to state *why* this pilot needs both strands.
   Legitimate reasons: **complementarity** (one deepens the other), **development**
   (one builds the instrument for the other — e.g. interviews shape the survey),
   **triangulation** (corroborate a finding via a different method), **expansion**
   (ask different questions), **explanation** (resolve a surprising/contradictory
   quantitative result), **credibility**. If you can't name the reason, you probably
   don't need both — say so.
2. **Novel integrated insights.** The pilot must deliver something beyond what a single
   method would (a **meta-inference**), and the report must say what integration
   bought. "We ran a survey and also some interviews" is not integration.
3. **Procedural rigor.** Each strand is run to its own standard *and* the mixing itself
   is rigorous (how and when the strands connect).
4. **Ethical research.** Especially with real users/employees: confidentiality, consent
   and opt-out, and framing qualitative findings so individuals can't be identified or
   evaluated from them (acute when telemetry could be traced to a person).

## Design types (pick one deliberately)

- **Exploratory sequential** (quaL → quaN): interviews/observation first to discover
  what matters, then a metric/survey to test whether it generalizes. Use when you
  don't yet know the right thing to measure.
- **Explanatory sequential** (quaN → quaL): metric/backtest first, then interviews to
  *explain* a surprising result. The classic "the number moved and we don't know why"
  follow-up.
- **Convergent parallel** (quaL ∥ quaN): both at once, then compare — look for where
  they converge *and* where they diverge (divergence is a finding, not a failure).
- **Embedded**: one strand nested inside a primarily-other-strand design (e.g. a lab
  experiment on speed with short between-task questions on user confidence). The
  secondary strand exists to capture something the dominant strand can't see.

## Types of integration

- **Sequential** — findings from one strand shape the instrument/sampling of the next.
- **Results-based** — combine/compare findings only after both analyses are done.
- **Data-based** — analyze both data types together, tied to the same cases.
The integration step is what makes it mixed-methods; plan it *before* running, and
report it explicitly in the results, not as an afterthought.

## Antipatterns to avoid

- **Cargo-cult method.** Bolting on a method the team lacks expertise in because it
  looked impressive in a cited paper. Bring in a collaborator with that expertise or
  drop the method.
- **Sample contamination.** Reusing the same participants across sequential strands
  without accounting for the earlier one influencing the later (e.g. interviewing
  people, then surveying the same people). If contamination is intentional (as in an
  embedded design), justify and report it.
- **Lost opportunity.** Failing to feed the first strand's findings into the design of
  the second (e.g. not using interview insights to write better survey questions).
  Catch this during execution — it can't be fixed in the write-up.
- **Integration failure.** Running both strands but never actually merging the
  findings — reporting two disconnected mini-studies. Plan where and how results
  combine, and integrate them in the findings.
- **Questionable ethics.** Even a well-run design can have questionable aims or means;
  state the motivation and expected benefit, and treat participants as real people.

## Practical takeaways for the pilot design

- A clear pilot decision/question that *aligns* with the mixed design; the methods
  must actually answer it.
- Use each strand's limitations to justify the other, but also report the limitations
  and threats introduced by *mixing*.
- Say up front whether the pilot is inductive (discovering) or deductive (testing) —
  it drives which design type fits and how the integrated findings are framed.
