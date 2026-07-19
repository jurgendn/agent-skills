# Design Philosophy

This repository is shaped by a few practical ideas rather than by one grand
theory. The goal is to make agent help more auditable: each skill should have a
clear trigger, a clear non-goal, and an output the user can inspect.

## Core Principles

**Narrow roles beat universal assistants.** Research work mixes teaching,
brainstorming, verification, review, writing, and implementation. Those are
different jobs, so the skills separate them instead of asking one assistant persona
to do everything at once.

**Cognitive and metacognitive layers are separate.** The skills split into two
families. The cognitive family (`professor-mentor-technical-teaching`,
`theory-proof-sketcher`, `theory-paper-to-theorem-distiller`) builds domain
competence; its relevant literature includes worked examples and heuristics. The
metacognitive family (`knowledge-debt-audit`, `naive-student`, the comprehension
gates) audits whether the user's monitoring of their own understanding is
calibrated, using metacognition in Flavell's sense [1]. The distinction has a
design consequence: audit probes interrupting a teaching flow can erode the
worked-example benefit, since self-explanation prompts carry a real opportunity
cost for novices [2]. A gate should therefore fire one sharp probe on the
load-bearing step, then teaching resumes.

**Understanding must be demonstrated.** The repo treats fluent explanation as weak
evidence for two documented reasons. Self-rated understanding is systematically
inflated until the person is forced to generate a step-by-step causal explanation,
at which point ratings collapse: the illusion of explanatory depth [3]. Processing
fluency can also masquerade as knowledge: re-reading and recognition feel like
understanding, but retrieval without the source present is a stronger discriminator
[4]. Self-report cannot gate anything by itself, because people missing a skill may
also lack the metacognition to notice [5]. Stronger checks therefore ask the user
to derive, predict, construct a counterexample, teach back, or solve a graded
exercise without looking at the answer. Where a probe elicits confidence alongside
the answer, confident-wrong is treated as more toxic than hesitant-wrong, following
certainty-based marking [6].

**Probes ask for inferences, not paraphrase.** Learners who benefit from worked
examples spontaneously generate self-explanations: inferences connecting steps that
the text left implicit. Weaker learners often say "makes sense" and move on [7].
This yields the repo's probe taxonomy: justification ("why does step N follow from
step N-1?"), anticipation ("without looking, what must the next step accomplish?"),
and violation ("if assumption A is dropped, which step fails first?"). The grading
rule follows directly: paraphrase is not understanding. A passing answer must add
an inference not present in the source.

Two calibrations matter. First, prompted self-explanation has evidence across
domains, including biology [8], probability, geometry tutoring, and programming,
with positive meta-analytic support [9], but targeted prompts beat generic ones.
No skill should issue a vague instruction like "explain your understanding of X."
Second, the effect is most relevant where material has causal or logical dependency
structure: proofs, derivations, mechanisms, and code. It is weaker for arbitrary
facts, so probes should fire only on dependency-structured content. One caveat:
most of this evidence concerns learners acquiring new material. Using the same
probes to audit whether an expert internalized AI-assisted work is an extrapolation.
The mechanism plausibly transfers, but no cited study tests that exact case.

**Wrong answers should diagnose which wrong model.** In exercise generation,
multiple-choice distractors should come from known misconceptions rather than
random perturbations, following the Force Concept Inventory design [10]. A wrong
choice then identifies which wrong mental model the learner holds, not merely that
one exists. A second archetype pairs this with an attractive intuitive-but-wrong
answer that only yields to deliberate verification, after the Cognitive Reflection
Test [11]. This directly probes whether the user accepts the fluent answer without
checking.

**Learning needs retrieval and spacing.** Practice testing and distributed practice
have broad support across materials and settings [12]. Retrieval combined with
spacing is a practical learning core [13]. In this repo, that becomes a simple
rule: important errors, proofs, and concepts should return later under changed
cues, not only be reviewed immediately. The 1-week -> 1-month -> 3-month rhythm
used by some skills is an operational heuristic, not a universal optimal interval.

**Variation matters.** Reusing the same prompt can test recognition rather than
ownership [4]. Variable-cue re-probes ask for transfer, boundary cases,
perturbations, or the load-bearing reason so the user has to regenerate the
dependency in a fresh form.

