# Design Basis

This repository package was designed on 2026-08-25 using the following official or project-authoritative sources. Product behavior can change; verify current documentation before changing automation permissions or protocol implementations.

## Grok Bot

- Overview: https://docs.x.ai/grok-bot/overview
- Computer and apps: https://docs.x.ai/grok-bot/computer-and-apps
- Skills and routines: https://docs.x.ai/grok-bot/skills-routines-and-automations
- Approvals, security, and privacy: https://docs.x.ai/grok-bot/approvals-security-and-privacy
- Teams and enterprises: https://docs.x.ai/grok-bot/teams-and-enterprises

Design implications:

- Skills define reusable procedures; routines schedule them.
- A one-time task should be made reliable before scheduling.
- Bots use a persistent cloud computer.
- Bots under the same user share files, browser sessions, and command-line credentials; separate Bot names are not security boundaries.
- Consequential actions require explicit boundaries and approvals.

## AGENTS.md

- Open format and examples: https://agents.md/

Design implication: maintain a root `AGENTS.md` as a predictable agent-facing companion to the human README.

## Model Context Protocol

Current specification referenced during design:

- Specification: https://modelcontextprotocol.io/specification/2026-07-28
- Tools: https://modelcontextprotocol.io/specification/2026-07-28/server/tools
- Resources: https://modelcontextprotocol.io/specification/2026-07-28/server/resources
- Prompts: https://modelcontextprotocol.io/specification/2026-07-28/server/prompts
- Key changes: https://modelcontextprotocol.io/specification/2026-07-28/changelog

Design implications:

- Use resources for read-only artifact and catalog context.
- Use prompts for user-controlled retrieval workflows.
- Use tools only for bounded model-controlled queries.
- Keep protocol-version assumptions explicit because the 2026-07-28 revision introduced breaking changes.

## GitHub

- Protected branches: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- Issue and pull-request templates: https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests
- Citation files: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files

Design implications:

- Use pull requests, required review, required status checks, conversation resolution, and blocked force pushes.
- Use structured issue forms for candidate and system-change intake.
- Include `CITATION.cff` for repository citation while preserving item-level source attribution.

## Prompt-injection risk

- OWASP LLM01 Prompt Injection: https://genai.owasp.org/llmrisk/llm01-prompt-injection/
- OWASP Agentic AI threats and mitigations: https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/

Design implications:

- External webpages, files, issues, and repository content are untrusted.
- Prompt text alone is not the security boundary.
- Least privilege, source isolation, no execution, sanitized persistence, deterministic validation, and human approval are required controls.
