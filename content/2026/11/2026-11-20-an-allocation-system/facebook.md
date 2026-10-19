# Facebook — an-allocation-system


IPAM isn't documentation. It's an allocation system, and that distinction is the whole problem.

Documentation describes what exists. An allocation system decides what happens next — and if it's wrong, two people get the same subnet.

Most estates run theirs on a spreadsheet: no locking.

Two engineers open the file. Both need a /24. Both take the first block that looks free. One saves, then the other. The second wins silently.

It surfaces weeks later, when both sites are live and the first hour of the outage goes on proving the addressing is fine.

You don't need better discipline. You need the careless path to be unavailable.

What would stop two engineers being given the same subnet?
