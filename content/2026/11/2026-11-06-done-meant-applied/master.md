# Master — done-meant-applied

**Preset:** Business (LinkedIn company page + Facebook + Instagram + X, all on the MZS account)
**Date:** 2026-11-06
**Thesis:** A maintenance window that finishes early is usually a window where verification was skipped rather than one where the work went well. "Done" has to mean verified against the condition the change was meant to produce, not applied without error.
**Pillar:** Lessons from Production
**Source:** ideas-2026-08-30 #30
**Stats:** none. Judgment and field practice only; no statistic stated as fact.

---

A maintenance window that finishes two hours early is not good news.

We have learned to ask what got skipped. Usually nothing was skipped on purpose. The work went in cleanly, nothing threw an error, the team was tired, and "applied without error" quietly became "done."

Those are not the same state, and the gap between them is where Monday morning lives.

The pattern is specific. A change goes in Saturday night. Every command returns without complaint. Interfaces come up, the device is reachable, the config matches what was staged. By every signal available at 2am, it worked. Then Monday arrives, real traffic shows up with real patterns, and something that only manifests under load or only on the path nobody tested starts failing.

The window was not too short. The definition of done was too small.

"Applied" is a statement about the device. "Verified" is a statement about the service, and only one of them is what the business asked for.

So we write the verification into the change record before the window opens, as a named condition with a named owner. Not "confirm change successful" — that is a checkbox, and a tired engineer will tick it honestly while meaning something narrower than you do. Something closer to: this specific transaction completes, from this specific client, measured this way.

Then the window is not over when the work is applied. It is over when that condition is observed, or when it is not and the rollback runs.

The inconvenient part is that this makes windows longer and more honest. A window that runs its full length because somebody is watching a real transaction is not inefficiency. It is the only part of the night that produces evidence.

A change that was applied is a change you made. A change that was verified is a change you can defend.
