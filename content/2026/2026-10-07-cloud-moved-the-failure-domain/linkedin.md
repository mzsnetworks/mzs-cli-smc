# LinkedIn — cloud-moved-the-failure-domain


The cloud didn't shrink your network. It moved a failure domain into somebody else's routing table and left you holding the ticket.

That trade is often worth making. It is rarely made deliberately.

Here is the pattern we keep inheriting. The first workload moves and someone builds a VPN to it, because that is the fastest thing that works. The second workload gets its own. By the fourth, there is a direct connect, two VPN tunnels nobody will decommission because nobody is certain what still uses them, and a routing policy that exists in three places and agrees in two.

Nobody designed that. It accumulated, one urgent project at a time, and each individual decision was correct when it was made.

What changed underneath is the shape of the problem. On-premises, when an application was slow, you owned every hop between the user and the server. You could instrument it, capture it, and fix it. Now the path runs through a provider edge you cannot see into, and the honest answer during an incident is often "it is not us, and we cannot prove that."

That last part is what costs you. Not the outage — the hour spent establishing whose outage it is.

So the questions worth asking are unglamorous. Which cloud paths are load-bearing, and do any of them share a physical route? What is your actual failover behavior if a direct connect drops — tested, not assumed? Can you see latency and loss to the provider edge, or only to your own firewall? And when the answer really is the provider, what evidence do you hand them?

Cloud does not remove network engineering. It moves it to a boundary you do not control, which is harder, and it makes the evidence you can produce the thing that closes the call.

Where does your visibility actually stop?

#NetworkEngineering #Cloud #NetOps
