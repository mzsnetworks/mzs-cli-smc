# LinkedIn — defining-what-good-means


SD-WAN did not remove the WAN engineer. It moved the hard part.

Configuring links used to be the work. Two circuits, a routing protocol, a failover design somebody could draw on a whiteboard. That part is largely solved now, and the vendors are not wrong when they say so.

What replaced it is a question nobody wants to answer: what does "good" mean for this application?

The policy engine will happily enforce whatever you tell it. It needs to know that the ERP tolerates 200 milliseconds but not packet loss, that the voice platform is the reverse, that the backup replication should take whatever is left and never compete with either. Those are not network facts. They are business decisions about which application loses when the circuit degrades.

So the project stalls in a meeting rather than in a lab. The network team cannot answer it, because the answer depends on what the business values at 2pm on a Tuesday. The application owners can answer it, but each one answers "mine is critical," which is the same as nobody answering.

What we usually end up doing is building a first draft of that policy ourselves, from observed traffic and a few direct questions, then putting it in front of the people who can argue with it. A draft somebody disagrees with produces a decision. A blank form produces another meeting.

The classification is the deliverable. The overlay is just what enforces it.

An SD-WAN rollout with no agreed definition of "good" is a faster way to run an unexamined policy. It will do exactly what the old network did, with better reporting.

Who in your organization is allowed to say which application loses?

#SDWAN #NetworkEngineering #NetOps
