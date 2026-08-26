# Automation

The recommended initial design is **one Grok Bot with multiple versioned skills and routines**, not multiple Bots as security boundaries.

Logical roles remain separate:

- source scout;
- hardened evaluator;
- archive curator;
- journal synthesizer;
- archive cartographer.

The Bot uses a staging directory outside the Git repository for raw, untrusted material. Only sanitized, evaluated outputs reach a review branch. Human review remains mandatory before merge.

Files:

- `bots.yaml` — recommended Bot identity and optional future role split;
- `routines.yaml` — schedules, budgets, outputs, and approvals;
- `search-plan.yaml` — source and query strategy;
- `permissions.md` — least-privilege boundary;
- `grok-bot/fieldbook-steward-system-prompt.md` — standing Bot instructions;
- `grok-bot/first-run.md` — one-time bootstrap prompt.
