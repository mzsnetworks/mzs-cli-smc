# Master — an-allocation-system

**Preset:** Business (LinkedIn company page + Facebook + Instagram + X, all on the MZS account)
**Date:** 2026-11-20
**Thesis:** Documentation describes what exists; an allocation system decides what happens next. A spreadsheet can hold address history accurately and still cannot arbitrate two simultaneous requests, so the failure is structural rather than a discipline problem. The requirement is that one thing can say no.
**Pillar:** Engineering Systems
**Source:** ideas-2026-08-30 #25
**Stats:** none. The two-engineer collision is an illustrative scenario, not a measurement.

---

IPAM is not documentation. It is an allocation system, and that distinction is the whole problem.

Documentation describes something that already exists. If it is wrong, you are misinformed. An allocation system decides what happens next. If it is wrong, two people get the same subnet.

Most estates run theirs on a spreadsheet, which is an allocation system with no locking.

Here is how it fails, and it is always the same way. Two engineers open the file on a Tuesday. Both need a /24 for a new site. Both scroll to the first block that looks free. Both take it. One saves, then the other saves, and the second save wins silently. Nobody has done anything careless. The tool simply has no concept of two people asking at once.

The failure does not surface that day. It surfaces weeks later when both sites are live and something between them stops working, and the first hour of that outage is spent proving the addressing is fine, because the spreadsheet says it is.

What makes a spreadsheet feel adequate is that it is accurate right up until the moment it matters. It holds the history perfectly well. What it cannot do is arbitrate a request.

The fix is not necessarily a product. It is that one thing has to be able to say no. Whether that is a proper IPAM tool, a database with a unique constraint, or a repository where allocation goes through review, the requirement is the same: a request for space gets answered by something that knows what it already gave away.

You do not need better discipline. You need a system where the careless path is unavailable.

If two of your engineers asked for a subnet at the same moment, what would stop them being given the same one?
