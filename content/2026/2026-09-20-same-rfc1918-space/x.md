# X — same-rfc1918-space

## Single (publish this)

The integration plan said "connect the two networks."

Both were using 10.10.0.0/16.

That's not an exotic failure. It's the normal one — and it turns the integration plan into an addressing plan with somebody else's deadline on it.

#NetOps #NetworkEngineering

## Thread (alternate)

1/ The integration plan said "connect the two networks." Both of them were using 10.10.0.0/16. 🧵

2/ That's not an exotic failure. It's the normal one. Everybody picked 10-dot for the same sensible reasons twenty years ago.

3/ Option 1 — renumber one side properly. Correct, and the slowest thing you'll ever schedule. Not the addresses: everything that quietly remembers them. DHCP, DNS, firewall rules written by IP, the appliance with a subnet hardcoded in 2019.

4/ Option 2 — NAT between the two. Fast, hits the deadline, leaves a permanent translation layer every engineer after you will curse. Also breaks anything carrying an address in the payload.

5/ Option 3 — renumber only what has to talk. What we recommend almost every time. Move the systems that need day-one reachability; let the full renumber run behind the deadline, not underneath it.

6/ The bigger lesson isn't addressing. Acquisition timelines treat the network as a switch somebody flips at close. Addressing is just the first place that assumption breaks.

7/ Whoever makes the addressing call in month one owns it for five years. That shouldn't be whoever happens to be free that week. #NetOps
