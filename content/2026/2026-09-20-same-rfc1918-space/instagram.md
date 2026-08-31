# Instagram — same-rfc1918-space

The integration plan said "connect the two networks." 🔀

Both of them were using 10.10.0.0/16.

That's not an exotic failure. It's the normal one.

Everybody picked 10-dot for the same sensible reasons twenty years ago. ⚙️

Three options — and all of them cost more than the slide suggested.

📍 Renumber one side properly

Correct, and the slowest thing you'll ever schedule.

It isn't the addresses. It's everything that quietly remembers them:

→ DHCP scopes
→ DNS records
→ firewall rules written by IP
→ monitoring targets and backup jobs
→ the appliance whose vendor hardcoded a subnet in 2019

You will find that last one late.

📍 NAT between the two

Fast. Works on the deadline. Leaves behind a permanent translation layer every engineer after you will curse.

It also breaks anything carrying an address inside the payload instead of the header — some voice signalling, some backup agents, some management protocols.

Those failures show up weeks later and never look like a NAT problem.

📍 Renumber only what has to talk

What we recommend almost every time.

Move the small set of systems that genuinely need day-one reachability. Let the full renumber run behind the integration deadline instead of underneath it.

The bigger lesson isn't addressing.

It's that acquisition timelines treat the network as a switch somebody flips at close — and addressing is just the first place that assumption breaks.

The integration plan was really an addressing plan with somebody else's deadline on it.

Would you know today if your space collides? 👇

#NetworkEngineering #MergersAndAcquisitions #NetOps #Networking #ITInfrastructure
