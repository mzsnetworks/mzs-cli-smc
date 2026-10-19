# Instagram — not-in-monitoring


The device that isn't in monitoring is the one that pages you. 🌙

Not immediately. At 2am, through a person, after it's already been broken a while.

And when you look, there's no history. No baseline, no graph, nothing to compare today against.

You're diagnosing a device you've never watched, in the hour you're least able to learn it. ⚠️

Here's why it keeps happening: coverage is reported as a percentage of the inventory — and the inventory is built from the same source that built monitoring. Neither can see what it doesn't know about.

The number is always high. Always reassuring.

The gaps are predictable:

→ The device stood up for a project that ended
→ The site that joined through an acquisition
→ The appliance a vendor manages, which means nobody here does
→ The box that was monitored until a credential rotated and the poller quietly started failing

Three checks find most of it, and none start from the inventory:

→ Diff ARP and MAC tables against what you think exists. The network already knows.
→ Pull DHCP leases and your address management.
→ Find monitored devices that haven't reported in a week. ⚙️

Coverage isn't "what percentage is monitored." It's "what would have to be true for something to run here and me not know."

Usually: not much.

#NetworkEngineering #NetOps #Observability #ITOps #Infrastructure
