# LinkedIn — segment-iot-without-forklift

Segmenting IoT doesn't need a forklift. It needs thirty days and the gear you already own.

A while back we argued the IoT problem is inventory, not security — you can't write policy for a device you can't name. The fair question that came back: fine, we counted them. Now what?

Here's the plan we run.

**Days 1–10: profile what's talking.**
Not a purchase. A capture. DHCP options and MAC OUI give you the vendor. mDNS and SSDP tell you what the device thinks it is. Flow data tells you where it actually goes. Group the results by device *class* — cameras, badge readers, HVAC controllers, printers, lab gear — not by vendor and not by building. Class is what policy gets written against.

**Days 10–20: one VLAN per class, logging only.**
Move a single class into its own VLAN with a routed gateway. Apply an ACL that permits everything and logs it. You're not enforcing yet; you're recording the truth. One class at a time, and pick the boring one first. The camera vendor is not who you want as your opening argument.

**Days 20–30: write the policy from the logs.**
Now the ACL writes itself. Cameras reach the NVR, NTP and DNS. Badge readers reach their controller. Nothing reaches the user VLAN, and nothing reaches the internet unless somebody can say why. Then flip from permit-and-log to deny-by-default with an explicit permit list — per class, in the order you profiled them.

That's the whole thing. No new platform, no agent on the endpoint, no rip-out. Routed VLANs and access lists on hardware you're already paying maintenance on.

The part nobody warns you about isn't technical. Segmentation forces a conversation about ownership. Somebody has to say out loud who owns the cameras, and who gets called when a badge reader stops opening a door at 6am. The network can enforce a policy. It can't invent one.

Find them. Fence them. Then let them out on purpose.

Which class would you segment first — and who would you have to convince?

#IoT #NetworkSecurity #NetworkEngineering
