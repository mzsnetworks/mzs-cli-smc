# Instagram — when-did-it-last-work


"What changed?" is the wrong first question. 🕰️

It sounds right. Something worked, now it doesn't, so something changed.

The problem is where it sends you: into the change record. A document written by people, about the things they remembered to write down.

The changes that cause outages are disproportionately the ones nobody logged:

→ A certificate that expired on its own
→ A lease that didn't renew
→ A scheduled job that ran for the first time in a year
→ A vendor updating something you don't administer

A search that starts in the change log will quietly conclude nothing changed. ⚠️

"When did it last work?" sends you somewhere else.

It's answerable from evidence, not memory — a graph, a log line, a transaction that completed.

And the answer bounds the problem. If it last worked at 3:40, the cause is after 3:40, and everything else just fell off the list.

It also survives disagreement. Three people give three sincere, incomplete accounts of what changed. A timestamp on a graph is nobody's recollection.

"What changed" accepts "nothing" as an answer. "When did it last work" makes somebody go and look.

What's your first question when something that worked stops working?

#NetworkEngineering #IncidentResponse #NetOps #ITOps #Troubleshooting
