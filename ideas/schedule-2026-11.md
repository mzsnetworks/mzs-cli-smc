# Publishing Schedule — Nov 2026

Standing cadence: **one post daily at 4:00 PM local — Professional Tue/Thu/Sat, Business Wed/Fri/Sun. Mondays are the Marketing lane** and carry two slots for one idea: ES at 2:00 PM, EN at 4:00 PM.

> **November runs on EST.** Daylight time ended Sun Nov 1, so every slot this month is `21:00:00Z` for 4:00 PM and `19:00:00Z` for the Marketing ES slot — not the `20:00Z`/`18:00Z` used through Oct 31, which now lands an hour early.

Fire each with: `/publish <idea> - <preset>, <date> 4pm`. A Marketing row fires both languages in one run. Mark rows DONE (with slug) as they're scheduled; update the source ideas file + the lane's INDEX per the normal publish flow.

Planned 2026-10-18 against `ideas-2026-08-27.md` (Professional) and `ideas-2026-08-30.md` (Business). Stat-gated rows were excluded by default; the one stat-*optional* row carried into the plan is flagged below.

## Professional (LI personal + IG @mzsnetworks)

| Date | Day | Idea | Source | Status |
|------|-----|------|--------|--------|
| Nov 3 | Tue | 4 questions before I automate anything: how often, who else runs it, what happens if it half-finishes, and how will I know it did | ideas-2026-08-27 #24 | DONE · `four-questions` |
| Nov 5 | Thu | Out-of-band access you've never tested is decoration — the one time you need it, you find out it depends on the thing that's down | ideas-2026-08-27 #18 | DONE · `oob-is-decoration` |
| Nov 7 | Sat | DNS TTLs are a migration plan. Lower them a week early or the cutover isn't yours to control | ideas-2026-08-27 #22 | DONE · `ttls-are-a-plan` |
| Nov 10 | Tue | EOL notices are a design input, not a purchasing problem — by the time it's a budget line the architecture decision has been made for you | ideas-2026-08-27 #8 | DONE · `eol-is-a-design-input` |
| Nov 12 | Thu | I use AI to write configs daily and still read every line — not because it's usually wrong, but because I'm the one who signs it | ideas-2026-08-27 #11 | DONE · `im-the-one-who-signs-it` |
| Nov 14 | Sat | Have you ever been unable to say "I don't know yet" during an incident? The silence costs more than the admission | ideas-2026-08-27 #21 | DONE · `i-dont-know-yet` |
| Nov 17 | Tue | Your NTP is wrong somewhere, and every log correlation you did last quarter was a guess with timestamps on it | ideas-2026-08-27 #5 | DONE · `a-guess-with-timestamps` |
| Nov 19 | Thu | The migration estimate I missed by three weeks — and the two questions I now ask before quoting any brownfield project | ideas-2026-08-27 #17 | DONE · `three-weeks-over` |
| Nov 21 | Sat | What would you actually let an AI change without asking you first? Most honest answers are "nothing" — and that's the real state of AIOps adoption | ideas-2026-08-27 #33 | DONE · `without-asking-you` |
| Nov 24 | Tue | Spare parts are a strategy, not a storeroom — RMA time is a design constraint you've probably never written down | ideas-2026-08-27 #25 | DONE · `rma-is-a-design-input` |
| Nov 26 | Thu | Did your last outage change a document, or change a default? Only one of those survives you | ideas-2026-08-27 #28 | DONE · `what-survives-you` |
| Nov 28 | Sat | If you cannot run it twice, it is not automation — idempotence is the whole game, and most scripts fail it quietly | ideas-2026-10-18 #8 | DONE · `run-it-twice` |

This plan drained `ideas-2026-08-27.md` to zero — eleven undeveloped rows against twelve November slots. The twelfth, Nov 28, draws from **`ideas-2026-10-18.md`**, generated the same day to refill the lane: 36 fresh rows, 35 of them gate-free.

