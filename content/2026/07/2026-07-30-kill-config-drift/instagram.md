# Instagram — kill-config-drift

**Media:** carousel (how-to, multi-point) or hero 4:5 — decided at visual step.

---

Your first config-drift check takes 30 minutes. Not six months. ⬇️

Three pieces:

1️⃣ Source of truth — intended state in NetBox. Not what's running: what SHOULD be running. Can't agree on "should"? That's the real finding.

2️⃣ Rendered intent — Python + Jinja pull NetBox and render the config you meant, per device. No push, no orchestration.

3️⃣ The diff — running config vs rendered intent. Every line is an undocumented fix, an unauthorized change, or stale intent. All three worth knowing before 2am.

The trap: skipping to enforcement. Auto-remediation is month six. Day one is visibility — and you can't enforce intent you never wrote down.

The diff turns drift from an opinion into a report. Arguments end. Tickets open. 📋

Drift isn't the disease. It's intent living in someone's head instead of a system. Write it down — the diff writes itself.

What would your first drift report show? 👇

.
.
.
#NetworkAutomation #NetBox #NetDevOps #ConfigManagement #NetworkEngineering