**Productive failure is useful when bounded.** For theorem-heavy learning,
attempting a proof or counterexample before reading the canonical solution can
improve conceptual understanding and transfer in scoped mathematics settings [14].
The repo uses this as a bounded protocol: try first, record the failure point, then
compare with the source.

**Interleaving is selective.** Interleaving helps most when the learner must
discriminate between similar tools or cases [12]. The skills should not randomize
everything; they should interleave concepts that are genuinely confusable.

**AI output creates knowledge debt.** If the user builds on an AI-produced result
they cannot regenerate, the work may be finished but the reasoning is borrowed.
`knowledge-debt-audit`, `naive-student`, and spaced re-probes exist to surface that
borrowed dependency before it becomes load-bearing. The audit's reactive mode is
the illusion-of-explanatory-depth procedure made operational [3]: elicit a
self-rating, force generative explanation of the load-bearing step, then re-rate.
The gap between ratings is the debt signal.

**Teaching an honest novice repays debt, but only if the novice pushes back.**
Explaining a result to a naive student is grounded in the protégé effect:
learners expend more effort, and learn more, when the goal is to teach an agent
than to learn for themselves, an effect most pronounced for lower-achieving
learners [25]. But the benefit is not automatic. Tutors default to a
*knowledge-telling bias* — summarizing the source with little elaboration — and
reflective knowledge-building is elicited specifically when the tutee asks
questions that require an inferential answer [26]. Merely explaining to a passive
fictitious student can even underperform plain self-explanation [27]. This shapes
`naive-student`'s design: the novice must be confused in a way that forces
elaboration, and its confusion must be *earned from the actual explanation*
rather than scripted. A canned "I don't get it" is knowledge-telling bait; an
inference-demanding question is what turns teaching into learning. The skill is
therefore the repayment counterpart to `knowledge-debt-audit`'s detection.

**A collaborator helps by co-constructing, not by solving.** `whiteboard-peer`
co-solves the unfinished middle rather than handing over an answer, following the
ICAP ordering: Interactive (co-generative) engagement tends to beat Constructive,
which beats Active, which beats Passive [28]. But the collaborative advantage is
fragile and conditional. In peer-tutoring data, "constructive" tutor dialog was
associated with *lower* learning when it reinforced wrong solutions or gave away
answers, while facilitative dialog helped [29]; and meta-analytically,
collaborative problem solving's effect on cognitive skills is real but only
upper-middle, moderated by group size and scaffolding [30]. Hence the skill's hard
constraint: commit real partial attempts and genuine disagreement, but *never take
over the full solution*. A peer that solves it for you converts an Interactive
exchange into passive receipt and can actively depress learning. This is the same
productive-failure discipline [14] enacted in dialogue: the struggle has to stay
the user's.

**Writing advice is mostly untested craft.** The writing skills, especially
`paper-writer`, distill canonical expert advice such as Halmos [15] and Krantz
[16], but treat that advice as expert testimony rather than settled evidence. Where
writing folklore has been tested, the results are mixed: large-scale abstract
analysis found that shorter abstracts predicted fewer citations, while shorter
sentences helped specifically in mathematics and physics [17]; readability appears
to be declining over time [18]; and title-length effects are contested [19], [20].
Every writing rule should therefore carry an epistemic flag such as expert,
supported, contested, or refuted. The same anti-hallucinated-consensus discipline
used by the literature skills applies to the writing-advice literature itself.

**Writing that follows a train of thought hides its dependencies.** A draft written
in the order ideas occurred often carries connective reasoning that stayed in the
author's head, plus claims that outrun their support: dropped hypotheses, quantifier
inflation, or correlation stated as cause. Draft audits should make this checkable:
classify claims by support status, validate paragraph flow as an argument, and
report broken inferences separately from cosmetic gaps by quoting the exact
sentence.

**Auditing an argument means checking the link, not the conclusion.** The
`argument-audit` skill reconstructs an argument into claim, stated support, and
unstated warrant, then interrogates the inference itself — a true conclusion can
rest on a broken argument. This is the critical-questions method from
argumentation theory: each argumentation scheme carries a fixed set of questions
that attack a premise, attack the conclusion on external grounds, or attack the
premise-to-conclusion step [21], [22], and reconstructing the structure before
attacking it is the argument-mining move [21]. The skill stays Socratic and
human-in-the-loop for an evidence-backed reason: LLMs are unreliable at this
exact task. They detect fallacy structure at near-chance accuracy [23], and
self-critique tends to degrade a model's own reasoning while a *sound external*
check improves it [24]. So the skill does not hand over a machine verdict; it
walks the user to construct the counterexample themselves. That move is also the
illusion-of-explanatory-depth procedure [3] applied to one's own argument: force
generative explanation of the load-bearing step and the gap becomes visible. The
handoff to `theorem-and-claim-audit` for a written report is the same
generation/audit split applied at the level of interaction mode — dialogue when
the user should earn the weak link, report when they want it handed over.

