# LinkedIn — sla-is-not-a-design

An SLA is not a design.

Four nines on the contract. One fiber path in the ground. One power feed at the demarc.

We've walked sites where the paperwork promised 99.99% and the physical reality was a single entrance facility, a single lateral into the building, and two "diverse" carriers whose fiber shared the same conduit under the same bridge. Diverse on the invoice. Adjacent in the dirt.

None of that is fraud. It's just that nobody asked the physical question, because the contract had already answered a different one.

Here's the distinction that matters: an SLA transfers risk. It does not reduce it.

When the fiber gets cut, the agreement tells you what you're owed. A service credit arrives, eventually, and it's usually a fraction of one month's bill. The credit does not run payroll. It does not open the stores. It compensates you for the outage; it was never designed to prevent one.

So the useful questions aren't in the contract:

→ Where do the two paths physically diverge — and can somebody show you on a map, not a logical diagram?
→ Whose conduit is that, and who else is in it?
→ What's the real restoration time for a cut in that metro, as opposed to the MTTR printed on the agreement?
→ When the primary is down, what actually runs — everything, or the subset somebody chose three years ago and nobody has revisited since?

Every one of those has an answer today. None of them require an incident to discover.

The teams that get this right treat the SLA as the floor, not the plan. They buy the agreement, then design as though it doesn't exist — because on the day it matters, it effectively doesn't.

An SLA tells you what you're owed when it breaks. A design tells you whether it breaks.

When did anyone last walk the physical path your redundancy depends on?

#NetworkDesign #Resilience #NetOps
