# Repository Structure

The repository separates accepted artifacts, candidate decisions, operating skills, automation configuration, generated indexes, and governing standards. This prevents untrusted intake from becoming part of the trusted corpus merely because it entered Git.

```text
agent-systems-fieldbook/
├── README.md                         Human landing page and navigation
├── AGENTS.md                         Instructions and safety boundaries for coding agents
├── LICENSE                           Apache-2.0 for repository-authored material
├── NOTICE                            Third-party rights and attribution boundary
├── CONTRIBUTING.md                   Submission, evaluation, and PR workflow
├── CODE_OF_CONDUCT.md                Community and integrity expectations
├── SECURITY.md                       Private reporting and automation security policy
├── GOVERNANCE.md                     Roles, decision classes, and change authority
├── SUPPORT.md                        Support routes and limits
├── ROADMAP.md                        Evidence-gated development phases
├── CHANGELOG.md                      Repository standard and tooling changes
├── CITATION.cff                      Human- and machine-readable repository citation
├── AUTHORS.md                        Project authorship and contributor policy
├── Makefile                          Common validation commands
├── pyproject.toml                    Python tooling metadata
├── requirements-dev.txt              Pinned validation dependencies
├── .github/
│   ├── CODEOWNERS                    Maintainer mapping placeholder
│   ├── PULL_REQUEST_TEMPLATE.md      Evidence, rights, risk, and validation checklist
│   ├── dependabot.yml                Monthly dependency and Actions update proposals
│   ├── ISSUE_TEMPLATE/
│   │   ├── candidate.yml             Source candidate intake
│   │   ├── taxonomy-change.yml       System proposal intake
│   │   ├── bug-report.yml            Repository tooling/documentation issue
│   │   └── config.yml                Issue chooser and contact links
│   └── workflows/
│       └── validate.yml              Read-only PR validation workflow
├── artifacts/                        Accepted public corpus only
│   ├── prompts/
│   ├── skills/
│   ├── rules/
│   ├── goals/
│   ├── agent-definitions/
│   ├── routines/
│   ├── workflows/
│   ├── orchestration/
│   ├── control-loops/
│   ├── state-and-memory/
│   ├── teams/
│   ├── mcp/
│   ├── tooling/
│   ├── evaluations/
│   ├── guardrails/
│   ├── failures/
│   └── use-cases/
├── catalog/                          Generated compact indexes
│   ├── artifacts.jsonl              Canonical agent-readable index
│   └── artifacts.csv                Human analysis/export format
├── evaluations/                      Sanitized non-accepted decision records
│   ├── accepted/
│   ├── watch/
│   ├── rejected/
│   ├── quarantined/
│   └── templates/
├── journal/                          Evidence-led longitudinal field journal
│   ├── YYYY/
│   ├── templates/
│   └── index.jsonl
├── meta/                             Versioned standards and self-governance
│   ├── evaluation-rubric.md
│   ├── scoring-schema.yaml
│   ├── taxonomy.md
│   ├── taxonomy.yaml
│   ├── provenance-policy.md
│   ├── rejection-policy.md
│   ├── deduplication-policy.md
│   ├── self-improvement-policy.md
│   ├── versioning.md
│   ├── source-registry.yaml
│   ├── calibration/
│   └── decisions/
├── schemas/                          JSON Schemas for artifact, evaluation, and journal metadata
├── skills/                           Skills that operate the repository itself
│   ├── hardened-candidate-evaluator/
│   ├── source-scout/
│   ├── archive-curator/
│   ├── journal-synthesizer/
│   └── archive-cartographer/
├── automation/                       Grok Bot design, routines, searches, and permissions
│   └── grok-bot/
├── proposals/                        Reviewed system-change proposals
├── docs/                             Architecture, querying, setup, and design basis
├── scripts/                          Deterministic catalog and validation tooling
└── tests/                            Unit tests and fixtures
```

## Top-level responsibilities

### `artifacts/`

Trusted corpus boundary. Only accepted artifacts belong here. Every non-README Markdown file must have valid front matter and an `accept` evaluation.

### `evaluations/`

Decision memory for candidates that are not part of the accepted corpus. Quarantine files are sanitized records, not payload storage.

### `catalog/`

Generated metadata optimized for agents and lightweight analysis. The catalog is derived, never authoritative over the source artifact.

### `journal/`

Time-bounded synthesis of verified developments, emerging mechanisms, failures, fieldbook changes, and coverage gaps. Journal claims should point to primary sources or accepted artifact IDs.

### `meta/`

The project’s constitution for classification, evaluation, provenance, rejection, versioning, and self-improvement. Ordinary artifact contributions cannot change these files.

### `skills/`

Versioned procedures used by the Fieldbook Steward Bot or human maintainers. These are operational controls for the repository, not automatically accepted external artifacts.

### `automation/`

Schedules, role descriptions, source strategy, and least-privilege boundaries. Raw candidate content is staged outside the repository.

### `proposals/`

The only normal route for changing how future artifacts are judged or classified.

### `schemas/`, `scripts/`, and `tests/`

Machine enforcement. The evaluator produces structured judgments; deterministic tooling checks metadata, score math, catalogs, links, and repository invariants.

## Adding a new top-level directory

A new top-level directory requires a system proposal when it changes a trust boundary, artifact lifecycle, or public interface. Convenience alone is not enough.
