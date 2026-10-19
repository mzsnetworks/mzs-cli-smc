# X — cloud-moved-the-failure-domain


## Single (publish this)

The cloud didn't shrink your network. It moved a failure domain into somebody else's routing table and left you holding the ticket.

The cost isn't the outage. It's the hour spent proving whose outage it is.

#Cloud #NetOps

---

## Thread

1/ The cloud didn't shrink your network.

It moved a failure domain into somebody else's routing table and left you holding the ticket.

That trade is often worth making. It's rarely made deliberately. 🧵

2/ The pattern we keep inheriting:

First workload moves, someone builds a VPN — it's the fastest thing that works.
Second workload gets its own.

3/ By the fourth there's a direct connect, two VPN tunnels nobody will decommission because nobody is certain what still uses them, and a routing policy that exists in three places and agrees in two.

4/ Nobody designed that. It accumulated one urgent project at a time, and each individual decision was correct when it was made.

5/ What changed is the shape of the problem.

On-premises, you owned every hop between the user and the server. You could instrument it, capture it, fix it.

6/ Now the path runs through a provider edge you cannot see into, and the honest answer during an incident is often:

"It isn't us, and we can't prove that."

That's the cost. Not the outage — the hour spent establishing whose it is.

7/ Worth asking:

• Which cloud paths are load-bearing?
• What's your tested failover if a direct connect drops?
• Can you see loss to the provider edge, or only to your firewall?

Where does your visibility actually stop?

#Cloud #NetOps
