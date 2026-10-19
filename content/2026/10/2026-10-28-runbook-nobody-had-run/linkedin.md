# LinkedIn — runbook-nobody-had-run


We were asked to automate a site failover runbook. Routine work, or so it looked.

The document was in good shape. Version controlled, reviewed every quarter, signed off. What it had not been in two years was run.

It had been tested by reading. Somebody followed the steps with their eyes, agreed it still made sense, and marked the review complete. That verifies exactly one thing: the document is still readable.

Automating it meant every ambiguity had to be resolved before anything could run. Three did not survive the translation.

One step referenced a VLAN by name. The VLAN had been renumbered during a refresh eighteen months earlier. A person reading the step would have silently corrected it. A script would have failed, or worse, matched something else.

Another ordered service restarts that would have brought the application up before its database was accepting connections. In a real failover somebody notices and reorders, and afterward nobody writes that down.

The third was the verification step. It checked that the interface came up. Not that traffic was flowing, not that sessions had re-established, not that the application answered. An interface being up is the weakest possible evidence that a failover worked, and it was the only evidence the runbook asked for.

None of this was found by testing the automation. It was found by writing it.

The value did not arrive when the script ran. It arrived when the procedure had to be stated precisely enough that its gaps became visible — and every one of them had been sitting in an approved, quarterly-reviewed document the whole time.

Encoding a runbook is the cheapest audit you will ever run, and it happens whether the automation ships or not.

When did you last run yours, rather than read it?

#NetworkAutomation #NetOps #ITOperations
