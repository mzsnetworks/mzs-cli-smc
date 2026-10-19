# LinkedIn — your-tickets-are-lies

AI can't learn much from your tickets, because your tickets are lies.

Not malicious ones. Tired ones.

"Resolved: rebooted." "Closed: no fault found." "Fixed: user error." Every one of those was typed at the end of a long day by somebody who had already solved the problem in their head and was being measured on close time.

Here's why it matters more than it used to. Every AIOps tool being sold this year learns from that history — it reads the symptom, reads the resolution field, and builds an association between them.

So if the resolution says "rebooted," the model learns that rebooting resolves this class of symptom. It does not learn what was actually wrong, because nobody wrote that down. You've taught it the workaround — at scale, with confidence, and without the hesitation the engineer felt when they typed it.

The gap between what actually happened and what got typed is the ceiling on every model you point at it. It isn't a tooling problem, so no purchase fixes it — a better model trained on a corpus of "rebooted" just gives you a faster, more articulate recommendation to reboot.

What changes it is unglamorous:

→ A resolution field that asks for a cause, not an action. "Rebooted" is what you did. "Process leaked memory until the daemon stopped answering" is what happened.

→ Closing codes that separate fixed from recovered from went away on its own. Those are three different outcomes and most systems record them identically.

→ Permission to write "unknown." An honest unknown is more useful to a model — and to the next engineer — than a confident wrong answer. Right now "unknown" feels like an admission, so people type "rebooted" instead.

None of that requires a platform. It requires treating the ticket as a record rather than a receipt.

Your ticket history is training data now, whether you meant it to be or not. Most of it currently teaches one lesson: turn it off and on again.

What percentage of your closed tickets name a cause?

#AIOps #NetworkOperations #NetOps
