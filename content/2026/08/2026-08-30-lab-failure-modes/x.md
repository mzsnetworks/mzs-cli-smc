# X — lab-failure-modes

## Single (publish this)

Your lab doesn't need to match production. It needs to match production's failure modes.

A faithful replica of a healthy network only proves the happy path works. That was never the question.

Can it reproduce your last three outages?

#NetDevOps #NetOps

## Thread (alternate)

1/ Your lab doesn't need to match production. It needs to match production's failure modes. 🧵

2/ The goal gets written down as a digital twin: same platforms, same topology, faithful at scale. A year later it exists, it's beautiful, and it proves the happy path works.

3/ The happy path was never the question.

4/ Outages don't come from the topology. They come from the seams:
• failover that misbehaves only under asymmetric return traffic
• an upgrade that fails on state left by a previous attempt
• a "multicast problem" that was an app design flaw

5/ A faithful replica of a healthy network reproduces none of that. It's healthy. That's the design goal.

6/ Different spec: can this lab reproduce our last three outages? Not port count. Not identical part numbers. Can you make it fail the way production failed?

7/ • break the link, watch convergence take the documented path
• leave stale state behind, run the upgrade again
• half-apply a change, rehearse the rollback
• generate the traffic that exposed the flaw

8/ Two switches and a VM that reproduce last quarter's incident teach more than a rack that mirrors the DC and has never been broken on purpose.

9/ A lab that matches production proves your design. A lab that matches production's failures proves your operations. Only one gets tested at 2am. #NetDevOps
