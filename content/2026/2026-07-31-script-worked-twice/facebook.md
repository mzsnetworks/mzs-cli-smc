# Facebook — script-worked-twice (MZS page)

The script worked perfectly. Twice.

Clean in the lab. Clean in the pilot — twenty switches, zero errors. Then production reached one switch carrying a manual fix from 2019, and "perfect" ended at device twenty-one.

The lab has no history — no 2am fixes, no undocumented workarounds. The lab is greenfield by construction. Production is brownfield by accumulation.

Real idempotency means safe on any device, in any state, including states nobody documented. Read the running state. Diff against intent. Converge — don't overwrite. And when a device surprises the script, stop, don't push through.

The lab tests your code. Production tests your assumptions.

What did your first production run teach you that the lab never could? 👇

#NetworkAutomation