# LinkedIn — audience-of-one

Most automation I meet has an audience of one.

If only the author can run it, it isn't automation. It's a personal productivity tool with very good PR.

The tells are consistent:

It runs from somebody's laptop. It needs three environment variables that live in that person's shell profile. The credentials come out of their keychain. The README, if there is one, says "ask me." And when they take two weeks off, it stops — and nobody notices until the thing it was quietly preventing happens.

I want to be careful here, because this is not a code quality problem. Some of the sharpest scripts I've seen were bus factor one. The logic was right, the error handling was thoughtful, the output was clean. It just couldn't leave the machine it was born on.

The gap is packaging and access. That's the unglamorous half of automation, and the incentives run against it — writing the script is the interesting part, making it runnable by somebody else is chores. So it doesn't get done, and the team ends up depending on a capability that has a pulse and takes holidays.

The test is simple and slightly uncomfortable: can somebody else run this, today, without you in the room? Not "could they work it out from the code." Can they run it.

Four things move a script across that line:

→ It runs somewhere shared, not on a laptop
→ Credentials come from somewhere other people can reach, with their own access
→ Failure explains itself — which step, which device, what state it left behind
→ Somebody else has actually run it once, in front of you, without help

That last one is the only real proof. Everything before it is a plan.

Automation that only one person can run hasn't removed the toil. It's moved the toil into one person's calendar and handed the team a single point of failure that takes holidays.

If you were out for two weeks, what stops?

#NetworkAutomation #NetDevOps #NetOps
