# Master — switch-nobody-dared-reboot

**Idea:** ideas-2026-07-27 #4 (Brownfield Engineering · Story)
**Preset:** Professional (personal LinkedIn + MZS Instagram) · **Slot:** 2026-08-18 4:00 PM EDT
**Thesis:** Seven years of uptime isn't stability — it's fear with a counter. Untested recovery, unpatched bugs, a reload nobody wants to own.
**Voice:** first person, war story.
**Stats:** none. The uptime figure is from the story, not a claim about the industry. Factcheck: PASS.

---

There was a switch in that data center with seven years of uptime. Nobody was proud of it. Everybody was afraid of it.

It came up in every maintenance window and left the same way. "Not that one." It had been installed by someone who'd left the company twice ago. It carried a couple of VLANs that appeared on no diagram. And it had never, in seven years, been power-cycled on purpose.

The uptime number got quoted like an achievement. It wasn't. It was a measure of how long we'd been avoiding a conversation.

Here's what seven years of uptime actually tells you. The recovery path has never been tested — not the config that loads on boot, not the licenses, not the optics that sometimes don't come back. Every unpatched bug from seven years of advisories is still in there, waiting for the right packet. And the config running in memory has drifted from the config on disk in ways nobody can enumerate, because every fix since the install was typed live and half of them were never saved.

That switch wasn't stable. It was untested. Those are very different states that look identical from a monitoring dashboard.

The real problem is that the fear compounds. Every year it stays up, rebooting gets scarier, because the blast radius of "it doesn't come back" grows with everything else you've hung off it since. Avoidance isn't free. It's a loan at a rising rate.

We eventually did it — on a Saturday, with the config backed up, a console cable in hand, a spare in the rack, and the vendor case open before we touched anything. It took four minutes. Two interfaces didn't come back cleanly and we fixed them in ten more.

That's the part I think about. The disaster we'd feared for seven years took fourteen minutes on a day of our choosing. The alternative was the same fourteen minutes on a day of its choosing — probably a Tuesday, at 9am, during a quarter close.

High uptime on a device you're afraid to touch isn't reliability. It's an untested restore with a nice-looking number on it.

You don't have a stable switch. You have an unscheduled outage with a countdown you can read.

What's the device on your network that everyone quietly steers around?

#NetworkEngineering #BrownfieldEngineering #NetOps
