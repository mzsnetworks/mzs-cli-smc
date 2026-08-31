# Facebook — same-rfc1918-space

The integration plan said "connect the two networks." Both were using 10.10.0.0/16. 🔀

Not an exotic failure — the normal one. Everybody picked 10-dot for the same sensible reasons twenty years ago.

Three options, all costing more than the slide suggested:

Renumber one side properly. The slowest thing you'll ever schedule — it isn't the addresses, it's everything that quietly remembers them. DHCP, DNS, firewall rules written by IP, the appliance with a subnet hardcoded in 2019.

NAT between them. Fast, hits the deadline, leaves a permanent translation layer every engineer after you will curse.

Renumber only what has to talk. What we recommend almost every time.

Acquisition timelines treat the network as a switch somebody flips at close. Addressing is just the first place that assumption breaks.

Would you know today whether your address space collides?
