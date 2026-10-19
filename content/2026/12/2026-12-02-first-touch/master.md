# Master — first-touch

**Preset:** Business (LinkedIn company page + Facebook + Instagram + X, all on the MZS account)
**Date:** 2026-12-02
**Thesis:** Most of the delay in a support case belongs to the case, not the vendor. Five things supplied on the first touch — the specific path, timestamps with an offset, simultaneous captures from both sides, what changed, and what was already ruled out — remove the exchanges that each cost a day of queue time.
**Pillar:** Enterprise Network Operations
**Source:** ideas-2026-08-09 #4
**Stats:** none. The "four days" is an illustrative scenario framed as the reader's experience, not a measurement.

---

The quality of a support case is the one variable in the process you fully control, and almost nobody treats it that way.

Open a case with "the VPN is slow for some users" and you have started a conversation that will take four days. Not because the vendor is slow, but because the first two exchanges are them asking what you could have said at the beginning, and each exchange costs a day of queue time.

Five things, in the case, on the first touch.

Topology. Not the corporate diagram. The specific path this traffic takes, drawn in two lines if necessary, including the things in the middle that are easy to forget: the firewall, the load balancer, the proxy that was added last year.

Timestamps with a timezone. The engineer reading this is somewhere else. "Yesterday afternoon" costs an exchange. An exact window with an offset costs nothing and lets them pull their own logs without asking.

Captures from both sides, taken at the same time. One-sided captures generate a request for the other side. Two captures of the same moment answer most of the questions a first responder has.

What changed. Including the honest version: nothing we know of, and here is the change record for the window anyway. A vendor who sees you looked first treats you differently.

What you already ruled out, and how. This is the one that moves a case out of tier one, because it says the person on the other end is not going to have to start from the beginning.

None of this requires the vendor to be good. It removes the part of the delay that belongs to you, which is usually more of it than anyone wants to admit.

A case is a document you are asking a stranger to act on. Write it like one.

What does your average case look like on the first touch?
