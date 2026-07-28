# Master — show-command-lied

**Idea:** ideas-2026-07-08 #7 (LP · Confession) — "Most outages are self-inflicted." The one I caused by trusting a `show` command that lied.
**Preset:** Professional (LinkedIn personal + IG @mzsnetworks)
**Publish date:** 2026-08-04
**Stat gate:** none — "most outages are self-inflicted" stays framed as judgment (defended opinion), no numeric claims.

---

Most outages are self-inflicted. I say that as someone who inflicted one.

Maintenance window. Before taking down the primary, I checked the failover path the way everyone does — a show command. Standby: hot. Sync: complete. Every field green.

I pulled it. The site went dark.

The standby was "ready" in every way the control plane could measure. But leftover state from an earlier change — never cleaned up — meant it couldn't actually take over. The command reported what the box believed. The network did what it was actually able to do.

Here's the part that changed how I work: the show command didn't lie. It answered, precisely, the question I asked. Which wasn't the question that mattered.

I asked: does the control plane think the standby is ready?
I needed: will packets flow when I do this?

Those are different questions. Outages live in the gap between them.

"Human error" would have been the easy write-up. The honest one: my verification step verified belief, not behavior. I read state instead of testing the path. Every failover plan I've written since includes actually failing over — in a window, on purpose, before it matters.

Blaming hardware is comfortable. Blaming the tool is convenient. Auditing your own verification is the only version that prevents the next one.

Show commands report belief. Traffic reports reality. Verify with the one that carries packets.

What's the show command that burned you?
