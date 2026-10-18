# LinkedIn — change-record-five-fields


Most change records are written to be filed, not to be read.

We ask for them early when we take over an environment, and the pattern is consistent. The records are complete and close to useless.

There is a ticket number, a requester, a category, a configuration item, a risk rating that is almost always "low," an approval chain, and a date. Everything an audit asks for, and nothing the person at 2am needs.

Five fields change that.

What changed — the configuration delta itself, not "updated ACL per request." The diff, pasted in.

Why — the condition that made the change necessary. Not the ticket that authorized it. The thing that was actually wrong.

Who approved it — a person's name. An approval queue is routing, not accountability.

How to undo it — the specific steps, written by somebody who has run them at least once. If nobody has, the record should say so. That is useful too.

The business reason, in one line — what breaks, for whom, if this change is wrong. It is the field that gets skipped, and the one that tells an engineer at 2am whether to roll back immediately or keep investigating.

The test for a change record is not whether it passed review. It is whether somebody who was not there, reading it six months later in the middle of an incident, can tell within a minute whether this change belongs on the suspect list.

Most of what sits in a change record is metadata about the process that produced it. Only those five fields are about the change.

A change record is not a receipt for work completed. It is a message to whoever is awake when it matters.

Which of the five is missing from yours?

#ChangeManagement #NetworkEngineering #ITOperations
