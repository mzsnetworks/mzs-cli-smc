# Master — rma-is-a-design-input

**Preset:** Professional — LinkedIn **personal profile** (no pageId) + Instagram @mzsnetworks
**Date:** 2026-11-24
**Thesis:** Replacement time is a design constraint that almost nobody writes down. It is decided years earlier by the support contract and the physical distance to the part, and a redundancy design that assumes a quick swap is really assuming a logistics outcome nobody has confirmed. The fix is to write the real replacement time next to the design and let the two disagree in public.
**Pillar:** Brownfield Engineering
**Source:** ideas-2026-08-27 #25
**Stats:** none. The four-hour and three-day figures are illustrative contract tiers, not measurements.

---

Spare parts are a strategy, not a storeroom. And the time it takes to replace a failed device is a design constraint almost nobody writes down.

Every resilient design carries an assumption about it. A pair of devices tolerates one failing, and the design is sound for as long as the second one holds. How long is that? Until the first is replaced. Which is a logistics question, answered years earlier by whoever signed the support contract, and usually not by anyone who was in the design review.

So the design says "redundant." The contract says next business day, to a receiving dock that is staffed weekdays, for a site whose nearest engineer is three hours away. Those two statements are about the same risk and they have never been in the same document.

What that produces is a quiet, specific gap. You are not running without redundancy for four hours. You are running without it for most of a week, and the design was never reviewed against that number because the number was never stated.

The part people get wrong is treating this as a procurement problem to be solved by buying better coverage. Sometimes it is. Often the right answer is the opposite: accept the slow replacement and design for it, because a four-hour contract on a site that is genuinely tolerant of a long single-device run is money spent on a risk you did not have.

Either way the decision needs the number. Not the contract tier, which describes a response rather than a resolution. The real elapsed time from "it died" to "it is running again," including the part of that which happens on a Saturday.

Write it next to the design. If the two disagree, you have found something worth an hour of somebody's time, which is cheaper than finding it during the week you are exposed.

Redundancy is not a property of the hardware. It is a property of how fast you can get the other one back.

What is your actual replacement time, and who knows it?
