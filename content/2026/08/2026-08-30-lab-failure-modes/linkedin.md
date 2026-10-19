# LinkedIn — lab-failure-modes

Your lab doesn't need to match production. It needs to match production's failure modes.

That distinction costs teams entire budgets.

The goal gets written down as a digital twin: same platforms, same code trains, same topology, scaled down but faithful. A year later it exists, it's beautiful, and what it proves is that the happy path works.

The happy path was never the question.

Outages don't come from the topology. They come from the seams. The failover that only misbehaves under asymmetric return traffic. The in-service upgrade that fails on operational state left behind by a previous attempt, not on anything in the documented procedure. The "multicast problem" that turns out to be an application design flaw the network merely exposed.

A faithful replica of a healthy network reproduces none of that. It's healthy. That's the whole design goal.

So here's the spec we'd write instead: can this lab reproduce our last three outages?

Not port count. Not identical part numbers. Can you make it fail the way production failed?

→ Break the link and watch convergence take the path the diagram claims it takes
→ Leave stale state behind on purpose, then run the upgrade again
→ Half-apply a change and rehearse the rollback somebody will need at 2am
→ Generate the traffic pattern that exposed the flaw — not the one that's easy to generate

Two switches and a VM that can reproduce last quarter's incident teach a team more than a rack that mirrors the data center and has never been broken on purpose.

A lab that matches production proves your design. A lab that matches production's failures proves your operations. Only one of those gets tested at 2am.

What's the last outage you could reproduce on demand?

#NetDevOps #NetworkEngineering #NetOps
