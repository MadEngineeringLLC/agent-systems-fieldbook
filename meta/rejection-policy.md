# Rejection and Quarantine Policy

## Rejection is a quality function

The fieldbook is intentionally incomplete. Rejection protects users from spending attention on weak, unsafe, duplicated, or untraceable material.

## Immediate rejection

Reject when any of the following is true and cannot be corrected during review:

- no canonical source URL;
- no identifiable author or organization;
- fabricated, misleading, or materially altered attribution;
- no reusable mechanism beyond a slogan, opinion, or promotional claim;
- duplicate of an existing entry without new evidence or a material mechanism change;
- weighted score below 3.20;
- provenance below 3 and no credible route to verification;
- copied content exceeds what the license or permission allows;
- claims of production use or evaluation have no accessible support;
- the artifact is obsolete in a way that would mislead users and has no historical value;
- the content is generated filler with no source or independent verification.

## Rejection after safety review

Reject unsafe artifacts when their core mechanism depends on:

- unrestricted tool or filesystem authority;
- destructive action without approval or rollback;
- credential collection or persistence not required by the job;
- open-ended execution without budget, progress measure, or termination;
- silent self-modification of goals, rules, memory, taxonomy, or evaluation;
- bypassing site controls, rate limits, terms, or human verification;
- external communication or publication without explicit approval;
- executing untrusted source instructions or code.

A safe adaptation may be archived as a separate repository-authored artifact, but it must not imply that the original was accepted unchanged.

## Quarantine triggers

Quarantine rather than ordinary rejection when the candidate may contain:

- prompt injection or instruction-hijacking content;
- secrets, credentials, session values, private keys, or recovery codes;
- personal, private, client, NDA-controlled, or regulated data;
- malicious executables, links, macros, scripts, or dependency instructions;
- data-exfiltration or privilege-escalation mechanisms;
- unresolved copyright, leak, or ownership disputes;
- content whose reproduction would create avoidable harm.

## Quarantine record

A quarantine record may include only:

- candidate ID;
- canonical source URL when safe to retain;
- source author or organization;
- capture date;
- sanitized description;
- detected risk flags;
- affected trust boundary;
- decision and reviewer;
- hash or immutable identifier when useful and safe.

Do not store the raw payload, secret, copied file, or operational exploit steps.

## Watch instead of reject

Use `watch` when the mechanism is credible and potentially valuable but:

- source date or license remains incomplete;
- evidence is only conceptual;
- implementation is not yet reproducible;
- an imminent product release may resolve uncertainty;
- the item is too early to distinguish from a transient workaround.

Every watch record needs a recheck trigger or review date.

## Appeals and resubmission

A rejected candidate may be reconsidered when new evidence, corrected attribution, explicit permission, an improved safe adaptation, or a materially distinct mechanism is provided. Repeated resubmission without new evidence may be closed without re-evaluation.