**One overlap to handle when writing.** Nov 26 (#28) argues that an outage changing a *default* outlives one that changes a document. `four-incidents-taught-me` (Oct 17) already made the default-versus-fact point. It is placed last deliberately — six weeks of separation — but write it toward postmortem artifacts and what survives a handover, not toward defaults, or it reads as a reprise of October.

## Business (all four on MZS · LI + IG full carousel · FB/X 16:9 hero)

| Date | Day | Idea | Source | Status |
|------|-----|------|--------|--------|
| Nov 1 | Sun | A change record worth reading has five fields: what changed, why, who approved, how to undo it, and the one-line business reason | ideas-2026-08-30 #26 | DONE · `change-record-five-fields` |
| Nov 4 | Wed | Guest Wi-Fi is a security posture, not an amenity — the captive portal is the least interesting decision in it | ideas-2026-08-30 #7 | DONE · `guest-wifi-is-a-posture` |
| Nov 6 | Fri | The maintenance window that finished early, and the outage it caused on Monday — because "done" meant applied, not verified | ideas-2026-08-30 #30 | DONE · `done-meant-applied` |
| Nov 8 | Sun | SD-WAN didn't remove the WAN engineer — it moved the hard part to defining what "good" means per application, and nobody wants to own that | ideas-2026-08-30 #2 | DONE · `defining-what-good-means` |
| Nov 11 | Wed | Post-incident actions expire — if it isn't scheduled, staffed and dated, it's a feeling somebody had on a bad day | ideas-2026-08-30 #33 | DONE · `post-incident-actions-expire` |
| Nov 13 | Fri | Who owns the network in your organization? Not who runs it — who decides | ideas-2026-08-30 #27 | DONE · `who-decides` |
| Nov 15 | Sun | Oversubscription isn't a dirty word — designing for zero contention buys a network you'll never use; the skill is choosing the ratio on purpose | ideas-2026-08-30 #8 | DONE · `choosing-the-ratio` |
| Nov 18 | Wed | AI is good at the part we're bad at — reading everything — and bad at the part we're good at: knowing what matters *here*. Staff accordingly | ideas-2026-08-30 #35 | DONE · `knowing-what-matters-here` |
| Nov 20 | Fri | IPAM isn't documentation, it's an allocation system — and a spreadsheet is an allocation system with no locking | ideas-2026-08-30 #25 | DONE · `an-allocation-system` |
| Nov 22 | Sun | 4 outages that had nothing to do with the network and everything to do with a change nobody told us about | ideas-2026-08-30 #32 | DONE · `nobody-told-us` |
| Nov 25 | Wed | Taking over an environment you didn't build: the first five things we collect before touching anything | ideas-2026-08-30 #20 | DONE · `before-touching-anything` |
| Nov 27 | Fri | Wi-Fi 7 will be sold on speed and bought for capacity — and most enterprises will still be capped by uplinks and AP placement | ideas-2026-08-30 #11 | DONE · `sold-on-speed` |
| Nov 29 | Sun | 5 things a network acceptance test must include before anyone signs — and why "it pings" isn't one of them | ideas-2026-08-30 #29 | DONE · `before-anyone-signs` |

**Nov 27 (#11) is the one stat-*optional* row in this plan.** Its pool entry reads "only if you quote adoption numbers." Write it as judgment and cite nothing; the moment it quotes a Wi-Fi 7 adoption figure it blocks on Factcheck until the figure has a named firm and year.

**Screened out of Business**, with 17 eligible rows against 13 slots:

- `#23` (vendor lock-in — "if your primary vendor doubled prices tomorrow") — the marketing lane owns that argument on Dec 7 with `one-vendor-isnt-automation`.
- `#14` ("what would a script have to prove before you'd let it run unattended") — near-duplicate of Professional `#24` on Nov 3. The same list, two lanes, three weeks apart.
- `#4` (cost per site) — repeats the "most organizations can name one line item" insight from `monitoring-bill-scales`, Oct 2.
- `#16` (4 automations that pay for themselves) — leads on evidence collection and pre-change validation, which the marketing lane covered Oct 26 (`evidence-not-assurances`) and covers again Nov 9 (`rollback-is-an-acceptance-criterion`). **Held as the alternate** if a row needs swapping.

Two adjacencies that were placed around rather than avoided: `#7` (guest Wi-Fi, Nov 4) and `#11` (Wi-Fi 7, Nov 27) sit at opposite ends of the month, and both are clear of `five-questions-before-wireless` (Oct 25). `#29` (acceptance tests, Nov 29) is twenty days past the marketing lane's `rollback-is-an-acceptance-criterion` (Nov 9), which is the nearest thing to it in either tree.

## Marketing (LI personal, EN + ES — Mondays)

Batch 2, transferred 2026-09-20. All five are **PUBLISHED** in `marketing/INDEX.md` — written, art generated, and already scheduled in Blotato. Nothing to run for these rows.

| Date | Day | Idea | Source | Status |
|------|-----|------|--------|--------|
| Nov 2 | Mon | An assessment is not a sales call with a report attached — what two weeks of looking turns up | batch 2 #01 | DONE · `assessment-what-it-finds` |
| Nov 9 | Mon | Rollback is an acceptance criterion, not a paragraph in the change record | batch 2 #10 | DONE · `rollback-is-an-acceptance-criterion` |
| Nov 16 | Mon | The tools don't talk and the glue is a person · Workflow Engine | batch 2 #05 | DONE · `tools-that-dont-talk` |
| Nov 23 | Mon | Your NOC sees alerts, not state · ITOC Dashboard | batch 2 #04 | DONE · `noc-sees-alerts-not-state` |
| Nov 30 | Mon | Buying automation without an automation team | batch 2 #12 | DONE · `buying-automation-without-a-team` |

---

**Dark days:** none. Every slot from Nov 1 to Nov 30 is assigned across the three lanes.

**Pool status after this plan.** Professional `ideas-2026-08-27.md`: **0 undeveloped** — fully drained. `ideas-2026-10-18.md` replaces it with **35 left** of 36 (#8 goes to Nov 28), which is about three months of Professional runway. Business `ideas-2026-08-30.md`: **4 left** (`#4`, `#14`, `#16`, `#23`), roughly a week and a half, and three of those four were screened out for collisions rather than quality — so Business, not Professional, is now the lane that runs dry first.

**Next open slots:** Professional **Dec 1** (Tue). Business **Dec 2** (Wed). Marketing **Dec 7** (Mon), already written and scheduled.

**December needs ideation in the Business lane.** Fourteen Professional slots and thirteen Business ones; Professional is covered by `ideas-2026-10-18.md`, Business has four rows and needs a fresh batch. Marketing is covered through Dec 14 and then stops entirely — `we-hand-it-back` is held for January and there is no batch 3, which has to be written upstream in `mzs-marketing`.
