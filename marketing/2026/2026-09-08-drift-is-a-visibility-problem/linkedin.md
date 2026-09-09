# LinkedIn — drift-is-a-visibility-problem


Quick test for multi-site network teams:

Can you say, with confidence, what's actually configured on every device across every site — right now?

Not what the standards doc says. Not what the change tickets say. What's really there.

For most teams the honest answer is no. Configs drift:
— an emergency fix at 3 AM that never got documented
— a site engineer's "temporary" workaround, now two years old
— a template update that reached 38 of 40 sites

Here's the part that usually gets misdiagnosed. Every one of those was a reasonable call by a competent engineer. The 3 AM fix restored service. The workaround unblocked a project that was already late. The template push hit two devices that were unreachable that night, Ansible logged the failures, and the run moved on.

Nobody was careless. Drift is not what happens when people stop following the process. It's what happens when the process has no way to tell you it didn't finish.

Which is why more discipline doesn't fix it. Stricter change control and longer checklists govern what you intend to deploy. None of it reads the running config back and tells you what is actually there.

Then the audit lands, and compliance validation becomes weeks of manual diffing.

This is why we built Driftguard — continuous detection of configuration drift across sites, so the answer to "what's deployed?" is a dashboard, not an archaeology project.

Drift is not a discipline problem. It's a visibility problem. Fix the visibility.

Book a consultation: mzsnetworks.com

#NetworkAutomation #Compliance #NetOps
