# Instagram — run-it-twice


If you can't run it twice, it isn't automation. 🔁

It's a one-shot procedure that happens to be typed out.

That sounds like a definition argument. It isn't. It decides what the thing is worth on the day you need it.

The value of automation is almost never the first run:

→ The run after something went wrong halfway
→ The run against a device that drifted
→ The scheduled run that pulls forty sites back to a known state

All of those are second runs. ⚠️

What makes it expensive is that scripts fail this quietly. The second run doesn't error.

It appends an access-list entry that's already there. Adds a second route statement. Pushes a block of config that was fine and is now duplicated.

The output says success. Nobody looks — why would you look at a success? ⚙️

Then someone runs it against a half-configured device during an incident and finds out.

The test is dull and takes a minute: run it twice against the same device and diff the config.

No change on the second run? Automation. A change? A procedure that assumes a starting state nobody will check.

Automation should describe the state you want, not the keystrokes you'd have typed. A description can be applied any number of times. Keystrokes exactly once.

Which of your scripts have you genuinely run twice in a row?

#NetworkAutomation #NetOps #InfrastructureAsCode #ITOperations #Infrastructure
