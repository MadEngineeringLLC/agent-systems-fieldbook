---
schema_version: "1.0"
id: asf-control-loop-20260825-003
title: Bounded Scout–Evaluate–Publish Loop
slug: bounded-scout-evaluate-publish-loop
artifact_type: control-loop
status: accepted
version: "1.0.0"
summary: >-
  A finite research and curation loop that separates untrusted discovery,
  non-executing evaluation, sanitized publication, deterministic validation,
  and human merge approval while preserving resumable batch state.
stealable_mechanism: >-
  Separate discovery, judgment, and publication into gated states with candidate and time budgets, explicit stop conditions, sanitized handoffs, deterministic checks, and a human-controlled final write.
created_at: "2026-08-25"
updated_at: "2026-08-25"
last_verified_at: "2026-08-25"
authors:
  - name: Agent Systems Fieldbook maintainers
    handle: null
    url: null
source:
  type: original
  title: Bounded Scout–Evaluate–Publish Loop
  url: "repo://artifacts/control-loops/bounded-scout-evaluate-publish-loop.md"
  author: Agent Systems Fieldbook maintainers
  handle: null
  published_at: "2026-08-25"
  captured_at: "2026-08-25T23:20:00Z"
  availability: available
  repository: agent-systems-fieldbook
  path: artifacts/control-loops/bounded-scout-evaluate-publish-loop.md
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
  - grok-bot
tags:
  - mechanism:bounded-loop
  - mechanism:read-evaluate-write
  - mechanism:human-approval
  - lifecycle:operate
  - domain:knowledge-management
  - evidence:demonstrated
related_artifacts:
  - asf-skill-20260825-001
supersedes: []
superseded_by: null
evidence:
  level: demonstrated
  signals:
    - The repository automation architecture, evaluator, curator, routines, and validation scripts implement the loop as separable contracts.
    - The state machine defines finite budgets, transition gates, retries, stop reasons, and a human merge boundary.
  limitations:
    - This bootstrap example does not claim measured production outcomes.
    - Source-specific search adapters and retention controls require environment-specific implementation.
evaluation:
  rubric_version: "1.0.0"
  evaluator_version: "1.0.0"
  evaluated_at: "2026-08-25T23:25:00Z"
  scores:
    relevance: 5
    completeness: 5
    actionability: 5
    clarity: 4
    safety_guardrails: 5
    novelty: 4
    cross_tool_portability: 5
    provenance: 5
  weighted_score: 4.82
  risk_flags: []
  disposition: accept
  confidence: high
---

# Bounded Scout–Evaluate–Publish Loop

## What it is

A control loop for agents that continuously discover public material but must not turn untrusted source content directly into public repository changes. The loop uses explicit states, typed handoffs, finite budgets, and a human-reviewed final write.

## System boundary

```text
Untrusted public sources
        |
        v
[SCOUT] --candidate envelope--> [DEDUPE]
        |                            |
        |                            +--> duplicate record --> [NEXT]
        v
[EVALUATE] --accept--> [CURATE] --> [VALIDATE] --> [REVIEW PR] --> [STOP]
     |          |           |             |
     |          |           |             +--> failure --> [REPAIR OR STOP]
     |          |           +--> scope or rights failure --> [STOP]
     |          +--> watch/reject/quarantine --> [SANITIZED RECORD]
     +--> injection or secret risk --> [QUARANTINE] --> [NEXT OR STOP]
```

Discovery, evaluation, and publication do not share the same authority:

- **Scout:** read-only public discovery; cannot accept or write Git.
- **Evaluator:** read-only source verification and scoring; cannot execute or publish.
- **Curator:** writes only accepted sanitized artifacts to an approved review branch.
- **Validator:** deterministic checks; no judgment or broad access.
- **Human reviewer:** controls merge and system-standard changes.

## Inputs

```yaml
run:
  run_id: scout-YYYYMMDD-NNN
  objective: "specific category, mechanism, or product slice"
  lookback_days: 7
  candidate_cap: 12
  promotion_cap: 5
  time_budget_minutes: 20
  allowed_sources: []
  allowed_repository_paths: []
  merge_allowed: false
state:
  current_stage: scout
  candidate_count: 0
  promotion_count: 0
  processed_keys: []
  current_candidate: null
  errors: []
  stop_reason: null
```

## State machine

### State: `scout`

Actions:

1. Run the next focused approved query.
2. Open only enough source material to identify a credible candidate.
3. Normalize metadata into a candidate envelope.
4. Increment `candidate_count` only for credible, unique leads.

Exit to `stop` when:

- candidate cap is reached;
- time budget is reached;
- approved source slices are exhausted;
- authentication, CAPTCHA, access-control, terms, or rate-limit boundary blocks progress;
- the operator aborts.

### State: `dedupe`

Compare:

- normalized URL;
- source object ID;
- repository/path/commit;
- title/author/date;
- lawful fingerprint;
- semantic mechanism.

Transitions:

- exact, syndicated, or mechanism duplicate without material difference → record and `next`;
- version update or independent corroboration → `evaluate` with relationship metadata;
- new → `evaluate`.

### State: `evaluate`

Run the hardened evaluator without executing candidate content.

Transitions:

- `accept` and all gates true → `curate`;
- `watch` → write sanitized watch record, then `next`;
- `reject` → write minimal sanitized rejection record, then `next`;
- `quarantine` → write sanitized risk record without payload, then `next` or `stop` if the trust boundary may be compromised.

