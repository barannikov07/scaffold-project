# Decisions: ChoirHub

Append-only. A decision earns an entry when a future owner or a fresh Claude session would
otherwise wonder "why is it like this?": stack choices, scope cuts, vision amendments, roadmap
reorders, tripwires, anything hard to reverse. Reversals are new entries that supersede the old
one; nothing is edited or deleted.

Format: ID · date · type (product / tech / process / scope) · status (Active / Superseded by D-nnn).
One paragraph: what was decided, why, and what was rejected.

---

## D-001 · 2026-09-16 · tech · Active

**Stack: Next.js, Postgres (Supabase), Supabase Auth, hosted on Vercel.**

Sasha already has GitHub and Vercel accounts, so hosting decided itself: push to GitHub, Vercel
builds and serves it, and nobody ever deploys from a command line. Next.js follows from Vercel
(it is the framework Vercel deploys with no configuration) and from the answer "a website that
works on phones": one responsive site, one thing to build and keep, no app store. Supabase gives
a real Postgres database with automatic backups on a free tier, which the choir's data needs
because attendance history must survive and must not be editable by hand. Supabase Auth comes
with that same project, so sign-in costs nothing extra: email link for everyone and Google for
the singers who prefer it, which was the "you decide" in the interview. Payments are not chosen
today; money arrives at milestone 3 and gets its own decision then.

Rejected: a native phone app (Expo), because the ask was a website that works on phones and an
app store adds a release queue for no gain today; a separate sign-in provider such as Clerk or
Auth0, because it is a second account and a second bill for something Supabase already includes;
a spreadsheet plus a form, because it is free and quick but anyone with the link can silently
rewrite attendance history, which breaks the first tripwire on day one; picking a payments
provider now, because a choice made a year before the first payment is a choice made without
information.

## D-002 · 2026-09-16 · process · Active

**Adopt the documented product process, planning stack, and deploy rules.**

The project follows the nine-stage pipeline in `workflow.md` with size-tiered ceremony, keeps
PRDs and specs as records once built, guides living, the roadmap fluid, treats docs as a merge requirement, ships only via git to
Vercel, and tracks work in the four-altitude planning stack (vision, roadmap, product index,
decisions). Rejected: ad-hoc building without written plans, which is fast for a week and
unrecoverable after a month; a single "status" document mixing plan, history, and reasoning,
which drifts.

## D-003 · 2026-09-16 · tech · Active

**Three tripwires from day one: attendance and replies are append-only, singers never see each
other's contact details, card details never touch the app.**

