# LinkedIn — change-freezes-batch-risk

Change freezes don't reduce risk. They batch it.

Every December, the same ritual: freeze the network. Nothing changes, so nothing breaks. It feels like safety. It reads well in a status meeting.

Then January arrives — and every postponed change lands in the same two weeks. The diffs are bigger. The context is stale. The engineer who scoped the change in November is reconstructing their own reasoning from a ticket comment. And everything moves at once, so when something breaks, "what changed?" has thirty answers.

Here's the mechanism: the risk of a change isn't the date you run it. It's the size of the diff, times the staleness of the context, times how much else is moving around it. A freeze inflates all three — then releases them together.

Small, frequent, well-reviewed changes are the lowest-risk shape we know. A freeze outlaws exactly that shape and calls it prudence.

I understand why freezes exist. Skeleton crews, revenue-critical weeks, nobody wants to be the reason the quarter-end went dark. That part is real.

But the honest version is narrower: freeze the risky and the optional, keep the small and the routine flowing, and staff the thaw like the event it is. If a calendar block is your strongest safety control, your change process is built on abstinence — not on discipline.

A freeze doesn't cancel risk. It schedules it — for the first week the calendar thaws.

Small changes, often, reviewed: that's safety. Big changes, batched, rushed: that's January.

Does your org freeze? What does the first week after look like?

#ChangeManagement #NetworkEngineering #SRE
