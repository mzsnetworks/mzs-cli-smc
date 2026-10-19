# LinkedIn — root-cause-is-a-decision


Root cause is usually a decision, not a device.

Five whys works right up until the honest answer names a tradeoff somebody made. Then it quietly stops.

You have read the report. The supervisor failed. Why did the supervisor failing take the site down? Because the redundant path was not carrying the routes it was supposed to. Why not? Because a migration config was never reverted. Why wasn't that caught? Because the validation step was dropped when the maintenance window got compressed. Why was it compressed?

That is where the document usually ends: "hardware failure."

But the chain was still going. The window got compressed because the change had already slipped twice and a business deadline was fixed. Somebody weighed a real risk against a real cost and chose. Given what they knew, it was probably right.

Naming it is not blame. It is the only way to change the outcome, because the device was never the variable. You cannot buy a supervisor that survives having its redundancy silently removed.

What makes this hard is that the last "why" stops being technical and starts being organizational, and the person who has to write it down usually reports to the person who made the call.

So the postmortems that actually change anything tend to share two habits. They record the constraint, not just the event — "the window was compressed to meet a fixed date" is a finding, and it is actionable in a way that "human error" never is. And they separate the decision from the outcome, because a reasonable decision can still produce an outage, and pretending otherwise teaches people to hide their reasoning rather than improve it.

A postmortem that ends at a component has found where the failure surfaced. It has not found why it was possible.

Where do your five whys usually stop?

#NetworkEngineering #NetOps #IncidentResponse
