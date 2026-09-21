# Master — not-in-monitoring

**Preset:** Professional (LinkedIn personal profile + Instagram @mzsnetworks)
**Date:** 2026-10-27
**Thesis:** The device that is not in monitoring is the one that pages you, and it pages you the worst way: at 2am, via a human, with no history. Monitoring coverage is not a percentage of what you know about — it is a question about what you do not.
**Pillar:** Engineering Systems
**Source:** ideas-2026-08-27 #9
**Stats:** none. Judgment and practice only; no statistic stated as fact.

---

The device that is not in monitoring is the one that pages you.

Not immediately. It pages you at 2am, through a person, after something has already been broken for a while.

And when you go looking, there is no history. No baseline, no graph, nothing to compare today against. You are diagnosing a device you have never watched, during the hour you are least able to learn it.

The reason this keeps happening is that monitoring coverage gets reported as a percentage of the inventory, and the inventory is built from the same source that built monitoring. Both are generated from the system that knows about things. Neither can see what it does not know about, so the number is always high and always reassuring.

The gaps are predictable. The device somebody stood up for a project that ended. The one at a site that joined through an acquisition. The appliance a vendor manages, which means nobody here does. The box that was in monitoring until a credential rotated and the poller quietly started failing, which is worse than never having been added, because the dashboard still shows a tile.

Three checks find most of it, and none of them start from the inventory.

Pull the ARP and MAC tables off your core and edge, and diff what is actually talking against what you think exists. The network already knows.

Pull DHCP leases and your address management for the same reason, from a different angle.

Then check which monitored devices have not reported in a week. A silent poller looks identical to a healthy quiet device until the day you need the data.

The honest version of coverage is not "what percentage of devices are monitored." It is "what would have to be true for something to be running here and me not know about it."

Usually the answer is: not much.
