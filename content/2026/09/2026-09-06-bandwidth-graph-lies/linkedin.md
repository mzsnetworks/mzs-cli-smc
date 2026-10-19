# LinkedIn — bandwidth-graph-lies

Your bandwidth graph lies.

The link shows 40% utilization. The graph is flat, green, unremarkable. And the calls keep breaking up.

Here's what that graph is. Something polls the interface counter every five minutes, divides by 300 seconds, and plots a point. That point is an average. Traffic is not average.

A microburst lasts milliseconds. A backup job starts. Two hundred clients hit the same server at the top of the hour. For a few milliseconds the interface is asked to send more than it can send, because a port moves one bit at a time at exactly its rated speed. Everything arriving while it's busy goes into the egress buffer. When the buffer is full, frames are dropped.

Then it's over. Twenty milliseconds of line rate inside a five-minute window barely moves the average at all. The event that dropped the frames is invisible on the graph that's supposed to show it.

The graph is calm because the sampling is.

So the first counter we look at isn't utilization. It's drops.

→ Output drops on a link that "isn't busy" — the most under-read counter we know
→ Egress queue depth and buffer statistics, not the five-minute rate
→ Drops per queue where QoS is configured, because the policy decides who loses
→ Streaming telemetry where the platform supports it — sub-second visibility, not five-minute smoothing

And faster polling is not the fix. Thirty-second polling still averages thirty seconds — a smaller lie, not a truer one. The problem was never the interval; averaging is simply the wrong operation for a bursty medium.

Operationally this changes one habit. When a link shows drops and low utilization, stop treating that as a contradiction. That combination is the signature of a burst. Add buffer, shape the source, or move the traffic — but stop arguing with the graph.

Utilization is an average. Drops are an event. Users live in the events.

When did you last look at output drops on a link nobody thinks is busy?

#NetworkEngineering #NetOps #Observability
