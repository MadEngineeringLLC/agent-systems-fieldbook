---
evaluation_schema: asf-evaluation/v1
evaluator_version: 1.0.0
rubric_version: 1.0.0
evaluated_at: "2026-08-26T08:20:00Z"
candidate:
  candidate_id: "asf-control-loop-20260826-002"
  title: "MCP 2026-07-28 multi round-trip tool calls without a session"
  source:
    url: "https://modelcontextprotocol.io/specification/2026-07-28/server/tools"
    type: "official-docs"
    author: "Model Context Protocol"
    handle: null
    published_at: "2026-07-28"
    captured_at: "2026-08-26T08:00:00Z"
    license_spdx: "Apache-2.0"
    license_status: "declared"
    immutable_reference: "https://github.com/modelcontextprotocol/modelcontextprotocol/commit/0cb6c6a31768cbb16129b35e6b569a31fecfe1b6"
    availability: "available"
    alternate_urls:
      - "https://blog.modelcontextprotocol.io/posts/2026-07-28/"
      - "https://github.com/modelcontextprotocol/modelcontextprotocol/commit/0cb6c6a31768cbb16129b35e6b569a31fecfe1b6"
  rights_treatment: "summary-only"
  content_fingerprint: null
classification:
  primary_type: "control-loop"
  secondary_types:
    - "mcp-artifact"
    - "state-memory-pattern"
  products:
    - "mcp"
  tags:
    - "product:mcp"
    - "mechanism:bounded-loop"
    - "mechanism:human-approval"
    - "lifecycle:operate"
    - "domain:software-engineering"
    - "evidence:conceptual"
  evidence_level: "conceptual"
  duplicate_status: "new"
scores:
  relevance: 4
  completeness: 4
  actionability: 4
  clarity: 4
  safety_guardrails: 4
  novelty: 4
  cross_tool_portability: 5
  provenance: 4
weighted_score: 4.08
gates:
  provenance_complete: true
  safety_minimum_met: true
  rights_clear: true
  not_duplicate: true
  no_unresolved_critical_risk: true
  facts_inferences_unknowns_separated: true
risks:
  - flag: "ambiguous-state"
    severity: "high"
    evidence: "Retry carries server-issued requestState. The tools page does not specify integrity, binding, or replay rules for that blob."
    effect: "A client that echoes requestState blindly could replay a prior elicitation or attach another caller's state."
    remediation: "Bind requestState to the original method, tool name, caller, and a short TTL; reject mismatched retries."
  - flag: "secret-or-credential-exposure"
    severity: "high"
    evidence: "Elicitation forms can request usernames or other user input mid-call. Adjacent Grok/Claude docs warn against collecting passwords in chat; this spec example requests a GitHub username."
    effect: "Servers may use elicitation to harvest credentials if hosts render forms uncritically."
    remediation: "Hosts should classify elicitation fields, block secret-like fields, and show the requesting tool and server before accept."
  - flag: "missing-termination"
    severity: "moderate"
    evidence: "The tools page shows one retry after input_required. It does not cap how many input_required rounds a server may demand."
    effect: "A hostile server could loop elicitations."
    remediation: "Hosts should cap MRTR rounds per call and fail closed."
  - flag: "unverified-claim"
    severity: "moderate"
    evidence: "The 2026-07-28 blog describes MRTR as replacing held-open streams. SDK behavior was not executed."
    effect: "Implementations may still hold streams while advertising the new spec."
    remediation: "Verify a host/SDK against the message examples before treating the loop as production-verified."
decision:
  disposition: "accept"
  rationale: "MRTR is a distinct bounded control loop from candidate 003: complete the original tools/call by retrying with inputResponses instead of a bidirectional session. The spec gives concrete message shapes, a new JSON-RPC id on retry, and optional requestState. Hard gates pass at 4.08. Remaining risks are host caps and requestState binding, which are implementation gaps rather than unresolved critical flaws in the mechanism."
  confidence: "medium"
  recheck_trigger: "The MRTR pattern page or schema adds requestState integrity rules, a round cap, or a host profile that forbids secret elicitation."
