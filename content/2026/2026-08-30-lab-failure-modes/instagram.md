# Instagram — lab-failure-modes

Your lab doesn't need to match production. It needs to match production's failure modes. 🧪

That distinction costs teams entire budgets.

The goal gets written down as a digital twin — same platforms, same topology, faithful at scale.

A year later it exists, it's beautiful, and what it proves is that the happy path works.

The happy path was never the question.

Outages don't come from the topology. They come from the seams:

→ the failover that only misbehaves under asymmetric return traffic
→ the upgrade that fails on state left behind by a previous attempt, not on anything in the documented procedure
→ the "multicast problem" that was an application design flaw the network merely exposed

A faithful replica of a healthy network reproduces none of that. It's healthy. That's the design goal. ⚙️

So write a different spec: can this lab reproduce our last three outages?

Not port count. Not identical part numbers. Can you make it fail the way production failed?

→ break the link, watch convergence take the path the diagram claims
→ leave stale state behind on purpose, then run the upgrade again
→ half-apply a change and rehearse the rollback somebody needs at 2am
→ generate the traffic that exposed the flaw, not the traffic that's easy to generate

Two switches and a VM that reproduce last quarter's incident teach more than a rack that mirrors the data center and has never been broken on purpose.

A lab that matches production proves your design. A lab that matches production's failures proves your operations.

Only one of those gets tested at 2am.

What's the last outage you could reproduce on demand? 👇

#NetDevOps #NetworkEngineering #NetOps #NetworkAutomation #Networking
