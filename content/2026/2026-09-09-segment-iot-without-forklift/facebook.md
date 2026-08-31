# Facebook — segment-iot-without-forklift

Segmenting IoT doesn't need a forklift. It needs thirty days and the gear you already own. 🔒

Days 1–10: profile what's talking. Not a purchase — a capture. DHCP options and MAC OUI give you the vendor, flow data tells you where it goes. Group by device class, not by vendor.

Days 10–20: one VLAN per class, with an ACL that permits everything and logs it. You're recording the truth, not enforcing it. One class at a time, and pick the boring one first.

Days 20–30: the ACL writes itself. Cameras reach the NVR, NTP and DNS. Badge readers reach their controller. Nothing reaches the user VLAN. Flip to deny-by-default.

No new platform. No endpoint agent.

The hard part isn't technical — it's that segmentation forces a conversation about who owns the cameras.

Which class would you segment first?
