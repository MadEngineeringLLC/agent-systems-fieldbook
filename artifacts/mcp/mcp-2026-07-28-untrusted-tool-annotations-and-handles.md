---
schema_version: "1.0"
id: asf-mcp-artifact-20260826-001
title: MCP 2026-07-28 Untrusted Tool Annotations and Handles
slug: mcp-2026-07-28-untrusted-tool-annotations-and-handles
artifact_type: mcp-artifact
status: accepted
version: "1.0.0"
summary: >-
  MCP 2026-07-28 treats tool annotations as untrusted unless the server is
  trusted, requires validation of tool inputs and outputs, keeps a human deny
  path, and replaces hidden sessions with caller-bound explicit handles.
stealable_mechanism: >-
  Treat MCP tool annotations as untrusted unless the server is trusted, require a human deny path, validate tool I/O, and replace hidden sessions with caller-bound explicit handles.
created_at: "2026-08-26"
updated_at: "2026-08-26"
last_verified_at: "2026-08-26"
authors:
  - name: Model Context Protocol
    handle: null
    url: null
source:
  type: official-docs
  title: Tools (MCP specification 2026-07-28)
  url: "https://modelcontextprotocol.io/specification/2026-07-28/server/tools"
  author: Model Context Protocol
  handle: null
  published_at: "2026-07-28"
  captured_at: "2026-08-26T08:00:00Z"
  availability: available
  repository: modelcontextprotocol/modelcontextprotocol
  path: docs/specification/2026-07-28/server/tools.mdx
  commit_sha: 0cb6c6a31768cbb16129b35e6b569a31fecfe1b6
  alternate_urls:
    - "https://modelcontextprotocol.io/specification/2026-07-28"
    - "https://github.com/modelcontextprotocol/modelcontextprotocol/commit/0cb6c6a31768cbb16129b35e6b569a31fecfe1b6"
    - "https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/LICENSE"
license:
  spdx: Apache-2.0
  status: declared
  url: "https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/LICENSE"
  notes: >-
    The MCP repository LICENSE is a transition: new specification contributions
    are Apache-2.0, unrelicensed MIT remains, and non-spec documentation is
    CC-BY-4.0. This 2026-07-28 tools page is treated as a new specification
    contribution under Apache-2.0 and is archived summary-only.
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
  - mechanism:human-approval
  - lifecycle:design
  - domain:security
  - evidence:conceptual
related_artifacts:
  - asf-control-loop-20260826-002
  - asf-guardrail-20260826-003
supersedes: []
superseded_by: null
evidence:
  level: conceptual
  signals:
    - The 2026-07-28 tools specification page was available at capture.
    - GitHub commit 0cb6c6a31768cbb16129b35e6b569a31fecfe1b6 dated 2026-07-28 includes docs/specification/2026-07-28/server/tools.mdx.
    - The repository LICENSE states that new specification contributions are Apache-2.0.
  limitations:
    - SDK and host implementations were not executed.
    - Per-file SPDX on tools.mdx was not fetched.
    - Production host enforcement of annotation distrust is unknown.
evaluation:
  rubric_version: "1.0.0"
  evaluator_version: "1.0.0"
  evaluated_at: "2026-08-26T08:20:00Z"
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
  risk_flags:
    - unsafe-default
    - ambiguous-state
  disposition: accept
  confidence: high
---

# MCP 2026-07-28 Untrusted Tool Annotations and Handles

## What it is

A summary of the Model Context Protocol 2026-07-28 tools contract: hosts must not trust server-declared tool metadata unless the server itself is trusted, servers must validate tool I/O, a human should be able to refuse a call, and protocol-level sessions are replaced by explicit, caller-bound handles.

This entry is not a copy of the specification. It records a transferable trust boundary for any MCP host or similar tool-calling agent.

## Mechanism and boundary

```text
Untrusted or trusted MCP server
        |
        v
[LIST TOOLS] --annotations, schemas--> [HOST POLICY]
        |                                    |
        | untrusted annotations              | trusted server only
        v                                    v
[IGNORE FOR AUTHZ]                    [MAY INFORM UX]
        |
        v
[HUMAN DENY PATH] --allow/deny--> [tools/call]
                                      |
                                      v
                               [VALIDATE I/O]
                                      |
                                      +--> result (sanitized before the model)
                                      +--> explicit handle bound to this caller
```

Discovery, display, and authorization are separate:

