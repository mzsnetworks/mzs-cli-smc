# Master — run-it-twice

**Preset:** Professional — LinkedIn **personal profile** (no pageId) + Instagram @mzsnetworks
**Date:** 2026-11-28
**Thesis:** A script that only works on a clean device is a one-shot procedure, not automation, because the operational value of automation is being able to run it again — after a partial failure, on a device that drifted, as a routine convergence. Scripts fail idempotence quietly: the second run returns success while appending rather than converging. The test is to run it twice and diff.
**Pillar:** Network Automation
**Source:** ideas-2026-10-18 #8
**Stats:** none. Judgment and practice only.

---

If you cannot run it twice, it is not automation. It is a one-shot procedure that happens to be typed out.

This sounds like a definition argument and it is not. It decides what the thing is worth on the day you need it.

The value of automation is almost never the first run. It is the run after something went wrong halfway. It is the run against a device that drifted. It is the run you do on a schedule to pull forty sites back to a known state. All of those are second runs, and a script that only works against a clean device cannot do any of them.

What makes this expensive is that scripts fail this test quietly. The second run does not error. It appends an access-list entry that is already there, adds a second route statement, or pushes a block of config that was fine and is now duplicated. The output says success. Nobody looks, because why would you look at a success.

Then someone runs it against a half-configured device during an actual incident and finds out.

The test is dull and takes a minute. Run it twice against the same device and diff the config. If the second run produced no change, you have automation. If it produced a change, you have a procedure that assumes a starting state nobody will remember to check.

Most of the fix is unexciting: check before you set, make the operation declarative rather than additive, and let the tooling do the comparison where it can. Modern config management handles a lot of this, which is why hand-rolled scripts are where this bites.

The useful mental model is that automation should describe the state you want, not the keystrokes you would have typed. A description can be applied any number of times. Keystrokes can be applied exactly once.

Run it twice. The second run tells you what you actually built.

Which of your scripts have you genuinely run twice in a row?

#NetworkAutomation #NetOps #InfrastructureAsCode
