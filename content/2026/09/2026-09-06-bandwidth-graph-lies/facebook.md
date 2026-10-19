# Facebook — bandwidth-graph-lies

Your bandwidth graph lies.

The link shows 40% utilization. Flat, green. And the calls keep breaking up. 📉

Here's why. Something polls the interface every five minutes and divides by 300 seconds. That's an average — and traffic isn't average.

A microburst lasts milliseconds. A backup starts, two hundred clients hit one server, and the interface is asked to send more than it can. The rest queues. The buffer fills. Frames drop.

Twenty milliseconds of line rate inside a five-minute window barely moves the average. The event that dropped your frames is invisible on the graph meant to show it.

The graph is calm because the sampling is.

Look at output drops instead — especially on links nobody thinks are busy.

Utilization is an average. Drops are an event. Users live in the events.