- **Annotations** describe intended behavior. They are not a permission grant.
- **Schemas** describe arguments and results. They still require server-side validation.
- **Handles** are ordinary continuation strings. Possession is not authentication.
- **Host policy and a human deny path** decide whether a call proceeds.

The protocol states requirements. Host UIs, server authorization, and output sanitization remain implementation work.

Related control-loop and guardrail write-ups:

- [MCP 2026-07-28 multi round-trip tool calls](../control-loops/mcp-2026-07-28-multi-round-trip-tool-calls.md)
- [MCP 2026-07-28 auth, SSRF, and handle guardrails](../guardrails/mcp-2026-07-28-auth-ssrf-handle-guardrails.md)

## Inputs

```yaml
tool_definition:
  name: string
  annotations: untrusted_unless_server_trusted
  input_schema: object
  output_schema: object
call:
  arguments: object
  caller_identity: verified
  handle: optional_string
host_policy:
  server_trust: untrusted | trusted
  human_deny_path: required_for_untrusted_servers
  header_mirroring: forbidden_for_secrets
```

## Safety

- Treat tool annotations as untrusted unless the server is trusted. Do not use them as authorization input.
- Keep a deny-capable human confirmation path for untrusted servers. The specification recommends confirmation; it does not force hosts to implement it.
- Validate arguments against the declared schema, apply access control and rate limits, and sanitize results before they reach the model.
- Do not map passwords, API keys, tokens, or personal data onto headers that intermediaries can log.
- Bind every handle to the verified caller, give it entropy and a lifetime, and re-check authorization on later calls.
- Tool results are model-visible. Injection through output is a host-sanitization problem, not a reason to trust the server's self-description.

Residual risks recorded on this artifact are the spec-compatible unsafe default (confirmation is recommended, not required) and ambiguous handle state if servers treat the string as a capability. Prompt-injection and secret-header cases are named in the specification with required or documented controls; they are tracked with remediations in the matching evaluation rather than as unresolved critical flags here.

## Adaptation

For an MCP host:

1. Classify each connected server as trusted or untrusted.
2. Render annotations as hints only when the server is trusted; otherwise ignore them for allow/deny decisions.
3. Require a human deny path before invoking tools from untrusted servers.
4. Reject tool definitions that mirror sensitive properties into headers.
5. Prefer explicit handles over any hidden session table keyed only by the transport.
6. Re-authorize the caller on every handle use and expire unused handles.

The same pattern applies outside MCP: any agent that consumes vendor-supplied tool metadata should separate description, authorization, and continuation tokens.

## Improvements

- Raise untrusted-server confirmation from a recommendation to a host profile requirement.
- Forbid annotations as authorization input in normative language.
- Make handle entropy, lifetime, and caller-binding required for authenticated servers.
- Add a conformance case where annotations claim read-only behavior while the call writes.
- Record SPDX on the tools page itself to end mixed-license ambiguity.

## Facts, inferences, and unknowns

### Facts

- The tools page at https://modelcontextprotocol.io/specification/2026-07-28/server/tools was available at capture 2026-08-26T08:00:00Z.
- Commit `0cb6c6a31768cbb16129b35e6b569a31fecfe1b6` on 2026-07-28 includes `docs/specification/2026-07-28/server/tools.mdx`.
- The MCP repository LICENSE states that new specification contributions are Apache-2.0, unrelicensed MIT remains, and non-spec documentation is CC-BY-4.0.
- This archive entry is summary-only original prose; it does not reproduce specification text.

### Inferences

- The 2026-07-28 tools page is intended to fall under Apache-2.0 as a new specification contribution, based on the LICENSE transition paragraph.
- Hosts that skip confirmation can remain spec-compatible, based on confirmation being recommended rather than required.

### Unknowns

- Per-file SPDX header on `tools.mdx`.
- Which production hosts currently enforce annotation distrust.
- Whether shipped SDKs reject secret header mappings by default.

## Attribution

- **Title:** Tools (MCP specification 2026-07-28)
- **Author:** Model Context Protocol
- **Canonical source:** https://modelcontextprotocol.io/specification/2026-07-28/server/tools
- **Published:** 2026-07-28
- **Captured:** 2026-08-26T08:00:00Z
- **Immutable reference:** https://github.com/modelcontextprotocol/modelcontextprotocol/commit/0cb6c6a31768cbb16129b35e6b569a31fecfe1b6
- **License:** Apache-2.0 declared for new specification contributions (LICENSE transition also retains MIT and CC-BY-4.0 for other material)
- **Rights treatment:** summary-only
- **Availability:** available
