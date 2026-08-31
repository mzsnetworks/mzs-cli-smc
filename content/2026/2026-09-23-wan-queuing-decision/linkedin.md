# LinkedIn — wan-queuing-decision


Most "slow WAN" tickets we're handed aren't a bandwidth problem.

The circuit has headroom on paper. The complaint is completely real. Both are true at once, because "how much can this link carry" and "what happens to my call when the link is busy" are different questions — and only one is answered by buying more.

Here's the mechanism. The moment more traffic wants to leave than the circuit can carry — even for a few milliseconds — something has to wait. If nobody has decided what waits, the device decides, and its default is roughly first come, first served. So the file sync and the voice packet queue up together and get treated identically. The file sync doesn't care. The call does.

Adding bandwidth doesn't remove the queue. It changes how often it forms. And traffic obligingly expands to fill it.

The decision nobody wants to make is which traffic loses. That's what a queuing policy actually is: not a feature you enable, but a written statement that some things matter less. Somebody has to say out loud that the file sync yields to the call.

What we implement, once that decision exists:

→ Classify and mark once, at the edge, and trust nothing downstream that you didn't mark
→ A small number of classes — four or five. Twelve classes is a policy nobody can reason about at 2am
→ A strict-priority queue for real-time, with a hard ceiling so it can't starve everything else
→ Guaranteed minimums, not caps — bandwidth you're owed, not bandwidth you're limited to
→ Shape to the rate you actually bought, not the interface rate

That last one catches people constantly. Your router sees a gigabit interface; the carrier is policing at two hundred megabits. Without shaping below that policer, the drops happen at the provider — where your policy has no say, and where you can't see them.

Bandwidth is a purchase. Priority is a decision. Only one of them requires somebody to say what matters least.

When your WAN is saturated, what are you willing to let wait?

#NetworkEngineering #QoS #NetOps
