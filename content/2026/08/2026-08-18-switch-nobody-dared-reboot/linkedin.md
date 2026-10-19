# LinkedIn — switch-nobody-dared-reboot

There was a switch in that data center with seven years of uptime. Nobody was proud of it. Everybody was afraid of it.

It came up in every maintenance window and left the same way: "not that one." Installed by someone who'd left the company twice ago. It carried a couple of VLANs that appeared on no diagram. And it had never, in seven years, been power-cycled on purpose.

The uptime number got quoted like an achievement. It wasn't. It was a measure of how long we'd been avoiding a conversation.

Here's what seven years of uptime actually tells you. The recovery path has never been tested — not the boot config, not the licenses, not the optics that sometimes don't come back. Every unpatched bug from seven years of advisories is still in there, waiting for the right packet. And the running config drifted from the saved config in ways nobody can enumerate — every fix since the install typed live, half never written.

That switch wasn't stable. It was untested. Those are very different states that look identical on a dashboard.

The fear compounds. Every year it stays up, rebooting gets scarier — the blast radius of "it doesn't come back" grows with everything else you've hung off it since. Avoidance isn't free. It's a loan at a rising rate.

We eventually did it. Saturday, config backed up, console cable in hand, a spare in the rack, vendor case open. It took four minutes. Two interfaces didn't come back cleanly and we fixed them in ten more.

That's the part I think about. The disaster we'd feared for seven years took fourteen minutes on a day of our choosing. The alternative was the same fourteen minutes on a day of its choosing — probably a Tuesday, at 9am, during a quarter close.

You don't have a stable switch. You have an unscheduled outage with a countdown you can read.

What's the device on your network that everyone quietly steers around?

#NetworkEngineering #BrownfieldEngineering #NetOps
