# Instagram — audience-of-one

Most automation I meet has an audience of one. 👤

If only the author can run it, it isn't automation. It's a personal productivity tool with very good PR.

The tells are consistent:

→ it runs from somebody's laptop
→ it needs three environment variables that live in that person's shell profile
→ the credentials come out of their keychain
→ the README, if there is one, says "ask me"
→ when they take two weeks off it stops — and nobody notices until the thing it was quietly preventing happens

I want to be careful here, because this is not a code quality problem. ⚙️

Some of the sharpest scripts I've seen were bus factor one. The logic was right, the error handling was thoughtful, the output was clean.

It just couldn't leave the machine it was born on.

The gap is packaging and access — the unglamorous half of automation. And the incentives run against it: writing the script is the interesting part, making it runnable by somebody else is chores.

So it doesn't get done, and the team ends up depending on a capability that has a pulse and takes holidays.

The test is simple and slightly uncomfortable:

Can somebody else run this, today, without you in the room? Not "could they work it out from the code." Can they run it.

Four things move a script across that line:

→ it runs somewhere shared, not on a laptop
→ credentials come from somewhere other people can reach, with their own access
→ failure explains itself — which step, which device, what state it left behind
→ somebody else has actually run it once, in front of you, without help

That last one is the only real proof. Everything before it is a plan.

Automation only one person can run hasn't removed the toil. It's moved it into one person's calendar.

If you were out for two weeks, what stops? 👇

#NetworkAutomation #NetDevOps #NetOps #Python #Networking