stealable_mechanism: "Finish a tool call without a session by returning input_required plus requestState, then retrying the original call with inputResponses instead of holding a stream."
improvements:
  - "Normatively bind and expire requestState."
  - "Cap elicitation rounds per call."
  - "Forbid password, token, and payment fields in elicitation schemas."
  - "Publish a conformance test that a retry with a swapped requestState is rejected."
  - "Keep this artifact separate from the tool-annotation contract so the control loop is not lost inside a larger MCP summary."
verification:
  facts:
    - "The 2026-07-28 tools page documents InputRequiredResult, inputResponses, requestState, and a new JSON-RPC id on retry."
    - "The project blog dated 2026-07-28 describes MRTR as replacing server-initiated elicitation over a held-open stream (SEP-2322)."
    - "GitHub commit 0cb6c6a31768cbb16129b35e6b569a31fecfe1b6 includes docs/specification/2026-07-28/basic/patterns/mrtr.mdx."
    - "This is not the same mechanism as Bounded Scout–Evaluate–Publish Loop, which gates catalog publication rather than mid-tool elicitation."
  inferences:
    - "MRTR is the control-loop adaptation required by the stateless core, based on the blog's session-retirement description plus the tools-page retry examples."
    - "Without a documented round cap, hosts must supply termination themselves."
  unknowns:
    - "Integrity algorithm for requestState."
    - "Maximum intended rounds."
    - "Whether production hosts already cap elicitations."
archive_target: "artifacts/control-loops/mcp-2026-07-28-multi-round-trip-tool-calls.md"
rubric_change_proposal: null
---

# Evaluation: MCP 2026-07-28 multi round-trip tool calls without a session

## Executive assessment

Accept at weighted score 4.08, summary-only. Strongest value is a bounded retry that preserves elicitation after sessions were removed. Principal risk is underspecified requestState binding and missing round caps, which keep confidence at medium.

## Stealable mechanism

Finish a tool call without a session by returning input_required plus requestState, then retrying the original call with inputResponses instead of holding a stream.

## Mechanism and context

Inputs are the original `tools/call` plus later `inputResponses`. Transformation: server returns `resultType: input_required` with named input requests and optional `requestState`; client retries the same method and arguments with answers and a new JSON-RPC id. State is the server-side continuation referenced by requestState, not a transport session. Output is a completed tool result or another input_required. Intended environment: Streamable HTTP MCP 2026-07-28. Boundary: one logical tool call, possibly several HTTP requests; not a general agent loop.

## Evidence

Signals: specification examples and the dated release blog. Evidence level conceptual. Adjacent to candidate 003 but not a mechanism duplicate: 003 is trust metadata and handles; 004 is the elicitation retry loop. Distinct from the fieldbook's scout-evaluate-publish loop.

## Safety review

The loop is finite only if the host stops repeating input_required. Elicitation can collect user input, including identity fields. requestState is an opaque continuation. Permissions still sit on the original tool. No unresolved critical flag; high risks have host-side remediations the spec implies but does not fully nail down.

## Improvements

Bind and expire requestState, cap rounds, and block secret fields. Keep the control-loop write-up separate from the broader tools-safety artifact.

## Attribution

Title: MCP 2026-07-28 Tools / Multi Round-Trip Requests. Author: Model Context Protocol. Canonical URL: https://modelcontextprotocol.io/specification/2026-07-28/server/tools. Published: 2026-07-28. Capture: 2026-08-26T08:00:00Z. Immutable reference: commit 0cb6c6a31768cbb16129b35e6b569a31fecfe1b6. License: Apache-2.0 declared for new specification contributions. Rights treatment: summary-only. Availability: available.

## Facts, inferences, and unknowns

### Facts

- Tools page and blog document input_required retries without a session stream.
- mrtr.mdx is in commit 0cb6c6a.

### Inferences

- MRTR exists because the stateless core retired held-open server-to-client streams.
- Hosts must add round caps themselves.

### Unknowns

- requestState integrity, maximum rounds, production host behavior.

## Archive action

Curator may draft `artifacts/control-loops/mcp-2026-07-28-multi-round-trip-tool-calls.md` as summary-only. Acceptance permits a reviewable draft only. It does not authorize merge or execution.
