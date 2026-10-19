# Master — runbook-nobody-had-run

**Preset:** Business (LinkedIn company page + Facebook + Instagram + X, all on the MZS account)
**Date:** 2026-10-28
**Thesis:** We automated a failover runbook nobody had executed manually in two years. Encoding it revealed the procedure had been quietly wrong the whole time. Automation's first return is not speed — it is that a procedure finally has to be stated exactly enough to be wrong out loud.
**Pillar:** Network Automation
**Source:** ideas-2026-08-30 #15
**Stats:** none. Field narrative and judgment; no statistic stated as fact.

---

We were asked to automate a site failover runbook. Routine work, or so it looked.

The document was in good shape. Version controlled, reviewed every quarter, signed off. What it had not been in two years was run.

It had been tested by reading. Somebody opened it, followed the steps with their eyes, agreed it still made sense, and marked the quarterly review complete. That is a real and common practice, and it verifies exactly one thing: that the document is still readable.

Automating it meant turning each step into something a machine could execute, which meant every ambiguity had to be resolved before anything could run. Three of them did not survive the translation.

One step referenced a VLAN by name. The VLAN had been renumbered during a refresh eighteen months earlier. A person reading the step would have silently corrected it. A script would have failed, or worse, matched something else.

Another ordered a sequence of service restarts that would have brought the application up before its database was accepting connections. In a real failover somebody would have noticed the errors and restarted things again in a different order, and afterward nobody would have written that down.

The third was the verification step. It checked that the interface came up. Not that traffic was flowing, not that sessions had re-established, not that the application answered. An interface being up is the weakest possible evidence that a failover worked, and it was the only evidence the runbook asked for.

None of this was discovered by testing the automation. It was discovered by writing it.

That is the part worth taking away. The value did not arrive when the script ran. It arrived when the procedure had to be stated precisely enough that its gaps became visible — and every one of those gaps had been sitting in an approved, quarterly-reviewed document the whole time.

A runbook nobody executes is a description of how the failover went the last time somebody remembered it. Encoding it is the cheapest audit you will ever run, and it happens whether the automation ships or not.
