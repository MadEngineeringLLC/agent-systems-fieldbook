# Governance

## Project model

The Agent Systems Fieldbook uses maintainer stewardship with public, reviewable decision records. The project optimizes for trust and long-term usefulness, not contribution throughput.

## Roles

### Contributors

Contributors may submit candidates, artifacts, corrections, evaluations, tooling, journal evidence, and system proposals.

### Reviewers

Reviewers assess provenance, licensing, technical quality, safety, duplication, and taxonomy fit. A reviewer should not approve an entry they authored without an independent review when another reviewer is available.

### Maintainers

Maintainers may merge changes, release versions, manage repository settings, appoint reviewers, and enforce project policies. Maintainers are responsible for protecting the quality gate from social pressure, automation drift, and promotional capture.

### Automated contributors

Bots may scout, normalize metadata, run evaluations, build catalogs, draft journal entries, and open pull requests. Bots are contributors, not maintainers. They may not merge, change governance, or silently modify the rubric or taxonomy.

## Decision classes

### Routine decisions

Artifact acceptance, typo fixes, source corrections, and non-breaking tooling changes use normal pull-request review.

### System decisions

Changes to taxonomy, scoring weights, admission thresholds, schemas, license policy, governance, or automation permissions require:

1. a proposal under `proposals/`;
2. evidence of the current problem;
3. impact and migration analysis;
4. calibration against known cases;
5. a public review period appropriate to the change;
6. explicit maintainer approval.

### Emergency decisions

A maintainer may temporarily disable workflows, remove exposed secrets, or quarantine malicious material without waiting for normal review. The action should be documented after the immediate risk is contained.

## Conflicts of interest

Contributors and reviewers must disclose material relationships to products, repositories, or authors being evaluated. A disclosed conflict does not automatically disqualify participation, but an independent reviewer should make the final acceptance decision.

## Appeals

A rejected contribution may be resubmitted with new evidence, corrected attribution, a safer adaptation, or a clearer mechanism. Popularity or contributor status is not grounds for an exception.

## Versioned standards

The evaluator, rubric, taxonomy, schemas, and automation prompts carry explicit versions. Historical decisions should remain interpretable under the version used at the time. Breaking changes require a migration plan.

## Maintainer succession

Maintainers should document ownership, release access, security-reporting access, and automation credentials so the project can continue without a single point of failure. Credentials must not be stored in the repository.
