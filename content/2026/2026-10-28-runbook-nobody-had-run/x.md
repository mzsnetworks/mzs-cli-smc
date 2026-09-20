# X — runbook-nobody-had-run


## Single (publish this)

We automated a failover runbook nobody had run in two years.

Reviewed quarterly. Signed off. Tested by reading.

Encoding it surfaced three defects, including a verification step that only checked the interface was up.

Found by writing it, not running it.

#NetOps

---

## Thread

1/ We were asked to automate a site failover runbook. Routine work, or so it looked. 🧵

2/ The document was in good shape. Version controlled, reviewed every quarter, signed off.

What it had not been in two years was run.

3/ It had been tested by reading.

Somebody followed the steps with their eyes, agreed it still made sense, marked the review complete.

That verifies exactly one thing: the document is still readable.

4/ Automating it meant every ambiguity had to be resolved before anything could execute.

Three did not survive the translation.

5/ One step referenced a VLAN by name. It had been renumbered eighteen months earlier.

A person reading the step silently corrects that. A script fails — or worse, matches something else.

6/ Another ordered service restarts that would have brought the application up before its database was accepting connections.

In a real failover somebody notices and reorders. Afterward nobody writes it down.

7/ The third was the verification step. It checked the interface came up.

Not that traffic flowed. Not that sessions re-established. Not that the application answered.

8/ None of this was found by testing the automation.

It was found by writing it.

Encoding a runbook is the cheapest audit you'll ever run — and it happens whether the automation ships or not.

#NetworkAutomation #NetOps
