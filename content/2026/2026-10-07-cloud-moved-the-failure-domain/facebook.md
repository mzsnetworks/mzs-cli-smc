# Facebook — cloud-moved-the-failure-domain


The cloud didn't shrink your network. It moved a failure domain into somebody else's routing table and left you holding the ticket.

That trade is often worth making. It's rarely made deliberately.

The pattern we keep inheriting: first workload moves, someone builds a VPN. Second gets its own. By the fourth there's a direct connect, two tunnels nobody will remove, and a routing policy in three places that agrees in two.

On-prem, when an app was slow you owned every hop. Now the path crosses a provider edge you can't see into, and the honest answer in an incident is "it isn't us, and we can't prove that."

That's the real cost. Not the outage — the hour spent establishing whose outage it is.

Where does your visibility actually stop?
