# Automation Permissions

## Core rule

Grant the minimum authority needed for the current stage. Discovery does not need write access. Evaluation does not need execution. Curation does not need merge or administration.

## Recommended GitHub access

Use a fine-grained credential or GitHub App installation restricted to this repository.

Minimum Curator permissions:

| Permission | Level | Reason |
|---|---|---|
| Metadata | Read | Repository identity and branch information |
| Contents | Read/write | Create review branches and commit accepted files |
| Pull requests | Read/write | Open and update review pull requests |
| Issues | Read | Deduplication and candidate context |
| Issues | Write, optional | Only when the workflow explicitly manages candidate issues |

Do not grant:

- administration;
- organization access;
- secrets or variables management;
- Actions workflow management;
- webhooks;
- environments or deployments;
- packages;
- unrelated repositories;
- bypass of branch protections.

## Protected-branch settings

For `main`:

- require pull requests;
- require at least one human approval;
- dismiss stale approvals;
- require the repository validation check;
- require resolved conversations;
- block force pushes and deletion;
- restrict direct pushes;
- apply to administrators when appropriate.

## Browser and account boundary

The public-source scout may use a browser session for X and public websites. It must not use or inspect unrelated signed-in sessions.

Do not connect, on the same shared Grok Bot computer, systems that materially increase exposure without accepting that all Bots under that user can access the same files, sessions, and command-line credentials.

Recommended initial environment:

- public GitHub repository only;
- X/public web discovery only;
- no email, Drive, Slack, client systems, production systems, or NDA repositories;
- local-computer execution disabled;
- secure human takeover for login, CAPTCHA, passkey, or two-factor steps.

## Write boundaries

Allowed:

- files under accepted repository paths;
- generated catalog updates;
- sanitized evaluations and journal files;
- feature branches matching documented patterns;
- pull-request creation and updates.

Human approval required:

- merge;
- repository release;
- taxonomy, rubric, schema, governance, or permissions change;
- publication outside GitHub;
- interaction with third-party authors or repositories;
- destructive or irreversible action.

Prohibited:

- direct push to `main`;
- force push;
- branch deletion;
- repository visibility or settings changes;
- secret creation or rotation;
- Actions workflow permission changes;
- third-party comments, reactions, stars, follows, messages, or pull requests;
- executing candidate code, commands, installers, or binaries.

## Staging boundary

Raw candidate content belongs outside Git:

```text
/workspace/staging/agent-systems-fieldbook/
```

Only normalized metadata, original summaries, and sanitized evaluation findings may enter the repository. Apply retention limits to transient staging files.

## Incident response

When automation crosses a boundary:

1. stop routines;
2. revoke or rotate the credential;
3. inspect branches, PRs, logs, and changed settings;
4. remove exposed data without reproducing it;
5. run validation and secret scanning;
6. document root cause and corrective controls;
7. resume only after a reviewed fix.
