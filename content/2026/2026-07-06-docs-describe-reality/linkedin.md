# LinkedIn — publish-ready

The most dangerous document in your network isn't the one that's missing.

It's the one that's confidently wrong.

Every network diagram describes one moment: the day someone designed it. Production started diverging the week it went live. The emergency change at 11pm. The VLAN someone added "temporarily" three years ago. The failover path that got rewired during an outage and never made it back into Visio.

I watched this play out after a migration that went exactly to plan. The cutover was the easy part. The hard part came in the weeks after — config inconsistencies surfacing one by one, accumulated over years, none of them on any diagram. Production never looks like the drawings.

Here's the part that matters operationally: wrong documentation is worse than no documentation.

With no docs, the 2am troubleshooter verifies everything. Slow, but honest.

With wrong docs, they trust. They walk the "documented" failover path while the real one burns. They spend the first hour of an outage disproving their own diagram — the one document that was supposed to save them that hour.

The fix isn't better drawing discipline. Nobody updates diagrams at 11pm, and everybody makes changes at 11pm.

The fix is documentation that can't drift: generated from the network, not about the network. Pull it from the running configs. Reconcile your source of truth against live state on a schedule. A document produced by the network is evidence; a document produced about the network is a memory.

Intent lives in diagrams.
Decisions live in configs.
Truth lives only in the running network.

Document the truth.

What's the worst thing a "current" diagram ever did to you at 2am?

#NetworkEngineering #NetDevOps
