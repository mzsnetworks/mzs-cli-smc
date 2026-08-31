# Facebook — wan-queuing-decision

Most "slow WAN" tickets aren't a bandwidth problem. 📶

The circuit has headroom on paper. The complaint is completely real. Both are true — because "how much can this link carry" and "what happens to my call when it's busy" are different questions.

The moment more traffic wants out than the circuit can carry, something has to wait. If nobody decided what waits, the device decides — roughly first come, first served. So the file sync and the voice packet queue together and get treated identically. The file sync doesn't care. The call does.

Adding bandwidth doesn't remove the queue. It changes how often it forms.

The decision nobody wants to make is which traffic loses. That's what a queuing policy is: not a feature you enable, but a written statement that some things matter less.

Bandwidth is a purchase. Priority is a decision.

What are you willing to let wait?
