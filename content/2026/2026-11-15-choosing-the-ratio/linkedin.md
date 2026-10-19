# LinkedIn — choosing-the-ratio


Oversubscription is not a dirty word. Undeclared oversubscription is.

Every network you have ever run was oversubscribed somewhere. The access layer assumes not every port transmits at once. The uplink assumes not every access switch bursts together. The internet circuit assumes a fraction of what the LAN could theoretically generate. This is not a compromise anybody snuck past you. It is what makes the network affordable.

Designing for zero contention means buying capacity the business will never use, and justifying it every budget cycle to somebody who can see the utilization graphs.

The real problem is not the ratio. It is that in most estates nobody can tell you what it is.

Somebody chose 20 to 1 at the access layer in 2019, for reasons that made sense with the traffic patterns of 2019. Then video conferencing became constant rather than occasional, a backup job moved into business hours, and three sites started replicating to each other. The ratio did not change. The thing it was a bet about did.

So the question we ask on an assessment is not "are you oversubscribed." Everyone is. It is: what ratio did you choose, what did you assume about traffic, and when did anybody last check that assumption.

If nobody can answer the first part, the ratio was not chosen. It was inherited from a default, a budget constraint or a predecessor, and it is now a load-bearing assumption nobody has examined.

A deliberate 20 to 1 that gets reviewed yearly is engineering. An accidental 20 to 1 that nobody remembers agreeing to is a liability that happens to be working.

The capacity conversation is not about whether to oversubscribe. It is about whether you can defend the number when it finally matters.

What is your access layer ratio, and who chose it?

#NetworkEngineering #NetOps #CapacityPlanning
