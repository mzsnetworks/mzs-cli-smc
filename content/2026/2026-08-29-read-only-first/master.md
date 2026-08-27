# Master — read-only-first

**Preset:** Professional (personal LinkedIn + IG @mzsnetworks)
**Date:** 2026-08-29 (Sat)
**Source idea:** ideas-2026-07-27 #3 (NA · How-to)
**Thesis:** Your first automation should change nothing. Read-only first — collect, diff, report. Write access is earned.
**Stats:** none — judgment/how-to post, no factcheck gate.

---

My first automation in a new environment changes nothing. On purpose.

The instinct runs the other way. Prove value fast, push a config, save somebody an hour, point at the hour. I understand the pull. I think it's backwards.

Nobody's real objection to automation is "it doesn't save time." The objection is "I don't want that thing near production." A script that writes on day one is asking for trust it hasn't earned yet — and the first time it surprises anyone, it doesn't get a second run.

So: read-only first. Collect, diff, report.

It can't hurt anyone. That's not a limitation, it's the feature — it's the only version of the script you're allowed to point at every device on day one.

And running everywhere is where the value actually is:

→ Collect, and you find out how many devices genuinely answer. The inventory is wrong. It always is. The collector proves it harmlessly, in an afternoon, instead of a change window proving it at 2am.

→ Diff, and you learn which changes happen that nobody files a ticket for. That list is the most honest document in the environment.

→ Report, and you've built the thing that makes people want the fix automated. Nobody asks for a remediation script. Everybody asks for one after they've stared at the drift report for a month.

There's a second payoff. Every failure mode of the write version shows up in the read version first, for free — bad credentials, timeouts, the platform that formats output differently, the one device that answers slowly enough to break your loop. Find those while the worst outcome is a blank column in a CSV.

Then you move: read, report, suggest, apply with approval, apply.

A script that can't hurt anyone gets to run everywhere. A script that can hurt someone gets to run on three devices with a person watching.

Reach comes before power. Write access is earned.

What was the first thing you automated — and did it write?
