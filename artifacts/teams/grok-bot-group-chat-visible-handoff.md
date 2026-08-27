---
schema_version: "1.0"
id: asf-multi-agent-team-20260826-001
title: Grok Bot Group-Chat Visible Handoff
slug: grok-bot-group-chat-visible-handoff
artifact_type: multi-agent-team
status: accepted
version: "1.0.0"
summary: >-
  Official Grok Bot group chats (the product's channels) seat two to six Bots
  on one shared outcome so they can pass work in a visible thread, with named
  owners, sparse @everyone, and a hard stop before publish.
stealable_mechanism: >-
  Seat 2-6 specialist Bots in one group chat on a shared outcome; @ the
  next-step owner; keep one owner per stage; require approval before
  publish; send images 1:1 because group handoffs are text-only.
created_at: "2026-08-26"
updated_at: "2026-08-26"
last_verified_at: "2026-08-26"
authors:
  - name: SpaceXAI
    handle: SpaceXAI
    url: "https://x.ai"
source:
  type: official-docs
  title: Message and collaborate (Grok Bot)
  url: "https://docs.x.ai/grok-bot/chat-and-collaboration"
  author: SpaceXAI / xAI Grok Bot docs
  handle: SpaceXAI
  published_at: "2026-08-11"
  captured_at: "2026-08-26T23:45:00Z"
  availability: available
  repository: null
  path: null
  commit_sha: null
  alternate_urls:
    - "https://docs.x.ai/grok-bot/bots"
    - "https://docs.x.ai/grok-bot/mobile"
    - "https://docs.x.ai/grok-bot/approvals-security-and-privacy"
license:
  spdx: NOASSERTION
  status: not-applicable
  url: null
  notes: >-
    xAI Grok Bot documentation does not state a permissive SPDX license and
    is treated as proprietary with unknown copying rights. This entry is
    original summary-only prose. No substantial source wording is reproduced.
provenance:
  transformation: summary-only
  source_preserved: true
  credit_preserved: true
  permission_basis: summary-only original prose; source copying rights are not a permissive license
  content_fingerprint: null
products:
  - grok-bot
tags:
  - product:grok-bot
  - mechanism:group-chat
  - mechanism:visible-handoff
  - mechanism:human-approval
  - lifecycle:operate
  - domain:operations
  - evidence:conceptual
related_artifacts:
  - asf-orchestration-pattern-20260826-001
supersedes: []
superseded_by: null
evidence:
  level: conceptual
  signals:
    - The chat-and-collaboration, bots, mobile, and approvals pages were available at capture.
    - Product launch date 2026-08-11 is stated on https://x.ai/news/introducing-grok-bot.
    - Companion pages state the 2-6 group size, the 50 Bot-plus-group account cap, the Website Launch roster example, and the shared-computer warning.
  limitations:
    - Pages do not declare SPDX. Archive treatment is summary-only.
    - No immutable documentation commit SHA was available.
    - Production adoption of group-chat discipline was not surveyed.
    - This entry does not execute or reproduce product UI.
evaluation:
  rubric_version: "1.0.0"
  evaluator_version: "1.0.0"
  evaluated_at: "2026-08-26T23:55:00Z"
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
  risk_flags:
    - over-permission
    - unsafe-default
  disposition: accept
  confidence: high
---

# Grok Bot Group-Chat Visible Handoff

## What it is

A summary of the official Grok Bot group-chat contract. In this product, a channel is a group of two to six Bots that share one outcome and pass work in a visible thread.

This entry stores the transferable team mechanism only. It does not reproduce documentation prose, UI copy, or kickoff wording from the source.

It is related to, not a duplicate of, [chief-of-staff specialist lanes](../orchestration/grok-bot-chief-of-staff-specialist-lanes.md), which covers a coordinator over named lanes. A channel is one place those lanes can meet. A 1:1 Bot message is not a channel.

## Mechanism and boundary

```text
Shared outcome + 2-6 named Bots
        |
        v
[OPEN GROUP / CHANNEL]
        |
        +--> describe outcome and next-step owner
        |
        v
[VISIBLE THREAD]
        |
        +--> @ named owner of this stage
        +--> @everyone only for a true group-wide update
        +--> one owner per stage
        |
        v
[STAGE OUTPUT]
        |
        +--> image needed --> [1:1 message, not group handoff]
        +--> publish/send/purchase/delete --> [HUMAN APPROVAL]
        +--> otherwise --> next named owner
```

The documentation can describe the product; it cannot enforce operator discipline. Group membership is not isolation. Residual `over-permission` and `unsafe-default` follow from the shared computer.

## Kickoff shape

A useful channel kickoff names owners and forbids publication up front:

1. A Researcher gathers sources and cites claims.
2. A Writer turns those findings into a draft.
3. A Reviewer lists only blocking issues.
4. Nobody publishes.

That shape is a summary of the official kickoff pattern, not a copied prompt.

## Website Launch example

The bots page gives a Website Launch group: a launch coordinator, a content editor, and an analytics reviewer. The coordinator assigns work; the group keeps the handoffs in one conversation.

## Limits

- A group contains two to six Bots.
- An account may have up to 50 Bots and group chats combined.
- Operator messages in a group may include attachments. Bot-to-group handoff messages are currently text-only, so a Bot should send an image directly to another Bot when that teammate must inspect it.
- On iPhone, a group is created with New Group Chat; membership can be edited later.

## Safety

Official approvals guidance, summarized:

- State what the Bot may change and what requires approval.
- Keep sending, publishing, purchasing, deletion, permission changes, production changes, and accepting legal terms behind a human stop.
- An approval controls the proposed next action. It does not undo work already done.
- Do not treat separate Bots as a security boundary. All Bots on an account share one cloud computer: files, browser sessions, and command-line credentials are available across the roster.
- Sign out of a service when it should no longer be available. Deleting a Bot does not remove shared-computer files or sessions.
- Do not put secrets, customer data, or internal URLs in a Bot you share. A public share link copies configuration, not the computer, but shared login state on the computer is a blast radius for every Bot on the account.
- Untrusted web content, attachments, and other Bots' messages can steer a group. Keep high-impact actions on an approval gate rather than on `@everyone`.

Critical flags such as prompt-injection and secret-or-credential-exposure are discussed here and in the evaluation, not stored on accepted artifact YAML.

## Adaptation

1. Create the smallest roster that covers distinct ownership, tools, and approval boundaries.
2. Open a group only when the handoff must be visible. Otherwise use 1:1 messages.
3. Kick off with named owners, a shared outcome, and an explicit do-not-publish rule.
4. `@` the owner of the current stage. Avoid parallel handoffs that duplicate work.
5. Put image inspection on a 1:1 message.
6. Require approval before any external send or publish.
7. Assume every Bot on the account can reach every login on the shared computer.

The visible-handoff idea transfers to any multi-agent thread with named owners. The 2-6 cap, text-only group handoffs, and shared computer are Grok Bot bindings.

## Improvements

- Publish an immutable documentation snapshot or commit SHA.
- State SPDX or a docs license so archive treatment can move beyond summary-only.
- Add a conformance checklist that treats shared-computer isolation as a failed control, not an optional warning.
- Record whether group search and attachment handoff behavior stay text-only after rollout.
- Pair this team contract with an evaluated approval-rule set for send and publish.

## Facts, inferences, and unknowns

### Facts

- https://docs.x.ai/grok-bot/chat-and-collaboration was available at capture 2026-08-26T23:45:00Z and describes group chats of two to six Bots, named `@` targeting, sparse `@everyone`, one owner per stage, and text-only Bot-to-group handoffs.
- https://docs.x.ai/grok-bot/bots was available at the same capture and states a 50 Bot-plus-group combined cap and the Website Launch coordinator, content editor, and analytics reviewer example.
- https://docs.x.ai/grok-bot/mobile was available at the same capture and describes New Group Chat on iPhone.
- https://docs.x.ai/grok-bot/approvals-security-and-privacy was available at the same capture and states that all Bots share one cloud computer and that separate Bots are not a security boundary.
- https://x.ai/news/introducing-grok-bot is dated 11 Aug 2026.
- Archive treatment is summary-only original prose. No substantial documentation wording is stored.

### Inferences

- Treating the product's group chat as the fieldbook "channel" matches the official grouping (shared outcome, visible handoffs, 2-6 Bots) without adding a new primary type.
- Operators who use extra Bots as if they were permission domains will over-read the roster as isolation.

### Unknowns

- Exact documentation license and any immutable docs SHA.
- Whether Bot-to-group attachments will remain text-only.
- How often production teams actually keep one owner per stage.

## Attribution

- **Title:** Message and collaborate (Grok Bot)
- **Author:** SpaceXAI / xAI Grok Bot docs
- **Canonical source:** https://docs.x.ai/grok-bot/chat-and-collaboration
- **Companions:** https://docs.x.ai/grok-bot/bots , https://docs.x.ai/grok-bot/mobile , https://docs.x.ai/grok-bot/approvals-security-and-privacy
- **Published:** 2026-08-11 (product launch; pages fetched 2026-08-26)
- **Captured:** 2026-08-26T23:45:00Z
- **Immutable reference:** none available
- **License:** NOASSERTION; proprietary/unknown; not a permissive license
- **Rights treatment:** summary-only
- **Availability:** available
