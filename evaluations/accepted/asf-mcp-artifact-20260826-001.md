---
evaluation_schema: asf-evaluation/v1
evaluator_version: 1.0.0
rubric_version: 1.0.0
evaluated_at: "2026-08-26T08:20:00Z"
candidate:
  candidate_id: "asf-mcp-artifact-20260826-001"
  title: "MCP 2026-07-28 untrusted tool annotations and explicit handles"
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
      - "https://modelcontextprotocol.io/specification/2026-07-28"
      - "https://github.com/modelcontextprotocol/modelcontextprotocol/commit/b488c16623e5202a3961e551886044577ae0f096"
      - "https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/LICENSE"
  rights_treatment: "summary-only"
  content_fingerprint: null
classification:
  primary_type: "mcp-artifact"
  secondary_types:
    - "guardrail"
    - "state-memory-pattern"
  products:
    - "mcp"
  tags:
    - "product:mcp"
    - "mechanism:human-approval"
    - "lifecycle:design"
    - "domain:security"
    - "evidence:conceptual"
  evidence_level: "conceptual"
  duplicate_status: "new"
scores:
  relevance: 5
  completeness: 5
  actionability: 4
  clarity: 4
  safety_guardrails: 4
  novelty: 4
  cross_tool_portability: 5
  provenance: 4
weighted_score: 4.38
gates:
  provenance_complete: true
  safety_minimum_met: true
  rights_clear: true
  not_duplicate: true
  no_unresolved_critical_risk: true
  facts_inferences_unknowns_separated: true
risks:
  - flag: "unsafe-default"
    severity: "high"
    evidence: "Human-in-the-loop confirmation is SHOULD, not MUST. The protocol cannot enforce host consent."
    effect: "A host can auto-invoke tools while remaining spec-compatible."
    remediation: "Hosts should require deny-capable confirmation for untrusted servers and treat annotations as untrusted."
  - flag: "secret-or-credential-exposure"
    severity: "high"
    evidence: "Spec warns not to mark passwords, API keys, tokens, or PII with x-mcp-header because headers are visible to intermediaries."
    effect: "A server that annotates a secret parameter can leak it through proxies and logs."
    remediation: "Reject tool definitions that map sensitive properties to headers; never place secrets in x-mcp-header."
  - flag: "prompt-injection"
    severity: "high"
    evidence: "Clients MUST treat tool annotations as untrusted unless they come from a trusted server. Tool results are passed to the model."
    effect: "A malicious server can over-claim safety in annotations or inject instructions through tool output."
    remediation: "Ignore untrusted annotations for authorization decisions; validate and sanitize results before model consumption."
  - flag: "ambiguous-state"
    severity: "moderate"
    evidence: "Handles are ordinary strings. Unauthenticated servers must treat them as bearer tokens with entropy and lifetime."
    effect: "Guessable handles become confused-deputy accessors if authorization is not re-checked."
    remediation: "Bind handles to the verified caller on every call; expire them; never equate possession with authentication."
decision:
  disposition: "accept"
  rationale: "The 2026-07-28 tools specification states a complete, portable contract: untrusted annotations, input/output validation, human deny capability, and explicit handles instead of hidden sessions. Hard gates pass. License for new specification contributions is declared Apache-2.0 in the repository LICENSE; archive treatment remains summary-only. Prompt-injection and header-leak risks are identified in the spec with remediations, so they are not unresolved critical flags."
  confidence: "high"
  recheck_trigger: "A later spec revision changes annotation trust, handle authorization, or the Apache-2.0/MIT relicensing status of this page."
stealable_mechanism: "Treat MCP tool annotations as untrusted unless the server is trusted, require a human deny path, validate tool I/O, and replace hidden sessions with caller-bound explicit handles."
improvements:
  - "Raise human confirmation from SHOULD to a host profile that is MUST for untrusted servers."
  - "Add a normative prohibition on using annotations as authorization input."
  - "Specify handle entropy, lifetime, and caller-binding as MUST for authenticated servers, not guidance."
  - "Add a test vector for a tool whose annotations claim read-only while the call writes."
  - "Record SPDX on the tools page itself to end mixed-license ambiguity."