Sasha named two of these in the interview ("attendance history must never be lost or edited after
the fact"; "singers must never see each other's phone numbers or emails") and the third follows
from fees arriving later. All three are cheap today and expensive to retrofit. Append-only
records are a decision about the shape of the data: if replies and attendance are rows that are
added and superseded rather than fields that are overwritten, honesty is free forever; if they
start as editable fields, the history is already gone by the time anyone notices, and no later
feature can recover it. Contact privacy is a rule about who can read which column, enforced in
the database itself rather than by remembering to leave an email off a screen; added later, it
means auditing every screen, export and API response that already exists. Keeping card details
out of the app entirely is what lets ChoirHub take fees at milestone 3 without becoming a system
that has to be audited.

Rejected: "we will remember it during review", which is what every project says before the review
that forgets; and soft deletes on replies, which look like history but let an edit pass as the
truth. Each line lives in AGENTS.md so a fresh session reads it before touching anything, and the
detail lives in infra.md (Data model, Identities and access).

## D-004 · 2026-09-16 · product · Active

**Design system: warm paper and terracotta, Fraunces over Inter, one accent, light and dark both
designed.**

Sasha's three adjectives were calm, warm, clear; she admires Linear and Airbnb and does not want
to look like Facebook; she wants light and dark; the tone is friendly and brief; the
accessibility floor is the default (readable on a phone in sunlight, one thumb, WCAG AA).
Linear supplies the restraint — one accent colour used only for the primary action, a lot of air,
no decoration that carries no information — and Airbnb supplies the warmth: a paper-coloured
ground rather than white, 12 px corners, and a serif for headings so a choir of volunteers does
not feel handed enterprise software. Terracotta was chosen as the accent because it is warm
without being the coral every consumer app uses, and because it reaches 5.96:1 against white, so
the primary button passes AA with normal-weight text. Every token pair in
`docs/design/system.md` was checked against AA before it was written down.

Rejected: a blue accent, which is what every framework default gives and reads as "software"
rather than "our choir"; inverting the light palette to make the dark one, which produces grey
mud and an accent too dark to see on a dark ground (the dark accent is a separate, lighter
terracotta with `on-accent` flipping to dark text); a second display face for numbers, because
two faces on a screen is the rule.

## D-005 · 2026-09-16 · tech · Active

**The pasted message is read by Anthropic's API, starting at the cheapest tier and stepping up
only if the evaluation set fails.**

The paste-a-message step in the rehearsals-and-replies spec is the first place any of the choir's
words leave the app, so the provider is a decision rather than an implementation detail. Anthropic
was chosen because the stack needs no other model provider, the call is a single structured
extraction with no state, and the provider's API can constrain the answer to a fixed six-field
schema, which is what makes an instruction hidden inside a pasted message unable to do anything.
The tier is chosen by the ten-example evaluation set in the spec, not by price: the ladder is
Claude Haiku 4.5 (`claude-haiku-4-5`), then Claude Sonnet 5 (`claude-sonnet-5`), then Claude Opus
5 (`claude-opus-5`), and whichever passes first is recorded here at QA. At roughly forty
rehearsals a year the whole year's calls cost under a euro at the cheapest tier and about three at
the dearest, so cost genuinely does not decide; the applied-AI playbook's "cheapest tier that
passes" and the spec's quality bar agree because the difference is noise. The key lives in
`ANTHROPIC_API_KEY`, server environment only, and the step sits behind
`PASTE_A_MESSAGE_ENABLED` so it can be switched off without a deploy.

Rejected: sending the text from the browser, because the key would be in it; a self-hosted or
on-device model, because it is a weekend of work and a server to keep alive to save under a euro a
year; writing our own parser with regular expressions, because it handles the message in the
mockup and nothing else, and every Tuesday is a different message; and choosing the tier now on
price, because the only thing that matters is whether it reads a real WhatsApp message correctly,
which the evaluation set answers and a price list does not. This is a one-way door in the sense
that matters: once the conductor is used to pasting, removing the step is a feature being taken
away — the manual form is therefore permanent, not a fallback that gets tidied up later.

## D-006 · 2026-09-16 · tech · Active

**One choir. No choir or tenant column on any table, until a second choir is a decision of its
own.**

The rehearsals-and-replies data model has `singer`, `rehearsal` and `reply` and nothing above
them: there is no `choir` table and no `choir_id` on any row. The vision says it plainly — "serve
many choirs at once before this one choir is run well by it" is a non-goal — and a tenancy column
that nothing reads is not free: it appears in every query, every row-level rule and every index,
and it makes every rule harder to prove right at exactly the moment when proving them right is
the whole job (a singer must not see another singer's answer). Doing without it is worth
recording because it is the expensive kind of choice to reverse: a second choir means adding the
column to three tables, backfilling, and rewriting every policy and every query, with real data
already in place. That is a week, knowingly deferred, and it buys a simpler and more auditable
first milestone.

Rejected: a `choir_id` on every table from day one, which is the standard advice and is right for
a product sold to many customers, but this one is being built for one conductor and the vision
forbids widening it before she is well served; and a single-row `choir` table for the name shown
on screen ("Warsaw Community Choir"), because a constant in the code says the same thing with
nothing to keep in step.
