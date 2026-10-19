# X — definition-of-normal


## Single (publish this)

Anomaly detection needs a definition of normal, and most networks have never had a quiet enough week to learn one.

Train it on three years of running slightly wrong and it learns the mess as the baseline — then stays quiet about it.

#AIOps #NetOps

---

## Thread

1/ Anomaly detection needs a definition of normal.

Most networks have never had a quiet enough week to learn one. 🧵

2/ That's the part the demo skips.

Clean baseline, injected fault, everyone impressed. Then it goes into an environment that's been running slightly wrong for three years.

3/ Here's what it learns there:

• The interface that resets every few days
• The link that saturates every afternoon
• The device that stops answering SNMP during its backup window

All normal, as far as the model can tell.

4/ None of it was labeled as broken. It's all in the training data.

The model has no way to tell "this is how the network behaves" from "this is what nobody has fixed yet."

5/ The result is a system that is quietest about your oldest problems.

It'll catch a new fault tomorrow and stay silent on the chronic one costing you a few hours a month since 2023.

By its only definition, that isn't an anomaly. It's the baseline.

6/ That's not an argument against the tools. It's an argument about sequencing.

Fix or explicitly accept what you already know about. Label the known-bad periods. Start with metrics where normal is genuinely stable.

7/ A model trained on a network nobody has cleaned will faithfully learn the mess and defend it.

Anomaly detection tells you what changed. It can't tell you what was wrong all along.

#AIOps #NetOps
