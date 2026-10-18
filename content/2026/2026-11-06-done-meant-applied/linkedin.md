# LinkedIn — done-meant-applied


A maintenance window that finishes two hours early is not good news.

We ask what got skipped. Usually nothing was skipped on purpose. The work went in cleanly, nothing threw an error, the team was tired, and "applied without error" quietly became "done."

Those are not the same state, and the gap between them is where Monday morning lives.

The pattern is specific. A change goes in Saturday night. Every command returns without complaint. Interfaces come up, the device is reachable, the config matches what was staged. By every signal available at 2am, it worked. Then Monday arrives, real traffic shows up with real patterns, and something that only shows under load, or only on the path nobody tested, starts failing.

The window was not too short. The definition of done was too small.

"Applied" is a statement about the device. "Verified" is a statement about the service — and only one of them is what the business asked for.

So write the verification into the change record before the window opens, as a named condition with a named owner. Not "confirm change successful." That is a checkbox, and a tired engineer will tick it honestly while meaning something narrower than you do. Closer to: this specific transaction completes, from this specific client, measured this way.

Then the window is not over when the work is applied. It is over when that condition is observed, or when it is not and the rollback runs.

This makes windows longer and more honest. A window that runs its full length because somebody is watching a real transaction is not inefficiency. It is the only part of the night that produces evidence.

A change that was applied is a change you made. A change that was verified is one you can defend.

What does "done" mean in your change process?

#ChangeManagement #NetworkEngineering #ITOperations
