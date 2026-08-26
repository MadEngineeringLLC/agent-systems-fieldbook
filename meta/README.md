# Meta: how the fieldbook governs itself

This directory contains the standards that determine what the fieldbook accepts, how entries are classified, and how the system may improve without silently moving its own goalposts.

## Authoritative files

| File | Purpose |
|---|---|
| `evaluation-rubric.md` | Human-readable scoring definitions, hard gates, and disposition rules |
| `scoring-schema.yaml` | Machine-readable weights, thresholds, risk flags, and output contract |
| `taxonomy.md` | Human-readable category and tagging guidance |
| `taxonomy.yaml` | Machine-readable taxonomy |
| `provenance-policy.md` | Attribution, copyright, source, and transformation requirements |
| `rejection-policy.md` | Reject and quarantine criteria |
| `deduplication-policy.md` | Identity, supersession, and near-duplicate handling |
| `self-improvement-policy.md` | How audits and proposals may change the system |
| `versioning.md` | Compatibility and migration rules |
| `source-registry.yaml` | Priority source classes and initial watchlist |
| `calibration/` | Fixed cases used to detect evaluator drift |
| `decisions/` | Architecture and policy decision records |

## Precedence

When files conflict, use this order:

1. `SECURITY.md`
2. `GOVERNANCE.md`
3. `meta/provenance-policy.md`
4. `meta/rejection-policy.md`
5. `meta/evaluation-rubric.md`
6. `meta/scoring-schema.yaml`
7. `meta/taxonomy.md` and `meta/taxonomy.yaml`
8. automation prompts and skills

A conflict is a system issue. Do not silently choose the more permissive interpretation.
