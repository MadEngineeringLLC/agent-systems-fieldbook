# Deduplication and Lineage Policy

## Why deduplication matters

The fieldbook should compress repeated examples into durable mechanisms. Ten posts repeating the same advice are not ten artifacts.

## Identity keys

Evaluate duplicate status using, in order:

1. normalized canonical URL;
2. repository + path + immutable commit SHA;
3. source platform object ID, such as issue, pull request, or X status ID;
4. normalized title + author + publication date;
5. content fingerprint when lawful and available;
6. semantic mechanism: inputs, transformation, state, outputs, and controls.

## Duplicate classes

### Exact duplicate

Same source or effectively identical content. Keep one entry and add corroborating links only when useful.

### Syndicated duplicate

Same artifact published in multiple places. Prefer the canonical or author-controlled source and record mirrors as alternate URLs.

### Mechanism duplicate

Different wording or product syntax implements the same mechanism. Keep one general entry when the product differences are superficial. Keep separate entries only when permissions, state, failure behavior, or evidence materially differ.

### Version update

A newer version supersedes the existing artifact. Update the entry, preserve previous versions in Git history, and record the change. Create a new entry only when the mechanism materially changes or both versions remain useful.

### Independent corroboration

Separate sources provide distinct evidence for the same mechanism. Keep the mechanism entry and add the new evidence, or create an evaluation/use-case entry when the corroboration itself is important.

## Material difference test

A separate entry is justified when at least one changes materially:

- authority or permission model;
- state or memory design;
- termination or recovery behavior;
- evidence level;
- product constraint that changes implementation;
- threat model;
- measurable outcome;
- orchestration contract.

A new title, model name, or social post is not enough.

## Supersession fields

Use:

- `supersedes`
- `superseded_by`
- `related_artifacts`
- `alternate_sources`

Do not delete historical context solely because a newer version exists.
