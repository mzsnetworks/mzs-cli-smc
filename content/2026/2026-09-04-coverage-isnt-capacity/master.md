# Master — coverage-isnt-capacity

**Preset:** Business (MZS company account — LI page, FB, IG, X)
**Date:** 2026-09-04 (Fri)
**Source idea:** ideas-2026-08-09 #1 (ENO · Contrarian)
**Thesis:** A heat map proves signal arrived. It says nothing about whether the user got a turn to speak.
**Stats:** none — judgment/mechanism post, no factcheck gate.

---

Coverage isn't capacity.

The survey comes back green in every corner. The heat map goes in the report. And the complaints keep arriving, because users don't feel dBm. They feel contention.

A radio is a shared medium. One device talks at a time, and everyone else waits their turn. Forty devices on one access point aren't forty conversations — they're one conversation, taken in turns, very quickly.

Which is why the slowest client on a cell sets the tax everyone else pays. A device out at the edge, negotiating a low data rate, holds the medium longer to move the same amount of data. It isn't just slow for its owner. It's slow for everyone sharing that radio.

None of that appears on a coverage map. The map answers "did signal reach here." The complaint is about "did I get a turn."

So when the ticket says the Wi-Fi is bad, the first numbers we look at aren't signal strength:

→ Channel utilization — how busy the air already is before anyone else joins
→ Retry rate — the tell that frames are being sent more than once
→ Clients per radio at peak, not averaged across the day
→ The data rates in use, because the slow ones are the expensive ones

And the instinct to fix it with more power usually makes it worse. Higher transmit power builds bigger cells. Bigger cells mean more clients per radio and more overlap between neighbors. The heat map gets greener while the experience degrades — you've optimized the exact thing that was already fine.

Most of the time the answer is smaller cells, more of them, and a hard look at what's actually on the network. Coverage is a design input. Capacity is the design.

A heat map tells you the signal arrived. It doesn't tell you the user got a turn to speak.

When the Wi-Fi complaint comes in, what's the first number you look at?
