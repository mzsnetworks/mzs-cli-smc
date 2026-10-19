# Instagram — an-allocation-system


IPAM isn't documentation. 🗂️ It's an allocation system.

Documentation describes what exists. If it's wrong, you're misinformed.

An allocation system decides what happens next. If it's wrong, two people get the same subnet. ⚠️

Most estates run theirs on a spreadsheet — an allocation system with no locking.

How it fails, every time:

→ Two engineers open the file on a Tuesday
→ Both need a /24 for a new site
→ Both take the first block that looks free
→ One saves. Then the other. The second wins silently

Nobody was careless. The tool has no concept of two people asking.

It surfaces weeks later: both sites live, and the first hour of the outage goes on proving the addressing is fine — because the spreadsheet says it is. ⚙️

You don't need better discipline. You need a system where the careless path is unavailable.

#NetworkEngineering #NetOps #ITOperations #Infrastructure #Networking

---

## Carousel slide ideas

1. Cover — "IPAM isn't documentation. It's an *allocation system*."
2. Documentation — Describes what already exists. Wrong = you're misinformed.
3. Allocation — Decides what happens next. Wrong = two people get the same subnet.
4. What most estates run — A spreadsheet. An allocation system with no locking.
5. Tuesday — Two engineers open the file. Both need a /24.
6. Both — Scroll to the first block that looks free. Both take it.
7. The save — One saves, then the other. The second wins silently.
8. Nobody was careless — The tool has no concept of two people asking at once.
9. Weeks later — Both sites live. The first hour goes on proving addressing is fine.
10. CTA — "You don't need discipline. You need the careless path *unavailable*."
