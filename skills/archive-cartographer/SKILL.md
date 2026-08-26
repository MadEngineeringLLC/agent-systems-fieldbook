---
name: archive-cartographer
version: 1.0.0
status: active
owner: Agent Systems Fieldbook maintainers
license: Apache-2.0
---

# Archive Cartographer

## When to use

Use monthly or after each additional 50 accepted artifacts to audit organization, coverage, scoring, and evaluator drift.

## Inputs

- generated catalog;
- evaluation records by disposition;
- journal index;
- source registry;
- calibration set;
- current taxonomy, rubric, schemas, and automation versions.

## Metrics

Calculate:

- counts by primary type, product, domain, source class, author or organization, and evidence level;
- score distribution by dimension and category;
- acceptance/watch/reject/quarantine rate;
- duplicate and repeated-review rate;
- source and vendor concentration;
- stale-source and broken-link rate;
- risk-flag frequency;
- evaluator disagreement and calibration drift;
- categories with low coverage, high ambiguity, or excessive breadth;
- journal observations not connected to accepted artifacts.

## Procedure

1. Rebuild the catalog from source artifacts.
2. Validate data quality before interpreting metrics.
3. Report material findings with counts and denominators.
4. Distinguish corpus facts from hypotheses about the broader field.
5. Identify the smallest high-value search or system improvement.
6. Draft a proposal only when evidence meets `meta/self-improvement-policy.md`.
7. Include migration, calibration, risk, and rollback analysis.
8. Never apply or merge the proposal.

## Output

- answer-first audit summary;
- metrics and data-quality caveats;
- undercovered mechanisms and overrepresented sources;
- scoring or taxonomy anomalies;
- recommended search slices;
- zero or more proposal files;
- exact validation results;
- explicit list of standards not changed.
