# Master — before-its-not-the-network

**Preset:** Professional (LinkedIn personal profile + Instagram @mzsnetworks)
**Date:** 2026-10-08
**Thesis:** "It's not the network" is a sentence that costs credibility if you are wrong once, and it is only worth saying when you can follow it with where the problem actually is. Six checks earn the right to say it.
**Pillar:** Enterprise Network Ops
**Source:** ideas-2026-08-27 #34
**Stats:** none. Judgment and practice only; no statistic stated as fact.

---

"It's not the network" is a sentence that costs you credibility if you are wrong once.

Be wrong once and it follows you. Every incident after that, somebody quietly checks behind you, and the sentence stops carrying weight exactly when you need it to.

So here is what I check before saying it.

Can I reproduce it from somewhere else? One client having a problem and every client having a problem are different incidents with different causes, and the difference takes ninety seconds to establish.

What do the counters actually say, at both ends? Not whether the interface is up. Errors, discards, light levels, and whether either number is moving right now. An interface can be up and unhealthy for months.

Does it behave the same in both directions? Asymmetry turns a one-way problem into something that looks like everyone's problem, and the return path is the half nobody checks.

Where did the traffic actually go? Not where the diagram says. What the client resolved and which path it took, confirmed rather than assumed.

Did anything scheduled run? Backups, replication, a sync job, a batch window. Load that arrives on a timetable looks like a network fault to everyone who is not holding the timetable.

Is the application healthy on its own terms? Can it reach its own database, is it out of connections, is it waiting on something that has nothing to do with me.

None of that is exotic, and none of it takes long. What it buys is the right to say the sentence.

Because the useful version is never "it's not the network" on its own. It is "it's not the network, and here is where it actually is."

The first one ends a conversation. The second one ends an outage.
