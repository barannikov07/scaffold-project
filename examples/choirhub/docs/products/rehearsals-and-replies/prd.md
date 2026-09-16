# PRD: Rehearsals and replies

Status: Approved · Approved on: 2026-09-16 · Build started on: not yet

A PRD says what we are building and why, in the owner's language. It is a draft until the build
starts and a record of what was agreed after that. If reality turns out different, the guide
records it; if you change your mind, that is a new PRD in this folder, not an edit of this one.

## Assessment

| | |
|---|---|
| Size | Full: new screens, new tables, a new permission boundary |
| Has UI | yes — the Design stage applies |
| Risk tags | privacy · sign-in · external service |
| Depends on | Milestone 0 (tech setup). Hidden dependency: replies mean nothing until singers exist, so a thin "add singers" step is inside this feature rather than before it |
| Decision | go, by Sasha, 2026-09-16 |

The external-service tag was not in the first assessment. It was added on 2026-09-16 when the
paste-a-message opportunity below was chosen, because pasted text then leaves the app to a model
provider. The security playbook's threat pass at Spec covers all three tags.

## Vision fit

This is the vision's first principle made concrete: "the app does the tedious part; the person
keeps the decision". It attacks the exact job Sasha named as the worst one — counting replies in
WhatsApp and chasing the people who never answered — and it is the first of the three signs of
winning: "before a rehearsal the conductor opens one screen instead of scrolling the group, and
believes what it says". It also puts the second principle under test: a singer's answer has to be
one tap on a phone, or the replies will keep happening in WhatsApp.

It strains nothing in the vision. It deliberately stops short of two things the vision wants
later — the register of who actually turned up, and fees — because both need the rehearsal to
exist first.

## Problem

Today the conductor posts the rehearsal in the WhatsApp group and the answers come back as a
scroll of messages, thumbs-up emoji and side conversations. Counting them takes twenty minutes
and the count is already out of date when it is finished; the people who never answered have to
be chased one at a time. Nobody has a trustworthy list before the night, and afterwards nothing
is left to look back at. The cost is an evening a week of admin for a person who joined a choir
to make music, and a rehearsal where the conductor does not know whether the tenors will be four
or one.

## Users

- **The conductor.** Plans the rehearsals, adds the singers, and is the only person who sees who
  answered what. Usually at a laptop when planning, on a phone the evening before.
- **The singers.** Adults with day jobs. They arrive through a link, sign in, glance, tap once,
  and leave. They see their own choir life and the size of the room, never each other's details.

## Scope

What this feature does. Short bullets, each one observable.

- The conductor adds a singer with a name, an email and a voice section (soprano, alto, tenor,
  bass). Thin on purpose: no profiles, no photos, no history — just enough for a singer to sign
  in and be counted.
- The conductor creates a rehearsal: date and time, place (a line of text) with an optional note,
  and the songs for that night.
- The conductor can instead paste the message they already wrote in WhatsApp, or dictate it, and
  ChoirHub proposes the rehearsal — date, time, place, songs — on a confirmation card. Nothing is
  saved until the conductor confirms, and the ordinary form is always there.
- A singer signs in and sees every rehearsal in the term, next one first, with the place, the
  note and the songs to prepare.
- A singer answers "I'm coming" or "Can't make it" in one tap, and can change that answer until
  the rehearsal starts.
- A singer sees how many are coming, by section. Never who.
- The conductor sees, for each rehearsal, who is coming, who is not, and who has not answered
  yet, by name and section, with contact details one tap away for chasing.
- Every answer is stored as a new entry. Changing an answer supersedes the old entry; nothing is
  overwritten, and once the rehearsal has started nothing changes at all.

## Non-goals

What this feature deliberately does not do, even though someone will ask. This is the section
that keeps the build small.

- No register of who actually turned up. Replies are intentions; attendance is milestone 2.
- No fees or payments of any kind.
- No repeating rehearsals. The choir rehearses every Tuesday and Sasha is happy to create each
  one by hand for now; a generator waits until that stops being true.
- No messages sent from ChoirHub: no chat, no notifications, no emails, no WhatsApp integration.
  The conductor still posts the link in the group, as today.
- No singer directory. A singer never sees another singer's email, phone number, or individual
  answer — only the counts.
- No self sign-up. A singer exists because the conductor added them; anyone else who signs in is
  told to ask the conductor.
- No editing of a past rehearsal's answers, by anyone, including the conductor.
- No assistant to chat with. A chat box on the side of this feature removes no step; every AI
  item below either removes a step or is not built (see AI opportunities, rows 2 to 4).

## Flows

The main path and the important alternatives, as numbered steps the owner can picture. One
flow per heading.

### Main flow: the conductor plans next Tuesday

