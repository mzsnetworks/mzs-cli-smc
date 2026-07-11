A runbook nobody runs isn't documentation. It's fiction with a table of contents.

We write them with the best intentions. The failover procedure, the disaster-recovery steps, the "how to rebuild the core switch" doc. Then we file it in the wiki and feel safer. The safety is imaginary.

Because a runbook is only true the day it's written. The network keeps moving. Someone decommissions the jump host in step 4. The IP in step 7 gets re-used. The CLI syntax changes in a firmware upgrade. None of that updates the doc — it has no idea the world moved. It just sits there, quietly going stale, wearing the authority of something that was once correct.

You find out at 3am. Production is down, you open the trusted runbook, and step 4 references a server that hasn't existed since last year. Now you're debugging the outage and the runbook at the same time.

The value of a runbook was never in writing it. It's in running it. An unexecuted procedure is an untested assumption in a nice font.

There are only two ways to keep one honest:

Automate it — make the script the runbook, so it can't drift without failing loudly. A procedure that runs weekly can't quietly rot; the rot surfaces as a broken job, not a 3am surprise.

Or rehearse it — run the failover on a Tuesday afternoon on purpose. Game days turn documentation into muscle memory and flush out the stale steps while the stakes are low.

Both share the same principle: the only runbook you can trust is one that gets exercised. Everything else is confidence you haven't earned.

Stop writing runbooks to feel prepared. Run them, so you actually are.

Which of your "critical" runbooks has nobody actually executed in the last year?

#NetworkOperations #NetDevOps #Reliability
