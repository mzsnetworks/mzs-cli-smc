# Instagram — bandwidth-graph-lies

Your bandwidth graph lies. 📉

The link shows 40% utilization. Flat, green, unremarkable.

And the calls keep breaking up.

Here's what that graph actually is: something polls the interface every five minutes, divides by 300 seconds, and plots a point.

That point is an average. Traffic is not average. ⚙️

A microburst lasts milliseconds:

→ a backup job starts
→ two hundred clients hit one server at the top of the hour
→ the interface is asked to send more than it can
→ the rest queues, the buffer fills, frames drop

Then it's over.

Twenty milliseconds of line rate inside a five-minute window barely moves the average at all. The event that dropped your frames is invisible on the graph that's supposed to show it.

The graph is calm because the sampling is.

So the first counter we look at isn't utilization. It's drops:

→ output drops on a link that "isn't busy"
→ egress queue depth and buffer stats
→ drops per queue where QoS is configured
→ streaming telemetry instead of five-minute smoothing

And faster polling isn't the fix. Thirty-second polling still averages thirty seconds — a smaller lie, not a truer one.

Utilization is an average. Drops are an event. Users live in the events.

When did you last check drops on a quiet link? 👇

#NetworkEngineering #NetOps #Observability #Networking #ITInfrastructure
