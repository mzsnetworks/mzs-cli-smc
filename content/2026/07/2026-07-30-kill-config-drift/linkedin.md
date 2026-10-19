# LinkedIn — kill-config-drift

You don't need a six-month automation project to kill config drift. The first working drift check takes about 30 minutes.

Three pieces:

1. Source of truth. Put the intended state in NetBox — VLANs, interfaces, IPs, descriptions. Not what's running today: what should be running. If your team can't agree on what "should" looks like, stop here — drift isn't your problem yet. Ambiguity is.

2. Rendered intent. A short Python script and a Jinja template pull from NetBox and render the config you meant, per device, as plain text. No push. No orchestration. Just: "here is what this switch is supposed to look like."

3. The diff. Pull the running config and diff it against the rendered intent. Every line that shows up is one of three things: an undocumented fix, an unauthorized change, or stale intent. All three are worth knowing before they page you at 2am.

The trap is skipping straight to enforcement — auto-push, auto-remediation, closed loops. That's month six. Day one is visibility, and visibility alone changes behavior: the first time an engineer sees their "temporary" workaround in a drift report, it stops being invisible. And you can't enforce intent you never wrote down.

Operationally, the diff does something subtle: it turns drift from an opinion into a report. "I think someone changed something" becomes twelve lines with a device name on them. Arguments end. Tickets open.

Config drift isn't the disease. It's the symptom of intent that lives in someone's head instead of in a system. Write the intent down, and the diff writes itself.

What would your first drift report show?

#NetworkAutomation #NetBox #NetDevOps
