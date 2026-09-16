# The conversation, as the owner saw it

Every owner-facing message from the ChoirHub run, in order: the scaffold session, the PRD with the applied-AI pass, the design stage, and the spec with the security and CTO passes. Replies marked as assumed were not given by a person; the run had no owner available.

---

# Everything Sasha would have seen, in order

The owner could not reply during this run, so every message below was written as it would have
been sent, and the replies in the grey blocks are the answers supplied with the task (or the
"assume yes" the task allowed). Nothing here was invented to make the flow work; where a reply
was assumed rather than given, the block says so.

Owner profile driving the tone: *understands how apps work but doesn't code; worked alongside
product managers for years.* So: no glossing of ordinary terms, a recommendation plus the
alternative rather than every option, gates named rather than explained, file names instead of
code.

---

## Message 1 — the stack, the summary, and the one yes/no before anything is written

You gave me everything in one go, so I'll skip the interview and state back what I'm assuming.

**Two things I would have asked you, answered by me. Correct either if I've got it wrong.**

- Your first feature needs singers to exist before "coming / not coming" means anything. I'm
  putting a thin *add a singer* step (name, email, voice section) **inside** the first feature
  rather than making it a milestone of its own — otherwise the first thing you can use is a list
  of people that does nothing.
- You said "a website that works on phones", so I am not building a phone app: one website,
  designed for a phone first, that also works on a laptop. No app store, no review queue.

**The stack, one line each.** These are the choices you asked me to make for you.

- **Next.js** — the standard way to build a website that works well on a phone, and Vercel
  deploys it with no setup.
- **Supabase (Postgres)** — a real database with automatic backups, free to start. Sign-in comes
  with it, so there is nothing else to pay for or connect.
- **Supabase Auth** — email link *and* Google, since you said either was fine. Singers won't
  invent another password.
- **Vercel** — you already have it. Push to GitHub, the site deploys itself; nobody ever deploys
  by hand.
- **Payments: nothing yet.** Fees are milestone 3, and the provider gets chosen then, when we
  know what we need. Card details will never touch ChoirHub either way.

The one alternative I considered and rejected: a real phone app (Expo). It would add an app-store
release queue and a second thing to build, for nothing you asked for. All of this goes into the
decisions log as D-001, so nobody has to re-litigate it in six months.

**Three rules I'm hard-wiring from what you told me.** These become "tripwires": one line each at
the top of the project, read by any Claude session before it touches anything.

1. Attendance and replies are append-only — never edited or deleted after the fact.
2. A singer never sees another singer's email or phone number. Only you do.
3. Card details never touch this app or its logs.

**What I'm about to create** — documents and process, no app code:

| Document | What it is for |
|---|---|
| `AGENTS.md` | The map every agent reads |
| `docs/vision.md` | The end state, written down |
| `docs/roadmap.md` | Milestones in order, with status |
| `docs/product-index.md` | Where every feature stands today |
| `docs/decisions.md` | Why things are this way |
| `workflow.md` | How work flows, with gates |
| `infra.md` | How the system is built |
| `docs/design/` | How everything should look |
| `docs/qa/regression.md` | What must never break |
| `docs/tech-debt.md` | Shortcuts, each with a due date |
| `docs/playbooks/` (nine) | The commands you can say |
| `docs/products/tech-setup/` | Day-one setup, tracked like a feature |
| `docs/products/rehearsals-and-replies/` | Your first feature's four documents |
| `.github/pull_request_template.md` | The checklist every change must pass |

Project name **ChoirHub**; purpose *helps a community choir's conductor manage members,
rehearsals and attendance, so nobody has to chase people on WhatsApp*; first feature *rehearsals
and replies*.

**Shall I create these?**

> **Sasha (assumed "yes" — the task allowed me to assume yes at every yes/no gate):** Yes.

---

## Message 2 — what exists now, and the three things only you can do

