# Instagram — read-it-in-execution-order


Reading somebody else's config is a skill nobody teaches. 📜

We read top to bottom, because that's how files work.

But a config is printed in the order a parser wants to emit it — which has almost nothing to do with the order the device evaluates it.

Read it as a document and you build a mental model of a box that doesn't exist. ⚠️

Read it in the order it executes instead. Start where traffic arrives. What decides before what. Which statement wins when two disagree.

Three habits that make it faster:

→ Find the defaults that aren't printed. Every vendor omits what it considers normal, so half of what a device does is invisible in its own config.

→ Read the negations. Something deliberately turned off looks identical to something never turned on — unless you go looking.

→ Follow one packet, not one section. This source, this destination, this port. Ten minutes of that beats an hour of reading stanzas in file order.

And when you find something strange, assume it was deliberate until proven otherwise. ⚙️

Inherited configs are full of decisions whose reasons left the company. Some are mistakes. Plenty are scar tissue from an outage you haven't heard about yet.

How did you learn to read a config you didn't write?

#NetworkEngineering #NetOps #BrownfieldEngineering #ITOps #Infrastructure
