---
description: Plan the next publishing cycle — assign unpublished ideas to dates per preset (Professional/Business)
argument-hint: [horizon or instructions, e.g. "2 weeks" or "through Sep 15, Business only"]
---

Build the forward publishing schedule.

Instructions for this run: **$ARGUMENTS** (default: the next 2 weeks after the current queue tail).

Follow `agents/SCHEDULER.md` exactly. In short:

1. **Find the queue tail** in `content/INDEX.md` — last scheduled date + preset — and continue the standing cadence: daily 4pm EDT, alternating Professional/Business, Mondays dark. Check `ideas/schedule-*.md` for unfired rows; never double-book a date.

2. **Pull eligible ideas per preset:** only rows with `Developed? = —` from `ideas/ideas-*.md`, matching each file's declared preset. Skip stat-gated ideas (`Cited stat? = yes`) unless told otherwise. Drain Top-5 leftovers first, then oldest file first; spread themes.

3. **Show the plan** — Professional section first, then Business, with Date · Day · Idea · Source · Status — and **wait for approval**.

4. On approval, **write `ideas/schedule-<YYYY-MM>.md`** and commit (never stage images).

If a pool is dry, stop and recommend `/ideate` for that preset instead of stretching. This command never publishes — each row fires later via `/publish <idea> - <preset>, <date> 4pm`.
