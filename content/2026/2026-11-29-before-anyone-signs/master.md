# Master — before-anyone-signs

**Preset:** Business (LinkedIn company page + Facebook + Instagram + X, all on the MZS account)
**Date:** 2026-11-29
**Thesis:** An acceptance criterion that cannot fail is not a criterion. Five that can: the application rather than the link, each direction separately, a deliberately triggered failure case, behavior under real load at the hour that matters, and a named signer. The test exists so that later, when something is wrong, you can tell whether it was ever right.
**Pillar:** Engineering Systems
**Source:** ideas-2026-08-30 #29
**Stats:** none. Judgment and field practice only; no statistic stated as fact.

---

"It pings" is not an acceptance test. It is a pulse check on a patient nobody has examined.

We get asked to review acceptance criteria for projects that are already late, which is the worst moment to find that the criteria say nothing. Five things separate a document that closes a project from one that protects you after it closes.

The application, not the link. Not that the circuit is up, but that the thing the circuit exists for completes successfully, run by somebody who would recognize a wrong answer. A link can be perfect while the service behind it is unusable.

Both directions, separately. Upload and download fail differently and for different reasons, and a test that only measures one of them will pass a half-broken path. This is the cheapest check on the list and the one most often skipped.

The failure case, deliberately triggered. If the design claims resilience, the acceptance test takes the primary path away and measures what the user experiences while it is gone. Not whether the route converges. Whether the transaction completes.

Behavior under real load, at the hour that matters. A test run at 7am measures an empty network. The number you need comes from the shift change or the batch window.

And a named person who signs. Not a team, not a mailbox. Somebody whose judgment you would accept if they said no.

What these have in common is that each one can fail. A criterion that cannot fail is not a criterion, it is a sentence in a document, and most acceptance tests we read are made entirely of those.

The test is not there to prove the project finished. It is there so that six months later, when something is wrong, you can tell whether it was ever right.

What would it take for your last project to have failed acceptance?