verification:
  facts:
    - "The tools page at https://modelcontextprotocol.io/specification/2026-07-28/server/tools was available at capture 2026-08-26T08:00:00Z."
    - "GitHub commit 0cb6c6a31768cbb16129b35e6b569a31fecfe1b6 on 2026-07-28T16:11:22Z touches docs/specification/2026-07-28/server/tools.mdx."
    - "Commit b488c16623e5202a3961e551886044577ae0f096 on 2026-07-28T15:56:05Z is titled 'Add 2026-07-28 MCP specification'."
    - "Repository LICENSE states new specification contributions are Apache-2.0, with unrelicensed MIT remaining and non-spec documentation under CC-BY-4.0."
    - "Clients MUST consider tool annotations untrusted unless from a trusted server."
    - "Servers MUST validate tool inputs, implement access controls, rate limit, and sanitize outputs."
    - "Stateful-tools guidance says MCP has no protocol-level session and that handles must not be treated as capabilities for authenticated servers."
  inferences:
    - "The 2026-07-28 tools page is a new specification contribution and therefore intended to fall under Apache-2.0, based on the LICENSE transition paragraph."
    - "Hosts that skip confirmation remain spec-legal, based on SHOULD rather than MUST for human-in-the-loop."
  unknowns:
    - "Per-file SPDX header on tools.mdx was not fetched."
    - "Which hosts currently enforce annotation distrust in production."
archive_target: "artifacts/mcp/mcp-2026-07-28-untrusted-tool-annotations-and-handles.md"
rubric_change_proposal: null
---

# Evaluation: MCP 2026-07-28 untrusted tool annotations and explicit handles

## Executive assessment

Accept at weighted score 4.38, summary-only. Strongest value is the combination of untrusted tool metadata, required I/O validation, and explicit handles after sessions were removed. Principal residual risk is that human confirmation is recommended rather than required.

## Stealable mechanism

Treat MCP tool annotations as untrusted unless the server is trusted, require a human deny path, validate tool I/O, and replace hidden sessions with caller-bound explicit handles.

## Mechanism and context

Inputs are tool definitions, call arguments, and caller credentials. Transformation lists tools deterministically, invokes `tools/call`, and optionally returns a handle that later calls must present. State lives in server-side handle maps, not transport sessions. Outputs are structured or unstructured results, errors, or an input-required pause. Intended environment is any MCP host and server on protocol 2026-07-28. Boundary: the protocol states requirements; host UIs and server authorization still have to implement them.

## Evidence

Signals: dated specification, GitHub commits on 2026-07-28, and a repository LICENSE covering new specification contributions. Evidence level conceptual. SDKs are claimed updated in the project blog; those binaries were not executed. Not a catalog duplicate: none of the three bootstrap artifacts is an MCP tool-trust contract.

## Safety review

Annotation distrust and input validation are MUST. Human-in-the-loop is SHOULD. Header mirroring can leak secrets if misused; the spec warns. Handles must be re-authorized per caller. Prompt-injection via annotations is named and mitigated by distrust. No unresolved critical flag because the dangerous cases are specified with required or documented controls; remaining gaps are host-implementation defaults.

## Improvements

Make untrusted-server confirmation mandatory in a host profile, forbid annotations as authorization, and add handle-binding MUSTs plus an adversarial test vector.

## Attribution

Title: Tools (MCP specification 2026-07-28). Author: Model Context Protocol. Canonical URL: https://modelcontextprotocol.io/specification/2026-07-28/server/tools. Published: 2026-07-28. Capture: 2026-08-26T08:00:00Z. Immutable reference: commit 0cb6c6a31768cbb16129b35e6b569a31fecfe1b6. License: Apache-2.0 declared for new specification contributions. Rights treatment: summary-only. Availability: available.

## Facts, inferences, and unknowns

### Facts

- Dated spec page, commits, annotation distrust MUST, server validation MUST, and LICENSE transition text as fetched.

### Inferences

- This page is intended to be Apache-2.0 as a new specification contribution.
- Hosts can omit confirmation and still claim protocol compatibility.

### Unknowns

- Per-file SPDX and production host enforcement.

## Archive action

Curator may draft `artifacts/mcp/mcp-2026-07-28-untrusted-tool-annotations-and-handles.md` as a summary-only entry. Acceptance permits only a reviewable draft. It does not authorize merge, verbatim copying of the specification, or execution of candidate code.
