# The interview

Ask one question at a time. Each question comes with an example answer and a "you decide"
option, because a non-technical owner often does not know they are allowed to delegate the
choice. If the owner answers several questions in one message, skip the ones already covered.
Keep your own messages short; the owner should be doing most of the talking.

Where the owner's answer is vague, ask one follow-up at most, then move on and mark the gap as a
`TBD(owner):` line in the relevant document. Do not invent to fill a gap.

## Questions

Two questions about the owner come first. They set how Claude talks for the life of the project:
how much to explain, how many options to show, whether code ever appears. They never change what
the process requires. Three answers each, no "you decide".

0a. **How technical are you?**
    Never written code · I understand how apps work but don't code · I can read code.
0b. **How familiar are you with product development?**
    Never written a PRD · Worked alongside product managers · I am a product manager.
    Record both in the owner profile block of CLAUDE.md (passed to the stamping script as
    `TECH_LEVEL` and `PRODUCT_LEVEL`). The behaviour each answer buys is in workflow.md,
    "How Claude talks to the owner".

1. **What is the project called?**
   Example: "Orbit" or "Family Meal Planner". A working name is fine; it can change.

2. **In one sentence, what will it do for whom?**
   Example: "Helps small landlords track rent payments and send reminders."
   This sentence becomes the purpose line in CLAUDE.md and the seed of the vision.

3. **When this is finished and working perfectly, what exists? Describe the end state.**
   Example: "Every tenant pays through the app, landlords never chase anyone, and taxes are
   one click." Push gently for the ambitious version; this is the vision's north star.
   Follow-up if thin: "What would make you say it was worth building?"

4. **Who uses it? Are there different kinds of users with different powers?**
   Example: "Landlords, who manage everything, and tenants, who only see their own payments."
   This decides whether roles and permissions exist.

5. **Do people need to sign in? If so, how would they like to?**
   Example: "Email and password" or "Google login" or "you decide".
   "No sign-in" is a valid answer for tools and public sites.

6. **Does it store information that must not be lost or must not be seen by the wrong person?**
   Example: "Payment history must never be deleted; tenants must never see each other's data."
   Answers here become the first tripwires and shape the data model section of infra.md.

7. **Does money move through it, now or eventually?**
   Example: "Yes, tenants will pay rent through it later" or "No".
   A yes adds a money tripwire and a payments provider to the identities list.

8. **What is the first thing you want to be able to use?**
   Example: "Add a property and a tenant, and see who has paid this month."
   This is the first feature and the first PRD. Keep it to one thing that can be built and
   accepted on its own. If the owner names three things, help them pick the one the others
   depend on. Then check the hidden dependency: does this feature need people or records to
   exist first (members to invite, a list to fill, an account to link)? If so, ask whether a thin
   version of that belongs inside the first feature or comes before it. Most first features
   need a thin "add the people" step; say so plainly and record the answer for the PRD.

9. **Where should it run? (Optional; skip if the owner shrugs.)**
   Example: "A website" or "phone app" or "you decide". Default is a website.

10. **Anything you have already decided or already have?**
    Example: "I already have a Vercel account" or "It must work in Polish". Captures existing
    constraints so they land in decisions or infra rather than being rediscovered.

## Turning answers into a stack

Pick a default when the owner says "you decide". State the choice back in one sentence with one
short reason per part, then record the whole thing as D-001 in the decisions log.

| Signal from the interview | Choice | Reason to give the owner |
|---|---|---|
| Website, no strong constraint | Next.js (React framework) | Widely used, Claude builds it reliably, hosts on Vercel with zero configuration |
| Stores data | Postgres via Supabase | A real database with backups, plus built-in sign-in, on a free tier to start |
| Sign-in needed | Supabase Auth | Comes with the database; email/password and Google out of the box |
| No data at all | No database; static or file-based | Nothing to migrate or secure |
| Money moves | Stripe | The standard; never store card details yourself |
| Hosting | Vercel via GitHub | Push to GitHub, Vercel deploys. No command-line deploys, ever |
| Phone app | Ask one more question: is a website that works well on phones enough? Usually yes. If a true app is needed, Expo (React Native) and say the process is unchanged |

If the owner already has accounts or preferences, those win over the defaults. Record what won
and what was rejected in D-001.

## Deciding the first feature's slug

Lowercase, hyphenated, two or three words that name the capability, not the screen:
`rent-tracking`, `tenant-onboarding`, `weekly-plan`. This becomes the folder under
`docs/products/` and the branch name later, so it should still make sense in a year.
