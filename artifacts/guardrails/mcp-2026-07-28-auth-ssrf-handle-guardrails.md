---
schema_version: "1.0"
id: asf-guardrail-20260826-003
title: MCP 2026-07-28 Auth, SSRF, and Handle Guardrails
slug: mcp-2026-07-28-auth-ssrf-handle-guardrails
artifact_type: guardrail
status: accepted
version: "1.0.0"
summary: >-
  MCP 2026-07-28 authorization guardrails reject token passthrough, require
  per-client consent before proxying OAuth, constrain metadata URL fetches
  against SSRF, and refuse to treat a state handle as authentication.
stealable_mechanism: >-
  Reject token passthrough, require per-client consent before proxying OAuth, block SSRF on metadata URLs, and never treat a state handle as authentication.
created_at: "2026-08-26"
updated_at: "2026-08-26"
last_verified_at: "2026-08-26"
authors:
  - name: Model Context Protocol
    handle: null
    url: null
source:
  type: official-docs
  title: Security Best Practices (MCP 2026-07-28)
  url: "https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices"
  author: Model Context Protocol
  handle: null
  published_at: "2026-07-28"
  captured_at: "2026-08-26T08:00:00Z"
  availability: available
  repository: modelcontextprotocol/modelcontextprotocol
  path: null
  commit_sha: b488c16623e5202a3961e551886044577ae0f096
  alternate_urls:
    - "https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations"
    - "https://blog.modelcontextprotocol.io/posts/2026-07-28/"
    - "https://github.com/modelcontextprotocol/modelcontextprotocol/commit/b488c16623e5202a3961e551886044577ae0f096"
license:
  spdx: Apache-2.0
  status: declared
  url: "https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/LICENSE"
  notes: >-
    The MCP repository LICENSE is a transition: new specification contributions
    are Apache-2.0, unrelicensed MIT remains, and non-spec documentation is
    CC-BY-4.0. This 2026-07-28 security page is treated as a new specification
    contribution under Apache-2.0 and is archived summary-only. The exact
    GitHub file path for the HTML page was not resolved.
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
  - asf-mcp-artifact-20260826-001
  - asf-control-loop-20260826-002
supersedes: []
superseded_by: null
evidence:
  level: conceptual
  signals:
    - The 2026-07-28 security best-practices page was available at capture.
    - The authorization security-considerations page in the same specification family requires audience checks, PKCE, and issuer validation.
    - Commit b488c16623e5202a3961e551886044577ae0f096 is titled Add 2026-07-28 MCP specification and dated 2026-07-28.
  limitations:
    - The queried GitHub path ending in security_best_practices.mdx returned no commits; exact repository path and blob SHA remain unknown.
    - Production proxy adoption was not surveyed.
    - Attack diagrams in the source were used only to classify mitigations and are not archived.
evaluation:
  rubric_version: "1.0.0"
  evaluator_version: "1.0.0"
  evaluated_at: "2026-08-26T08:20:00Z"
  scores:
    relevance: 5
    completeness: 5
    actionability: 4
    clarity: 4
    safety_guardrails: 5
    novelty: 4
    cross_tool_portability: 5
    provenance: 4
  weighted_score: 4.56
  risk_flags:
    - unsafe-default
    - hidden-dependency
  disposition: accept
  confidence: high
---

# MCP 2026-07-28 Auth, SSRF, and Handle Guardrails

## What it is

A summary of the Model Context Protocol 2026-07-28 authorization guardrail set: do not pass tokens through, obtain per-client consent before proxying OAuth with a static upstream client id, constrain discovery URL fetches against SSRF, and never treat a state handle as proof of authentication.

This entry stores mitigations only. It does not reproduce threat walk-throughs, payloads, or exploit steps from the source.

It is not a duplicate of [untrusted tool annotations and handles](../mcp/mcp-2026-07-28-untrusted-tool-annotations-and-handles.md), which covers tool metadata trust and handle minting rather than OAuth mix-up, confused-deputy consent, and SSRF on metadata URLs.

## Mechanism and boundary

```text
Token, redirect, metadata URL, registration, handle
        |
        v
[AUDIENCE AND ISSUER CHECKS]
        |
        +--> passthrough attempted --> [REJECT]
        |
        +--> proxy with static upstream client id
                |
                +--> no per-client consent --> [REJECT]
                +--> consent recorded --> [CONTINUE]
        |
        v
[METADATA URL FETCH]
        |
        +--> scheme or destination not allowed --> [REJECT]
        +--> allowed --> [PARSE]
        |
        v
[HANDLE USE]
        |
        +--> possession only --> [REJECT]
        +--> caller re-authorized --> [ALLOW]
```