Done: 54 files in one commit on `main`. In short — ChoirHub now has a north star it can be
checked against, a roadmap of five milestones, a dashboard that says where every feature stands,
a decisions log with the stack and the three tripwires written down, a ten-stage process with
gates where your judgement is actually needed, and a first feature folder waiting for its PRD.
No application code, on purpose: the technical setup is milestone 0 and is tracked like a feature.

**Three things I cannot do for you** (they need a human, a password, and accepting terms). They
are in `docs/products/tech-setup/checklist.md`:

1. In the GitHub account you already have, create an empty repository called `choirhub`.
2. In the Vercel account you already have, connect it to that repository so `main` deploys.
3. Create a free Supabase project — this is the database and the sign-in in one — and keep the
   keys. I'll tell you exactly which variable names to paste them under; I never see them.

Optional, and only if you want singers to sign in with Google: a free Google OAuth client.
Email sign-in needs nothing extra. Payments: nothing to do until milestone 3.

**Before the PRD, one thing to read.** `docs/vision.md` is a first draft in your words, and it is
the document every future decision gets checked against, so it is worth ten minutes now. The end
state, five principles, what we will not do, and how we'd know we'd won. The principles are the
part I'd push on: number 1 ("the app does the tedious part; the person keeps the decision") is my
suggestion, not your words. Three of the non-goals are mine too and are marked as suggestions.

**Does the vision read right to you?** I'll start the PRD for *rehearsals and replies* the moment
you react. After the PRD: I run an applied-AI pass over it before you approve, then a design stage
where you'll open mockups in your browser and approve pictures rather than paragraphs, then the
spec. That's the shape of every feature from now on; I'll stop explaining it after this one.

> **Sasha (given in the task):** Looks right.

---

## Message 3 — the assessment, and one decision

Assessment of *rehearsals and replies*, before I write anything:

- **Size:** Full — new screens, new tables, a new permission boundary.
- **Has a screen:** yes. So there is a design stage and you approve mockups.
- **Risk:** privacy and sign-in. Singers' contact details and who-answered-what are both things
  the wrong person must never see, so the security pass runs at the spec and again at QA.
- **Depends on:** milestone 0 (tech setup), and on singers existing — which is why the thin
  *add a singer* step lives inside this feature.
- **Vision fit:** it is principle 1 made concrete, and the first of the three signs of winning
  ("before a rehearsal the conductor opens one screen instead of scrolling the group").
- **Recommendation:** go now. It is the smallest thing you can use on a Tuesday, and it is the
  exact job you called the worst.

**Go, later, or no?**

> **Sasha (assumed "go", per the task):** Go.

---

## Message 4 — the PRD draft, the AI opportunities, and six questions

Draft is in `docs/products/rehearsals-and-replies/prd.md`. The short version:

**Problem.** The answers arrive as a scroll of WhatsApp messages; counting takes twenty minutes
and is out of date when it finishes; the people who never answered get chased one at a time; and
afterwards nothing is left to look back at.

**Scope.** You add singers (name, email, section). You create a rehearsal with date, time, place,
an optional note and the songs. Singers sign in, see the term, and answer coming / can't make it
in one tap, changeable until the rehearsal starts. Singers see counts by section, never names.
You see names, in three groups, with contact details one tap away for chasing.

**Non-goals**, so the build stays small: no register of who actually turned up (milestone 2), no
fees, no repeating rehearsals, nothing sent from ChoirHub (you still post the link in WhatsApp),
no singer directory, no self sign-up, and no editing a past rehearsal's answers — by anyone,
including you.

**Success criteria**, which become your acceptance checklist later: a rehearsal created in under
a minute; a singer answering in one tap without asking how; you seeing the whole room the evening
before without counting; a singer never able to reach another singer's name-against-answer or
contact details; last week's answer still there this week and unchangeable.

**Where AI would remove a step** (four candidates, ranked; each has to remove a step or it does
not get built):

1. **Paste the WhatsApp message and I fill in the rehearsal** — date, time, place, songs — and
   show you what I understood before anything is saved. One confirmation, one correction at most.
   Removes retyping what you already wrote. *Recommend: now.*
