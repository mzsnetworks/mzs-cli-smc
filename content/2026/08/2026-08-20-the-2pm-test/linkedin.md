# LinkedIn — the-2pm-test

Here's a maturity metric nobody puts on a slide: what percentage of your changes would you be willing to run at 2pm?

Not "could" — it would technically execute at any hour. Willing. With users online, phones ringing, somebody from finance three desks away.

For most teams the honest answer is low. That number tells you more about your operation than any dashboard — because a 2am window isn't a safety control. It's a confession.

Think about what the window actually buys. Not safety — the same commands run against the same devices with the same blast radius. It buys fewer witnesses. We schedule at 2am because we expect breakage and we'd rather it happen when nobody's watching.

That isn't managing risk. It's managing embarrassment.

It costs more than people admit. At 2am you're working with your worst engineers — not the least skilled, the least rested. Same people, six hours past good judgment. Detection is slower because normal traffic is gone — the thing that would have screamed at 2pm sits quietly until morning. And the vendor TAC you might need has its B-team on.

You've traded observability, judgment, and support for privacy.

Not every change belongs in daylight. Some genuinely require a quiet network — a core upgrade, a migration that drops sessions no matter how careful you are. Those are real. But they should be the exception you can name, not the default you've stopped questioning.

The test is diagnostic, not aspirational. Sort last quarter's changes: which would you have run at 2pm? The ones that fail aren't failing because of the hour. They're failing because the pre-checks are thin, the rollback is theoretical, the blast radius is unclear, or the change is bigger than it needs to be.

Fix those four things and the change moves into daylight on its own. Nobody has to be brave.

The goal isn't to be braver at 2am. It's to build changes you'd be willing to run at 2pm.

What percentage of yours would pass?

#NetworkEngineering #ChangeManagement #NetOps
