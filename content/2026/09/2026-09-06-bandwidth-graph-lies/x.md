# X — bandwidth-graph-lies

## Single (publish this)

Your bandwidth graph lies.

The link reads 40% all week and the calls still break up.

A five-minute average can't show a 20ms burst that filled the buffer and dropped frames.

The graph is calm because the sampling is.

#NetOps #NetworkEngineering

## Thread (alternate)

1/ Your bandwidth graph lies. The link shows 40% utilization, flat and green — and the calls keep breaking up. 🧵

2/ That graph is a poll of the interface counter every five minutes, divided by 300 seconds. It's an average. Traffic is not average.

3/ A microburst lasts milliseconds. A backup starts, 200 clients hit one server, and the interface is asked to send more than it can. The rest queues. Buffer fills. Frames drop.

4/ Twenty milliseconds of line rate inside a five-minute window barely moves the average. The event that dropped your frames is invisible on the graph meant to show it.

5/ The graph is calm because the sampling is.

6/ So look at drops first:
• output drops on a link that "isn't busy"
• egress queue depth and buffer stats
• drops per queue where QoS is on
• streaming telemetry, not 5-min smoothing

7/ Faster polling isn't the fix. 30-second polling still averages 30 seconds — a smaller lie, not a truer one.

8/ Utilization is an average. Drops are an event. Users live in the events. #NetOps #NetworkEngineering
