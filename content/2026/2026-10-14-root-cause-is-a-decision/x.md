# X — root-cause-is-a-decision


## Single (publish this)

Root cause is usually a decision, not a device.

Five whys works right up until the honest answer names a tradeoff somebody made. Then the document ends and the finding reads "hardware failure."

The device was never the variable.

#NetOps #IncidentResponse

---

## Thread

1/ Root cause is usually a decision, not a device.

Five whys works right up until the honest answer names a tradeoff somebody made. Then it quietly stops. 🧵

2/ The supervisor failed.

Why did that take the site down? The redundant path wasn't carrying the routes it was supposed to.

Why not? A config was changed during a migration and never reverted.

3/ Why wasn't that caught?

The validation step was dropped when the maintenance window got compressed.

Why was it compressed?

4/ That's where the document ends. The finding reads "hardware failure."

But the chain was still going.

5/ The window got compressed because the change had already slipped twice and a business deadline was fixed.

Somebody weighed a real risk against a real cost and chose. Given what they knew, probably correctly.

6/ Naming that isn't blame. It's the only way to change the outcome.

You cannot buy a supervisor that survives having its redundancy silently removed. The device was never the variable.

7/ Postmortems that change anything do two things:

• Record the constraint, not just the event
• Separate the decision from the outcome

A reasonable decision can still produce an outage. Pretending otherwise teaches people to hide their reasoning.

#NetOps #IncidentResponse
