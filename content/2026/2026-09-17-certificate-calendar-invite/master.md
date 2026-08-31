# Master — certificate-calendar-invite

**Preset:** Professional (LinkedIn personal + Instagram @mzsnetworks)
**Date:** 2026-09-17 (Thu)
**Source idea:** ideas-2026-08-27 #14
**Thesis:** Certificate expiry is the only outage that warns you for months and still lands. Nobody owns certificates as a category, so the warning goes to a mailbox nobody reads.
**Stats:** none — judgment/ops post, no factcheck gate.

---

Certificate expiry is an outage with a calendar invite you declined.

Every other outage arrives unannounced. This one tells you the exact second it will happen, months ahead, in writing. And it still takes people down, over and over, at organizations that are otherwise well run.

The reason isn't carelessness. It's that nobody owns certificates as a category.

They own systems. And certificates live inside systems — the VPN gateway, the load balancer, the RADIUS server doing 802.1X, the internal CA, the syslog collector doing TLS, the API integration somebody stood up two years ago. Each one has a different owner, a different renewal path, a different expiry date, and a notification address that made sense at the time.

That's the failure mode. Not "we forgot" — the warning was delivered accurately, to a mailbox belonging to someone who left in 2024.

What I've seen actually work:

Inventory by scanning, not by asking. Ask what certificates people have and you get the ones they remember. Scan what's presenting a certificate on the wire and you get the ones that will hurt you.

One list, with real owners and real dates. Not a per-team spreadsheet. One place, where "who renews this" has a person's name in it.

Alert at sixty, thirty and seven days — to a team address, never an individual. The seven-day alert exists because the sixty-day one gets acknowledged and forgotten.

And rehearse on something small. Renew a low-stakes certificate early, on purpose, to find out whether the procedure still works before the one that matters comes due.

The two that catch people hardest are the ones nobody thinks of as certificates at all: the internal CA's own certificate, which takes everything with it, and client certificates on devices you never log into, which fail silently and one at a time until somebody notices a pattern.

Every other outage surprises you. This one just waits.

Without looking it up: when does your oldest certificate expire?
