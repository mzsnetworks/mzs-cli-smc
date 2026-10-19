# Master — five-questions-before-wireless

**Preset:** Business (LinkedIn company page + Facebook + Instagram + X, all on the MZS account)
**Date:** 2026-10-25
**Thesis:** Every wireless RFP opens with an access point count. That number is an answer to questions nobody has asked yet. Five questions decide the design — density at peak, building materials, client mix, the application, and who controls physical access to the ceiling — and the AP count falls out of them.
**Pillar:** Enterprise Network Ops
**Source:** ideas-2026-08-30 #6
**Stats:** none. Judgment and field practice only; no statistic stated as fact.

---

Every wireless RFP we receive opens with a number of access points.

That number is an answer. Nobody has asked the questions yet.

We ask five before quoting, and none of them is how many APs.

How many devices in the worst room at the worst moment? Not the average across a floor. The all-hands, the shift change, the exam hall, the first morning of term. Designing to average density builds a network that works most of the time, which is another way of saying it fails on the days somebody is watching.

What are the walls made of? Plasterboard and glass behave nothing like poured concrete, foil-backed insulation, or a cold store. An afternoon on site answers this. A floor plan does not, and neither does a predictive model fed the wrong assumption about a wall.

What is actually going to connect? The laptops are the easy part. It is the decade-old barcode scanners that only speak 2.4 GHz, the medical carts, the badge readers, the guest phones nobody counted. One legacy client class can hold an entire band hostage.

What is the application? Email tolerates a roam that takes half a second. A voice call does not. Location services need coverage overlap that a pure data design would call waste. The application decides the layout, not the square footage.

Who owns the ceiling? This is the question that moves dates. Mounting, cable routes, conduit, asbestos surveys, landlord consent, and the rules about who is allowed on a lift. We have seen an RF design finish in two weeks and wait four months for ceiling access.

None of these are difficult questions. They are unwelcome ones at quoting time, because every one of them can change the number.

A quote that skips them is not cheaper. It is the same project with the surprises still in it, moved to the part of the timeline where surprises cost the most.

The AP count is the last thing we work out. It falls out of the answers.
