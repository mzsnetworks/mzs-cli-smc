# LinkedIn — check-both-directions


Most times I've blamed the wrong device, it's because I only looked at traffic going one way.

Nothing enforces symmetry. Each direction gets routed independently, and the return path is free to take a different set of hops than the one that got you there. That's not a fault. It's often the correct behavior.

It only becomes a problem when something in the path is stateful and quietly assumes it won't happen.

That's where the confusing symptoms come from:

→ A firewall that permits the outbound flow perfectly and drops the return, because the return arrived on an interface its state table wasn't expecting
→ A capture at one end that looks clean while the other end is retransmitting
→ A health check that passes while real users fail, because the check leaves from somewhere else
→ Two engineers who both say "it works from here," and both are right

The habit that fixed this for me is unglamorous: capture at both ends of the same flow, at the same time, and compare.

Because that comparison answers the only question that matters early on. If a packet left A and never arrived at B, the problem lives between them. If it arrived at B and B did nothing with it, the problem is at B. Those are completely different investigations, and without both captures you're choosing between them by instinct.

The second habit is to trace the return path deliberately rather than assuming it mirrors the forward one. Run it from both sides. Asymmetry that would have cost you an afternoon shows up in about ninety seconds, and the conversation stops being an argument about whose device is at fault.

None of this requires better tooling. It requires resisting the pull of the first capture you took — always the one from the end you happened to be logged into.

One-way evidence produces one-way conclusions. Capture both ends, or you're not diagnosing — you're choosing who to blame.

When did you last capture both ends of the same flow at the same time?

#Troubleshooting #NetworkEngineering #NetOps
