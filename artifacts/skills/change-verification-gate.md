---
schema_version: "1.0"
id: asf-skill-20260825-001
title: Change Verification Gate
slug: change-verification-gate
artifact_type: skill
status: accepted
version: "1.0.0"
summary: >-
  A repository-change procedure that requires a scoped baseline, small edits,
  deterministic checks, complete diff inspection, explicit rollback, and an
  evidence-based completion report before any merge decision.
stealable_mechanism: >-
  Convert “make the change” into a proof obligation: constrain scope, capture a baseline, run targeted and regression checks, inspect the full diff, and stop before merge.
created_at: "2026-08-25"
updated_at: "2026-08-25"
last_verified_at: "2026-08-25"
authors:
  - name: Agent Systems Fieldbook maintainers
    handle: null
    url: null
source:
  type: original
  title: Change Verification Gate
  url: "repo://artifacts/skills/change-verification-gate.md"
  author: Agent Systems Fieldbook maintainers
  handle: null
  published_at: "2026-08-25"
  captured_at: "2026-08-25T23:00:00Z"
  availability: available
  repository: agent-systems-fieldbook
  path: artifacts/skills/change-verification-gate.md
  commit_sha: null
  alternate_urls: []
license:
  spdx: Apache-2.0
  status: verified
  url: "repo://LICENSE"
  notes: Repository-authored bootstrap example.
provenance:
  transformation: original
  source_preserved: true
  credit_preserved: true
  permission_basis: Apache-2.0 repository license
  content_fingerprint: null
products:
  - tool-agnostic
tags:
  - mechanism:verification-gate
  - mechanism:human-approval
  - lifecycle:test
  - domain:software-engineering
  - evidence:demonstrated
related_artifacts:
  - asf-control-loop-20260825-003
supersedes: []
superseded_by: null
evidence:
  level: demonstrated
  signals:
    - The repository includes deterministic catalog, schema, link, and unit-test commands that instantiate the gate.
    - The procedure defines observable completion evidence and a stop-before-merge boundary.
  limitations:
    - This bootstrap example does not claim external production use.
    - Targeted tests and rollback commands must be adapted to the repository under review.
evaluation:
  rubric_version: "1.0.0"
  evaluator_version: "1.0.0"
  evaluated_at: "2026-08-25T23:05:00Z"
  scores:
    relevance: 5
    completeness: 5
    actionability: 5
    clarity: 5
    safety_guardrails: 5
    novelty: 3
    cross_tool_portability: 5
    provenance: 5
  weighted_score: 4.84
  risk_flags: []
  disposition: accept
  confidence: high
---

# Change Verification Gate

## What it is

A skill for any coding or repository agent that converts a requested modification into a bounded, testable proof obligation. The agent is not finished when the file changes; it is finished when the intended behavior is demonstrated, unintended changes are ruled out to a stated degree, and the review boundary is respected.

## When to use

Use after an agent is authorized to modify a repository, especially when:

- the request spans more than one file;
- the change can alter behavior, data, permissions, or public interfaces;
- a previous attempt failed or produced uncertain results;
- the repository will be reviewed by another person or agent;
- “done” could otherwise be judged subjectively.

Do not use this skill as authorization to make the change. Scope and write permission must already be explicit.

## Required inputs

```yaml
request:
  desired_outcome: "observable result"
  allowed_paths: []
  prohibited_paths: []
  acceptance_tests: []
  regression_checks: []
  approval_boundary: "stop before merge"
repository:
  base_revision: "commit SHA or working-tree baseline"
  test_commands: []
  rollback_method: "revert, restore, or branch deletion"
```

## Procedure

### 1. Restate the proof obligation

Before editing, state:

- the observable outcome;
- allowed and prohibited paths;
- assumptions;
- tests that would prove success;
- checks that would reveal likely regressions;
- actions that remain human-controlled.

Stop when the outcome or authority is materially ambiguous.

### 2. Capture a baseline

Record:

```bash
git status --short
git rev-parse HEAD
git diff --stat
git diff --check
```

