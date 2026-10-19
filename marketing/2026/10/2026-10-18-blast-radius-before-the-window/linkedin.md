# LinkedIn — blast-radius-before-the-window


A change review reads a diff. The risk is almost never in the diff.

The diff is honest about what it shows: these lines on this device become those lines. Reviewers check the syntax, check it matches the standard, and approve. The part they cannot check from that view is what else the change touches, because that lives in the topology rather than in the device.

So the question gets answered by memory. Somebody senior reads the change and says it looks fine, meaning they cannot immediately think of a dependency it breaks. That is genuinely valuable and it is not a method. It scales exactly as far as one person's recall of an estate that changed last Tuesday.

Modeling the change against the intended network is the part that does scale. A prefix removed here stops being advertised there. A policy tightened on one firewall moves traffic onto a path that was sized for failover rather than for steady state. An MTU change on a link affects a tunnel three hops away that nobody in the room is thinking about.

These are not exotic failures. They are the ordinary ones, and what they have in common is that the device-level change was correct. Nothing in a diff was going to reveal them.

Config Modeling answers the blast-radius question before the window opens, as part of the review, rather than leaving it to be discovered by traffic at two in the morning. The output is not a pass or a fail. It is a list of what else is affected, which is what a reviewer needed in order to approve properly in the first place.

An approved change is one somebody decided was safe. A modeled change is one where the question was actually asked.

Talk to an engineer: mzsnetworks.com

#NetworkAutomation #NetOps #ChangeManagement
