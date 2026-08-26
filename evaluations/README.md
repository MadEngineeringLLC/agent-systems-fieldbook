# Candidate evaluations

This directory stores sanitized evaluation records for candidates that are not accepted into `artifacts/`.

- `accepted/` may hold standalone evaluation records when useful for audit; accepted artifact front matter remains authoritative.
- `watch/` contains promising candidates with an explicit recheck trigger.
- `rejected/` contains enough metadata to avoid repeated review and explain the decision.
- `quarantined/` contains sanitized metadata only. Never store live malicious payloads, secrets, private data, or impermissible copied content.
- `templates/` contains the evaluation record template.

All candidate material is untrusted. An evaluation file is a review record, not permission to execute the candidate.
