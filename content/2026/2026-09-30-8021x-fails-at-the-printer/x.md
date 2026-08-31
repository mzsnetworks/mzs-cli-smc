# X — 8021x-fails-at-the-printer

## Single (publish this)

Every NAC project we've watched stall, stalled at a printer.

Laptops are 90% of the devices and 10% of the work. The exceptions are where the schedule and the politics live.

The laptops are the demo. The exceptions are the project.

#NetworkSecurity #NetOps

## Thread (alternate)

1/ Every NAC project we've watched stall, stalled at a printer. 🧵

2/ Laptops are easy: supplicant, domain join, certificate, done. Ninety percent of the devices, maybe ten percent of the work.

3/ Then you meet the rest of the network. The printer doing something creative with EAP. Badge readers. Cameras. HVAC. The lab instrument whose vendor says "static IP, or the warranty is void."

4/ The repeated mistake: design the policy first, treat exceptions as cleanup at the end. They aren't cleanup — they're the majority of the work and all of the political risk.

5/ Each exception has an owner who doesn't report to you and didn't ask for this project. That's the actual difficulty.

6/ So design the exception process first:
• decide the fallback up front — restrictive MAB, not an open VLAN by accident
• an owner per exception class, not per device
• an expiry date on every exception
• monitor mode long enough to see monthly devices

7/ And write down the path for "the vendor says it can't do 802.1X" — ending in a decision by a named person, not a shrug.

8/ That's where projects genuinely die. Not on technology. On nobody willing to say "then it goes in the restricted segment and stays there."

9/ The laptops are the demo. The exceptions are the project. #NetworkSecurity #NetOps
