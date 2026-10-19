# X — segment-iot-without-forklift

## Single (publish this)

Segmenting IoT doesn't need a forklift.

Days 1–10: profile by class, not vendor.
Days 10–20: one VLAN per class, ACL permits everything and logs it.
Days 20–30: the ACL writes itself.

Find them. Fence them. Then let them out on purpose.

#IoT #NetOps

## Thread (alternate)

1/ Segmenting IoT doesn't need a forklift. It needs thirty days and the gear you already own. 🧵

2/ Days 1–10 — profile what's talking. DHCP options and MAC OUI give you the vendor. mDNS says what the device thinks it is. Flow data says where it actually goes.

3/ Group by device class — cameras, badge readers, HVAC, printers, lab gear. Not by vendor, not by building. Class is what policy gets written against.

4/ Days 10–20 — one VLAN per class, routed gateway, ACL that permits everything and logs it. You're not enforcing yet. You're recording the truth.

5/ One class at a time. Pick the boring one first — the camera vendor is not who you want as your opening argument.

6/ Days 20–30 — the ACL writes itself. Cameras reach the NVR, NTP and DNS. Badge readers reach their controller. Nothing reaches the user VLAN. Flip to deny-by-default with an explicit permit list.

7/ No new platform. No endpoint agent. Routed VLANs and access lists on hardware you already pay maintenance on.

8/ The hard part isn't technical. Segmentation forces a conversation about who owns the cameras — and who gets called when a badge reader stops opening a door at 6am.

9/ Find them. Fence them. Then let them out on purpose. #IoT #NetOps
