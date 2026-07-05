# Cross-community writing norms (for resubmission reframing)

When a paper moves to a different community — the core reason for most resubmissions —
what actually changes is not the results but the *writing norms*. Reviewers judge a
paper partly against the tacit conventions of their community, and a paper that reads
as an outsider's gets discounted even when the science is sound.

Source: Bhatt, August, Antoniak, *Research Borderlands: Analysing Writing Across
Research Cultures* (2025), arXiv:2506.00784. They interviewed interdisciplinary
researchers (experts at exactly this move) and derived a framework of norms that vary
across research cultures, then measured them at scale across 11 CS communities.
Two findings drive this reference:

1. When researchers adapt a paper for a new community, they **nearly always rewrite
   the introduction** — it is the section carrying the framing, and framing is what
   varies most. Prioritize the intro when reframing.
2. General-purpose LLMs, asked to adapt writing across communities, **homogenize** it
   — they move length, readability, table/figure mentions, and quantitative-evidence
   density all in one direction regardless of the target. So an LLM "reframe for venue
   X" pass is unreliable; use the checklist below to steer deliberately, and treat any
   LLM draft as needing a human community-fit pass.

## The four axes that vary across communities

### Structural
- **Length.** Page limits encode a norm (e.g. ~8–9 pages at NLP venues vs ~14 at
  FAccT). Moving to a longer-limit community isn't just "add pages" — verbosity and
  depth expectations rise with the space.
- **Artifacts (tables vs figures).** Communities differ in what they'd rather look at.
  Vision leans on figures; NLP uses more tables; a healthcare venue may prefer one
  over the other for the same result. Match the artifact type to the target.

### Stylistic
- **Jargon / specialized vocabulary.** The single most community-specific signal.
  Terms one community takes as given ("RoBERTa", "the preponderance of work") must be
  defined — or dropped — for another. Watch for "red-flag" words: a term that reads as
  neutral in one field marks you as an outsider (or worse) in another.
- **Readability, formality, verbosity.** Sentence length and prose "quality"
  expectations differ (a humanities audience tolerates — even expects — longer,
  more discursive framing; a two-column ML venue punishes it visually).

### Rhetorical
- **Quantitative-evidence density.** ML/NLP/AI communities expect numbers everywhere
  and treat them as *the* contribution signal; other communities weight qualitative
  evidence, examples, and argument. Adjust how much numerical scaffolding the intro
  carries.
- **Figurative language / storytelling.** Some communities open with a lyrical or
  narrative hook; others want the claim stated plainly and early.
- **Framing.** The overwhelming consensus lever (9/10 interviewees): the *same result*
  is foregrounded differently per community — what's "the icing on the cake" vs the
  core value shifts with the community's priorities. Reframing is not spin; it is
  re-selecting which true aspect of the contribution leads.
- **Narrative organization.** Where contributions, methods, and results appear in the
  intro varies. ML/NLP/AI tend to state objectives and even results early and follow a
  formulaic background→data→methods→results "recipe"; other fields ramp up more slowly.

### Citational
- **Canonicity.** The same concept has a different canonical citation in each
  community (e.g. "mental models" in cog-sci ↔ "folk theories" in HCI). Citing the
  target community's foundational works signals membership; citing the source
  community's can read as not having done the reading.
- **Engagement style.** Direct quotation of cited work is common in the humanities,
  rare on the computational side.

## Resubmission reframing checklist

When redirecting a paper to a different community, walk these in order (intro first):

1. **Reframe the intro** around the target community's priorities — lead with the
   aspect of the contribution *they* value; demote what the previous community valued.
2. **Retune jargon**: define/replace source-community terms; adopt the target's
   shared vocabulary; scan for red-flag words.
3. **Recalibrate quantitative-evidence density** up or down to the target's norm.
4. **Swap canonical citations** to the target community's foundational works; add the
   ones they'd expect to see engaged.
5. **Adjust structure**: length, and whether the key result is a table or a figure.
6. **Match narrative organization**: how early to state objectives/results, how
   formulaic the section order should be.

A resubmission that only fixes the reviewers' technical objections but keeps the
original community's framing tends to fail again for "fit" reasons that no reviewer
states outright.
