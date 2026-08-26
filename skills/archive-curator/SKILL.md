---
name: archive-curator
version: 1.0.0
status: active
owner: Agent Systems Fieldbook maintainers
license: Apache-2.0
---

# Archive Curator

## When to use

Use only after the Hardened Candidate Evaluator returns `decision.disposition: accept` and every hard gate is true.

## Inputs

- complete evaluation record;
- minimum safe source material needed for an original summary;
- current taxonomy and schema;
- current catalog;
- designated repository and allowed paths.

## Access

Write access to a non-protected review branch in this repository. Pull-request creation may be permitted. No merge, administration, secrets, Actions settings, webhooks, organization, or unrelated repository access.

## Procedure

1. Reconfirm the evaluation is internally consistent and no critical risk is unresolved.
2. Recheck duplicate status against the latest catalog.
3. Write one artifact file under the proposed taxonomy folder.
4. Preserve exact source, author, date, immutable reference, license, and transformation metadata.
5. Use original language. Do not copy substantial source content.
6. Include mechanism, context, adaptation, safety, failures, improvements, attribution, facts, inferences, and unknowns.
7. Recalculate weighted score from integer dimensions.
8. Run catalog generation, schema validation, internal-link checks, tests, and `git diff --check`.
9. Inspect every changed file and confirm no file outside the approved scope changed.
10. Create `bot/ingest/YYYY-MM-DD-<batch>` and open or update a pull request.
11. Stop before merge.

## Failure handling

- If source attribution changed or became unavailable, stop and return to evaluation.
- If rights are unclear, convert to summary-only or stop.
- If validation fails, do not push; report exact output.
- If the catalog changed unexpectedly, inspect the source artifacts and regenerate.
- If a branch conflict occurs, update safely and rerun all checks; do not force-push without explicit approval.

## Required output

- artifact IDs and paths;
- source and rights treatment;
- exact files changed;
- exact validation commands and results;
- facts, inferences, unknowns, and residual risks;
- branch and pull-request status;
- explicit statement that merge was not performed.

## Approval boundary

Opening a review pull request is the maximum external write. Human approval and protected-branch rules control merge.
