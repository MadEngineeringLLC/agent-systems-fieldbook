# Taxonomy

**Taxonomy version:** 1.0.0
**Machine form:** [`taxonomy.yaml`](taxonomy.yaml)

## Design rules

- Classify by the artifact’s **primary operating function**, not its filename or vendor.
- Assign exactly one primary artifact type.
- Use secondary tags for products, domains, mechanisms, risks, evidence, and lifecycle stage.
- Prefer an existing category unless the candidate cannot be retrieved accurately under it.
- Do not create a category to accommodate one artifact.
- Product names are tags, not top-level folders.

## Primary artifact types

### `prompt`

A reusable message or instruction set that defines a task, role, decision process, or output contract.

Use when the main value is the wording and structure of the model instruction. A prompt that specifies a repeatable operational procedure with validation and approvals may fit better as a `skill`.

Folder: `artifacts/prompts/`

### `skill`

A reusable procedure with trigger conditions, required inputs or access, ordered steps, validation, failure handling, expected output, and approval boundaries.

Folder: `artifacts/skills/`

### `rule-set`

Repository or environment instructions such as `AGENTS.md`, `CLAUDE.md`, Cursor rules, policy files, or persistent operating constraints.

Folder: `artifacts/rules/`

### `goal`

A goal specification that defines outcome, scope, success criteria, constraints, budgets, and termination.

Folder: `artifacts/goals/`

### `agent-definition`

A named agent role with responsibility, authority, inputs, tools, outputs, escalation, and limits.

Folder: `artifacts/agent-definitions/`

### `routine`

A scheduled or event-triggered invocation of a bounded workflow or skill.

Folder: `artifacts/routines/`

### `workflow`

A finite ordered process combining model reasoning, tools, systems, or human actions.

Folder: `artifacts/workflows/`

### `orchestration-pattern`

A coordination mechanism such as routing, delegation, fan-out/fan-in, review, debate, arbitration, or handoff.

Folder: `artifacts/orchestration/`

### `control-loop`

An iterative mechanism that observes state, selects an action, measures progress, updates state, and terminates under explicit conditions.

Folder: `artifacts/control-loops/`

### `state-memory-pattern`

A mechanism for checkpoints, ledgers, session state, durable memory, context compression, resumability, provenance, or state isolation.

Folder: `artifacts/state-and-memory/`

### `multi-agent-team`

A coordinated set of agent roles with communication contracts, task boundaries, and an integration or decision mechanism.

Folder: `artifacts/teams/`

### `mcp-artifact`

An MCP server, tool, resource, prompt, contract, authorization pattern, or integration design whose primary value depends on MCP.

Folder: `artifacts/mcp/`

### `tooling`

A plugin, connector, harness, validator, browser automation, code-generation utility, or supporting infrastructure component.

Folder: `artifacts/tooling/`

### `evaluation`

A benchmark, test harness, rubric, review pattern, adversarial test, or evaluation workflow.

Folder: `artifacts/evaluations/`

### `guardrail`

A safety control such as approval gating, least privilege, output validation, injection containment, sandboxing, or audit evidence.

Folder: `artifacts/guardrails/`

### `failure-analysis`

A postmortem or failure pattern with evidence, root cause, impact, and corrective mechanism.

Folder: `artifacts/failures/`

### `use-case`

A concrete, evidence-backed application of an agent system to a job to be done. The mechanism and operating context must be clearer than a product testimonial.

Folder: `artifacts/use-cases/`

## Secondary tag namespaces

Tags use lowercase kebab case. Prefer namespaced tags where ambiguity is likely.

### Product

Examples:

- `product:grok-bot`
- `product:claude-code`
- `product:codex`
- `product:gemini-cli`
- `product:cursor`
- `product:mcp`
- `product:tool-agnostic`

### Mechanism

Examples:

- `mechanism:read-evaluate-write`
- `mechanism:fan-out-fan-in`
- `mechanism:critic-gate`
- `mechanism:checkpoint-resume`
- `mechanism:bounded-loop`
- `mechanism:human-approval`
- `mechanism:structured-output`

### Lifecycle

- `lifecycle:design`
- `lifecycle:build`
- `lifecycle:test`
- `lifecycle:deploy`
- `lifecycle:operate`
- `lifecycle:incident`

### Domain

Examples:

- `domain:software-engineering`
- `domain:research`
- `domain:security`
- `domain:knowledge-management`
- `domain:operations`

### Evidence

- `evidence:conceptual`
- `evidence:demonstrated`
- `evidence:reproduced`
- `evidence:production-reported`
- `evidence:production-verified`

### Risk

Risk tags mirror the evaluator’s risk flags, prefixed with `risk:` only when useful for browsing. The structured `evaluation.risk_flags` remains authoritative.

## Product and source registries

Product and source labels may evolve faster than primary artifact types. Add a product tag when:

- the product is materially involved in the artifact;
- its behavior changes implementation or risk;
- the tag will improve retrieval.

Do not tag every product merely mentioned by an author.

## New-category test

A new primary category requires a proposal showing:

1. at least five existing or imminent artifacts that are consistently misclassified;
2. a distinct retrieval question the category answers;
3. a definition with positive and negative examples;
4. migration effects on existing entries;
5. no simpler solution through tags or a secondary field;
6. calibration showing reviewers can apply it consistently.

## Deprecation and merges

Categories are deprecated, never silently repurposed. A migration records:

- old and new identifiers;
- affected artifact IDs;
- catalog migration logic;
- compatibility window;
- rationale and proposal link.
