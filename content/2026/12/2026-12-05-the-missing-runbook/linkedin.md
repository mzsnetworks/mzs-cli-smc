# LinkedIn — the-missing-runbook


Every AIOps tool promises to cut alert noise. The noise was never the problem. The missing runbook was.

The pitch is consistent and it is not dishonest. Thousands of events become dozens of incidents, the duplicate storms collapse, the thing that fired four hundred times becomes one line. Those tools do work. I have seen the before and after.

What I have also seen is a team six months later, ignoring a much smaller number of alerts.

Because an alert is not noise because there are many of it. An alert is noise because nobody knows what to do when it arrives. One alert a week that nobody can act on is noise. Two hundred a day that each have a known response are a busy Tuesday.

The question that sorts them is simple and uncomfortable: when this fires at 3am, what is the person supposed to do? If the answer is "look at it and decide," you have not built an alert. You have built an interruption with a technical description attached, and the person receiving it will learn to stop reading it at whatever volume you deliver it.

So the honest sequence is the opposite of the sales one. Go through what currently fires and sort it into three piles. The ones with a clear response, which are fine. The ones that need a response written, which is the actual work and takes weeks. And the ones that should not exist, which is usually the largest pile and the fastest win nobody takes, because deleting an alert feels like removing a safety net.

Then correlate. Correlation on top of alerts that each mean something is genuinely valuable. Correlation on top of alerts nobody can act on produces a tidier version of the same problem.

A tool can tell you what happened. It cannot tell you what you do about it, and that was always the missing part.

How many of your alerts have a documented response?

#AIOps #ITOperations #NetworkEngineering
