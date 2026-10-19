# LinkedIn — boring-on-purpose


We build with Python and Ansible, and that choice is deliberately unexciting.

There are more elegant options. Frameworks that express the same work in less code, platforms with their own language that handle a problem beautifully if you adopt their model of the world. We have used several and some are genuinely good.

The question we ask instead is what happens eighteen months after the engagement ends.

By then the work has to be maintained by your team, not by us. Three things decide whether that is possible, and none of them is how expressive the tool was on day one.

Can you hire for it. There is a real market of engineers who have written Ansible and read Python. There is a much smaller one for any given vendor's domain-specific language, and that market is in the vendor's control rather than yours.

Can a new engineer read it. Ordinary code is reviewable by somebody who did not write it, which is what makes it safe to change. A clever abstraction that requires a tour before anyone touches it quietly becomes untouchable, and then it becomes a thing nobody runs.

Can you leave. If the automation only runs inside one vendor's platform, your options at renewal are not really options. Portability is a decision made early, in the artifacts, or paid for later at the negotiating table.

Sometimes the right answer is a vendor's native tooling, and we will say so when it is. The point is that it should be a decision with those three questions answered, rather than a default inherited from whoever built it first.

The best automation we leave behind is the kind your team forgets we wrote.

Talk to an engineer: mzsnetworks.com

#NetworkAutomation #NetOps #InfrastructureAsCode
