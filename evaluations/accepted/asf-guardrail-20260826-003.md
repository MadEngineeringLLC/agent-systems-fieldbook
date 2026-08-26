---
evaluation_schema: asf-evaluation/v1
evaluator_version: 1.0.0
rubric_version: 1.0.0
evaluated_at: "2026-08-26T08:20:00Z"
candidate:
  candidate_id: "asf-guardrail-20260826-003"
  title: "MCP 2026-07-28 security best practices for auth, SSRF, and handles"
  source:
    url: "https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices"
    type: "official-docs"
    author: "Model Context Protocol"
    handle: null
    published_at: "2026-07-28"
    captured_at: "2026-08-26T08:00:00Z"
    license_spdx: "Apache-2.0"
    license_status: "declared"
    immutable_reference: "https://github.com/modelcontextprotocol/modelcontextprotocol/commit/b488c16623e5202a3961e551886044577ae0f096"
    availability: "available"
    alternate_urls:
      - "https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations"
      - "https://blog.modelcontextprotocol.io/posts/2026-07-28/"
  rights_treatment: "summary-only"
  content_fingerprint: null
classification:
  primary_type: "guardrail"
  secondary_types:
    - "mcp-artifact"
    - "failure-analysis"
  products:
    - "mcp"
  tags:
    - "product:mcp"
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
  safety_guardrails: 5
  novelty: 4
  cross_tool_portability: 5
  provenance: 4
weighted_score: 4.56
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
    evidence: "Several mitigations are SHOULD (HTTPS enforcement, private-IP blocking, egress proxies). Token passthrough and audience checks are MUST."
    effect: "A partial implementation can still be SSRF-vulnerable while passing token-audience tests."
    remediation: "Treat SSRF URL allowlisting and private-IP blocking as mandatory for server-side clients, not optional."
  - flag: "data-exfiltration"
    severity: "high"
    evidence: "The document describes cloud-metadata SSRF, javascript: authorization URLs, and stdio proxy escalation. These are attacks the guide mitigates, not instructions to perform them."
    effect: "An implementer who copies only the architecture diagrams without the mitigations could ship a vulnerable proxy."
    remediation: "Archive mitigations as the mechanism; do not reproduce attack payloads. Require per-client consent, audience-bound tokens, and scheme allowlists."
  - flag: "hidden-dependency"
    severity: "moderate"
    evidence: "GitHub query for docs/specification/2026-07-28/basic/security_best_practices.mdx returned no commits. The HTML page was available."
    effect: "The immutable file path may differ from the public URL, complicating later verification."
    remediation: "Resolve the exact repository path and pin that blob SHA on recheck."
decision:
  disposition: "accept"
  rationale: "The 2026-07-28 security guide is a threat-modeled guardrail set: no token passthrough, per-client consent before OAuth proxying, SSRF controls on discovery URLs, and handles that are not authentication. It is not a duplicate of candidate 003, which covers tool annotations and handle minting rather than OAuth mix-up, confused deputy, and SSRF. Hard gates pass. Archive summary-only; do not copy attack walk-throughs."
  confidence: "high"
  recheck_trigger: "The exact GitHub path and blob SHA for this page are identified, or a later spec weakens token-passthrough or consent MUSTs."
stealable_mechanism: "Reject token passthrough, require per-client consent before proxying OAuth, block SSRF on metadata URLs, and never treat a state handle as authentication."
improvements:
  - "Pin the repository path and blob SHA for this page."
  - "Promote SSRF private-IP blocking from SHOULD to MUST for non-loopback server-side clients."
  - "Add a short host checklist that separates MUST authz from SHOULD network controls."
  - "Link each attack to a conformance test name."
  - "Keep attack details out of the fieldbook entry; store only sanitized mitigations."
