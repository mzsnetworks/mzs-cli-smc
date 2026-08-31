# Master — firewall-rule-nobody-deletes

**Preset:** Business (MZS company account — LI page, FB, IG, X)
**Date:** 2026-09-16 (Wed)
**Source idea:** ideas-2026-08-09 #2 (ES · Observation)
**Thesis:** Rule bases only grow because adding is rewarded and deleting is the one action with a downside and no upside. Fix the incentive, not the rule base.
**Note:** `brownfield-is-a-negotiation` (2026-08-27) mentions the undeletable rule in one clause. This post takes a different frame — incentive asymmetry plus an evidenced deletion process — and does not reuse that anecdote.
**Stats:** none — judgment post, no factcheck gate.

---

Nobody has ever been promoted for deleting a firewall rule.

That single fact explains almost every rule base we're handed.

Adding a rule solves a visible problem today. Somebody is unblocked, the ticket closes, and a person says thank you. Deleting a rule solves nothing anyone can see, and carries a small chance of breaking something nobody remembers depends on it. One action has upside. The other has only downside. Rule bases grow the way water runs downhill.

So they become archaeology. You can date the layers.

→ The permit any/any from a migration, added "temporarily"
→ A vendor rule for a product decommissioned two years ago, permitting inbound to nothing
→ Rules referencing a subnet that no longer exists
→ Four near-identical rules written by four different people who each didn't trust the existing three

The real cost isn't clutter. It's that nobody can answer the question the rule base exists to answer: what is actually allowed here? And once nobody can read it, nobody can safely change it — so the next engineer does the only safe thing available: adds another rule.

The fix is not a cleanup project. Those fail because they're one-time, unfunded, and terrifying. What works is making deletion evidenced and boring:

→ Hit counters as a candidate list. Zero hits in ninety days is a question, not a verdict.
→ Disable and watch, rather than delete and hope. A disabled rule can be re-enabled in ten seconds. A deleted one gets rebuilt from memory at 3am.
→ An owner and a review date on every new rule, captured at creation — the only moment anybody knows why.
→ Expiry by default on anything opened during an incident. Temporary should mean temporary in the config, not the intention.

None of that is a product. It's a decision to make removal as normal as addition.

Adding a rule is a ticket. Deleting one is a risk. Until that changes, your rule base only grows.

Which rule in your environment is everyone quietly scared to touch?
