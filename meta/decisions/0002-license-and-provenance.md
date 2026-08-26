# ADR-0002: Apache-2.0 for original content; preserve source licenses per artifact

- **Status:** accepted
- **Date:** 2026-08-25

## Context

The repository contains code, schemas, prompts, evaluation methods, and documentation, while also describing or adapting third-party artifacts under many licenses.

## Decision

License repository-authored material under Apache-2.0. Do not treat the repository license as relicensing third-party works. Preserve source license and transformation metadata in every artifact.

## Rationale

Apache-2.0 is permissive, explicit about notices, and includes a patent grant that is useful for code and tooling. A single repository license keeps contributions straightforward. Item-level provenance prevents the umbrella license from obscuring third-party rights.

## Consequences

- No-license sources default to `summary-only`.
- Copied or adapted content must record its rights basis.
- `NOTICE` explains the boundary.
- Contributors must not strip upstream notices.