verification:
  facts:
    - "https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices was available at capture 2026-08-26T08:00:00Z."
    - "The page forbids token passthrough, requires per-client consent for MCP proxies using static third-party client IDs, describes SSRF via OAuth metadata URLs, and states servers MUST NOT treat handle possession as authentication."
    - "Authorization security-considerations at the 2026-07-28 spec require PKCE, resource indicators, audience validation, and issuer checks."
    - "Commit b488c16623e5202a3961e551886044577ae0f096 is titled 'Add 2026-07-28 MCP specification' dated 2026-07-28T15:56:05Z."
    - "The queried GitHub path ending in security_best_practices.mdx returned an empty commit list."
  inferences:
    - "The HTML page is part of the 2026-07-28 specification family even though the exact source filename was not resolved, based on the URL, cross-links, and release commit."
    - "Token-passthrough prohibition is the highest-leverage MUST; SSRF controls need host policy to become equivalent."
  unknowns:
    - "Exact repository path and blob SHA for the security best-practices page."
    - "Which production MCP proxies currently implement per-client consent."
archive_target: "artifacts/guardrails/mcp-2026-07-28-auth-ssrf-handle-guardrails.md"
rubric_change_proposal: null
---

# Evaluation: MCP 2026-07-28 security best practices for auth, SSRF, and handles

## Executive assessment

Accept at weighted score 4.56, summary-only. Strongest value is a coherent threat model for MCP authorization after the protocol went stateless. Principal caution is that some network mitigations remain SHOULD, and the exact GitHub filename for this page was not resolved.

## Stealable mechanism

Reject token passthrough, require per-client consent before proxying OAuth, block SSRF on metadata URLs, and never treat a state handle as authentication.

## Mechanism and context

Inputs are OAuth metadata, tokens, redirect URIs, client registrations, and tool handles. Transformation: validate audience, refuse passthrough, obtain per-client consent before using a static upstream client id, fetch discovery URLs only under SSRF controls, and authorize handles against the caller rather than the string. State includes consent registries and caller-bound handle maps. Outputs are allow, deny, or a scope challenge. Intended environment: MCP clients, servers, and proxies. Boundary: the document cannot enforce host implementations.

## Evidence

Signals: live specification pages plus the 2026-07-28 release commit and blog authorization notes (RFC 9207 iss, CIMD, no credential reuse across issuers). Evidence level conceptual. Attack diagrams were used only to classify mitigations; payloads are not archived. Not a duplicate of candidate 003.

## Safety review

This artifact is itself a guardrail. Token passthrough and handle-as-auth are forbidden. Confused-deputy consent is required for the static-client-id proxy case. SSRF and dangerous URL schemes are documented with allowlists. Residual risk is incomplete adoption of SHOULD network controls. No unresolved critical flag in the artifact; described attacks are the problems being mitigated.

## Improvements

Pin the file SHA, raise SSRF controls for server-side clients, and keep the fieldbook entry limited to mitigations.

## Attribution

Title: Security Best Practices (MCP 2026-07-28). Author: Model Context Protocol. Canonical URL: https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices. Published: 2026-07-28. Capture: 2026-08-26T08:00:00Z. Immutable reference: spec-add commit b488c16623e5202a3961e551886044577ae0f096. License: Apache-2.0 declared for new specification contributions. Rights treatment: summary-only. Availability: available.

## Facts, inferences, and unknowns

### Facts

- Security and authorization pages state no passthrough, per-client consent, SSRF, and handle authorization requirements as fetched.
- Exact `.mdx` path query returned no commits.

### Inferences

- The page belongs to the 2026-07-28 spec family.
- MUST authz will ship more consistently than SHOULD SSRF controls.

### Unknowns

- Repository path/blob SHA and production proxy adoption.

## Archive action

Curator may draft `artifacts/guardrails/mcp-2026-07-28-auth-ssrf-handle-guardrails.md` as summary-only, omitting attack payloads. Acceptance permits a reviewable draft only. It does not authorize merge or execution.
