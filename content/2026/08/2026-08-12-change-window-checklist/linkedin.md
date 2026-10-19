# LinkedIn — change-window-checklist

The 2am rollback isn't bad luck. It's a checklist that was never written.

Every messy change window we've ever been called into failed the same way: not on the change itself, but on everything around it. The checklist that kills those nights has four lines.

1. Pre-checks, captured. Snapshot the state before touching anything — configs, routing tables, neighbors, counters. Not "looks good." Recorded. The post-change comparison is only as good as the baseline you saved.

2. Blast radius, written down. What can this change break, worst case? Which services, which sites, which users. If the honest answer is "we're not sure," the change isn't ready for a window — it's still in design.

3. A back-out that's been run. A rollback plan that has never been executed is a theory. Rehearse it before the window, and mark the point of no return — the step after which rolling back stops being an option and becomes its own incident.

4. One named decision-maker. When it goes sideways at 1:40am, the worst possible instrument is a group-chat vote. One person owns the proceed-or-rollback call — against criteria written at 2pm, not vibes at 2am.

Notice what the checklist really does: it moves every decision out of the window. The window is for execution. The thinking happened earlier, in daylight, with coffee and a whiteboard — not adrenaline.

That's why well-run changes look boring. Boring is the achievement.

Plan at 2pm. Execute at 2am. Never think at 2am.

What's the one item on your change checklist that has saved a night?

#NetworkEngineering #ChangeManagement #NetOps
