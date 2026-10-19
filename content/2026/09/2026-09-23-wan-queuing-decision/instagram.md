# Instagram — wan-queuing-decision

Most "slow WAN" tickets aren't a bandwidth problem. 📶

The circuit has headroom on paper. The complaint is completely real.

Both are true at once.

Because "how much can this link carry" and "what happens to my call when the link is busy" are different questions — and only one is answered by buying more. ⚙️

The mechanism:

→ more traffic wants out than the circuit can carry, even for milliseconds
→ something has to wait
→ if nobody decided what waits, the device decides
→ its default is roughly first come, first served

So the file sync and the voice packet queue up together and get treated identically.

The file sync doesn't care. The call does.

Adding bandwidth doesn't remove the queue. It changes how often it forms — and traffic obligingly expands to fill it.

The decision nobody wants to make is which traffic loses.

That's what a queuing policy actually is. Not a feature you enable — a written statement that some things matter less.

What we implement once that decision exists:

→ classify and mark once, at the edge; trust nothing downstream you didn't mark
→ four or five classes, not twelve — nobody can reason about twelve at 2am
→ a strict-priority queue for real-time, with a hard ceiling so it can't starve the rest
→ guaranteed minimums, not caps
→ shape to the rate you actually bought, not the interface rate

That last one catches people constantly. Your router sees a gigabit. The carrier polices at 200 Mbps. Without shaping below that, the drops happen at the provider — where your policy has no say and you can't see them.

Bandwidth is a purchase. Priority is a decision.

What are you willing to let wait? 👇

#NetworkEngineering #QoS #NetOps #Networking #ITInfrastructure