**Generation and audit are separate jobs.** Following the narrow-roles principle,
drafting (`paper-writer`), results prose (`results-writeup`), citation checking
(`citation-auditor`), and submission readiness (`submission-readiness-audit`) are
separate skills with explicit boundaries. A drafting skill should prepare handoff
to the relevant audit or review skill rather than silently grading its own output.

**Process rigor must not multiply artifacts.** Separating generation from audit
is about *passes*, not *files*. The workspace research pipeline
(`init-workspace`'s `_shared/agents/pipeline.md`) began as four agent files
whose stages each wrote their own output (`research.md`, `draft.md`,
`review.md`, `cited.md`); in practice this produced swarms of tiny intermediate
files the user could not track and re-read costs at every stage. It was
consolidated into one four-pass protocol (evidence → draft → review → verify)
run inside the artifact's own file — scaffolding sections (evidence table,
inline review items) live in the working file and are compressed away by the
final pass — with a size gate so small notes skip the pipeline entirely. The
durable rule: a quality process may add passes over an artifact, but its net
file output should be the artifact itself; and rigor should scale with the
stakes of the artifact, not apply uniformly to every note.

**A gap is an absence; a motivation is a consequence.** Finding a hole in the
literature and justifying work on it are different jobs, so `gap-finder` and
`gap-motivation-builder` are separate skills. The design follows the
gap-spotting vs. problematization distinction from research-methodology work:
most research questions are constructed by spotting an absence ("understudied",
"no prior work"), but absence alone is compatible with "not worth doing", and
gap-spotting tends to reproduce rather than challenge the assumptions of the
literature it extends [31]. The motivation skill therefore refuses absence as
motivation and probes a consequence chain instead — what fails today, for whom,
why the obvious extension doesn't close it, why now, and what filling it
unlocks — a structure that deliberately tracks the Heilmeier catechism's core
questions ("How is it done today, and what are the limits of current
practice?", "Who cares? If you succeed, what difference will it make?") [32].
The load-bearing probe is "why hasn't this been done?", whose three answers
route differently: trivial (not a paper), done under another name (route to
literature search), or a genuine blocker — and the blocker is what makes a
later method non-arbitrary, because the method must be an answer to it. The
skill's output is desiderata derived *before* any design exists, so that a
proposed solution is answerable to the motivation rather than retrofitted onto
it; proposing the method itself is out of scope by construction.

## References

[1] J. H. Flavell, "Metacognition and cognitive monitoring: A new area of
cognitive-developmental inquiry," *American Psychologist*, vol. 34, no. 10,
pp. 906-911, 1979. doi:
[10.1037/0003-066X.34.10.906](https://doi.org/10.1037/0003-066X.34.10.906).

[2] A. Renkl, "Learning from worked-out examples: A study on individual
differences," *Cognitive Science*, vol. 21, no. 1, pp. 1-29, 1997. doi:
[10.1207/s15516709cog2101_1](https://doi.org/10.1207/s15516709cog2101_1).

[3] L. Rozenblit and F. Keil, "The misunderstood limits of folk science: an
illusion of explanatory depth," *Cognitive Science*, vol. 26, no. 5, pp. 521-562,
2002. doi:
[10.1207/s15516709cog2605_1](https://doi.org/10.1207/s15516709cog2605_1).

[4] A. Koriat and R. A. Bjork, "Illusions of competence in monitoring one's
knowledge during study," *Journal of Experimental Psychology: Learning, Memory,
and Cognition*, vol. 31, no. 2, pp. 187-194, 2005. doi:
[10.1037/0278-7393.31.2.187](https://doi.org/10.1037/0278-7393.31.2.187).

[5] J. Kruger and D. Dunning, "Unskilled and unaware of it: How difficulties in
recognizing one's own incompetence lead to inflated self-assessments," *Journal
of Personality and Social Psychology*, vol. 77, no. 6, pp. 1121-1134, 1999. doi:
[10.1037/0022-3514.77.6.1121](https://doi.org/10.1037/0022-3514.77.6.1121).

[6] A. R. Gardner-Medwin, "Confidence assessment in the teaching of basic science,"
*Association for Learning Technology Journal*, vol. 3, no. 1, pp. 80-85, 1995.
doi: [10.1080/0968776950030113](https://doi.org/10.1080/0968776950030113).

[7] M. T. H. Chi, M. Bassok, M. W. Lewis, P. Reimann, and R. Glaser,
"Self-explanations: How students study and use examples in learning to solve
problems," *Cognitive Science*, vol. 13, no. 2, pp. 145-182, 1989. doi:
[10.1207/s15516709cog1302_1](https://doi.org/10.1207/s15516709cog1302_1).
Note: this is a small-N study; the transferable content here is the probe-design
principle, not the effect size.

[8] M. T. H. Chi, N. de Leeuw, M.-H. Chiu, and C. LaVancher, "Eliciting
self-explanations improves understanding," *Cognitive Science*, vol. 18, no. 3,
pp. 439-477, 1994. doi:
[10.1207/s15516709cog1803_3](https://doi.org/10.1207/s15516709cog1803_3).

[9] K. Bisra, Q. Liu, J. C. Nesbit, F. Salimi, and P. H. Winne, "Inducing
self-explanation: A meta-analysis," *Educational Psychology Review*, vol. 30,
pp. 703-725, 2018. doi:
[10.1007/s10648-018-9434-x](https://doi.org/10.1007/s10648-018-9434-x).

[10] D. Hestenes, M. Wells, and G. Swackhamer, "Force Concept Inventory," *The
Physics Teacher*, vol. 30, no. 3, pp. 141-158, 1992. doi:
[10.1119/1.2343497](https://doi.org/10.1119/1.2343497).

[11] S. Frederick, "Cognitive reflection and decision making," *Journal of Economic
Perspectives*, vol. 19, no. 4, pp. 25-42, 2005. doi:
[10.1257/089533005775196732](https://doi.org/10.1257/089533005775196732).

[12] J. Dunlosky, K. A. Rawson, E. J. Marsh, M. J. Nathan, and D. T. Willingham,
"Improving Students' Learning With Effective Learning Techniques: Promising
Directions From Cognitive and Educational Psychology," *Psychological Science in
the Public Interest*, vol. 14, no. 1, pp. 4-58, 2013. doi:
[10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266).

[13] S. K. Carpenter, S. C. Pan, and A. C. Butler, "The Science of Effective
Learning With Spacing and Retrieval Practice," *Nature Reviews Psychology*,
vol. 1, pp. 496-511, 2022. doi:
[10.1038/s44159-022-00089-1](https://doi.org/10.1038/s44159-022-00089-1).

[14] M. Kapur, "Productive Failure in Learning Math," *Cognitive Science*, vol. 38,
no. 5, pp. 1008-1022, 2014. doi:
[10.1111/cogs.12107](https://doi.org/10.1111/cogs.12107).

[15] P. R. Halmos, "How to Write Mathematics," *L'Enseignement Mathematique*,
vol. 16, pp. 123-152, 1970. doi:
[10.5169/seals-43857](https://doi.org/10.5169/seals-43857).

[16] S. G. Krantz, "How to Write Your First Paper," *Notices of the AMS*,
vol. 54, no. 11, pp. 1507-1511, 2007.

[17] C. J. Weinberger, J. A. Evans, and S. Allesina, "Ten Simple (Empirical) Rules
for Writing Science," *PLOS Computational Biology*, vol. 11, no. 4, e1004205,
2015. doi:
[10.1371/journal.pcbi.1004205](https://doi.org/10.1371/journal.pcbi.1004205).

[18] P. Plaven-Sigray, G. J. Matheson, B. C. Schiffler, and W. H. Thompson, "The
readability of scientific texts is decreasing over time," *eLife*, vol. 6,
e27725, 2017. doi:
[10.7554/eLife.27725](https://doi.org/10.7554/eLife.27725).

[19] A. Letchford, H. S. Moat, and T. Preis, "The advantage of short paper titles,"
*Royal Society Open Science*, vol. 2, no. 8, 150266, 2015. doi:
[10.1098/rsos.150266](https://doi.org/10.1098/rsos.150266).

[20] F. Didegah and M. Thelwall, "Which factors help authors produce the highest
impact research? Collaboration, journal and document properties," *Journal of
Informetrics*, vol. 7, no. 4, pp. 861-873, 2013. doi:
[10.1016/j.joi.2013.08.006](https://doi.org/10.1016/j.joi.2013.08.006).

[21] J. Lawrence and C. Reed, "Argument Mining: A Survey," *Computational
Linguistics*, vol. 45, no. 4, pp. 765-818, 2020. doi:
[10.1162/coli_a_00364](https://doi.org/10.1162/coli_a_00364).

[22] D. Walton, C. Reed, and F. Macagno, *Argumentation Schemes*. Cambridge:
Cambridge University Press, 2008. doi:
[10.1017/CBO9780511802034](https://doi.org/10.1017/CBO9780511802034).

[23] I. Robbani, T. Hirst, et al., "Flee the Flaw: Annotating the Underlying
Logic of Fallacious Arguments Through Templates and Slot-filling," 2024. Preprint.
Note: reports state-of-the-art language models detecting fallacy templates at
~0.47 accuracy; cited for the limitation, not a settled effect size.

[24] K. Stechly, K. Valmeekam, and S. Kambhampati, "On the Self-Verification
Limitations of Large Language Models on Reasoning and Planning Tasks,"
arXiv:2402.08115, 2024. doi:
[10.48550/arXiv.2402.08115](https://doi.org/10.48550/arXiv.2402.08115).

[25] C. C. Chase, D. B. Chin, M. A. Oppezzo, and D. L. Schwartz, "Teachable
Agents and the Protégé Effect: Increasing the Effort Towards Learning," *Journal
of Science Education and Technology*, vol. 18, no. 4, pp. 334-352, 2009. doi:
[10.1007/s10956-009-9180-4](https://doi.org/10.1007/s10956-009-9180-4).

[26] R. D. Roscoe and M. T. H. Chi, "Tutor learning: the role of explaining and
responding to questions," *Instructional Science*, vol. 36, no. 4, pp. 321-350,
2008. doi:
[10.1007/s11251-007-9034-5](https://doi.org/10.1007/s11251-007-9034-5).

[27] Z. Pi et al., "Is self-explanation better than explaining to a fictitious
student when learning from video lectures?" *British Journal of Educational
Technology*, vol. 53, no. 6, 2022. Note: cited as a boundary condition (passive
fictitious-audience explanation underperformed self-explanation); exact DOI not
verified here.

[28] M. T. H. Chi and R. Wylie, "The ICAP Framework: Linking Cognitive Engagement
to Active Learning Outcomes," *Educational Psychologist*, vol. 49, no. 4,
pp. 219-243, 2014. doi:
[10.1080/00461520.2014.965823](https://doi.org/10.1080/00461520.2014.965823).

[29] C. Borchers et al., "Combining Dialog Acts and Skill Modeling: What Chat
Interactions Enhance Learning Rates During AI-Supported Peer Tutoring?" 2024.
Preprint. Note: reports that give-away or incorrect-reinforcing "constructive"
tutor dialog correlated with lower tutee learning; cited for the limitation, not a
settled effect size.

[30] E. Xu, W. Wang, and Q. Wang, "The effectiveness of collaborative problem
solving in promoting students' critical thinking: A meta-analysis based on
empirical literature," *Humanities and Social Sciences Communications*, vol. 10,
art. 16, 2023. doi:
[10.1057/s41599-023-01508-1](https://doi.org/10.1057/s41599-023-01508-1).

[31] J. Sandberg and M. Alvesson, "Ways of constructing research questions:
gap-spotting or problematization?" *Organization*, vol. 18, no. 1, pp. 23-44,
2011. doi:
[10.1177/1350508410372151](https://doi.org/10.1177/1350508410372151). See also
M. Alvesson and J. Sandberg, "Generating research questions through
problematization," *Academy of Management Review*, vol. 36, no. 2, pp. 247-271,
2011. doi: [10.5465/amr.2009.0188](https://doi.org/10.5465/amr.2009.0188).

[32] G. H. Heilmeier, "The Heilmeier Catechism," DARPA.
[https://www.darpa.mil/about/heilmeier-catechism](https://www.darpa.mil/about/heilmeier-catechism).
Attributed to Heilmeier's tenure as DARPA director (1975-1977); cited as the
canonical question set for motivating proposed research, not as an empirical
study.
