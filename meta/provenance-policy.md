# Provenance and Rights Policy

## Principle

Attribution is part of the artifact, not a courtesy added later. The fieldbook must preserve enough information for a reader or agent to locate the source, understand what was transformed, and determine which license governs the underlying work.

This policy is operational guidance, not legal advice.

## Required source fields

Every accepted entry records:

- canonical source title;
- author or organization;
- public handle when known;
- canonical source URL;
- source type;
- publication date, release date, or commit date;
- capture date and time;
- repository name, file path, and immutable commit SHA for GitHub file sources when practical;
- original license or `NOASSERTION`;
- license verification status;
- archive transformation;
- evidence level;
- material verification limits.

Unknown dates may be `null`, but the evaluator must state how date discovery was attempted. Missing author or source URL blocks acceptance.

## Source hierarchy

Prefer sources in this order:

1. official specifications, documentation, release notes, or source repositories;
2. immutable repository files, commits, pull requests, and issues from maintainers;
3. reproducible demonstrations and tests;
4. author or practitioner posts that link to primary evidence;
5. secondary analysis that adds a distinct, attributable interpretation.

Social engagement may prioritize review but never substitutes for evidence.

## Transformation types

### `original`

Created for this repository. Use `repo://` source URLs and identify repository authorship.

### `summary-only`

The fieldbook stores original metadata, an original summary, evaluation, and direct links. It does not reproduce the source artifact. This is the default when the source has no license or copying rights are unclear.

### `adapted-with-permission`

The fieldbook includes an adaptation under explicit permission. Record the permission basis and any conditions.

### `verbatim-per-license`

The fieldbook reproduces the artifact because its license permits it. Preserve required notices and identify modifications.

### Prohibited

- `unknown-copy`
- `unauthorized-copy`
- copied material with stripped credit or license notices
- substantial excerpts used as a substitute for linking to the source

## License handling

### Explicit compatible license

Record the SPDX identifier, license URL, copyright notice, and any required attribution. Preserve source notices in the entry or adjacent notice file when required.

### No license

A public GitHub repository without a license is not assumed to permit copying. Use `summary-only`, link to the source, and set SPDX to `NOASSERTION`.

### Conflicting or changed license

Record the license applicable to the captured version and the verification date. If rights become unclear, stop reproducing the artifact and convert the entry to summary-only or quarantine it.

### Multiple sources

Credit each material source. Do not attribute a composite mechanism to the most visible author alone.

## Immutable references

For GitHub sources, prefer:

- repository owner and name;
- file path;
- commit SHA;
- release tag when relevant;
- pull request or issue number.

A branch URL may be included for usability, but it is not an immutable reference.

For X posts or articles, record the canonical status or article URL, author handle, publication date, and capture date. Link to any referenced primary evidence separately.

## Quotes and copied text

Use original summaries by default. Include a direct quote only when the wording itself is the mechanism or evidence and when the license or applicable use permits it. Keep excerpts minimal and clearly marked.

Do not copy complete posts, threads, articles, prompts, skills, README sections, or source files merely because they are public.

## Removed or inaccessible sources

When a source disappears:

- mark `source_availability: unavailable`;
- retain safe metadata and the repository-authored analysis when lawful;
- do not reconstruct or republish the original from private caches;
- seek an archived canonical copy only when access and rights are legitimate;
- lower provenance or deprecate the entry when verification is no longer adequate.

## Generated content

AI assistance does not eliminate attribution obligations. If a contributor used a model to summarize or adapt a source, record the human or organizational source and the transformation. Do not list the model as the original author of third-party material.

## Corrections

Attribution corrections receive priority. Preserve the correction in Git history and update the artifact’s verification date. Material misattribution may require temporary removal until resolved.
