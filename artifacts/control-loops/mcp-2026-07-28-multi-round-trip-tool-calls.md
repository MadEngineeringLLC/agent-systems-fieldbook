---
schema_version: "1.0"
id: asf-control-loop-20260826-002
title: MCP 2026-07-28 Multi Round-Trip Tool Calls
slug: mcp-2026-07-28-multi-round-trip-tool-calls
artifact_type: control-loop
status: accepted
version: "1.0.0"
summary: >-
  After MCP dropped protocol-level sessions, a tool call can pause with
  input_required and optional requestState, then finish by retrying the
  original call with inputResponses instead of holding a stream open.
stealable_mechanism: >-
  Finish a tool call without a session by returning input_required plus requestState, then retrying the original call with inputResponses instead of holding a stream.
created_at: "2026-08-26"
updated_at: "2026-08-26"
last_verified_at: "2026-08-26"
authors:
  - name: Model Context Protocol
    handle: null
    url: null
source:
  type: official-docs
  title: MCP 2026-07-28 Tools / Multi Round-Trip Requests
  url: "https://modelcontextprotocol.io/specification/2026-07-28/server/tools"
  author: Model Context Protocol
  handle: null
  published_at: "2026-07-28"
  captured_at: "2026-08-26T08:00:00Z"
  availability: available
  repository: modelcontextprotocol/modelcontextprotocol
  path: docs/specification/2026-07-28/basic/patterns/mrtr.mdx
  commit_sha: 0cb6c6a31768cbb16129b35e6b569a31fecfe1b6
  alternate_urls:
    - "https://blog.modelcontextprotocol.io/posts/2026-07-28/"
    - "https://github.com/modelcontextprotocol/modelcontextprotocol/commit/0cb6c6a31768cbb16129b35e6b569a31fecfe1b6"
license:
  spdx: Apache-2.0
  status: declared
  url: "https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/LICENSE"
  notes: >-
    The MCP repository LICENSE is a transition: new specification contributions
    are Apache-2.0, unrelicensed MIT remains, and non-spec documentation is
    CC-BY-4.0. This 2026-07-28 tools and MRTR material is treated as a new
    specification contribution under Apache-2.0 and is archived summary-only.
provenance:
  transformation: summary-only
  source_preserved: true
  credit_preserved: true
  permission_basis: Apache-2.0 declared for new specification contributions; archive treatment is summary-only
  content_fingerprint: null
products:
  - mcp
tags:
  - product:mcp
  - mechanism:bounded-loop
  - mechanism:human-approval
  - lifecycle:operate
  - domain:software-engineering
  - evidence:conceptual
related_artifacts:
  - asf-mcp-artifact-20260826-001
  - asf-guardrail-20260826-003
  - asf-control-loop-20260825-003
supersedes: []
superseded_by: null
evidence:
  level: conceptual
  signals:
    - The 2026-07-28 tools page documents a pause-and-retry tool call using input_required, inputResponses, and optional requestState.
    - The project blog dated 2026-07-28 describes multi round-trip requests as replacing elicitation over a held-open stream.
    - Commit 0cb6c6a31768cbb16129b35e6b569a31fecfe1b6 includes docs/specification/2026-07-28/basic/patterns/mrtr.mdx.
  limitations:
    - Host and SDK behavior was not executed.
    - requestState integrity, binding, and replay rules are not specified on the tools page.
    - No documented cap on elicitation rounds.
evaluation:
  rubric_version: "1.0.0"
  evaluator_version: "1.0.0"
  evaluated_at: "2026-08-26T08:20:00Z"
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
  risk_flags:
    - missing-termination
    - unverified-claim
    - ambiguous-state
  disposition: accept
  confidence: medium
---

# MCP 2026-07-28 Multi Round-Trip Tool Calls

## What it is

A bounded control loop for finishing one MCP `tools/call` after the protocol removed hidden sessions. If the server needs user input mid-call, it returns `input_required` plus optional `requestState`. The host collects answers and retries the original method with `inputResponses` and a new JSON-RPC id, instead of holding a bidirectional stream.

This is not a duplicate of the fieldbook's [Bounded Scout–Evaluate–Publish Loop](bounded-scout-evaluate-publish-loop.md). That loop gates catalog publication. This loop gates mid-tool elicitation for a single call.

It is also distinct from [untrusted tool annotations and handles](../mcp/mcp-2026-07-28-untrusted-tool-annotations-and-handles.md), which cover metadata trust and continuation tokens rather than the retry sequence.

