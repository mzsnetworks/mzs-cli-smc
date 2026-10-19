# Master — automate-toil-first

**Idea:** ideas-2026-07-11 #9 (NA · Listicle) — The 5 tasks worth automating first are never the ones people ask for.
**Preset:** Business (all four on the MZS account) — company voice "we"
**Publish date:** 2026-08-07
**Stat gate:** none — no numeric claims.

---

The 5 tasks worth automating first are never the ones people ask for.

The asks we hear: a self-service portal, a chatbot, auto-remediation, something that demos well in front of leadership. Impressive on a projector. Irrelevant at 3am.

The five that actually pay, in the order we build them:

1. State capture, before and after every change. Configs, routes, neighbors, counters — snapshotted automatically. When something breaks, "what changed?" takes one diff, not one hour.

2. Config backup with diff alerting. Every device, every day, and a notification when running config drifts from the last approved change. Boring. Priceless.

3. Pre- and post-maintenance health checks. The same checklist the senior engineer runs by hand — encoded, so every window opens and closes with the same rigor at 2am as at 2pm.

4. The recurring restart runbook. Whatever you already restart on a schedule out of self-defense — automate the procedure and its verification, identically, every time, while you hunt the root cause.

5. Alert enrichment. Attach the device's state, recent changes, and last occurrence to the ticket before a human opens it. The first fifteen minutes of every incident is an engineer collecting context — hand it to them.

Notice the pattern: none of these change the network. They capture, verify, and inform. That's deliberate — automation earns trust by being right before it earns write access.

The demo automates what impresses. The discipline automates what pages you.

Automate the toil first. The portal can wait.

What pages your team most — and is it on anyone's automation list?
