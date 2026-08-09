# LinkedIn — iot-inventory-not-security

Your IoT problem isn't security. It's inventory.

The budget always arrives pointed at the same things: segmentation, NAC, a firewall rule set. Reasonable purchases. Then the project kicks off, someone asks the first real question, and the room goes quiet.

What's actually on the network? Not what the asset spreadsheet says — what's on it right now, drawing an IP.

We've walked into buildings where a single flat VLAN was carrying hundreds of devices nobody in the room could name. Not carelessness — IoT never arrives through the network team. Facilities buys the cameras. Clinical buys the pumps. Marketing buys the lobby displays. A pilot ends, the team disbands, and the devices stay powered on for six more years.

The MAC address table is the most honest document in the building. It doesn't care what the spreadsheet claims.

This is why security-first sequencing stalls. A policy needs a subject. "Least privilege for IoT" isn't a policy until you can say which devices, doing what, talking to whom. Write the rule before the count and you get one of two outcomes: a rule so loose it permits everything, or a rule so tight it breaks a system nobody knew was load-bearing — usually at 3am, usually something clinical.

The order that works is boring. Enumerate what's there. Identify what each thing is. Classify by behavior — what does this device actually need to talk to? Then, and only then, write policy per class.

The uncomfortable part is that enumeration finds things nobody wants to own. The badge reader on firmware that went out of support four years ago. The camera quietly shipping video to a vendor cloud. That discomfort isn't a reason to skip the count — it's the value of it. Those devices were risks the whole time. Just unlisted.

You can't write policy for a device you can't name.

Count first. Segment second. The firewall is the last step, not the first.

How many devices are on your network right now — within ten?

#IoT #NetworkSecurity #NetworkEngineering
