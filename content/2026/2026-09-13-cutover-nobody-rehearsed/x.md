# X — cutover-nobody-rehearsed

## Single (publish this)

Every project we've been called into late failed at the same milestone: the cutover.

Everything before it was tested in pieces. The cutover is the only integration test — and it runs in production, once, at 2am.

Has anyone actually run it?

#NetOps #ChangeManagement

## Thread (alternate)

1/ Every project we've been called into late failed at the same milestone. Not design. Not staging. The cutover. 🧵

2/ Design gets reviewed by four people who all want to be right. The gear arrives, gets built, configured, burned in, and works on the bench.

3/ Then it fails at the cutover — because the cutover is the first time any of it runs together.

4/ Everything before was tested in pieces. The cutover is the only integration test the project ever gets, and it runs in production, once, at 2am, with users arriving in six hours.

5/ Reading the runbook aloud in a conference room is not a rehearsal. A rehearsal has the actual commands, run by the actual person, in the actual order, with a clock going.

6/ What a rehearsal surfaces:
• the 10-minute step that takes 40
• order dependencies nobody wrote down
• a credential on one laptop, owner on PTO
• the back-out that's only ever been written

7/ That last one matters most. A rollback you've never performed isn't a safety net. It's a second unrehearsed cutover, attempted by tired people at 4am when the first has already gone wrong.

8/ Design gets reviewed. Hardware gets staged. The sequence gets discovered — at 2am, in front of everyone. #NetOps #ChangeManagement
