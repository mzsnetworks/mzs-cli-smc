# Master — 8021x-fails-at-the-printer

**Preset:** Business (MZS company account — LI page, FB, IG, X)
**Date:** 2026-09-30 (Wed)
**Source idea:** ideas-2026-08-30 #9 (ENO · Contrarian)
**Thesis:** NAC rollouts die in the exceptions, so the exception process is the design — not the cleanup.
**Note:** kept off the inventory thesis of `iot-inventory-not-security` (2026-08-19) and the VLAN/ACL method of `segment-iot-without-forklift` (2026-09-09). This one is about exception handling as the actual project.
**Stats:** none — judgment/method post, no factcheck gate.

---

Every NAC project we've watched stall, stalled at a printer.

The laptops are the easy part. Supplicant, domain join, certificate, done — ninety percent of the devices and maybe ten percent of the work.

Then you meet the rest of the network. The printer whose supplicant exists but does something creative with EAP. The badge readers. The HVAC controllers. The lab instrument whose vendor answers "static IP, or the warranty is void." The conference room kit that authenticates fine until it firmware-updates itself over a weekend.

The mistake we see repeatedly is designing the policy first and treating the exceptions as cleanup at the end. They aren't cleanup. They are the majority of the work, all of the schedule risk, and all of the political risk — because each one has an owner who doesn't report to you and didn't ask for this project.

So we design the exception process before the policy:

→ Decide the fallback behavior up front. MAC authentication into a restrictive profile is a decision. Falling back to an open VLAN because nothing else was configured is an accident with a network in it.
→ Assign an owner per exception class, not per device. "Printers" has an owner. "This printer" has a ticket.
→ Put an expiry date on every exception at creation, so "temporary MAB" doesn't become the permanent architecture.
→ Run in monitor mode long enough to enumerate what actually connects — including the things that only appear monthly.
→ Write down the path for "the vendor says it can't do 802.1X," ending in a decision by a named person rather than a shrug.

That last one is where projects genuinely die. Not on technology — on nobody willing to say "then that device goes in the restricted segment and stays there."

None of this is harder than the authentication design. It's just less interesting, and it's the part that determines whether you finish.

The laptops are the demo. The exceptions are the project.

If you enforced 802.1X everywhere on Monday, which device would break first — and who would you have to call?
