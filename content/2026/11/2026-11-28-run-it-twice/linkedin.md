# LinkedIn — run-it-twice


If you cannot run it twice, it is not automation. It is a one-shot procedure that happens to be typed out.

This sounds like a definition argument and it is not. It decides what the thing is worth on the day you need it.

The value of automation is almost never the first run. It is the run after something went wrong halfway. It is the run against a device that drifted. It is the run you do on a schedule to pull forty sites back to a known state. All of those are second runs, and a script that only works against a clean device cannot do any of them.

What makes this expensive is that scripts fail the test quietly. The second run does not error. It appends an access-list entry that is already there, adds a second route statement, or pushes a block of config that was fine and is now duplicated. The output says success. Nobody looks, because why would you look at a success.

Then someone runs it against a half-configured device during an incident and finds out.

The test is dull and takes a minute. Run it twice against the same device and diff the config. If the second run produced no change, you have automation. If it produced a change, you have a procedure that assumes a starting state nobody will remember to check.

Most of the fix is unexciting: check before you set, make the operation declarative rather than additive, and let the tooling compare where it can.

The useful model is that automation should describe the state you want, not the keystrokes you would have typed. A description can be applied any number of times. Keystrokes can be applied exactly once.

Run it twice. The second run tells you what you actually built.

Which of your scripts have you genuinely run twice in a row?

#NetworkAutomation #NetOps #InfrastructureAsCode
