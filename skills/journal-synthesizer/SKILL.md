---
name: journal-synthesizer
version: 1.0.0
status: active
owner: Agent Systems Fieldbook maintainers
license: Apache-2.0
---

# Journal Synthesizer

## When to use

Use after a defined weekly period or meaningful event batch to draft the Agent Systems Field Journal.

## Inputs

- accepted artifact IDs and evaluations from the period;
- primary-source product or protocol updates;
- watch, reject, and quarantine counts and sanitized reasons;
- repository changes;
- prior journal entry;
- current coverage metrics.

## Procedure

1. Define period start and end in absolute dates.
2. Verify event dates separately from publication dates.
3. Group evidence into verified developments, emerging mechanisms, failures and corrections, fieldbook changes, and gaps.
4. Require at least two independent observations before calling something a trend, unless a primary specification change directly establishes it.
5. Link claims to accepted artifact IDs or primary sources.
6. Separate facts, inferences, and unknowns.
7. Keep rejected and quarantined content sanitized.
8. Validate front matter against `schemas/journal.schema.json`.
9. Update `journal/index.jsonl` deterministically.
10. Open a review pull request and stop before merge.

## Quality rules

- No generic AI news roundup.
- No trend from engagement alone.
- No copied posts or release-note prose.
- No hidden promotional relationships.
- Correct prior claims visibly when new evidence contradicts them.
- Empty categories may be omitted; do not manufacture observations.

## Output

A concise weekly entry using `journal/templates/weekly.md`, plus source list, confidence, files changed, validation results, and unresolved questions.
