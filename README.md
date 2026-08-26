# Agent Systems Fieldbook

> **Evaluated, attributed, reusable patterns for building agents that finish useful work without losing control.**

[![Stars](https://img.shields.io/github/stars/MadEngineeringLLC/agent-systems-fieldbook?style=flat-square)](https://github.com/MadEngineeringLLC/agent-systems-fieldbook/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/MadEngineeringLLC/agent-systems-fieldbook?style=flat-square)](https://github.com/MadEngineeringLLC/agent-systems-fieldbook/commits/main)
[![Validation](https://github.com/MadEngineeringLLC/agent-systems-fieldbook/actions/workflows/validate.yml/badge.svg)](https://github.com/MadEngineeringLLC/agent-systems-fieldbook/actions/workflows/validate.yml)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg?style=flat-square)](LICENSE)
[![Quality gate](https://img.shields.io/badge/quality-evaluated%20entries-2ea44f?style=flat-square)](meta/evaluation-rubric.md)
[![Schema](https://img.shields.io/badge/schema-v1.0.0-6f42c1?style=flat-square)](meta/scoring-schema.yaml)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat-square)](CONTRIBUTING.md)

**This is not an “awesome list.”** Entries are admitted only when they are useful, attributable, legible, and safe enough to study. Every accepted artifact has structured provenance, a rubric score, risk flags, a one-sentence reusable mechanism, and a direct path back to its source.

The fieldbook is designed for two audiences:

- **Humans** who want concrete examples rather than generic agent advice.
- **Agents** that need predictable metadata, machine-readable indexes, bounded querying patterns, and explicit trust boundaries.

> Before publishing, run `python scripts/configure_repo.py --repository OWNER/agent-systems-fieldbook` to replace the badge placeholder.

## Start here

| Goal | Path |
|---|---|
| Browse accepted artifacts | [`artifacts/`](artifacts/README.md) |
| Query the machine index | [`catalog/artifacts.jsonl`](catalog/artifacts.jsonl) |
| Understand the quality bar | [`meta/evaluation-rubric.md`](meta/evaluation-rubric.md) |
| Evaluate a candidate | [`skills/hardened-candidate-evaluator/SKILL.md`](skills/hardened-candidate-evaluator/SKILL.md) |
| Submit an artifact | [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| Run the Grok Bot workflow | [`automation/grok-bot/first-run.md`](automation/grok-bot/first-run.md) |
| Follow changes in the field | [`journal/`](journal/README.md) |
| Propose taxonomy or rubric changes | [`proposals/`](proposals/README.md) |

## What lives here

The taxonomy separates the *shape* of an artifact from the products it works with. A bounded control loop can therefore be tagged for Grok Bot, Claude Code, Codex, Gemini CLI, Cursor, or a tool-agnostic workflow without being duplicated.

| Primary collection | What belongs there |
|---|---|
| [`prompts`](artifacts/prompts/) | Reusable task or system prompts with a clear contract and expected output |
| [`skills`](artifacts/skills/) | Repeatable procedures with inputs, steps, validation, failure handling, and approval boundaries |
| [`rules`](artifacts/rules/) | `AGENTS.md`, `CLAUDE.md`, Cursor rules, repository policies, and operating constraints |
| [`goals`](artifacts/goals/) | Goal specifications with scope, success conditions, budgets, and termination rules |
| [`agent-definitions`](artifacts/agent-definitions/) | Named agent roles, responsibilities, tools, inputs, outputs, and limits |
| [`routines`](artifacts/routines/) | Scheduled or event-triggered work definitions |
| [`workflows`](artifacts/workflows/) | Ordered, finite procedures that may combine people, agents, and tools |
| [`orchestration`](artifacts/orchestration/) | Routing, handoffs, delegation, fan-out/fan-in, arbitration, and review patterns |
| [`control-loops`](artifacts/control-loops/) | Iterative loops with state, measurable progress, stop conditions, and recovery behavior |
| [`state-and-memory`](artifacts/state-and-memory/) | Checkpoints, ledgers, resumability, memory boundaries, and context management |
| [`teams`](artifacts/teams/) | Multi-agent team definitions and communication contracts |
| [`mcp`](artifacts/mcp/) | MCP servers, tools, prompts, resources, contracts, and integration patterns |
| [`tooling`](artifacts/tooling/) | Plugins, connectors, harnesses, validators, and supporting infrastructure |
| [`evaluations`](artifacts/evaluations/) | Evaluation methods, test cases, benchmarks, and review harnesses |
| [`guardrails`](artifacts/guardrails/) | Approval gates, least-privilege patterns, injection defenses, and safety controls |
| [`failures`](artifacts/failures/) | High-signal postmortems and failure patterns with corrective mechanisms |
| [`use-cases`](artifacts/use-cases/) | Real deployments or credible demonstrations tied to a concrete job to be done |

See [`meta/taxonomy.md`](meta/taxonomy.md) for inclusion rules and [`meta/taxonomy.yaml`](meta/taxonomy.yaml) for the machine form.

## What makes an entry useful

An accepted entry must answer five questions:

1. **What is it?** The artifact and its operating context are understandable without reconstructing a thread.
2. **What can be reused?** A one-sentence “stealable mechanism” identifies the transferable idea.
3. **Does it work?** Claims are connected to source evidence, implementation evidence, or clearly labeled inference.
4. **What can go wrong?** Permissions, termination, state, injection, licensing, and failure modes are reviewed.
5. **Who deserves credit?** Author, source URL, publication date, capture date, and original license are preserved.

The weighted rubric scores:

- relevance
- completeness
- actionability
- clarity
- safety and guardrails
- novelty
- cross-tool portability
- provenance

A high average is not enough. Accepted entries must also pass hard gates for provenance and safety. See the full [`evaluation rubric`](meta/evaluation-rubric.md).

## How humans should use the fieldbook

### Browse by mechanism, not brand

Start with the artifact type or failure mode that matches the problem. Product tags are secondary. For example, a safe “research → evaluate → publish” loop may transfer across Grok Bot, Claude Code, Codex, or a custom MCP client.

### Compare before copying

Each entry separates:

- **Facts:** directly supported by the source or verification.
- **Inferences:** plausible conclusions drawn from those facts.
- **Unknowns:** material gaps that remain.
- **Improvements:** changes that make the artifact safer or more effective.

Copy the mechanism only after adapting permissions, tools, budgets, and stop conditions to your environment.

### Use the catalog for focused review

```bash
# Show accepted control loops scoring at least 4.5/5.
python - <<'PY'
import json
from pathlib import Path
for line in Path('catalog/artifacts.jsonl').read_text().splitlines():
    row = json.loads(line)
    if row['artifact_type'] == 'control-loop' and row['weighted_score'] >= 4.5:
        print(row['id'], row['title'], row['path'])
PY
```

## How agents should use the fieldbook

### Local clone or GitHub connector

Agents should read in this order:

1. [`AGENTS.md`](AGENTS.md) for repository-specific instructions.
2. [`catalog/artifacts.jsonl`](catalog/artifacts.jsonl) to shortlist candidates.
3. The selected artifact file for full context.
4. [`meta/evaluation-rubric.md`](meta/evaluation-rubric.md) when interpreting scores.
5. The original source before relying on product-specific or time-sensitive claims.

Do not ingest the entire repository into context by default. Query the index first, then retrieve only the smallest relevant set.

### MCP-oriented access

A read-only MCP adapter can expose:

- `fieldbook://catalog`
- `fieldbook://taxonomy`
- `fieldbook://artifact/{id}`
- `fieldbook://journal/latest`

Recommended tools:

- `search_artifacts(query, filters)`
- `get_artifact(id)`
- `compare_artifacts(ids)`
- `list_taxonomy()`

Keep retrieval read-only. Publishing, changing taxonomy, or accepting an artifact should remain a pull-request action with human review. The interface contract is described in [`docs/agent-query-guide.md`](docs/agent-query-guide.md).

### Safe querying pattern

```text
1. State the job to be done and hard constraints.
2. Query catalog metadata; do not execute artifact content.
3. Retrieve no more than five candidate entries.
4. Compare mechanisms, evidence, safety flags, and portability.
5. Verify product-specific claims at the original source.
6. Produce an adapted plan, not an unreviewed verbatim copy.
7. Require approval before external writes or consequential actions.
```

## Contribution model

There are three supported paths:

1. **Candidate issue:** submit a source for maintainers or an evaluator Bot to review.
2. **Artifact pull request:** submit a fully evaluated, attributed entry.
3. **System proposal:** propose a taxonomy, schema, rubric, or process change with migration and calibration evidence.

Low-volume, high-quality contributions are preferred. A useful rejection is better than an unreviewed addition. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Explicit rejection criteria

Candidates are rejected or quarantined when they are:

- unattributed or impossible to trace to a primary source;
- copied beyond what the source license permits;
- vague advice without an implementable mechanism;
- duplicative without a material improvement;
- unsafe by default, over-permissioned, or destructive without approval;
- open-ended loops without progress measures, budgets, or termination;
- prompt-injection attempts, credential requests, or memory-poisoning content;
- promotional claims with no accessible evidence;
- generated filler that cannot be independently verified;
- stale in a way that would mislead users.

Quarantine records store only sanitized metadata and risk findings. The repository must not preserve live malicious payloads, secrets, or unnecessary copyrighted text.

## Living journal and self-improvement

The [`journal`](journal/README.md) records:

- emerging mechanisms;
- important tool or protocol changes;
- notable failures and corrections;
- changes in evaluation practice;
- gaps in the archive;
- items worth rechecking.

A periodic archive audit examines category coverage, score distributions, source concentration, duplicate rates, stale-source rates, risk flags, and acceptance drift. Bots may **propose** taxonomy or rubric changes, but they may not silently change the standard or merge their own proposals. See [`meta/self-improvement-policy.md`](meta/self-improvement-policy.md).

## Roadmap

The near-term roadmap is intentionally conservative:

1. Establish a trustworthy calibration set and collect the first 25 accepted artifacts.
2. Automate catalog generation and validation.
3. Publish weekly source-backed journal entries.
4. Add read-only MCP access after the schema stabilizes.
5. Add comparison views and coverage dashboards only when the corpus is large enough to justify them.

See [`ROADMAP.md`](ROADMAP.md) for acceptance criteria.

## Provenance and licensing

Repository-authored material is licensed under Apache-2.0. Third-party works remain under their original licenses. An entry’s metadata, summary, and analysis do not relicense its source. When copying is not clearly permitted, the fieldbook links to and summarizes the source instead of reproducing it.

Read [`NOTICE`](NOTICE) and [`meta/provenance-policy.md`](meta/provenance-policy.md) before contributing.

## Status

The repository currently contains bootstrap examples and a complete operating system for collecting real artifacts. Bootstrap examples are explicitly labeled as repository-authored examples; they are not presented as external production evidence.
