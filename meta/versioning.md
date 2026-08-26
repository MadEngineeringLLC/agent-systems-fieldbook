# Versioning

## Versioned components

The project versions these components independently:

- repository release;
- artifact front-matter schema;
- evaluation output schema;
- taxonomy;
- rubric and scoring schema;
- hardened evaluator skill;
- automation prompts and routines.

## Semantic versioning

- **Patch:** wording clarification or bug fix that does not change valid decisions or fields.
- **Minor:** backward-compatible field, tag, risk flag, or optional behavior.
- **Major:** changed meaning, required field, category, weight, threshold, disposition rule, or incompatible automation contract.

## Artifact version fields

Each artifact records:

- `schema_version`;
- artifact `version`;
- `evaluation.rubric_version`;
- `evaluation.evaluator_version`;
- `updated_at`;
- `last_verified_at`.

## Migration

A breaking proposal must include:

- source and target versions;
- affected paths and artifact IDs;
- deterministic migration steps where possible;
- validation changes;
- catalog regeneration;
- rollback instructions;
- whether historical scores require re-evaluation.

## Historical interpretation

Do not rewrite history to make old evaluations appear to have used a newer rubric. Current artifacts may be re-evaluated, but Git history and changelog entries preserve the earlier decision context.
