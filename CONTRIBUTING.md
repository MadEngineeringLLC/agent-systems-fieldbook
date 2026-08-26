# Contributing

Thank you for helping build a smaller, more trustworthy collection rather than a larger, noisier one.

The fieldbook accepts prompts, skills, rules, goals, agent definitions, routines, workflows, orchestration patterns, control loops, state systems, team definitions, MCP artifacts, tools, evaluations, guardrails, failure analyses, and concrete use cases. Acceptance depends on evidence and transferability, not popularity.

## Before submitting

Confirm that the candidate:

- has a stable source URL;
- has an identifiable author or organization;
- has a publication or commit date, or clearly records that the date is unknown;
- has a stated license, or can be safely represented through a link and original summary;
- contains a reusable mechanism rather than only a result or opinion;
- is not already represented in the catalog;
- can be reviewed without executing untrusted instructions or code.

Do not submit secrets, private material, leaked content, paywalled copies, credential-bearing configuration, or live malicious prompt-injection payloads.

## Contribution paths

### 1. Submit a candidate issue

Use the **Candidate submission** issue form when you have a source but have not prepared an archive entry. Include the source URL, author, date, apparent license, artifact type, and why the mechanism matters.

A candidate issue is a lead, not an acceptance decision.

### 2. Submit an evaluated artifact

Use an existing accepted artifact as a structural example, then:

1. Classify it using `meta/taxonomy.md`.
2. Evaluate it using `skills/hardened-candidate-evaluator/SKILL.md`.
3. Create one Markdown file under the appropriate `artifacts/<category>/` directory.
4. Preserve source attribution in front matter and in the Attribution section.
5. Summarize in original language. Quote only when necessary and permitted.
6. Run the repository validation commands.
7. Open a focused pull request using the template.

### 3. Propose a system change

Rubric, taxonomy, schema, automation, or governance changes use `proposals/template.md`. A proposal must state:

- the observed problem;
- supporting repository data;
- the exact proposed change;
- compatibility and migration effects;
- calibration results against known cases;
- rollback conditions.

Bots may draft proposals. A human maintainer must approve them.

## Attribution requirements

Every artifact must preserve:

- original title;
- author or organization;
- handle when known;
- canonical source URL;
- publication date or commit date;
- capture date;
- repository path and immutable commit SHA for GitHub file sources when practical;
- original license or `unknown`;
- the transformation performed by this repository, such as `summary-only`, `adapted-with-permission`, or `verbatim-per-license`.

Do not use “source unknown.” If provenance cannot be reconstructed, reject the candidate.

## Licensing rules

Repository-authored summaries, schemas, prompts, and tooling are Apache-2.0 unless a file states otherwise.

Third-party material remains governed by its original license:

- **Compatible and explicit license:** preserve the notice and comply with its terms.
- **No license or unclear license:** store metadata, analysis, and a link; do not copy the artifact.
- **Restrictive license:** include only what the license permits and state the restriction.
- **Removed source:** retain the historical metadata only when lawful and useful; mark availability accurately.

See `meta/provenance-policy.md`.

## Evaluation process

Each candidate is scored from 1–5 on:

- relevance;
- completeness;
- actionability;
- clarity;
- safety and guardrails;
- novelty;
- cross-tool portability;
- provenance.

The weighted score is only one input. Accepted entries must also meet hard safety and provenance gates. Critical risk flags cause quarantine or rejection regardless of the average.

Disposition definitions:

- **accept:** high-value, adequately evidenced, safe to archive, and above the admission threshold;
- **watch:** promising but incomplete, immature, or insufficiently verified;
- **reject:** below the quality bar, duplicative, misleading, unsafe, or untraceable;
- **quarantine:** potentially malicious, secret-bearing, legally unclear, or unsafe to preserve in raw form.

See `meta/evaluation-rubric.md` and `meta/rejection-policy.md`.

## Pull-request expectations

Keep pull requests narrow:

- one to five related artifacts;
- generated catalog updates;
- no unrelated formatting churn;
- no taxonomy or rubric changes hidden inside artifact submissions;
- no direct modifications to generated catalog files without changing source artifacts.

A maintainer should be able to answer:

1. What mechanism is being added?
2. What evidence supports it?
3. What rights permit the repository treatment?
4. What risks were found?
5. Why is the entry materially different from existing entries?
6. Did all validation commands pass?

## Validation

```bash
python -m pip install -r requirements-dev.txt
python scripts/build_catalog.py
python scripts/validate_archive.py
python scripts/check_internal_links.py
python -m compileall -q scripts tests
python -m unittest discover -s tests -v
git diff --check
```

The pull request must include the exact command results. Do not state that checks passed if they were not run.

## Writing style

- Use direct, concrete language.
- Define unfamiliar terms.
- Separate facts, inferences, and unknowns.
- Avoid marketing claims and model tribalism.
- Prefer the smallest example that demonstrates the mechanism.
- State failure conditions and limits.
- Credit the source prominently.

## Review conduct

Review the work, not the person. Specific evidence-backed criticism is expected. Dismissive, hostile, or promotional behavior is not.

By contributing, you agree to follow `CODE_OF_CONDUCT.md` and certify that your contribution complies with the Developer Certificate of Origin in `.github/PULL_REQUEST_TEMPLATE.md`.
