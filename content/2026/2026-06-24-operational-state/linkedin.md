Two supervisors. Full redundancy. Every health check green.

The ISSU still refused to run.

The problem wasn't the procedure. It never is.

Most in-service upgrade failures don't come from skipping a step. They come from operational state the procedure assumes is clean — and isn't.

This box had survived years of maintenance windows. Somewhere in that history, a previous install attempt left residue behind. Not in the running config. Not in anything redundancy reporting would flag. In the upgrade machinery's own memory of what it had already tried.

Health checks read the running system. Redundancy status reads the running system. ISSU doesn't run on the running system — it runs on the accumulated state underneath it. That's the part nobody was looking at, because nothing in the dashboards points there.

Operationally, this is the brownfield tax. A greenfield box has no history to contradict you. A ten-year-old production device carries the residue of every prior change window, and most of it stays invisible until the one operation that depends on it fails.

The fix wasn't a better procedure. It was reconstructing what the device still remembered from upgrades that never finished, and clearing it before trying again.

Configuration tells you what a device should do. Logs tell you what it did. Operational state tells you what it still remembers — and that's the one that fails your upgrade at 2 a.m.

What's the last "healthy" device that lied to you?

#NetworkEngineering #NetworkOperations

## Sources

Experience-based post — no external statistics cited. All claims are operational judgment from direct fieldwork, not third-party data.