## Mechanism and boundary

```text
Host: tools/call (JSON-RPC id n)
        |
        v
[SERVER WORK]
        |
        +--> complete result --> [STOP]
        |
        +--> input_required + named fields + optional requestState
                    |
                    v
             [HOST ELICITS]
                    |
                    +--> user denies or round cap --> [FAIL CLOSED]
                    |
                    +--> tools/call retry
                         same method and arguments
                         inputResponses
                         requestState echoed
                         JSON-RPC id n+1
                    |
                    v
             [SERVER WORK] --> result or another input_required
```

Loop invariant: one logical tool call; several HTTP requests; no transport session. Permissions remain those of the original tool. The host, not the server, must supply a round cap.

Related guardrails: [auth, SSRF, and handle guardrails](../guardrails/mcp-2026-07-28-auth-ssrf-handle-guardrails.md).

## Inputs

```yaml
original_call:
  method: tools/call
  name: string
  arguments: object
  jsonrpc_id: unique
pause:
  resultType: input_required
  requested_inputs: [named_fields]
  requestState: optional_opaque
retry:
  method: tools/call
  arguments: original_arguments
  inputResponses: object
  requestState: echoed_if_present
  jsonrpc_id: new_unique
host_limits:
  max_rounds: integer
  secret_fields: block
```

## Safety

- The loop is finite only if the host stops repeating `input_required`. The tools page shows one retry; it does not cap rounds.
- Bind `requestState` to the original method, tool name, caller, and a short lifetime. Reject a retry that carries another caller's blob or a stale blob. The specification leaves integrity rules to implementers.
- Classify elicitation fields before rendering them. Block password, token, and payment-like fields. Show the requesting tool and server before accept.
- Do not treat a successful elicitation as extra authorization beyond the original tool.
- SDK and blog claims that this pattern replaces held-open streams were not executed here (`unverified-claim`).

Credential harvesting through elicitation is a host-policy problem. The matching evaluation records that risk with a remediation; this accepted artifact does not leave it as an unresolved critical flag.

## Adaptation

1. Implement `tools/call` so a pause is a completed HTTP response, not an open stream.
2. Store server-side continuation under `requestState` with caller, tool, and TTL binding.
3. On retry, require the same method and arguments, a new JSON-RPC id, and a matching `requestState`.
4. Cap rounds per logical call and fail closed.
5. Keep this control loop documented separately from the broader tools-safety contract so the retry rule is not lost inside a larger summary.

The pattern transfers to any tool API that must ask the user a question without a session: return a pause token, collect answers out of band, resume the original call.

## Improvements

- Specify integrity, binding, and expiry for `requestState`.
- Cap elicitation rounds per call in the protocol or in a host profile.
- Forbid secret and payment fields in elicitation schemas.
- Publish a conformance test that a swapped `requestState` is rejected.
- Keep this artifact separate from the annotation-and-handle contract.

## Facts, inferences, and unknowns

### Facts

- The tools page and the 2026-07-28 project blog describe pause-and-retry tool calls without a session stream.
- Commit `0cb6c6a31768cbb16129b35e6b569a31fecfe1b6` includes `docs/specification/2026-07-28/basic/patterns/mrtr.mdx`.
- This mechanism is not the Bounded Scout–Evaluate–Publish Loop.
- Archive treatment is summary-only original prose.

### Inferences

- Multi round-trip requests exist because the stateless core retired held-open server-to-client streams.
- Without a documented round cap, hosts must supply termination themselves.

### Unknowns

- Integrity algorithm for `requestState`.
- Maximum intended rounds.
- Whether production hosts already cap elicitations.

## Attribution

- **Title:** MCP 2026-07-28 Tools / Multi Round-Trip Requests
- **Author:** Model Context Protocol
- **Canonical source:** https://modelcontextprotocol.io/specification/2026-07-28/server/tools
- **Companion:** https://blog.modelcontextprotocol.io/posts/2026-07-28/
- **Published:** 2026-07-28
- **Captured:** 2026-08-26T08:00:00Z
- **Immutable reference:** https://github.com/modelcontextprotocol/modelcontextprotocol/commit/0cb6c6a31768cbb16129b35e6b569a31fecfe1b6 (`mrtr.mdx` in that commit)
- **License:** Apache-2.0 declared for new specification contributions (LICENSE transition also retains MIT and CC-BY-4.0 for other material)
- **Rights treatment:** summary-only
- **Availability:** available
