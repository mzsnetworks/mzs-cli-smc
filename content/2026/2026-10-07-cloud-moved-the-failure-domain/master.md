# Master — cloud-moved-the-failure-domain

**Preset:** Business (LinkedIn company page + Facebook + Instagram + X, all on the MZS account)
**Date:** 2026-10-07
**Thesis:** Cloud migration did not reduce the network. It relocated a failure domain into a provider's routing table, where the team still owns the user experience but no longer owns the path, the telemetry, or the fix.
**Pillar:** Enterprise Network Operations — cloud connectivity
**Source:** ideas-2026-08-30 #10
**Stats:** none. Judgment and field experience only; no statistic stated as fact, so Factcheck passes with no source gate.

---

The cloud didn't shrink your network. It moved a failure domain into somebody else's routing table and left you holding the ticket.

That trade is often worth making. It is rarely made deliberately.

Here is the pattern we keep inheriting. The first workload moves and someone builds a VPN to it, because that is the fastest thing that works. The second workload gets its own. By the fourth, there is a direct connect, two VPN tunnels nobody will decommission because nobody is certain what still uses them, and a routing policy that exists in three places and agrees in two.

Nobody designed that. It accumulated, one urgent project at a time, and each individual decision was correct.

What changed underneath is the shape of the problem. On-premises, when an application was slow, you owned every hop between the user and the server. You could instrument it, packet-capture it, and fix it. Now the path runs through a provider edge you cannot see into, and the honest answer during an incident is often "it is not us, and we cannot prove that."

That last part is what costs you. Not the outage — the hour spent establishing whose outage it is.

So the questions worth asking are unglamorous. Which cloud paths are load-bearing, and do any of them share a physical route? What is your actual failover behavior if a direct connect drops — tested, not assumed? Can you see latency and loss to the provider edge, or only to your own firewall? And when the answer is "it is the provider," what evidence do you hand them?

Cloud does not remove network engineering. It moves it to a boundary you do not control, which is harder, and makes the evidence you can produce the thing that resolves the call.

Where does your visibility actually stop?
