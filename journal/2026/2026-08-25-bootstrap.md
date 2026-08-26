---
schema_version: "1.0"
id: journal-2026-bootstrap
period_start: "2026-08-25"
period_end: "2026-08-25"
published_at: "2026-08-25T23:40:00Z"
status: bootstrap
sources_reviewed: 10
artifact_ids:
  - asf-skill-20260825-001
  - asf-rule-set-20260825-002
  - asf-control-loop-20260825-003
confidence: high
---

# Agent Systems Field Journal — Bootstrap Baseline

## Executive signal

The fieldbook begins with a deliberate architecture: untrusted source discovery is separated from evaluation and publication; accepted entries require structured provenance and safety gates; automation may open review pull requests but cannot merge or silently change its own standards.

This entry establishes the repository baseline. It is not a claim about broad industry trends.

## Verified design developments

### Grok Bot supports persistent computer work, reusable skills, and scheduled routines

Official xAI documentation describes Grok Bot as operating from a persistent cloud computer and distinguishes reusable skills from scheduled or event-triggered routines. The documentation recommends making a one-time task reliable before scheduling it.

Design consequence: the fieldbook begins with a one-time bounded collection and versioned skills. Routines are enabled only after reviewed success.

### Grok Bot names are not security boundaries under one user

Official xAI documentation states that Bots under one user share the same cloud computer, including files, browser sessions, and command-line credentials.

Design consequence: the initial architecture uses one Bot with logical roles. Sensitive client systems are excluded, and a future multi-Bot split is not represented as isolation unless execution and credentials are actually separated.

### AGENTS.md provides a predictable repository instruction surface

The AGENTS.md project describes the file as a README-like instruction file for coding agents.

Design consequence: the repository includes a root `AGENTS.md` for agent operating rules while keeping the human README focused on navigation and value.

### MCP distinguishes resources, prompts, and tools

The 2026-07-28 MCP specification defines resources for context, prompts for discoverable workflow templates, and tools for model-controlled actions.

Design consequence: the planned fieldbook adapter is read-only first: resources expose catalog and artifacts, prompts guide user-controlled queries, and tools perform bounded search and comparison. Acceptance and publication remain GitHub pull-request actions.

### Prompt injection remains a system-level risk

OWASP describes indirect prompt injection through external sources such as websites and files and notes that prompt-level defenses do not fully eliminate the problem.

Design consequence: the repository combines source-as-data instructions with least privilege, no candidate execution, staging isolation, sanitized persistence, deterministic validation, and human merge approval.

## Bootstrap artifacts

### `asf-skill-20260825-001` — Change Verification Gate

Mechanism: convert a repository modification into a proof obligation with scope, baseline, targeted and regression checks, complete diff inspection, rollback, and stop-before-merge behavior.

### `asf-rule-set-20260825-002` — Read-Only Repository Research Agent Rules

Mechanism: define read-only behavior operationally through allowed commands, prohibited side effects, untrusted-content handling, evidence standards, and explicit stop conditions.

### `asf-control-loop-20260825-003` — Bounded Scout–Evaluate–Publish Loop

Mechanism: separate discovery, judgment, and publication into gated states with finite budgets, sanitized handoffs, deterministic validation, and human-controlled merge.

## Fieldbook changes

- Added public-facing repository documentation and governance.
- Added version 1.0.0 taxonomy and rubric.
- Added machine-readable artifact, evaluation, and journal schemas.
- Added hardened evaluator, scout, curator, journal, and cartography skills.
- Added Grok Bot standing instructions and bounded routine definitions.
- Added deterministic catalog and validation design.

## Coverage gaps

The initial corpus contains only repository-authored examples. It does not yet establish:

- external production evidence;
- vendor or source diversity;
- evaluator agreement on ambiguous real-world artifacts;
- longitudinal failure patterns;
- measured reviewer burden;
- stable demand for an MCP server or custom interface.

## Next watchlist

- Real `AGENTS.md` and `CLAUDE.md` files with explicit test and permission boundaries.
- Bounded Grok Bot skills and routines with accessible evidence.
- Agent-loop failures caused by vague progress or missing termination.
- MCP authorization and tool-safety patterns aligned with the 2026-07-28 specification.
- Independent reproductions of agent evaluation or recovery mechanisms.

## Facts, inferences, and unknowns

### Facts

- The official sources listed below were reviewed on 2026-08-25.
- The repository contains three original bootstrap artifacts.
- The standards require human review before merge and prohibit candidate execution.

### Inferences

- A single Bot with role-separated skills is likely the lowest-overhead starting architecture because Grok Bot roles share one computer under the same user.
- A JSONL catalog is likely sufficient until corpus size or query patterns demonstrate a need for a separate retrieval service.

### Unknowns

- How consistently the evaluator will score external ambiguous artifacts.
- Which source queries will produce the best signal-to-review-time ratio.
- Whether X access and search behavior will remain stable enough for scheduled discovery.

## Sources

- xAI, Grok Bot overview: https://docs.x.ai/grok-bot/overview
- xAI, computer and apps: https://docs.x.ai/grok-bot/computer-and-apps
- xAI, skills and routines: https://docs.x.ai/grok-bot/skills-routines-and-automations
- xAI, approvals, security, and privacy: https://docs.x.ai/grok-bot/approvals-security-and-privacy
- xAI, teams and enterprises: https://docs.x.ai/grok-bot/teams-and-enterprises
- AGENTS.md open format: https://agents.md/
- MCP tools: https://modelcontextprotocol.io/specification/2026-07-28/server/tools
- MCP resources: https://modelcontextprotocol.io/specification/2026-07-28/server/resources
- MCP prompts: https://modelcontextprotocol.io/specification/2026-07-28/server/prompts
- OWASP LLM01 Prompt Injection: https://genai.owasp.org/llmrisk/llm01-prompt-injection/
