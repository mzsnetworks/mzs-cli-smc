# Master — The Script That Worked Perfectly, Twice

**Idea:** ideas-2026-07-16 #6 (Automation, Confession). Clean in lab, clean in pilot, then it met the one switch with a manual fix from 2019. Idempotency isn't a coding concept; it's a brownfield problem.
**Preset:** Business (MZS company voice — field story told as "we").
**Spine:** hook (worked perfectly — twice) → story (lab, pilot, then the 2019 snowflake) → data (none — war story) → judgment (lab tests code; production tests assumptions; converge, don't overwrite) → landing (lab/production/idempotency triad + question).

---

The script worked perfectly. Twice.

Clean in the lab — every test green. Clean in the pilot — twenty switches updated, zero errors. Then the production rollout reached one switch that carried a manual fix from 2019, and "perfect" ended at device twenty-one.

Nobody remembered the fix. The engineer who applied it had left. The ticket, if there ever was one, didn't survive the ticketing-system migration. Just a few quiet lines of config, keeping a corner of the network alive for reasons that lived in no document — until a script built on the assumption of a standard baseline overwrote them at machine speed.

That's the day idempotency stops being a coding concept. In the lab it's trivial: run the script twice, same result, test passes. But the lab has no history. No 2am fixes, no undocumented workarounds, no half-finished standards from three re-orgs ago. The lab is greenfield by construction. Production is brownfield by accumulation.

Real idempotency in a brownfield network means something harsher: safe to run on any device, in any state, including states nobody documented. Which means the script can't assume — it has to ask. Read the running state first. Diff against intent. Converge the delta, don't overwrite the device. And when a device disagrees with the model in a way the script doesn't understand, stop and raise a hand — don't push through.

The uncomfortable arithmetic: writing the happy-path script took days. Making it converge safely took weeks. That ratio is normal — and it's exactly the work that separates a demo from a tool you can trust at 2am.

The lab tests your code. Production tests your assumptions. Idempotency is what survives the difference.

What did your first production run teach you that the lab never could?

---

**Sources**
- None required — field story, no statistics. Story pattern generalized from real brownfield automation work; no fabricated specifics beyond the illustrative shape.
