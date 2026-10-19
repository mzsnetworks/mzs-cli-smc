# Master — before-touching-anything

**Preset:** Business (LinkedIn company page + Facebook + Instagram + X, all on the MZS account)
**Date:** 2026-11-25
**Thesis:** The first week of a takeover is the only window in which naive questions are free, so it is spent collecting rather than changing. Five artifacts — fresh configs, a year of change records read for gaps, monitoring configuration rather than dashboards, abandoned automation, and the spoken list of things people fear — describe the estate more honestly than any document the outgoing team hands over.
**Pillar:** Brownfield Engineering
**Source:** ideas-2026-08-30 #20
**Stats:** none. Judgment and field practice only; no statistic stated as fact.

---

When we take over an environment we did not build, the first week is collection, not change.

Five things, in this order, before anything gets touched.

Configurations from every device, pulled the same day. Not the backup repository, which is usually a month stale and missing whatever was done in a hurry. A fresh pull, so the baseline is what is actually running rather than what was last saved.

The change record for the previous twelve months. We read it for the gaps as much as the entries. A quiet quarter rarely means a quiet quarter; it means changes were happening somewhere the record does not reach.

Monitoring configuration, not monitoring dashboards. What is being watched, with what thresholds, and more usefully what is not watched at all. The gaps in coverage are an accurate map of where the previous team stopped having time.

Whatever automation exists, including the parts nobody runs any more. There is almost always a script somewhere that half-worked. It matters because it tells you what somebody already tried, and usually why it stopped.

And the list of things people are afraid to touch. This one is not a document. You get it by asking, and the answers are specific: that switch, that firewall rule, that one site. Fear is institutional memory in its least useful form, but it is still memory, and every item on that list marks a real event somebody lived through.

None of this changes anything, which is exactly the point. The first week of a takeover is the only week where you can ask naive questions without cost, and the answers stop being available the moment you are the one responsible.

Collect it while you are still allowed to not know.

What would somebody find in your estate that nobody warned them about?
