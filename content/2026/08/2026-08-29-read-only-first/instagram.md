# Instagram — read-only-first

My first automation in a new environment changes nothing. On purpose. 🔒

The instinct runs the other way — prove value fast, push a config, save somebody an hour, point at the hour.

I think that's backwards.

Nobody's real objection to automation is "it doesn't save time." It's "I don't want that thing near production."

A script that writes on day one is asking for trust it hasn't earned. The first time it surprises anyone, it doesn't get a second run.

So: read-only first. Collect, diff, report.

It can't hurt anyone — and that's the feature, not the limitation. It's the only version of the script you're allowed to point at every device on day one. ⚙️

→ Collect, and you find out how many devices genuinely answer. The inventory is wrong. It always is. The collector proves it harmlessly, in an afternoon — instead of a change window proving it at 2am.

→ Diff, and you learn which changes happen that nobody files a ticket for. That list is the most honest document in the environment.

→ Report, and you've built the thing that makes people want the fix automated. Nobody asks for a remediation script. Everybody asks after a month of staring at the drift report.

Second payoff: every failure mode of the write version shows up in the read version first, for free. Bad credentials, timeouts, the platform that formats output differently, the one device slow enough to break your loop.

Find those while the worst outcome is a blank column in a CSV.

Then you move: read → report → suggest → apply with approval → apply.

A script that can't hurt anyone gets to run everywhere. A script that can hurt someone runs on three devices with a person watching.

Reach comes before power. Write access is earned. 👇

#NetworkAutomation #NetDevOps #NetOps #Python #Networking
