# Instagram — script-worked-twice (@mzsnetworks)

**Media:** hero image, 4:5 portrait (16:9 variant for LI/FB/X).

---

The script worked perfectly. Twice. 🧪

Clean in the lab — all green. Clean in the pilot — 20 switches, zero errors. Then production hit the one switch with a manual fix from 2019, and "perfect" ended at device 21.

Nobody remembered the fix. The engineer had left. The ticket didn't survive the ticketing-system migration. Just quiet config lines keeping a corner of the network alive — until a script assuming a standard baseline overwrote them at machine speed.

The lab has no history. No 2am fixes, no undocumented workarounds. The lab is greenfield by construction. Production is brownfield by accumulation.

Real idempotency: safe on ANY device in ANY state — including undocumented ones. Read state first. Diff against intent. Converge, don't overwrite. When a device surprises the script — stop. ✋

The lab tests your code. Production tests your assumptions. Idempotency is what survives the difference.

What did production teach you that the lab never could? 👇

.
.
.
#NetworkAutomation #NetDevOps #NetworkEngineering #Automation #Brownfield
