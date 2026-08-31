# LinkedIn — cutover-nobody-rehearsed


Every project we've been called into late failed at the same milestone.

Not design. Design gets reviewed by four people who all want to be right. Not procurement. Not staging either — the gear arrives, gets built, labeled, configured, burned in, and it works on the bench.

It fails at the cutover. Because the cutover is the first time any of it runs together.

That's the whole problem in one sentence. Everything before it was tested in pieces. The cutover is the only integration test the project ever gets, and it runs in production, once, at 2am, with users arriving in six hours.

So the question we ask before a cutover date gets committed is simple: has anyone run this?

Reading the runbook aloud in a conference room is not a rehearsal. A rehearsal has the actual commands, executed by the person who will execute them, in the actual order, against something real — even one pair of switches — with a clock running.

What a rehearsal reliably surfaces:

→ The step budgeted at ten minutes that takes forty
→ Order dependencies nobody wrote down, discovered the moment two steps get swapped
→ A credential that exists on one laptop, belonging to someone on PTO that weekend
→ The back-out that has never once been executed, only written

That last one matters most. Almost every plan has a back-out section. Almost none of them have been run. A rollback you've never performed isn't a safety net — it's a second unrehearsed cutover, attempted by tired people at 4am when the first one has already gone wrong.

None of this requires a digital twin or a lab that matches production. It requires running the sequence once, in advance, on whatever you've got, and being honest about what breaks.

Design gets reviewed. Hardware gets staged. The sequence gets discovered — at 2am, in front of everyone.

When did you last rehearse a back-out? Not write one. Run one.

#NetworkEngineering #ChangeManagement #NetOps
