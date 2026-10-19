# Master — read-it-in-execution-order

**Preset:** Professional (LinkedIn personal profile + Instagram @mzsnetworks)
**Date:** 2026-10-13
**Thesis:** Reading somebody else's config is a skill nobody teaches. The file is printed in the order a parser wants it, not the order the device evaluates it, and reading top to bottom quietly teaches you the wrong model of the box.
**Pillar:** Enterprise Network Ops
**Source:** ideas-2026-08-27 #31
**Stats:** none. Judgment and practice only; no statistic stated as fact.

---

Reading somebody else's configuration is a skill nobody teaches, and most of us learned it badly.

We read top to bottom, because that is how files work. But a config file is printed in the order a parser wants to emit it, which has almost nothing to do with the order the device evaluates it. Read it as a document and you build a mental model of a box that does not exist.

Read it in the order it executes instead.

That means starting at the bottom of the funnel and working out. What does traffic hit first, what decides before what, and which statement wins when two of them disagree. On most platforms that puts you in the access lists, the route maps, the policy order and the match clauses long before you get near the interface stanzas that open the file.

Three habits make it faster.

Find the defaults that are not printed. Every vendor omits what it considers normal, and half of what a device does is therefore invisible in its own config. The behavior you are trying to explain is frequently a default nobody chose, in a file that never mentions it.

Read the negations. "No" lines and missing statements carry as much intent as the present ones, and they are the easiest thing in the world to skim past. Something that was deliberately turned off looks identical to something that was never turned on, unless you go looking.

Follow one packet, not one section. Pick a real flow — this source, this destination, this port — and walk it through. You will learn more about the box in ten minutes of that than in an hour of reading stanzas in file order.

And when you find something strange, assume it was deliberate until proven otherwise. Inherited configs are full of decisions whose reasons have left the company. Some are mistakes. Plenty are the scar tissue of an outage you have not heard about yet, and removing one because it looked untidy is a well-established way to find out which.