2. **Draft the nudge for the people who haven't answered**, ready to copy into WhatsApp. Removes
   the chasing. *Recommend: later — ChoirHub deliberately sends nothing in this feature.*
3. **Pre-fill a new rehearsal from the last few** (same night, time, place). Makes typing nearly
   as fast as pasting, with no model involved. *Recommend: later — it needs a few rehearsals to
   learn from.*
4. **Flag singers whose replies are slipping.** *Recommend: later — it is already milestone 4,
   and one term of replies is too thin to see a pattern.*

**Six questions I need answered before you approve:**

1. How does a singer come to exist — you add them, or they sign themselves up?
2. What does a singer see about other people's answers: names, or just counts?
3. Do rehearsals repeat, and should ChoirHub create the term for you?
4. What are the sections?
5. How far ahead should a singer see?
6. How precise is "place" — a line of text, or something the app knows about?

Then: which AI items do you want, and is this approved?

> **Sasha (answers given in the task):** You add singers — name, email, voice section, keep it
> thin and inside this feature. Singers see counts only; I see names. We rehearse every Tuesday,
> and creating each one by hand is fine for now. Soprano, alto, tenor, bass. Singers see the whole
> term. Place is a line of text plus an optional note. Take the paste-the-message one now; park
> the rest.
>
> **Sasha (assumed, per the task):** Approved.

---

## Message 5 — approved and committed, and the five design questions

PRD approved and committed to `main`, index row moved to stage PRD, and the two parked AI items
are now one-liners on the roadmap so nobody re-proposes them from scratch. One thing changed
because of your choice: taking the paste step adds "external service" to this feature's risk
tags, because the pasted message goes to a language model to be read. That is recorded in the PRD
and it means the security pass covers it at the spec.

Next is design: I write what every screen does and build mockups you open in a browser. Before
that, ChoirHub needs a look, and it should be yours rather than mine. Five questions, one at a
time — this happens once for the whole project.

**Three adjectives for how ChoirHub should feel?** ("calm, warm, precise" — that kind of thing.)

> **Sasha (given in the task):** Calm, warm, clear.

**Two apps or sites whose look you admire, and one you don't?**

> **Sasha:** Linear and Airbnb. Not Facebook.

**Light, dark, or both?**

> **Sasha:** Both.

**Tone of voice in the interface?** ("friendly and brief", "formal", "dry")

> **Sasha:** Friendly and brief.

**Accessibility floor?** The default is: readable on a phone in sunlight, usable with one thumb,
WCAG AA contrast. Fine, or stricter?

> **Sasha:** The default.

---

## Message 6 — the design system, in four lines

Written into `docs/design/system.md` and recorded as decision D-004, so a session a year from now
knows why it looks like this:

- **Warm paper, not white,** with one accent — a terracotta — used for the primary action and
  nothing else. That is Linear's restraint with Airbnb's warmth, and it is the opposite of the
  busy, competing-for-attention thing you don't want.
- **Fraunces for headings, Inter for everything else.** A serif with character over a quiet body
  face; never more than two on a screen.
- **Light and dark both designed,** not one inverted into the other. Every colour pair was checked
  against the contrast floor before it went in — body text 15.8:1, the primary button 6:1.
- **Words that must be used:** rehearsal, singer, section. Words that must not: event, user, RSVP.

---

## Message 7 — the mockups are ready (this is the gate)

Eight screens, built on that system, in `docs/products/rehearsals-and-replies/mockups/`. Open
**`index.html`** in your browser — everything links from there, and your phone's light or dark
setting is what you'll see.

Walk them as a singer first — **Sign in → My rehearsals → Rehearsal** — because that is the part
everything depends on. Then as yourself: **Rehearsals → New rehearsal → the paste step → Who is
coming**, and **Singers** last.

| Screen | What it is |
|---|---|
| Sign in | An email link, no password. Also what a stranger sees: nothing. |
| My rehearsals | The singer's home. The next rehearsal's two buttons are on the list itself. |
| Rehearsal | One night in full: place, note, songs to prepare, how many are coming. |
| Rehearsals | Your term, each night with its three numbers. |
| New rehearsal | Creating one by hand, with the paste box waiting above the form. |
| New rehearsal · paste | The AI step end to end: thinking, what I understood, and the fallback. |
| Who is coming | The screen you open the evening before. Three groups, contact details one tap away. |
| Singers | The choir list. Thin on purpose. |

