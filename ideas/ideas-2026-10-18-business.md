# Content Ideas — 2026-10-18 (Business posts)

For the **Business preset** (all four platforms on the MZS company account: LinkedIn company page, Facebook, Instagram, X). Company voice — authoritative "we", field experience, client-facing credibility. Still the `content/` lane, so these end on a question and ask for nothing; the CTA belongs to `marketing/`.

**Filename note.** `ideas-2026-10-18.md` is the Professional batch generated the same day. This file carries the `-business` suffix rather than overwriting it — the first time two pools were refilled on one date.

**Why this batch looks the way it does.** `ideas-2026-08-30.md` is down to four rows, and three of those were held back for collisions rather than quality. Screened against roughly ninety developed ideas across both lanes, all thirteen November Business assignments, the 36-row Professional batch in `ideas-2026-10-18.md`, and every marketing post through Dec 14. What that screening left open is **money, time and people** rather than protocols: procurement and lead times, decommissioning, the human side of DR, governance-as-multi-tenancy, automation economics rather than automation adoption, insurance as a documentation driver, and retention policy as a constraint on what can be investigated at all.

**Deliberately avoided.** Vendor portability and lock-in (the marketing lane owns that argument on Dec 7 with `one-vendor-isnt-automation`), project handover (marketing's `we-hand-it-back`, held for January 2027), coverage-versus-capacity, and anything that restates `time-to-safe-change` or `monitoring-bill-scales`.

Pillars from `rules/VOICE.md`: **ENO** (Enterprise Network Ops) · **NA** (Network Automation) · **BE** (Brownfield Engineering) · **ES** (Engineering Systems) · **LP** (Lessons from Production).

**Developed?** column: `—` not started · `drafting` in pipeline · `SHIP` scored ≥85 · `PUBLISHED` live. Update when a post moves. Slug goes next to the status once created.

| # | Pillar | Format | Idea (specific angle) | Cited stat? | Developed? |
|---|--------|--------|-----------------------|-------------|------------|
| 1 | ENO | Contrarian | Capacity planning is a procurement calendar now. Lead times, not bandwidth, decide when you can grow | no | — |
| 2 | ENO | Observation | Your DR site is a staffing problem. Who drives there, who holds the badge, who is on shift at 3am on a holiday | no | — |
| 3 | ENO | Reframe | Inside one enterprise, departments behave like tenants with no contract. Multi-tenancy is governance, not VRFs | no | — |
| 4 | ENO | How-to | Decommissioning is a project, not a ticket: the five checks before a circuit or device actually goes away | no | — |
| 5 | ENO | Observation | At a site with no local IT, every design decision is a truck-roll decision priced in days | no | — |
| 6 | ENO | Question | Does your WAN SLA measure the circuit, or the path your traffic actually takes? | no | — |
| 7 | ENO | Observation | Power and cooling are network constraints that never appear on the network diagram | no | — |
| 8 | ENO | Listicle | 5 questions before adding a site: who supports it, what the lead times are, how it fails, what it costs monthly, who notices first | no | — |
| 9 | NA | Reframe | Automation ROI is measured in avoided change windows, not hours saved. Finance understands windows | no | — |
| 10 | NA | Contrarian | Standardize before you automate. Automating six snowflakes gives you six scripts and no standard | no | — |
| 11 | NA | Observation | Automation projects die in the approval workflow, not in the code | no | — |
| 12 | NA | How-to | Give automation an audit trail before you give it a scheduler: who ran what, against which intent, with what result | no | — |
| 13 | NA | Contrarian | When change gets cheap, it gets frequent — the second-order cost nobody models | no | — |
| 14 | NA | Question | If your automation engineer took a month off, what would stop? | no | — |
| 15 | BE | Observation | The refresh you deferred three times is no longer a refresh. It is a migration | no | — |
| 16 | BE | Reframe | Technical debt has an interest rate, and it is paid in change windows | no | — |
| 17 | BE | Story | The site that was "temporary" for nine years, and what it cost to make permanent | no | — |
| 18 | BE | Prediction | Cyber-insurance questionnaires will set network documentation standards before any regulator does — the questions are already getting specific | no | — |
| 19 | BE | Story | The migration we stopped halfway, and why that was the right call | no | — |
| 20 | BE | Question | What in your environment would you not buy again — and what is the plan for it? | no | — |
| 21 | ES | Reframe | Your ticket system is a data set. What your categories reveal about your network is usually unflattering | no | — |
| 22 | ES | Contrarian | An alert with no name attached is not monitoring. It is noise with a timestamp | no | — |
| 23 | ES | Observation | The report nobody reads describes a process that does not exist | no | — |
| 24 | ES | How-to | Make capacity review a calendar event: four inputs, one page, quarterly, before it becomes an incident | no | — |
| 25 | ES | Contrarian | Your source of truth needs an API before it needs a GUI | no | — |
| 26 | ES | Reframe | Change failure rate is the one number a board understands. Change volume tells them nothing | optional — only if it quotes a DORA figure | — |
| 27 | ES | Observation | What a new engineer breaks in week one tells you what your guardrails actually are | no | — |
| 28 | ES | Question | How far back can you investigate? Your retention policy already decided which incidents are solvable | no | — |
| 29 | LP | Story | The outage that was not ours and cost us anyway — a third-party dependency nobody had mapped | no | — |
| 30 | LP | Observation | The client who asked for redundancy and needed capacity. Two different problems, one budget line | no | — |
| 31 | LP | Reframe | Every emergency change is a planned change somebody deferred | no | — |
| 32 | LP | Story | The audit finding that was actually an architecture finding | no | — |
| 33 | LP | Observation | We stopped saying "best effort," and what we commit to instead | no | — |
| 34 | LP | Question | What does a 3am call reveal about your org chart? | no | — |
| 35 | LP | Listicle | 4 signs an estate is one person away from a problem: a single approver, one admin account used by three people, no second pair of hands at the hardest site, undocumented local scripts | no | — |
| 36 | LP | Contrarian | Most "we need better monitoring" conversations are really about who is allowed to act | no | — |

**35 of 36 are gate-free.** Only #26 can promise a number, and the judgment version publishes clean — if it quotes a DORA change-failure-rate figure it must name the report and the year, or Factcheck blocks it.

Format spread: 9 Observation · 6 Contrarian · 6 Reframe · 5 Question · 4 Story · 3 How-to · 2 Listicle · 1 Prediction.

## Top 5 to write now

1. **#16 — Technical debt is paid in change windows (BE, Reframe).** Converts an abstraction finance already half-believes into an operational unit they can count. Strongest carousel in the set, and it argues a position MZS can defend from field work rather than from theory.
2. **#2 — Your DR site is a staffing problem (ENO, Observation).** `failover-worked-app-didnt-follow` found the application layer; this finds the people layer, which no post in either tree has touched. Uncomfortable in the useful way.
3. **#1 — Capacity planning is a procurement calendar (ENO, Contrarian).** Aimed at whoever signs, and lead times are completely unmined across the corpus — nothing in either lane mentions them.
4. **#31 — Every emergency change is a planned change somebody deferred (LP, Reframe).** One quotable sentence that indicts a process rather than a person, which is the move that carried `root-cause-is-a-decision`.
5. **#11 — Automation projects die in the approval workflow (NA, Observation).** The business-voice counterpart to the technical automation posts, naming the blocker clients recognize in the first meeting.

---

Pick a number → `/post <idea>` runs the full pipeline. Want openers first → "hooks for #N". Publish these on the **Business** preset (all four on the MZS account, X single).
