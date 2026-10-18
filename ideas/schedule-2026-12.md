# Publishing Schedule — Dec 2026

Standing cadence: **one post daily at 4:00 PM local — Professional Tue/Thu/Sat, Business Wed/Fri/Sun. Mondays are the Marketing lane** and carry two slots for one idea: ES at 2:00 PM, EN at 4:00 PM.

> **December runs on EST, not EDT.** US daylight time ended **Sun Nov 1, 2026**, so the UTC offset is −5 and every slot in this file is **`21:00:00Z`** for 4:00 PM and **`19:00:00Z`** for the Marketing ES slot. The `20:00:00Z` / `18:00:00Z` used from July through Oct 31 now lands an hour early, at 3:00 PM and 1:00 PM. Check the offset on every `/publish` run in this month and in November.

Fire each with: `/publish <idea> - <preset>, <date> 4pm`. A Marketing row fires both languages in one run. Mark rows DONE (with slug) as they're scheduled; update the source ideas file + the lane's INDEX per the normal publish flow.

**This month stops on Dec 23.** Decided 2026-10-18: the calendar goes dark **Dec 24–31 in all three lanes** rather than spending strong ideas on the worst engagement week of the year. The marketing lane had already made that call for itself on 2026-09-20 by pulling `we-hand-it-back` out of Dec 21. So December carries **10 Professional + 10 Business + 2 Marketing** instead of the 14 + 13 + 4 the cadence would otherwise produce, and the seven freed ideas stay in their pools for January.

Planned 2026-10-18, oldest file first per `agents/SCHEDULER.md`. Eight of ten Professional rows and six of ten Business rows come out of the July and August pools; the batches written on 2026-10-18 only fill what the older files couldn't.

## Professional (LI personal + IG @mzsnetworks)

| Date | Day | Idea | Source | Status |
|------|-----|------|--------|--------|
| Dec 1 | Tue | What's the oldest device still in your production path — and why is it still there? | ideas-2026-07-08 #15 | — |
| Dec 3 | Thu | 5 things you automated that you should have deleted instead — toil you enshrined | ideas-2026-07-08 #8 | — |
| Dec 5 | Sat | Every AIOps tool promises to cut alert noise. The noise was never the problem — the missing runbook was | ideas-2026-07-08 #18 | — |
| Dec 8 | Tue | The ISSU that refused to upgrade — hidden operational state, not the documented procedure, killed it | ideas-2026-07-08 #2 | — |
| Dec 10 | Thu | CI for network configs: pre-merge lint + dry-run diff, so a bad change fails in the PR, not at 2am | ideas-2026-07-08 #13 | — |
| Dec 12 | Sat | The migration went to plan. The config inconsistencies that surfaced after were the real project | ideas-2026-07-08 #11 | — |
| Dec 15 | Tue | The "random slowness" that was unicast flooding — a MAC aging timer shorter than the ARP cache, and a switch flooding every unknown destination | ideas-2026-10-18 #4 | — |
| Dec 17 | Thu | AI copilots are fastest at being confidently wrong. The senior skill is now *disagreeing* with the model | ideas-2026-07-08 #10 | — |
| Dec 19 | Sat | A rollback plan that crosses an irreversible step is not a rollback plan | ideas-2026-10-18 #18 | — |
| Dec 22 | Tue | The multicast problem that wasn't multicast — the network exposed an app design flaw | ideas-2026-07-08 #9 | — |

**One adjacency to write around.** Dec 10 (`#13`, CI for network configs) argues what the marketing lane argued on Oct 19 with `test-before-it-touches-a-device` for Config Modeling. Seven weeks apart and a different lane, so it stands — but write it toward the pull-request workflow and the reviewer's experience, not toward "test it before it reaches production," or it reads as the same post in a different voice.

## Business (all four on MZS · LI + IG full carousel · FB/X 16:9 hero)

