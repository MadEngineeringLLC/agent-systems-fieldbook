# Self-Improvement Policy

## Objective

The fieldbook should improve its retrieval, scoring, coverage, and safety as evidence accumulates. It must not autonomously change the rules by which it judges itself.

## Permitted automated analysis

A Bot may calculate and report:

- artifact counts by primary type, product, domain, source, and evidence level;
- score distributions and dimension correlations;
- acceptance, watch, reject, and quarantine rates;
- duplicate rate and repeated-review rate;
- source and vendor concentration;
- stale-source and broken-link rates;
- unresolved risk-flag frequency;
- categories with low coverage or high reviewer disagreement;
- evaluator drift against the calibration set;
- journal topics that lack archived supporting artifacts.

## Permitted automated proposals

A Bot may open a proposal for:

- new or merged categories;
- tag normalization;
- clarification of a score definition;
- new risk flags;
- weight or threshold changes;
- schema fields;
- source filters;
- routine frequency changes;
- validation improvements.

Every proposal must include evidence, exact diffs, migration effects, calibration results, and rollback conditions.

## Prohibited autonomous changes

Bots may not, without a reviewed system proposal:

- change scoring weights or thresholds;
- alter accepted artifact scores in bulk;
- create, rename, merge, or delete primary categories;
- weaken provenance or safety gates;
- broaden repository, browser, connector, or local-computer permissions;
- change their own approval requirements;
- merge proposals or artifact pull requests;
- promote quarantined content;
- update durable operating memory from untrusted source content.

## Audit cadence

Recommended cadence:

- weekly: source coverage, duplicates, stale links, and journal gaps;
- monthly: taxonomy coverage, score distribution, risk flags, and source concentration;
- quarterly or every 50 accepted artifacts: rubric calibration, schema fitness, and governance review.

Cadence may be reduced when the corpus is small. Empty reports are not useful.

## Proposal quality gate

A self-improvement proposal must answer:

1. What repository evidence demonstrates the problem?
2. Is the problem classification, scoring, retrieval, safety, or process?
3. What is the smallest reversible change?
4. Which existing artifacts change interpretation?
5. How does the calibration set score before and after?
6. What new failure mode could the change introduce?
7. What metric determines whether to keep or roll back the change?

## Drift control

Maintain a fixed calibration set containing:

- clear accept cases;
- clear reject cases;
- critical-risk quarantine cases;
- borderline watch cases;
- duplicates;
- incomplete provenance cases.

After any evaluator or rubric change, compare disposition, dimension scores, risk flags, and rationale against expected ranges. Do not approve a change that improves one favored category while degrading safety or provenance consistency.
