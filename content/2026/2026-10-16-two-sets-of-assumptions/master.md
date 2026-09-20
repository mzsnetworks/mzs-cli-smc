# Master — two-sets-of-assumptions

**Preset:** Business (LinkedIn company page + Facebook + Instagram + X, all on the MZS account)
**Date:** 2026-10-16
**Thesis:** Network integration after an acquisition is treated as a routing and addressing problem, but the addressing is the easy half. What actually joins is two undocumented trust models, and neither company can hand you theirs because neither ever wrote it down.
**Pillar:** Brownfield Engineering — M&A integration
**Source:** ideas-2026-08-30 #19
**Stats:** none. Judgment and field experience only; no statistic stated as fact.

---

An acquisition doesn't join two networks. It joins two sets of assumptions about who is trusted — and nobody documented either one.

The technical work gets scoped first, because it is the part you can see. Overlapping address space, routing between two cores, a VPN while the circuits are ordered, DNS that has to resolve both ways. That work is real, and it is the easy half. It has known answers and you can estimate it.

The half that overruns is the part nobody wrote down.

Every network encodes a trust model in its access lists, its firewall zones, and the things it never bothered to restrict. Somewhere in the acquired estate there is a flat segment that carries production traffic because ten years ago the team was small and everyone was in one building. Somewhere in yours there is a rule permitting a source range that made sense during a project that ended in 2021. Neither is written down as a policy. Both are policies.

Connect the two and you have merged the permissions without merging the reasoning. What you get is not the union of two security postures. It is the weaker of the two, applied to everything.

So the first question on an integration is not how the routing works. It is which assumptions are we inheriting, and who can still explain them?

That means finding the people, not just the configs. It means treating "why does this rule exist" as a scoping activity with a budget, before the two estates can reach each other. And it means being willing to say that a segment does not get connected on day one, which is a conversation with the business rather than an engineering decision.

Integration is cheap. Reconciling two undocumented trust models is the project.

Which assumptions would you be inheriting?
