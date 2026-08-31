# Instagram — certificate-calendar-invite

Certificate expiry is an outage with a calendar invite you declined. 📅

Every other outage arrives unannounced.

This one tells you the exact second it will happen, months ahead, in writing.

And it still takes people down — at organizations that are otherwise well run. ⚙️

The reason isn't carelessness.

It's that nobody owns certificates as a category.

They own systems. And certificates live inside systems:

→ the VPN gateway
→ the load balancer
→ the RADIUS server doing 802.1X
→ management interfaces
→ the internal CA
→ the syslog collector doing TLS
→ the API integration somebody stood up two years ago

Each with a different owner, a different renewal path, a different date, and a notification address that made sense at the time.

That's the real failure mode.

Not "we forgot." The warning was delivered accurately — to a mailbox belonging to someone who left in 2024.

What I've seen actually work:

1️⃣ Inventory by scanning, not by asking. Ask what certificates people have and you get the ones they remember. Scan what's presenting a cert on the wire and you get the ones that will hurt you.

2️⃣ One list, with real owners and real dates. Not a per-team spreadsheet. One place where "who renews this" has a name in it.

3️⃣ Alert at 60, 30 and 7 days — to a team address, never a person. The 7-day alert exists because the 60-day one gets acknowledged and forgotten.

4️⃣ Rehearse on something small. Renew a low-stakes cert early, on purpose, to find out if the procedure still works.

The two that catch people hardest aren't thought of as certificates at all: the internal CA's own certificate, and client certs on devices you never log into — which fail silently, one at a time.

Every other outage surprises you. This one just waits.

Without looking: when does your oldest cert expire? 👇

#NetworkEngineering #NetOps #ITOperations #Networking #ITInfrastructure
