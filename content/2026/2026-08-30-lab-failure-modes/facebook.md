# Facebook — lab-failure-modes

Your lab doesn't need to match production. It needs to match production's failure modes.

That distinction costs teams entire budgets. The goal gets written down as a digital twin — same platforms, same topology, faithful at scale. A year later it exists, it's beautiful, and it proves the happy path works.

The happy path was never the question.

Outages come from the seams. The failover that misbehaves only under asymmetric return traffic. The upgrade that fails on state left by a previous attempt. A faithful replica of a healthy network reproduces none of it — it's healthy by design. 🔧

So write a different spec: can this lab reproduce our last three outages?

Two switches and a VM that can recreate last quarter's incident teach more than a rack that mirrors the data center and has never been broken on purpose.

What's the last outage you could reproduce on demand?
