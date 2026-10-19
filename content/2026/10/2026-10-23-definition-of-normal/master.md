# Master — definition-of-normal

**Preset:** Business (LinkedIn company page + Facebook + Instagram + X, all on the MZS account)
**Date:** 2026-10-23
**Thesis:** Anomaly detection learns normal from history. A network whose history contains a chronic fault learns that fault as normal and stops reporting it, so the tool is quietest about exactly the problem you have had longest.
**Pillar:** AIOps
**Source:** ideas-2026-08-30 #36
**Stats:** none. Judgment only; no statistic stated as fact.

---

Anomaly detection needs a definition of normal, and most networks have never had a quiet enough week to learn one.

That is the part the demo skips. The tool is shown against a clean baseline, finds the injected fault, and everyone is impressed. Then it goes into an environment that has been running slightly wrong for three years.

Here is what it learns there. The interface that resets every few days becomes normal. The link that saturates every afternoon becomes normal. The device that stops answering SNMP during its backup window becomes normal. All of that is in the training data, none of it was labeled as broken, and the model has no way to know the difference between "this is how the network behaves" and "this is what nobody has fixed yet."

The result is a system that is quietest about your oldest problems. It will catch a new fault tomorrow and stay silent on the chronic one that has been costing you a few hours a month since 2023, because by the only definition it has, that is not an anomaly. It is the baseline.

That is not an argument against the tools. It is an argument about sequencing.

Clean what you already know about first. Every team has a list of things they have stopped ticketing because nothing ever came of it — fix or explicitly accept each one before you set a baseline. Label the known-bad periods so they can be excluded. Start with the metrics where normal is genuinely stable, not the ones where it never was.

And be honest about which problems you want found. A model trained on a network nobody has cleaned will faithfully learn the mess and defend it.

Anomaly detection tells you what changed. It cannot tell you what was wrong all along — you still have to know that yourself.

What has your monitoring stopped alerting on because it happens every week?
