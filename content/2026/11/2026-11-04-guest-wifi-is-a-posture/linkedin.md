# LinkedIn — guest-wifi-is-a-posture


Guest Wi-Fi is a security posture, not an amenity.

It rarely gets designed that way. It gets designed around the splash page — the logo, the terms checkbox, whether it collects an email address. That is the least interesting decision in the whole thing, and it is usually the only one anybody reviews.

The decisions that matter are the ones nobody writes down.

What can the guest network reach? In most environments we assess, the honest answer is the internet plus three things somebody needed once: a printer, a conference room display, and a file share that was supposed to be temporary.

What is it allowed to resolve? A guest VLAN pointed at the internal resolver can enumerate the estate from the parking lot. No exploit required — just a name server answering questions it has no reason to answer.

How long does a device stay on it? A guest lease measured in days is not a guest network. It is an unmanaged corporate one with a nicer login page.

What happens when it gets abused? Somebody will eventually do something on it that generates a complaint to your ISP. The question is whether you can tell which device, and whether anybody owns the answer.

None of this argues for making guest access harder. The business reason for it is real, and friction at the splash page just moves people onto a hotspot, which is worse for everyone.

It argues for designing the parts that carry risk, and treating the portal as what it is: a greeting.

Guest Wi-Fi is the one network you intend strangers to use. It should be the one you can describe most precisely.

What can your guest network reach that you would not put in writing?

#NetworkSecurity #WirelessNetworking #NetworkEngineering
