---
description: Plan the next publishing cycle — assign unpublished ideas to dates per preset (Professional/Business/Marketing)
argument-hint: [horizon or instructions, e.g. "2 weeks" or "through Sep 15, Business only"]
---

Build the forward publishing schedule.

Instructions for this run: **$ARGUMENTS** (default: the next 2 weeks after the current queue tail).

Follow `agents/SCHEDULER.md` exactly. In short:

1. **Resolve the dates.** Preset is locked to weekday: **Marketing = Mon**, **Professional = Tue/Thu/Sat**, **Business = Wed/Fri/Sun**. Everything posts at 4pm EDT (`20:00:00Z`) — except Monday, which carries **two** slots for one marketing idea: ES at 2pm EDT (`18:00:00Z`) and EN at 4pm. If the run names a week ("Professional for the week of Aug 16" — weeks run Sunday→Saturday, named by their Sunday), plan exactly that preset's days in it: three for Professional or Business, **one Monday for Marketing**. Otherwise find that lane's queue tail — `content/INDEX.md` or `marketing/INDEX.md` — and continue forward. Check `ideas/schedule-*.md` for unfired rows; never double-book a date.

2. **Pull eligible ideas per preset:** only rows with `Developed? = —` from `ideas/ideas-*.md` (Professional, Business) or `ideas/marketing-ideas-*.md` (Marketing), matching each file's declared preset. Never cross-assign. Skip stat-gated ideas (`Cited stat? = yes`) unless told otherwise. Drain Top-5 leftovers first, then oldest file first; spread themes — across both trees, since a marketing post and a thought-leadership post on the same argument in one week reads as repetition.

3. **Show the plan** — Professional section first, then Business, then Marketing, with Date · Day · Idea · Source · Status — and **wait for approval**. Marketing rows need no language column; every row is both.

4. On approval, **write `ideas/schedule-<YYYY-MM>.md`** and commit (never stage images).

If a pool is dry, stop and recommend `/ideate` for that preset instead of stretching — and flag the Marketing pool early, below four undeveloped rows, since one idea a week empties it faster than it looks. This command never publishes — each row fires later via `/publish <idea> - <preset>, <date> 4pm`, and a Marketing row fires both languages in that one run.
