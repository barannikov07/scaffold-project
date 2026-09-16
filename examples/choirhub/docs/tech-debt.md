# Tech debt

Deliberate shortcuts, each with a date it comes due. Added by the CTO pass at spec or at tech
setup; reviewed at every Close. A row is closed when the work ships, with the pull request.
Nothing here is a surprise: if it is not on this list, it is not debt, it is a bug.

| # | Shortcut | Why it was taken | Pay by (milestone) | Cost of not paying | Closed |
|---|---|---|---|---|---|
| 1 | A rehearsal's songs are an ordered list of text lines on the rehearsal row, not their own table | The design's input is "one song a line" and nothing in milestone 1 reads a song as a thing in its own right. A table would be four columns and a join for no screen | 2 (attendance record), or whenever "what to prepare" gets parts, notes or links attached to a song | A song cannot carry an attachment or be linked to across rehearsals. Paying it later is a `create table` plus a backfill from the arrays — additive, and easy while the term is small | |
| 2 | The conductor is made a conductor by editing one row in the database by hand; there is no way to name a conductor inside the app | There is exactly one conductor, and a screen that grants the highest permission in the product is the most dangerous screen we could build first. Doing it by hand keeps the grant off the request path entirely (see the spec's Security section) | 2, or immediately if a second conductor or a section leader appears | Every change of conductor needs an agent and a database console. Harmless at one conductor, embarrassing at two | |
