# LinkedIn — same-rfc1918-space


The integration plan said "connect the two networks." Both of them were using 10.10.0.0/16.

That's not an exotic failure. It's the normal one. Everybody picked 10-dot for the same sensible reasons twenty years ago, so every merger has a decent chance of joining two networks that already believe they own the same addresses.

Nobody puts this in the deal timeline: three options, all of them costing more than the slide suggested.

Renumber one side properly. Correct, and the slowest thing you will ever schedule. It isn't the addresses — it's everything that quietly remembers them. DHCP scopes, DNS records, firewall rules written by IP, and the appliance whose vendor hardcoded a subnet into a config file in 2019. You will find that one late.

NAT between the two. Fast, works on the deadline, and leaves a permanent translation layer every engineer after you will curse. It also breaks anything that carries an address inside the payload rather than the header. Those failures show up weeks later and never look like a NAT problem.

Renumber only what has to talk. What we recommend almost every time. Identify the small set of systems that genuinely need cross-network reachability on day one, move those, and let the full renumber proceed behind the integration deadline instead of underneath it.

The bigger lesson isn't about addressing. It's that acquisition timelines treat the network as a switch somebody flips at close. Addressing is just the first place that assumption breaks — and a good early warning about how much else in the plan was assumed rather than checked.

One more thing worth saying out loud: whoever makes the addressing decision in month one owns the consequences for five years. That should not be whoever happens to be free that week.

The integration plan was really an addressing plan with somebody else's deadline on it.

If you acquired a company next quarter, would you know today whether your address space collides?

#NetworkEngineering #MergersAndAcquisitions #NetOps
