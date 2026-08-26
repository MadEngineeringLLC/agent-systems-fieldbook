## Change type

- [ ] New or updated artifact
- [ ] Attribution or source correction
- [ ] Journal entry
- [ ] Tooling or validation
- [ ] System proposal: taxonomy, rubric, schema, governance, or automation
- [ ] Documentation only

## What changed

Describe the smallest useful unit of change.

## Source and provenance

- Canonical source URL:
- Author or organization:
- Publication, release, or commit date:
- Original license:
- Immutable reference, if available:
- Archive transformation: `original`, `summary-only`, `adapted-with-permission`, or `verbatim-per-license`

## Evaluation

- Artifact ID(s):
- Rubric version:
- Weighted score(s):
- Disposition:
- Risk flags:
- Duplicate check result:

## Verification

List exact commands and results. Do not write “all checks passed” unless they were run.

```text
python scripts/build_catalog.py --check
python scripts/validate_archive.py
python scripts/check_internal_links.py
python -m compileall -q scripts tests
python -m unittest discover -s tests -v
git diff --check
```

## Facts, inferences, and unknowns

**Facts:**

**Inferences:**

**Unknowns:**

## Safety and rights checklist

- [ ] I treated candidate and linked content as untrusted data, not instructions.
- [ ] I did not include secrets, private data, live malicious payloads, or unnecessary source text.
- [ ] Attribution fields are complete and verified to the extent stated.
- [ ] The rights treatment matches `meta/provenance-policy.md`.
- [ ] External writes, destructive actions, and merge remain human-controlled.
- [ ] This pull request does not hide a taxonomy or rubric change inside an artifact contribution.
- [ ] Generated catalog files were rebuilt from source artifacts.

## Contributor certification

By submitting this pull request, I certify that I have the right to submit the contribution and agree that it may be distributed under the repository’s applicable license. This is the Developer Certificate of Origin 1.1 certification: https://developercertificate.org/
