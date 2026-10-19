# Facebook — 8021x-fails-at-the-printer

Every NAC project we've watched stall, stalled at a printer. 🖨️

The laptops are easy — supplicant, domain join, certificate, done. Ninety percent of the devices, maybe ten percent of the work.

Then you meet the rest of the network: the printer doing something creative with EAP, HVAC controllers, the lab instrument whose vendor says "static IP, or the warranty is void."

The repeated mistake is designing the policy first and treating exceptions as cleanup. They aren't cleanup — they're the majority of the work and all of the political risk, because each one has an owner who doesn't report to you.

So design the exception process before the policy — fallback decided up front, an owner per exception class, an expiry on every exception.

Projects die on the vendor who says "it can't do 802.1X" — and nobody willing to say "then it goes in the restricted segment."

The laptops are the demo. The exceptions are the project.