The document can require behavior; it cannot enforce host implementations. Several network controls remain recommendations, which is why `unsafe-default` remains a residual flag.

## Inputs

```yaml
authz:
  access_token: audience_bound
  resource_indicator: required
  pkce: required
  issuer: checked
proxy:
  static_upstream_client_id: boolean
  per_client_consent: required_if_static_id
discovery:
  metadata_url: string
  allowed_schemes: [https]
  destination_policy: allowlist_and_private_ip_block
handles:
  value: opaque_string
  caller: verified
  treat_as_authentication: false
```

## Safety

Mitigations to implement, without the source's attack narratives:

- Reject token passthrough. A token minted for the MCP server is not a ticket to call a third-party API on the user's behalf.
- Require per-client consent before an MCP proxy reuses a static third-party client id.
- Fetch OAuth metadata URLs only under SSRF controls: scheme allowlists, destination allowlists, and private-IP blocking for non-loopback server-side clients. Treat those network controls as mandatory in a host profile even where the specification only recommends them.
- Never equate handle possession with authentication. Re-check the caller on every use, as in the sibling tools artifact.
- Validate resource indicators, audience, issuer, and PKCE on the authorization path described by the companion security-considerations page.

Described attacks in the source are the problems being mitigated, not instructions to archive. Residual `unsafe-default` risk is incomplete adoption of recommended network controls. Residual `hidden-dependency` risk is the unresolved GitHub filename.

## Adaptation

1. Put token-audience and no-passthrough checks on every inbound token.
2. Store a consent registry keyed by downstream client before using a static upstream OAuth client id.
3. Place metadata URL fetches behind the same egress policy used for other untrusted URLs.
4. Authorize handles against the caller, not the string, using the same binding rule as [explicit handles](../mcp/mcp-2026-07-28-untrusted-tool-annotations-and-handles.md).
5. Keep a short host checklist that separates required authorization checks from recommended network controls so a partial implementation cannot claim completion.

The pattern transfers to any agent proxy that forwards OAuth or mints continuation tokens.

## Improvements

- Pin the repository path and blob SHA for the security best-practices page.
- Promote private-IP blocking from a recommendation to a requirement for non-loopback server-side clients.
- Add a host checklist that separates must-hold authorization from should-hold network controls.
- Link each mitigated failure class to a conformance test name.
- Keep attack details out of this fieldbook entry; store only sanitized mitigations.

## Facts, inferences, and unknowns

### Facts

- https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices was available at capture 2026-08-26T08:00:00Z.
- The page forbids token passthrough, requires per-client consent for MCP proxies that use static third-party client ids, describes SSRF controls on OAuth metadata URLs, and states that servers must not treat handle possession as authentication.
- Authorization security-considerations at the 2026-07-28 specification require PKCE, resource indicators, audience validation, and issuer checks.
- Commit `b488c16623e5202a3961e551886044577ae0f096` is titled "Add 2026-07-28 MCP specification" and dated 2026-07-28.
- A GitHub commits query for `docs/specification/2026-07-28/basic/security_best_practices.mdx` returned no commits. No file path is invented here.
- Archive treatment is summary-only original prose.

### Inferences

- The HTML page belongs to the 2026-07-28 specification family even though the exact source filename was not resolved, based on the URL, cross-links, and release commit.
- Token-passthrough prohibition is the highest-leverage required check; SSRF controls need host policy to become equivalent.

### Unknowns

- Exact repository path and blob SHA for the security best-practices page.
- Which production MCP proxies currently implement per-client consent.

## Attribution

- **Title:** Security Best Practices (MCP 2026-07-28)
- **Author:** Model Context Protocol
- **Canonical source:** https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices
- **Companion:** https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations
- **Published:** 2026-07-28
- **Captured:** 2026-08-26T08:00:00Z
- **Immutable reference:** spec-add commit https://github.com/modelcontextprotocol/modelcontextprotocol/commit/b488c16623e5202a3961e551886044577ae0f096 (file path unresolved)
- **License:** Apache-2.0 declared for new specification contributions (LICENSE transition also retains MIT and CC-BY-4.0 for other material)
- **Rights treatment:** summary-only
- **Availability:** available
