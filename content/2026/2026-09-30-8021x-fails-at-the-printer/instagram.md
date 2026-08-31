# Instagram — 8021x-fails-at-the-printer

Every NAC project we've watched stall, stalled at a printer. 🖨️

The laptops are the easy part.

Supplicant, domain join, certificate, done.

That's ninety percent of the devices and maybe ten percent of the work. ⚙️

Then you meet the rest of the network:

→ the printer whose supplicant does something creative with EAP
→ badge readers
→ cameras
→ HVAC controllers
→ the lab instrument whose vendor says "static IP, or the warranty is void"
→ the conference room kit that authenticates fine until it firmware-updates itself over a weekend

The mistake we see repeatedly: designing the policy first, treating exceptions as cleanup at the end.

They aren't cleanup.

They're the majority of the work, all of the schedule risk, and every bit of the political risk — because each one has an owner who doesn't report to you and didn't ask for this project.

So we design the exception process before the policy:

📍 Decide the fallback up front
MAC authentication into a restrictive profile is a decision. Falling back to an open VLAN because nothing else was configured is an accident with a network in it.

📍 An owner per exception class, not per device
"Printers" has an owner. "This printer" has a ticket.

📍 An expiry date on every exception
So "temporary MAB" doesn't quietly become the permanent architecture.

📍 Monitor mode, long enough
Enumerate what actually connects — including the things that only appear monthly.

📍 A written path for "the vendor says it can't"
Ending in a decision by a named person, not a shrug.

That last one is where projects genuinely die. Not on technology — on nobody willing to say "then that device goes in the restricted segment and stays there."

The laptops are the demo. The exceptions are the project.

Which device would break first on Monday? 👇

#NetworkSecurity #NetworkAccessControl #NetOps #NetworkEngineering #ITInfrastructure
