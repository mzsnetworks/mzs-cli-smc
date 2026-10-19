# Instagram — check-both-directions

Most times I've blamed the wrong device, I'd only looked at traffic going one way. ↔️

Nothing enforces symmetry.

Each direction gets routed independently. The return path is free to take a different set of hops than the one that got you there.

That's not a fault. It's often correct. ⚙️

It only becomes a problem when something in the path is stateful and quietly assumes it won't happen.

Which is where the confusing symptoms come from:

→ a firewall that permits the outbound flow perfectly and drops the return, because it arrived on an interface the state table wasn't expecting
→ a capture at one end that looks clean while the other end retransmits
→ a health check that passes while real users fail, because the check leaves from somewhere else
→ two engineers who both say "it works from here" — and both are right

The habit that fixed this for me is unglamorous.

Capture both ends of the same flow, at the same time, and compare.

Because that comparison answers the only question that matters early:

→ packet left A and never arrived at B? The problem is between them.
→ arrived at B and B did nothing with it? The problem is at B.

Those are completely different investigations. Without both captures, you're choosing between them by instinct.

Second habit: trace the return path deliberately instead of assuming it mirrors the forward one. Run it from both sides.

Asymmetry that would have cost you an afternoon shows up in about ninety seconds — and the conversation stops being an argument about whose device is at fault.

None of this needs better tooling. It needs resisting the pull of the first capture you took, which is always from the end you happened to be logged into.

One-way evidence produces one-way conclusions.

When did you last capture both ends at once? 👇

#Troubleshooting #NetworkEngineering #NetOps #Networking #ITInfrastructure
