# LinkedIn — read-it-in-execution-order


Reading somebody else's configuration is a skill nobody teaches, and most of us learned it badly.

We read top to bottom, because that is how files work. But a config file is printed in the order a parser wants to emit it, which has almost nothing to do with the order the device evaluates it. Read it as a document and you build a mental model of a box that does not exist.

Read it in the order it executes instead.

That means starting where traffic arrives and working through what decides before what, and which statement wins when two disagree. On most platforms that puts you in the access lists, route maps and match clauses long before the interface stanzas that open the file.

Three habits make it faster.

Find the defaults that are not printed. Every vendor omits what it considers normal, so half of what a device does is invisible in its own config. The behavior you are trying to explain is often a default nobody chose, in a file that never mentions it.

Read the negations. "No" lines and missing statements carry as much intent as the present ones, and they are the easiest thing to skim past. Something deliberately turned off looks identical to something never turned on, unless you go looking.

Follow one packet, not one section. Pick a real flow — this source, this destination, this port — and walk it through. Ten minutes of that beats an hour of reading stanzas in file order.

And when you find something strange, assume it was deliberate until proven otherwise. Inherited configs are full of decisions whose reasons have left the company. Some are mistakes. Plenty are the scar tissue of an outage you have not heard about yet, and removing one because it looked untidy is a well-established way to find out which.

How did you learn to read a config you did not write?

#NetworkEngineering #NetOps #BrownfieldEngineering