Every state is drawn, not just the happy one: empty lists, loading, a failed save, a rehearsal
that has already started and cannot be changed, someone who isn't on the choir list, a duplicate
email, and the model failing to read your message. A state nobody draws gets improvised in code,
badly.

I walked all eight against the ten-point critique before sending them, and three things changed
as a result: the reply buttons moved onto the list so answering is one tap from the link;
*No answer yet* moved to the top of your rehearsal screen, because it is the only group you can
act on; and the paste box's button lost its fill so that the one filled button on that screen is
still **Create rehearsal** — typing must never look like the punished path.

**Three things I'd like your reaction on:**

1. **The singer's one tap.** The two buttons sit on the list, and the detail screen repeats them.
   Right trade, or would you rather the list stayed a list?
2. **Who is coming.** *No answer yet* first, phone numbers one tap behind a name, and nowhere else
   in ChoirHub. Is that the screen you want open the evening before?
3. **The paste step.** "Here is what I understood" shows everything before saving and marks what
   it guessed at. Enough to trust weekly, or too much fuss?

Approving these means the build has to match them, screen by screen — so anything you want
different is cheapest to say now. Say "approved" and I'll write the spec.

> *(This is where the run stops. The mockups are not approved, the design is not committed, and
> no spec exists.)*

---

# Owner-facing messages — rehearsals-and-replies, design approval through the spec gate

Every message sent to Sasha in this session, in order. Calibrated to the owner profile in
`AGENTS.md` (understands how apps work, doesn't code · worked alongside product managers for
years): unusual terms glossed, gates named rather than explained, a recommendation plus one
alternative on every open question.

---

## Message 1 — after "approved" on the mockups

Design is locked. I've recorded the approval date in `design.md`, ticked the last box, moved
Rehearsals and replies to stage **Design** in the product index, and committed the design system,
the design, the eight mockups and the design-system decision (D-004) to `main`.

From here the mockups are the contract: the build has to match them screen by screen, and
anything you want different is a change to the design rather than a note in the code.

Next is the spec — how it gets built, with the permission rules, the migration, the test plan and
the rollout. Because this feature is tagged privacy, sign-in and external service, the security
threat pass runs inside it, and the CTO pass runs before you see it. I'll come back with the
plain-language version, the test plan and anything I need you to decide. No code until you
approve it.

---

## Message 2 — presenting the spec (the owner-approval gate; nothing is committed)

Spec drafted for Rehearsals and replies. Here it is in plain sentences, then the test plan, the
technical read, the security summary, and three things only you can answer.

**What it says, section by section**

- **What the app remembers:** three tables — the choir, the rehearsals, and every answer ever
  given. Answers are only ever added, never edited, which is your append-only rule made real:
  changing your mind writes a new row and the newest one shows.
- **What it does behind the screens:** eleven actions, from "send me a link" to "read this pasted
  message". Every one of them checks who is asking on the server, never in the browser.
- **The screens:** the seven you approved, at fixed addresses. `/r/<rehearsal>` is the link you
  paste into WhatsApp. A stranger who opens it gets the sign-in screen and stops there.
- **The AI step:** one, and only one. Paste, read, confirm, save. If it fails, is slow, is wrong,
  or is switched off, you get the ordinary form — and I've written ten real WhatsApp messages as
  the test set it has to pass before it goes anywhere near you.
- **Migration:** one script that adds three tables and their rules. It only adds, so running it
  twice changes nothing and rolling the code back never loses an answer.
- **The build:** seven work items. Two go first (the tables and the sign-in shell), the other five
  run in parallel, one screen group each.

**How it gets proved**

