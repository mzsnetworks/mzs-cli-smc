# Master — when-did-it-last-work

**Preset:** Professional (LinkedIn personal profile + Instagram @mzsnetworks)
**Date:** 2026-10-06
**Thesis:** "What changed?" sends you into a document written by people about what they remembered to write down, and it accepts "nothing" as an answer. "When did it last work?" is answerable from evidence, bounds the search to a window, and survives three people's disagreeing accounts.
**Pillar:** Enterprise Network Ops
**Source:** ideas-2026-08-27 #1
**Stats:** none. Judgment and practice only; no statistic stated as fact.

---

"What changed?" is the wrong first question.

It sounds right. Something worked, now it does not, so something must have changed. The logic is fine. The problem is where it sends you: into the change record, which is a document written by people about the things they remembered to write down.

The changes that cause outages are disproportionately the ones nobody logged. A certificate that expired on its own. A lease that did not renew. A scheduled job that ran for the first time in a year. A vendor pushing an update to something you do not administer. None of that is in your change record, and a search that starts there will quietly conclude nothing changed.

"When did it last work?" sends you somewhere else.

It is answerable from evidence rather than memory: a graph, a log line, a transaction that completed, a ticket that closed. And the answer bounds the problem. If it last worked at 3:40, then whatever you are looking for happened after 3:40, and the universe of possible causes collapses to a window you can actually search.

It also survives disagreement. Three people will give you three accounts of what changed, all sincere, none complete. A timestamp on a graph is nobody's recollection.

The practical version: before you open the change log, establish the last known good. Ask what the most recent evidence of correct behavior is and when it was. Then ask what happened inside that window, from every source, not only the ones staffed by people who file tickets.

The failure mode of "what changed" is that it accepts "nothing" as an answer. The failure mode of "when did it last work" is that somebody has to go and look.

That is the whole difference.
