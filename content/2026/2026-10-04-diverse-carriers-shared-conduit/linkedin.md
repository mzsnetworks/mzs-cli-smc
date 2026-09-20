# LinkedIn — diverse-carriers-shared-conduit


Two carriers. Two invoices. One conduit.

Here is a question worth asking before your next resilience review: which of your circuits have genuinely diverse paths?

Not diverse carriers. Diverse conduit.

Those are different purchases, and only one of them is usually on the contract. Carrier diversity is a commercial arrangement — two vendors, two bills, two support numbers. Path diversity is a physical fact about where the fiber is buried. You can have the first without the second, and most multi-site networks do.

The reason is mundane. Carriers lease capacity from each other. A regional provider sells you a circuit that rides another carrier's fiber for the middle third of its route. Both of your "diverse" links leave the building on the same side, cross the same bridge, and pass through the same manhole two miles away. Nobody lied to you. Nobody at either carrier had the whole picture either.

You find out on the day a contractor puts a backhoe through that manhole, both circuits drop inside the same second, and the failover you tested carefully has nowhere to fail over to.

The fix is not more redundancy. It is asking for the route.

Request the KMZ or the circuit layout record from both carriers and compare them. Some will provide it, some will resist, and a refusal is itself information. Where the routes converge you have a choice to make — accept the risk knowingly, buy a genuinely diverse path, or put a different medium on the second link, because fixed wireless or LTE shares no conduit with anything.

Redundancy you have not traced is not redundancy. It is two invoices.

What would your carriers say if you asked them for the route tomorrow?

#NetworkEngineering #WAN #NetOps
