# Roadmap

The roadmap is gated by evidence and corpus size. Features are added when they improve retrieval or trust, not because they are fashionable.

## Phase 0 — Bootstrap

Acceptance criteria:

- repository policies, schemas, evaluator skill, validation, and PR workflow exist;
- three repository-authored calibration examples pass validation;
- the first one-time Grok Bot collection can run without external writes beyond a review branch;
- branch protection and least-privilege access are configured.

## Phase 1 — Trustworthy seed corpus

Target: 25 accepted external artifacts across at least eight primary categories.

Acceptance criteria:

- every item has primary-source provenance or an explicit limitation;
- no source or vendor accounts for more than 30% of accepted items;
- at least five rejected or watch decisions are retained as sanitized evaluation records;
- evaluator agreement is tested on the calibration set;
- the first four weekly journal entries are published.

## Phase 2 — Retrieval and comparison

Target: 75 accepted artifacts.

Candidate work:

- stable search filters over JSONL metadata;
- generated category and tag indexes;
- comparison views for similar mechanisms;
- stale-source and broken-link reporting;
- optional read-only MCP adapter.

Admission criteria for MCP work:

- artifact and evaluation schemas have remained stable for at least two minor releases;
- read-only use cases materially exceed direct GitHub querying;
- security boundaries and version compatibility are documented.

## Phase 3 — Evidence and longitudinal analysis

Target: 150 accepted artifacts with enough history for trend analysis.

Candidate work:

- evidence-level tracking;
- score-distribution and source-concentration reports;
- mechanism lineage and supersession links;
- recurring failure-pattern analysis;
- transparent rubric drift reports.

## Explicit non-goals

Until evidence changes, the project will not optimize for:

- largest artifact count;
- automatic copying of public repositories;
- unattended merges;
- ranking products by social engagement;
- training a model on unreviewed source content;
- preserving malicious prompt payloads;
- a custom web application before GitHub and generated indexes become limiting.
