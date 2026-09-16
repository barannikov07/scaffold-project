<!-- Playbook: security. Canonical text; the .claude/skills and .codex/skills wrappers point here. -->

# Security

Keep the wrong people from seeing or changing the wrong things. Three moments, all called by the
spine playbooks so the owner never has to remember them:

- **Baseline**, once, during tech setup.
- **Threat pass** at Spec, for every feature tagged money, privacy, sign-in, or external service.
- **Diff checklist** at QA, for the same features.

Also runs on its own when the owner says "security", "is this safe", "who can see this", or
"review permissions". If the agent has a built-in security review skill, run it first and fold
its findings into the sections below; the sections are still filled, because the review skill
does not know the tripwires. Calibrate every message to the owner profile in `AGENTS.md`;
findings are explained as who could see or do what, never in jargon.

Read first: `AGENTS.md` (tripwires), `infra.md` (identities, roles, data model), the feature's
`prd.md` and `spec.md`.

## Baseline (tech setup)

Tick each in `infra.md` (Security baseline) with evidence:

- Secrets exist only in the host's environment settings and the gitignored `.env.local`. The
  repository history contains none (search it).
- Row-level rules are on for every table, default deny; the server key never reaches the browser.
- Sign-in is configured with sane expiry; the localhost test login cannot exist in production
  builds.
- HTTPS only; standard security headers set by the host or the framework.
- Backups are on at the database provider; a restore has been tried once.
- The verify script runs a dependency audit and fails on known critical vulnerabilities.
- Logs contain no personal data by default.

## Threat pass (Spec)

Fill the spec's Security section:

1. **Data classification.** One row per kind of data the feature touches: what it is, how
   sensitive (public · internal · personal · money), who may see it, where it is stored, whether
   it ever leaves the app (to a provider, an email, a webhook).
2. **Denied actions.** From the permission table: for each role, what it must not be able to do,
   including by crafting a request directly rather than through the interface.
3. **Rules that enforce it.** Which row-level rule or server check makes each denial real. A
   denial that exists only as a hidden button is not a denial.
4. **Input surfaces.** Forms, uploads, imports, URLs, and any text that reaches a model prompt.
   For prompts: user content is data, never instructions.
5. **Abuse cases.** Three to five sentences of the form "a malicious <role> tries to ...", each
   with what stops them.
6. **External services.** What each is trusted with; what happens if it is compromised or down.
7. **Logging.** What is logged, confirming no personal data.

Anything here that must hold forever becomes a tripwire line in `AGENTS.md`, and anything
surprising becomes a decision.

## Diff checklist (QA)

Executed against the branch, recorded in the QA run's Security section with evidence:

- No secret, token, or key in the diff or in any document. Search for key-like strings.
- Every denied action from the threat pass tested denied, by direct request where possible.
- Every new table has a row-level rule; the rule was tested with the test user, not assumed.
- Every input validated on the server, not only in the browser; uploads restricted by type and
  size.
- Model prompts: pasting an instruction into a user field ("ignore the above and ...") changes
  nothing.
- No personal data in logs or error messages; errors do not reveal internals.
- Public endpoints are rate-limited.
- Dependency audit clean of critical findings.

## Severity

- **Critical** (blocks release): data exposure across users, sign-in bypass, anything that moves
  or shows money wrongly, a tripwire broken.
- **Later**: hardening that does not change who can see or do what today. One roadmap line.
