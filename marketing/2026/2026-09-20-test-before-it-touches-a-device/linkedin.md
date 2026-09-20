# LinkedIn — test-before-it-touches-a-device


In most disciplines, "we'll run it and see what happens" is not a test plan.

In networking it is still the default. The change gets reviewed by reading it, approved by someone who also read it, and then validated by applying it to production during a window and watching what breaks. Nobody would call that a test anywhere else in the organization.

Reading a change tells you it is syntactically fine. It does not tell you that this ACL, on this device, with this routing table, drops the traffic you forgot about.

The alternative is not exotic. Build a model of the network — topology, addressing, policy, adjacencies — and evaluate the change against the model before it reaches a device. What you get back is not "the config parses." It is what the network would do differently, and which of those differences you did not intend.

That is what Config Modeling does, and it is the single practice that moves the most risk out of the change window, because it moves the discovery of a mistake from 2 AM in production to a Tuesday afternoon on a laptop.

A model does not catch everything, and it is worth being clear about that. It will not tell you an optic is degrading, or that the far end has an undocumented policy of its own, or that the vendor's implementation disagrees with the vendor's documentation. What it catches is the class of error that comes from reasoning about a large network inside one person's head. In a multi-site estate, that is most of them.

It also changes the review conversation. Reviewers stop arguing about syntax and start arguing about intent, which is the argument worth having.

Talk to an engineer: mzsnetworks.com

#NetworkAutomation #InfrastructureAsCode #NetOps
