---
evaluation_schema: asf-evaluation/v1
evaluator_version: 1.0.0
rubric_version: 1.0.0
evaluated_at: "2026-08-26T23:55:00Z"
candidate:
  candidate_id: "asf-multi-agent-team-20260826-001"
  title: "Grok Bot group-chat visible handoff"
  source:
    url: "https://docs.x.ai/grok-bot/chat-and-collaboration"
    type: "official-docs"
    author: "SpaceXAI / xAI Grok Bot docs"
    handle: "SpaceXAI"
    published_at: "2026-08-11"
    captured_at: "2026-08-26T23:45:00Z"
    license_spdx: "NOASSERTION"
    license_status: "unknown"
    immutable_reference: null
    availability: "available"
    alternate_urls:
      - "https://docs.x.ai/grok-bot/bots"
      - "https://docs.x.ai/grok-bot/mobile"
      - "https://docs.x.ai/grok-bot/approvals-security-and-privacy"
  rights_treatment: "summary-only"
  content_fingerprint: null
classification:
  primary_type: "multi-agent-team"
  secondary_types:
    - "orchestration-pattern"
  products:
    - "grok-bot"
  tags:
    - "product:grok-bot"
    - "mechanism:group-chat"
    - "mechanism:visible-handoff"
    - "mechanism:human-approval"
    - "lifecycle:operate"
    - "domain:operations"
    - "evidence:conceptual"
  evidence_level: "conceptual"
  duplicate_status: "new"
scores:
  relevance: 5
  completeness: 4
  actionability: 5
  clarity: 5
  safety_guardrails: 4
  novelty: 4
  cross_tool_portability: 3
  provenance: 4
weighted_score: 4.34
gates:
  provenance_complete: true
  safety_minimum_met: true
  rights_clear: true
  not_duplicate: true
  no_unresolved_critical_risk: true
  facts_inferences_unknowns_separated: true
risks:
  - flag: "over-permission"
    severity: "high"
    evidence: "Official approvals docs state that all Bots on an account share one cloud computer, including files, browser sessions, and command-line credentials."
    effect: "A specialist in a group can reach logins and files gathered for another Bot. Group membership is not isolation."
    remediation: "Treat the account computer as one trust zone. Sign out unused services. Keep send, publish, purchase, and deletion on approval."
  - flag: "unsafe-default"
    severity: "high"
    evidence: "Creating extra Bots is presented as a way to split jobs. The same pages warn not to use separate Bots as a security boundary."
    effect: "Operators may staff a channel as if roster size were least privilege."
    remediation: "Document the shared-computer blast radius in the kickoff. Do not encode isolation into Bot count."
decision:
  disposition: "accept"
  rationale: "Official Grok Bot docs define a concrete 2-6 Bot group chat with named owners, sparse @everyone, text-only group handoffs, and an approval stop before publish. Hard gates pass. License is unknown, so archive summary-only. Shared-computer blast radius is residual high risk, not an unresolved critical YAML flag."
  confidence: "high"
  recheck_trigger: "Docs declare SPDX or an immutable SHA, group handoffs gain attachments, or the shared-computer model changes."
stealable_mechanism: "Seat 2-6 specialist Bots in one group chat on a shared outcome; @ the next-step owner; keep one owner per stage; require approval before publish; send images 1:1 because group handoffs are text-only."
improvements:
  - "Pin an immutable documentation snapshot."
  - "State a docs license."
  - "Add a host checklist that treats shared-computer isolation as a failed control."
  - "Recheck whether Bot-to-group handoffs remain text-only."
  - "Pair the team contract with an evaluated send/publish approval rule set."
verification:
  facts:
    - "https://docs.x.ai/grok-bot/chat-and-collaboration was available at 2026-08-26T23:45:00Z and describes 2-6 Bot groups, named @ targeting, one owner per stage, and text-only Bot-to-group handoffs."
    - "https://docs.x.ai/grok-bot/bots states the 50 Bot-plus-group cap and the Website Launch coordinator, editor, reviewer example."
    - "https://docs.x.ai/grok-bot/approvals-security-and-privacy states that all Bots share one cloud computer and that separate Bots are not a security boundary."
    - "https://x.ai/news/introducing-grok-bot is dated 2026-08-11."
  inferences:
    - "The product's group chat is the fieldbook channel: shared outcome plus visible handoffs, without a new primary type."
    - "Operators who treat extra Bots as permission domains will misread the roster."
  unknowns:
    - "Documentation SPDX and immutable SHA."
    - "Whether group handoff attachments will remain text-only."
archive_target: "artifacts/teams/grok-bot-group-chat-visible-handoff.md"
rubric_change_proposal: null
---

# Evaluation: Grok Bot group-chat visible handoff

## Executive assessment

Accept at weighted score 4.34, summary-only. Strongest value is an official, implementable channel contract: two to six Bots, one shared outcome, named owners, and a hard stop before publish. Principal residual risk is the shared cloud computer, which is not a security boundary.

## Stealable mechanism

Seat 2-6 specialist Bots in one group chat on a shared outcome; @ the next-step owner; keep one owner per stage; require approval before publish; send images 1:1 because group handoffs are text-only.

## Mechanism and context

Inputs are a shared outcome, two to six named Bots, and an operator message that names the next-step owner. Transformation is a visible thread where Bots post and pass work. State is the group transcript plus whatever the shared computer holds. Outputs are stage results, image 1:1 messages when needed, and an approval request before publish or send. Intended environment: Grok Bot desktop and iOS. Boundary: documentation cannot enforce operator discipline or isolate Bots from one another.

## Evidence

Signals: live official pages for chat, bots, mobile, and approvals, plus the 11 Aug 2026 launch date. Evidence level conceptual. Kickoff wording and UI copy were used only to extract the mechanism and are not archived. Duplicate status new; related to the chief-of-staff orchestration candidate, not the same artifact.

## Safety review

Approvals exist for consequential actions. Named owners and a do-not-publish kickoff reduce accidental sends. Residual high risks: every Bot on the account shares files, browser sessions, and CLI credentials; extra Bots are an unsafe isolation default. Untrusted attachments and other Bots' messages can steer a group (prompt-injection class), and shared logins expand secret blast radius. Those critical classes are discussed here and omitted from accepted artifact YAML. No unresolved critical flag is accepted as a live payload.

## Improvements

Pin a docs snapshot, obtain a license statement, and treat shared-computer isolation as a failed control in any host profile.

## Attribution

Title: Message and collaborate (Grok Bot). Author: SpaceXAI / xAI Grok Bot docs. Canonical URL: https://docs.x.ai/grok-bot/chat-and-collaboration. Published: 2026-08-11 (product launch; pages fetched 2026-08-26). Capture: 2026-08-26T23:45:00Z. Immutable reference: none. License: NOASSERTION / unknown. Rights treatment: summary-only. Availability: available.

## Facts, inferences, and unknowns

### Facts

- Chat, bots, mobile, and approvals pages were available at capture and state the group-size, cap, Website Launch example, and shared-computer warning.
- Launch post dated 2026-08-11.

### Inferences

- Group chat is the product's channel.
- Roster size is not least privilege.

### Unknowns

- SPDX, docs SHA, and future attachment behavior in group handoffs.

## Archive action

Curator may draft `artifacts/teams/grok-bot-group-chat-visible-handoff.md` as summary-only. Acceptance permits a reviewable draft only. It does not authorize merge, execution, enabling routines, or creating a live Grok Bot channel.
