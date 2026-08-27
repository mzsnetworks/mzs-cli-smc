# LinkedIn — brownfield-is-a-negotiation

Greenfield is a design exercise. Brownfield is a negotiation.

Every portfolio I've ever reviewed leads with greenfield. Clean topology, current code, one vendor, a diagram that matches production because production was built from the diagram. It's real skill. It's also a skill with no opponent — nothing in a greenfield design pushes back.

Brownfield pushes back constantly.

The /24 that can't be renumbered because a vendor hardcoded it into an appliance that's out of support. The VLAN spanning two buildings because in 2016 that was the fast fix, and the fast fix outlived the person who made it. The firewall rule nobody will delete, because the last engineer who deleted an unknown rule took down payroll.

The junior instinct is to call all of it technical debt and propose a replacement.

Here's what I've concluded after enough of these: most of those decisions were correct when they were made. The context died. The config survived. "Debt" implies somebody was careless — usually somebody was constrained, and you're reading the receipt.

Which is why the work is a negotiation. You don't get to overrule the past. You trade with it. One migration window a quarter, not a green field. Every change asks something of someone who never asked for it.

That changes how I work:

→ Read the config as history, not as a spec — every oddity is an answer to a question you can't see anymore
→ Find the person, not the ticket. The reason lives in someone's head, and it walks out the door on their last day
→ Move in increments that are individually reversible
→ Earn the second change by not breaking anything with the first

Anyone can draw the right network. The skill is changing a wrong one while it's carrying payroll on Friday.

Greenfield rewards the best design. Brownfield rewards the best judgment.

What's the oldest decision in your network that you still can't undo?

#BrownfieldEngineering #NetworkEngineering #NetOps
