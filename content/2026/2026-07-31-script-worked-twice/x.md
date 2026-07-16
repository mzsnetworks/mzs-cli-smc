# X — script-worked-twice (@mzsnetworks)

## Single

The script worked perfectly. Twice.

Clean in lab. Clean in pilot. Then production hit the one switch with a manual fix from 2019.

The lab tests your code. Production tests your assumptions. Idempotency is what survives the difference.

#NetworkAutomation

## Thread

1/ The script worked perfectly. Twice. Clean in lab, clean in pilot — then production reached the one switch with a manual fix from 2019, and "perfect" ended at device 21.

2/ Nobody remembered the fix. The engineer left. The ticket didn't survive the ticketing migration. Just quiet config lines — until a script assuming a standard baseline overwrote them at machine speed.

3/ The lab has no history. No 2am fixes, no undocumented workarounds. The lab is greenfield by construction. Production is brownfield by accumulation.

4/ Real idempotency: safe on any device, in any state — including undocumented ones. Read state first. Diff against intent. Converge, don't overwrite. Surprised? Stop.

5/ The happy-path script took days. Converging safely took weeks. That ratio is normal — it's what separates a demo from a tool you trust at 2am.

The lab tests your code. Production tests your assumptions. What did production teach you that the lab never could?