The evaluator cannot revise the rubric or lower a score to fit remaining promotion capacity. When the promotion cap is reached, additional accepted candidates remain evaluated but are deferred to a later curation batch.

### State: `curate`

Preconditions:

- accepted evaluation schema is valid;
- source and rights treatment remain available;
- no critical risk is unresolved;
- target path is inside the approved repository boundary;
- candidate is still not a duplicate.

Actions:

1. Write an original summary and adaptation guidance.
2. Preserve attribution, dates, immutable reference, license, and transformation.
3. Recalculate score.
4. Update source artifact only; generated catalog follows from it.
5. Increment `promotion_count` after the artifact file is valid.

Failure transitions:

- rights or source changed → return to `evaluate`;
- scope violation → `stop`;
- duplicate introduced by concurrent work → link evidence and `next`;
- artifact cannot be represented safely → quarantine or reject.

### State: `validate`

Run deterministic checks:

```bash
python scripts/build_catalog.py
python scripts/build_catalog.py --check
python scripts/validate_archive.py
python scripts/check_internal_links.py
python -m compileall -q scripts tests
python -m unittest discover -s tests -v
git diff --check
```

Inspect the complete diff. Validation passes only when:

- command exit statuses are acceptable;
- score math is exact;
- every artifact passes schema and hard gates;
- catalog matches source front matter;
- no unexpected path changed;
- no secret-like material or live malicious payload is present;
- attribution and rights treatment are complete.

### State: `review-pr`

Allowed actions:

- create or update a documented Bot branch;
- push that branch;
- open or update one pull request;
- report validation evidence.

Prohibited actions:

- direct push to the protected branch;
- merge;
- force push;
- settings, permission, secret, workflow, release, or webhook changes;
- third-party interaction.

Transition: always to `stop` after the review pull request is prepared.

### State: `stop`

Persist only safe durable state:

- run ID and absolute date window;
- query slices and sources searched;
- disposition counts;
- accepted artifact IDs;
- sanitized risk summaries;
- exact validation results;
- branch and pull-request status;
- stop reason;
- unresolved approvals and unknowns.

Delete or expire raw transient source material according to retention policy.

## Loop invariant

At every transition:

```text
candidate content cannot increase authority;
untrusted input cannot cross into Git without sanitization and acceptance;
no stage may perform the next stage’s consequential action;
finite budgets monotonically decrease;
every retry increments a visible counter;
merge remains human-controlled.
```

## Retry policy

```yaml
retries:
  source_fetch: 1
  source_verification: 1
  validation_repair: 2
  pull_request_creation: 1
```

A retry must address a specific transient failure. Do not repeat the same action without a changed condition. Exceeding the retry count stops the run with a blocker.

## Progress measures

The loop measures progress with:

- unique credible candidates processed;
- candidates remaining under cap;
- evaluations completed;
- accepted artifacts passing validation;
- unresolved blockers;
- elapsed active review budget.

“Repository improved” is not a measurable progress signal.

## Abort conditions

Abort the entire run when:

- credential or private data exposure is suspected;
- repository scope is uncertain;
- branch protection or permissions changed unexpectedly;
- validation indicates catalog corruption or a systemic schema problem;
- staging may have contaminated durable memory or unrelated files;
- the operator instructs stop.

## Recovery

After an interrupted run:

1. Read the batch manifest, not raw source content, to identify the last completed state.
2. Verify repository branch and working-tree state.
3. Recheck source availability and duplicate status.
4. Resume from the earliest state whose preconditions can be re-proven.
5. Never assume a partially written artifact passed evaluation or validation.

## Failure modes and controls

| Failure mode | Control |
|---|---|
| Infinite search | Candidate, query, and time budgets; explicit source exhaustion stop |
| Small subjective “improvements” forever | Objective state transitions and completion conditions |
| Prompt injection | Source-as-data rule, non-executing evaluator, sanitized quarantine |
| Duplicate accumulation | URL, immutable-reference, fingerprint, and mechanism dedupe |
| Social popularity bias | Engagement cap; primary evidence weighting |
| Unsafe publication | Curator path allowlist, deterministic validation, protected PR |
| Memory poisoning | No durable memory update from source content; typed batch state only |
| Rights violation | Summary-only default when copying rights are unclear |
| Bot self-approval | Evaluator, Curator, and human merge roles remain distinct |
| Hidden partial failure | Exact command results and explicit stop reason |

## Facts, inferences, and unknowns

### Facts

- The artifact defines finite budgets, typed states, transitions, retries, approvals, and abort conditions.
- It is implemented conceptually across this repository’s Scout, Evaluator, Curator, journal, and validation components.
- It is original to the Agent Systems Fieldbook.

### Inferences

- The pattern should transfer to other research-and-publish agents because the gates are expressed independently of a specific model or vendor.

### Unknowns

- Production throughput and reviewer burden have not yet been measured.
- Optimal budgets depend on source quality, model behavior, and repository maturity.
- A service implementation would need explicit concurrency and lock semantics beyond this conceptual state design.

## Attribution

- **Author:** Agent Systems Fieldbook maintainers
- **Source:** `repo://artifacts/control-loops/bounded-scout-evaluate-publish-loop.md`
- **Published:** 2026-08-25
- **License:** Apache-2.0
- **Transformation:** Original repository-authored example