1. The conductor signs in and opens **Rehearsals**, which lists the term, next one first.
2. Taps **New rehearsal** and fills in date and time, the place, an optional note ("side door is
   locked, use the courtyard"), and the songs.
   - **Or** pastes the message they already wrote in WhatsApp into **Paste a message** and taps
     **Read it**. ChoirHub shows *Here is what I understood* — date, time, place, songs — with
     anything it is unsure about marked. The conductor corrects a field or taps **Create
     rehearsal**. Nothing is saved until that tap. If the reading is nonsense, or the model is
     unavailable, the form is there with whatever was understood and the conductor types.
3. The rehearsal is saved and appears at the top of the term list.
4. The conductor copies the link and posts it in the WhatsApp group, exactly as today.

### The singer answers

1. The singer taps the link and signs in with an email link or with Google.
2. **My rehearsals** shows the term, next one first: date, place, note, songs.
3. One tap: **I'm coming** or **Can't make it**. The answer is saved immediately and the screen
   says so.
4. The singer sees how many are coming, by section — "18 coming · S5 A4 T4 B5" — and can change
   their own answer until the rehearsal starts.

### The conductor sees the room before the night

1. The evening before, the conductor opens the rehearsal.
2. Three groups, by name and section: **Coming**, **Can't make it**, **No answer yet**, with a
   count on each.
3. Tapping a name in **No answer yet** shows that singer's email and phone so the conductor can
   chase them in WhatsApp by hand. This is the only screen in ChoirHub where contact details
   appear, and only the conductor can open it.

### When things go wrong

- **The rehearsal has already started.** The answer buttons are gone for everyone; the rehearsal
  is read-only, with one line saying why. This is the append-only tripwire made visible.
- **The paste step misreads the message, or the model is down.** The conductor lands in the
  ordinary form, prefilled with whatever was understood or empty, and types. The feature never
  depends on the model being right or available.
- **A singer is added twice.** The second add is refused with a line naming who already has that
  email.
- **Someone signs in who was never added.** They see "You are not on this choir's list yet. Ask
  your conductor to add you." and nothing else. No choir data is visible.
- **A singer answers on two devices.** The latest entry wins on screen; both entries stay in the
  history.

## Success criteria

How we will know it worked. Each line is something a person can check by using the product, and
it becomes the owner's acceptance checklist in QA.

- The conductor creates next Tuesday's rehearsal, with place and songs, in under a minute using
  the form.
- The conductor creates a rehearsal from a pasted WhatsApp message in under ten seconds, with one
  confirmation and at most one field corrected.
- A singer who has never seen ChoirHub answers "coming" from the link, on a phone, without asking
  anyone how.
- The evening before, the conductor sees who is coming, who is not, and who has not answered,
  without counting anything and without opening WhatsApp.
- A singer can see how many are coming but cannot reach another singer's name against an answer,
  email, or phone number from any screen.
- An answer given last week is still there this week, and no screen in ChoirHub can change an
  answer once the rehearsal has started.

## AI opportunities

Filled by the applied-AI pass after the first draft. Every row gets a decision: chosen (now in
Scope and Flows, with the confirmation step shown), deferred (a roadmap Later row), or rejected
(in Non-goals with the reason).

| # | Opportunity | Step it removes | Gain | Risk | Cost class | Decision |
|---|---|---|---|---|---|---|
| 1 | Paste the WhatsApp message, or dictate it, and ChoirHub proposes the rehearsal — date, time, place, songs — for one confirmation | The conductor retyping into a form what they already wrote in the group | "Under a minute" becomes "under ten seconds"; the conductor plans on a phone, standing up | privacy: the pasted text goes to a model provider and may contain singers' names · external service | a few seconds and cents | **Chosen.** In Scope and in the main flow, with the confirmation card and the manual form kept |
| 2 | Draft the nudge for the singers who have not answered, ready to send or to copy into WhatsApp | The conductor writing the same chasing message every week and working out who it goes to | Removes the second half of the job Sasha called the worst; serves "a term with no 'who is coming tomorrow?' message" | privacy: names in a draft · needs a way to deliver it | instant and cheap | **Deferred.** ChoirHub sends nothing in this feature, by design. Roadmap "Later" row, linked here |
| 3 | Pre-fill a new rehearsal from the last few: same night, same time, same place, songs left blank | Retyping the same place and time every Tuesday | Makes the manual path nearly as fast as the paste path, with no model call and no data leaving | none: it is arithmetic over the choir's own history | instant and cheap | **Deferred.** Needs a few rehearsals to learn from. Roadmap "Later" row, linked here |
| 4 | Flag singers whose replies are slipping, with the evidence behind the flag | The conductor noticing from memory who has drifted away | The whole point of milestone 4 | privacy | background job | **Deferred.** It is already milestone 4, and a term of replies is too thin to see a pattern |

## Open questions

All answered by Sasha on 2026-09-16, before approval. Kept here as the record of what was asked.

- How does a singer come to exist? → The conductor adds them: name, email, voice section. Kept
  thin and inside this feature.
- What does a singer see about other people's answers? → Counts only. The conductor sees names.
- Do rehearsals repeat? → Every Tuesday, but creating each one by hand is fine for now.
- What are the sections? → Soprano, alto, tenor, bass.
- How far ahead can a singer see? → The whole term.
- How precise is "place"? → A line of text, plus an optional note.

## Before this passes

The gate for stage 3. The agent ticks the first four when they are true; only the owner ticks
the last two. The owner approves only when every box is ticked.

- [x] Vision fit names a specific goal or principle
- [x] Non-goals section has at least one real exclusion
- [x] Every success criterion is checkable by using the product
- [x] AI opportunities considered, each with a decision; chosen ones visible in Scope and Flows
- [x] Every open question is answered or moved to the spec as a design question
- [x] Owner has read it and said "approved"