Run the narrow existing test that best represents the behavior before modification when practical. If the baseline already fails, record it and do not attribute that failure to the new change.

### 3. Make the smallest coherent change

- Modify only allowed paths.
- Avoid opportunistic refactors.
- Preserve unrelated working-tree changes.
- Add or update the narrowest meaningful test.
- Stop before installing new dependencies unless dependency changes were authorized.

### 4. Run layered verification

Run in this order:

1. syntax or schema validation;
2. the new or targeted behavior test;
3. the nearest relevant regression suite;
4. repository-wide checks required by policy;
5. security or permission checks when authority changed.

Capture exact commands, exit status, and material output. A passing command is evidence only for what it actually tests.

### 5. Inspect the complete change

```bash
git status --short
git diff --check
git diff --stat
git diff
```

Confirm:

- every changed file is expected;
- generated files correspond to source changes;
- no secret, credential, debug artifact, or unrelated content entered the diff;
- tests assert the intended behavior rather than only implementation details;
- comments and documentation match behavior;
- rollback remains possible.

### 6. Decide outcome

Use one of:

- `verified`: acceptance and required regression checks passed;
- `partially-verified`: the intended change appears correct, but named checks could not run;
- `not-verified`: evidence does not support completion;
- `blocked`: authority, environment, dependency, or external system prevents safe progress.

Never collapse partial verification into “done.”

### 7. Stop at the approval boundary

Prepare a reviewable branch, commit, or patch only as authorized. Do not merge, deploy, publish, delete, or alter permissions unless the task explicitly grants that action and its approval requirement is satisfied.

## Output contract

```text
Outcome: verified | partially-verified | not-verified | blocked

Facts:
- baseline revision and working-tree state
- files changed
- exact tests and checks run
- exact pass/fail results

Inferences:
- what the evidence supports beyond direct test assertions

Unknowns:
- checks not run and why
- environments or integrations not observed

Risks:
- residual failure modes

Rollback:
- exact reversible action

Approval required:
- next consequential action that remains human-controlled
```

## Failure handling

| Failure | Response |
|---|---|
| Baseline is dirty | Preserve unrelated work; isolate the authorized change or stop. |
| Baseline test already fails | Record pre-existing failure; avoid false causation. |
| Required dependency unavailable | Do not install silently; report the blocker or use an approved existing path. |
| Targeted test fails | Diagnose or revert the smallest change; do not broaden scope automatically. |
| Regression test fails | Treat as not verified until root cause is established. |
| Unexpected file changes | Stop, identify the generator or side effect, and restore unrelated files. |
| Secret-like content appears | Stop, remove it safely, and follow the security policy. |
| Merge permission exists | Permission is not approval; stop at the stated boundary. |

## Why the mechanism works

The gate separates three questions that agents often conflate:

1. Did the requested files change?
2. Does evidence show the intended behavior?
3. Is the agent authorized to make the next consequential action?

Making each question explicit prevents a plausible diff from being reported as a verified result and prevents successful tests from becoming implicit permission to merge or deploy.

## Improvements for production use

- Add repository-specific test tiers and time budgets.
- Record command output as CI artifacts for high-consequence changes.
- Require an independent reviewer for permission or security changes.
- Use ephemeral worktrees or branches to isolate agent edits.
- Add a rollback test when migrations or state changes are involved.

## Facts, inferences, and unknowns

### Facts

- This artifact is original to the Agent Systems Fieldbook.
- It defines scope, baseline, validation, diff inspection, rollback, and approval behavior.
- The repository provides deterministic commands that demonstrate the pattern.

### Inferences

- The mechanism should transfer across coding agents because it relies on repository evidence rather than model-specific behavior.

### Unknowns

- Its effect on defect rates has not been independently measured in production.
- The optimal test depth and approval model vary by repository risk.

## Attribution

- **Author:** Agent Systems Fieldbook maintainers
- **Source:** `repo://artifacts/skills/change-verification-gate.md`
- **Published:** 2026-08-25
- **License:** Apache-2.0
- **Transformation:** Original repository-authored example