Fifteen test lines, walked by hand on localhost before anything is pushed. The first six are your
success criteria from the PRD, in your order: create a rehearsal by hand in under a minute;
create one from a pasted message in under ten seconds; a singer answers from the link on a phone
with nobody explaining how; you see the room the evening before without counting; a singer cannot
reach another singer's answer, email or phone from any screen *or by asking the database
directly*; and an answer given last week is still there this week and cannot be changed once the
rehearsal has started. Then every designed state on every screen, the permission table row by
row, the ten AI examples, the app with the model switched off, phone and desktop widths, and the
accessibility floor.

**The technical read, in two sentences**

The biggest risk is that a singer could reach another singer's answer or contact details, so the
spec puts every "no" inside the database as a rule rather than in the screens, and QA tests each
one by asking the database directly rather than by clicking. The simplest build that meets every
one of your success criteria is three tables, seven screens and one model call — and that is
exactly what this is: I took out a "choirs" table and a "sections" table that this milestone has
no use for, and added nothing the PRD didn't ask for.

Two choices are hard to undo, so both are now in the decisions log. **D-005**: the pasted message
is read by Anthropic's API, starting at the cheapest model tier and stepping up only if the ten
examples fail — at forty rehearsals a year the whole year costs under a euro, so quality decides,
not price. **D-006**: one choir, with no "which choir" column on anything, because the vision says
one choir run well comes before many — a second choir would be a week's work later, knowingly
deferred. Two deliberate shortcuts are logged in `docs/tech-debt.md` with a pay-by milestone:
songs stored as lines of text rather than as their own records, and the conductor being made a
conductor by an edit in the database rather than by a screen.

**Security, in terms of who can see and do what**

You see everything: names against answers, emails, phones. A singer sees the term, one
rehearsal's details, how many are coming by section — and their own answer. Nothing else, on any
screen, and not by asking the database directly either: the rules sit on the tables, so the
browser's developer tools get the same answer the screen does. Nobody can change or delete an
answer once it exists, including you — there is no such command in the app or in the database.
Someone who signs in without being on your list sees "You're not on this choir's list yet" and no
choir data at all. The only thing that leaves ChoirHub is the text you paste, and only after the
box has told you so; the app never captures a phone number or an email out of a pasted message,
and an instruction hidden inside one ("ignore the above and...") can't do anything, because the
answer is locked to the six fields on the card.

The threat pass also found a gap in the tripwires: they say a singer never sees another singer's
*contact details*, but the rule this feature actually has to hold is wider — a singer never sees
**who answered what**. I've added that line to the tripwire list in `AGENTS.md`; it lands with
this spec.

**Three things I need from you**

1. **The phone number.** The contact sheet you approved shows Anna's phone, but the Add singer
   form only has name, email and section — so there is nowhere for a phone number to come from.
   *Recommendation:* add an optional phone field to Add singer, and hide the Phone row on the
   sheet when it's empty. That's one field and one line in the design. *Alternative:* drop the
   phone from the sheet and chase people from your own phone's contacts, as you do today.
2. **Fixing a typo.** There is no edit screen in the design, so a rehearsal created with the wrong
   place or time can't be corrected — and it can't be deleted either. *Recommendation:* let you
   edit a rehearsal's time, place, note and songs until it starts, reusing the New rehearsal form
   from the Who is coming screen. One extra work item, one line in the design. *Alternative:*
   ship without it and treat a typo as a new rehearsal plus an apology in the group; I'd rather
   not.
3. **Very small sections.** Singers see "18 coming · S 5 · A 4 · T 4 · B 5". If a section ever had
   one singer in it, that chip would tell the whole choir how that person answered.
   *Recommendation:* when a section has fewer than three singers, show the total only and drop
   the chips. Your choir has five to seven per section, so today you'd never see it.
   *Alternative:* leave it as designed and accept that a one-person section is readable.

**The gate.** This is the spec approval. Answer those three, say "approved", and I record the
date, tick the checklist, move the index to stage Spec and commit it to `main` — and only then
does building start: branch `feat/rehearsals-and-replies`, the migration first, then the seven
work items with me reviewing each against the spec and the mockups. Nothing is committed and no
code exists until you do.
