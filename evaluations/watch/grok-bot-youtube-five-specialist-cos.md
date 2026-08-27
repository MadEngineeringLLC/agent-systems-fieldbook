---
evaluation_schema: asf-evaluation/v1
evaluator_version: 1.0.0
rubric_version: 1.0.0
evaluated_at: "2026-08-26T23:55:00Z"
candidate:
  candidate_id: "candidate-grok-bot-youtube-five-specialist-cos-20260826"
  title: "YouTube five-specialist Grok Bot team under a chief of staff"
  source:
    url: "https://www.youtube.com/watch?v=t7YcnVtU-_k"
    type: "video"
    author: "Adam Chan / Legacy AI (as presented in the capture transcript)"
    handle: null
    published_at: null
    captured_at: "2026-08-26T23:50:00Z"
    license_spdx: "NOASSERTION"
    license_status: "unknown"
    immutable_reference: "https://www.youtube.com/watch?v=t7YcnVtU-_k"
    availability: "available"
    alternate_urls: []
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
    - "mechanism:chief-of-staff-orchestrator"
    - "lifecycle:operate"
    - "domain:operations"
    - "evidence:demonstrated"
  evidence_level: "demonstrated"
  duplicate_status: "independent-corroboration"
scores:
  relevance: 4
  completeness: 3
  actionability: 4
  clarity: 3
  safety_guardrails: 3
  novelty: 3
  cross_tool_portability: 3
  provenance: 3
weighted_score: 3.32
gates:
  provenance_complete: false
  safety_minimum_met: false
  rights_clear: false
  not_duplicate: true
  no_unresolved_critical_risk: true
  facts_inferences_unknowns_separated: true
risks:
  - flag: "external-side-effect-without-approval"
    severity: "high"
    evidence: "Capture transcript describes connecting Gmail and running prospect research against real businesses."
    effect: "Lead harvesting and mailbox access are consequential even when framed as a demo."
    remediation: "Do not accept. Recheck only with a verified transcript and an explicit approval path."
  - flag: "unverified-claim"
    severity: "moderate"
    evidence: "Working text is an unverified capture transcript, not a published official transcript. Computer-isolation wording in the capture conflicts with official shared-computer docs."
    effect: "Prompt text and setup steps may be misheard or model-generated captions."
    remediation: "Watch until a verified transcript or first-party write-up exists. Do not copy prompts."
  - flag: "over-permission"
    severity: "high"
    evidence: "Inbox, calendar, browser, and CRM-adjacent specialists are connected under one coordinator."
    effect: "A routing mistake can touch mail and outbound research in one turn."
    remediation: "Keep irreversible actions on approval. Do not treat the demo roster as least privilege."
decision:
  disposition: "watch"
  rationale: "The video appears to demonstrate a chief-of-staff Bot over five named specialists, which corroborates the official pattern, but the transcript is unverified, license is unknown, and the demo includes mailbox plus outbound prospecting side effects. Watch, do not accept."
  confidence: "low"
  recheck_trigger: "A verified transcript or author write-up is published, or YouTube metadata yields a stable title, date, and license sufficient for provenance 4."
stealable_mechanism: "Stand a chief-of-staff Bot that does not do the work over five named specialists and return one answer to the human."
improvements:
  - "Replace the capture transcript with a verified transcript or author notes."
  - "Record official video title, channel, and upload date."
  - "Strip any prompt text from future records."
  - "Reconcile per-Bot computer claims with official shared-computer docs."
  - "State approval rules before mail send or outreach."
verification:
  facts:
    - "https://www.youtube.com/watch?v=t7YcnVtU-_k was reachable at 2026-08-26T23:50:00Z."
    - "A capture transcript presented a chief-of-staff Bot plus inbox, calendar, prospect, content, and ops specialists, attributed on-screen to Adam Chan / Legacy AI."
    - "No official transcript, upload date, or license was independently verified."
  inferences:
    - "If the transcript is accurate, this is a demonstrated instance of the official chief-of-staff pattern, not a new mechanism."
  unknowns:
    - "Verified title, upload date, channel handle, and license."
    - "Whether the demo used a group chat or only 1:1 coordinator messages."
archive_target: "evaluations/watch/grok-bot-youtube-five-specialist-cos.md"
rubric_change_proposal: null
---

# Evaluation: YouTube five-specialist Grok Bot team under a chief of staff

## Executive assessment

Watch at weighted score 3.32. A five-specialist team under a chief of staff matches the official pattern, but the capture transcript is unverified and the demo includes mailbox and outbound prospecting side effects.

## Stealable mechanism

Stand a chief-of-staff Bot that does not do the work over five named specialists and return one answer to the human.

## Mechanism and context

Reported inputs are a coordinator Bot and five specialists (inbox, calendar, prospect, content, ops). Transformation is the human talking only to the coordinator, which delegates. Outputs are one combined answer plus specialist artifacts. Boundary: unverified transcript of a public video, not official docs.

## Evidence

Signals: YouTube URL reachable at capture; capture transcript only. Evidence level tentatively demonstrated, downgraded in confidence because the transcript is unverified. Duplicate status independent-corroboration. No prompts or substantial wording archived.

## Safety review

Connecting mail and running prospect research are external side effects. Per-Bot computer claims conflict with official docs. Safety score 3. Do not copy demo prompts.

## Improvements

Need verified metadata and transcript, plus an approval path, before any accept review.

## Attribution

Title: YouTube five-specialist Grok Bot team under a chief of staff (working title from capture). Author presented as Adam Chan / Legacy AI. Canonical URL: https://www.youtube.com/watch?v=t7YcnVtU-_k. Published: unknown. Capture: 2026-08-26T23:50:00Z. License: NOASSERTION. Rights treatment: summary-only. Availability: available.

## Facts, inferences, and unknowns

### Facts

- The video URL was reachable at capture. Transcript and metadata were not independently verified.

### Inferences

- If accurate, this corroborates official chief-of-staff lanes.

### Unknowns

- Title, date, license, and whether a group chat was used.

## Archive action

Store this sanitized watch record only. Do not accept. This record does not authorize merge or execution.
