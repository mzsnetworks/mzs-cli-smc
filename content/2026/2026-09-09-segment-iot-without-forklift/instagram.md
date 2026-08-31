# Instagram — segment-iot-without-forklift

Segmenting IoT doesn't need a forklift. 🔒

It needs thirty days and the gear you already own.

You counted the devices. Now what?

Here's the plan we run. ⚙️

📍 Days 1–10 — profile what's talking

Not a purchase. A capture.

→ DHCP options and MAC OUI give you the vendor
→ mDNS and SSDP tell you what the device thinks it is
→ flow data tells you where it actually goes

Group by device class — cameras, badge readers, HVAC, printers, lab gear. Not by vendor. Not by building. Class is what policy gets written against.

📍 Days 10–20 — one VLAN per class, logging only

Routed gateway. An ACL that permits everything and logs it.

You're not enforcing yet. You're recording the truth.

One class at a time — and pick the boring one first. The camera vendor is not who you want as your opening argument.

📍 Days 20–30 — write the policy from the logs

Now the ACL writes itself.

→ cameras reach the NVR, NTP and DNS
→ badge readers reach their controller
→ nothing reaches the user VLAN
→ nothing reaches the internet unless someone can say why

Then flip to deny-by-default with an explicit permit list.

No new platform. No endpoint agent. Hardware you already pay maintenance on.

The hard part isn't technical. Segmentation forces a conversation about who owns the cameras.

Find them. Fence them. Then let them out on purpose.

Which class would you start with? 👇

#IoT #NetworkSecurity #NetworkEngineering #NetOps #Networking
