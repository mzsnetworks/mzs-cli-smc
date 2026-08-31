# X — wan-queuing-decision

## Single (publish this)

Most "slow WAN" tickets aren't a bandwidth problem.

When the link is momentarily full, something waits. If nobody decided what, the device decides — and it treats your backup and your call identically.

Bandwidth is a purchase. Priority is a decision.

#QoS #NetOps

## Thread (alternate)

1/ Most "slow WAN" tickets we're handed aren't a bandwidth problem. The circuit has headroom on paper and the complaint is completely real. 🧵

2/ "How much can this link carry" and "what happens to my call when the link is busy" are different questions. Only one of them is answered by buying more.

3/ The moment more traffic wants out than the circuit can carry — even for milliseconds — something has to wait. If nobody decided what waits, the device decides, roughly first come first served.

4/ So the file sync and the voice packet queue together and get treated identically. The file sync doesn't care. The call does.

5/ Adding bandwidth doesn't remove the queue. It changes how often it forms. And traffic expands to fill it.

6/ A queuing policy isn't a feature you enable. It's a written statement that some things matter less — somebody has to say the file sync yields to the call.

7/ What we implement:
• mark once at the edge, trust nothing you didn't mark
• 4-5 classes, not 12
• strict priority for real-time, with a ceiling
• guaranteed minimums, not caps
• shape to the rate you bought

8/ That last one catches people. Your router sees a gigabit; the carrier polices at 200 Mbps. Without shaping below the policer, drops happen at the provider — where your policy has no say and you can't see them.

9/ Bandwidth is a purchase. Priority is a decision. Only one requires somebody to say what matters least. #QoS #NetOps
