# Master — Postmortems Are Becoming Code Review

**Idea:** ideas-2026-07-08 #14 (LP, Prediction). Postmortems are becoming code review — where "human error" stops being a root cause.
**Spine:** hook (human error disappearing) → POV (the mistake is now a commit) → data (SRE 70% of outages = changes; DORA failure→inquiry) → judgment (review and postmortem are the same activity in different tenses) → landing (triad + question).

---

"Human error" is quietly disappearing from root-cause fields. Not because engineers stopped making mistakes.

Because the mistake is now a commit.

When your network runs on code, every outage traces back to a diff. That diff had an author. It also had a reviewer who approved it, tests that passed it, and a pipeline that shipped it to production without hesitation.

Blame the human and you have to explain the other three.

Google's SRE book puts a number on why this matters: roughly 70% of outages are due to changes in a live system. Changes used to be keystrokes in a terminal window nobody watched. Now they're commits — with an author, an approval, a test run, a timestamp. The failure didn't change. The evidence did.

And once the evidence is a diff, the postmortem stops interrogating a person and starts interrogating a change. DORA's culture research has said this for years: in generative cultures, failure leads to inquiry. In pathological ones, it leads to scapegoating. Blameless isn't a courtesy — remove the blame and you remove the fear, and problems finally surface while they're still cheap.

Operationally, this means two rituals are converging into one discipline. Code review inspects a change for how it might fail. A postmortem inspects a change for how it did. Same activity, different tense.

Teams that notice this get better at both. Reviews start asking "how does this break at 2am?" instead of "is this formatted right?" Postmortems end in a merged fix instead of an action-item graveyard.

Code review is the postmortem you run before the incident.
The postmortem is the code review you run after.
The best teams are making them the same conversation.

When did "human error" last close one of your postmortems?

---

**Sources**
- Google, *Site Reliability Engineering* (O'Reilly, 2016), Introduction — "SRE has found that roughly 70% of outages are due to changes in a live system." https://sre.google/sre-book/introduction/
- DORA, *Generative organizational culture* (Westrum model; blameless postmortems — "failure leads to inquiry"). https://dora.dev/capabilities/generative-organizational-culture/