| Date | Day | Idea | Source | Status |
|------|-----|------|--------|--------|
| Dec 2 | Wed | The support case that gets solved on the first touch: topology, timestamps, captures from both sides, what changed, what you already ruled out | ideas-2026-08-09 #4 | — |
| Dec 4 | Fri | Your most valuable asset isn't the config. It's the reason behind the config — and it lives in one person's head | ideas-2026-07-11 #8 | — |
| Dec 6 | Sun | Technical debt has an interest rate, and it is paid in change windows | ideas-2026-10-18-business #16 | — |
| Dec 9 | Wed | Your DR site is a staffing problem — who drives there, who holds the badge, who is on shift at 3am on a holiday | ideas-2026-10-18-business #2 | — |
| Dec 11 | Fri | What would you automate first if you actually trusted your data? Every automation conversation is secretly a data-quality conversation | ideas-2026-07-16 #7 | — |
| Dec 13 | Sun | Every emergency change is a planned change somebody deferred | ideas-2026-10-18-business #31 | — |
| Dec 16 | Wed | Every snowflake branch is a support contract you pay twice — standardization isn't tidiness, it's the only thing that makes automation possible | ideas-2026-08-09 #5 | — |
| Dec 18 | Fri | Capacity planning is a procurement calendar now. Lead times, not bandwidth, decide when you can grow | ideas-2026-10-18-business #1 | — |
| Dec 20 | Sun | 4 automations that pay for themselves in a quarter, and none of them are provisioning: evidence collection, pre-change validation, inventory reconciliation, access audits | ideas-2026-08-30 #16 | — |
| Dec 23 | Wed | What does your network cost per site, per month? Most organizations can name the circuit bill and nothing else | ideas-2026-08-30 #4 | — |

**Screened out of December:**

- **Stat-gated, skipped by default** — `ideas-2026-07-08 #5` and `#19`, `ideas-2026-07-11 #7`, `ideas-2026-07-16 #8`. All four promise a Gartner, IDC or EMA figure and block on Factcheck until it has a named firm and year.
- **`ideas-2026-08-09 #9`** (handover is the deliverable, not the appendix) — collides with the marketing lane's `we-hand-it-back`, which publishes in January 2027. Marketing owns handover.
- **`ideas-2026-08-30 #23`** (if your primary vendor doubled prices tomorrow) — the marketing lane runs `one-vendor-isnt-automation` on **Dec 7**, inside this plan. Same argument, same month.

## Marketing (LI personal, EN + ES — Mondays)

Batch 2, transferred 2026-09-20. Both remaining rows are **PUBLISHED** in `marketing/INDEX.md` — written, art generated, already scheduled in Blotato. Nothing to run for them, though see the EST note above: both were submitted at the EDT offset.

| Date | Day | Idea | Source | Status |
|------|-----|------|--------|--------|
| Dec 7 | Mon | One vendor isn't automation — portability is a design decision made early or paid for later | batch 2 #06 | DONE · `one-vendor-isnt-automation` |
| Dec 14 | Mon | Three countries, one standard — multi-site drift across a language and supplier boundary | batch 2 #09 | DONE · `three-countries-one-standard` |
| ~~Dec 21~~ | Mon | We hand it back — handover as a design constraint | batch 2 #11 | **HELD to Jan 2027** |

**Dec 21 is held.** Decided 2026-09-20: `we-hand-it-back` moves to January 2027 rather than publishing in Christmas week. Its hero is generated and both renders are SHIP — it needs only a date, and the lane resumes with it on the first Monday of January.

**After Dec 14** the lane has exactly one written post left, and it is that held one. **There is no batch 3.** Writing it upstream in `mzs-marketing` — which owns the brand voice and the EN→ES glossary — is the only work in this system with a real deadline: it has to exist before January 2027.

---

**Dark days:** **Dec 21** (Mon — the Marketing lane's held post) and **Dec 24 through Dec 31** (all three lanes, by the decision above). Every other slot from Dec 1 to Dec 23 is assigned.

**Pool status after this plan**, counted across *every* pool file rather than the newest one — counting only the newest file is what made the earlier November notes wrong:

| Lane | Undeveloped rows left | Where they are |
|------|----------------------|----------------|
| Professional | ~36 | 34 of 36 in `ideas-2026-10-18`, plus two stat-gated July rows |
| Business | ~37 | 33 of 36 in `ideas-2026-10-18-business`, plus scattered older rows |

Both lanes hold roughly three months of runway at the standing cadence. Marketing holds one post, and it is already spoken for.

**Three rows retired on 2026-10-18** rather than carried forward, each a duplicate of something already scheduled: `ideas-2026-07-27 #10` (Professional Nov 26 carries the same argument), `ideas-2026-08-30 #14` (Professional Nov 3 is the same list), and `ideas-2026-08-30 #13` (the same multicast story as `ideas-2026-07-08 #9`, scheduled here for Dec 22). Each is marked RETIRED in its own file with the reason, so a later `/schedule` run doesn't re-offer it.

**Next open slots:** everything resumes in January. Marketing **Mon Jan 4** with `we-hand-it-back`. On the standing lock, Business would fall on **Fri Jan 1** and Professional on **Sat Jan 2** — both inside New Year's weekend, so the dark stretch probably wants extending to **Mon Jan 4**, which is a decision for whoever plans January.
