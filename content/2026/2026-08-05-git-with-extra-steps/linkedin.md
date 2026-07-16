# LinkedIn — git-with-extra-steps (MZS company page)

Five signs your "NetDevOps transformation" is just Git with extra steps.

We see these in real environments, usually all five at once:

1. Configs live in a repo — and get pushed by hand. The repo is where truth is stored, but the CLI session is still where truth is decided. That's not a source of truth. That's a backup folder with a commit history.

2. PRs approved unread. Four hundred changed lines, "LGTM" in forty seconds. Review became a turnstile instead of a gate — the process ships the appearance of scrutiny without the scrutiny.

3. A green pipeline nobody trusts. The checks pass, and then an engineer SSHes in to verify anyway. Everyone senses the truth: the pipeline tests what was easy to test, not what actually fails.

4. A branch named prod-final-v2. Branch names are process ambiguity written down. When nobody knows which branch is real, the strategy isn't a strategy — it's archaeology.

5. Rollback = SSH. The forward path is automated; the reverse path is a senior engineer typing fast at 2am. Automation without a reverse gear isn't a pipeline. It's a one-way door at machine speed.

All five have the same root cause: the tool got adopted, the behavior didn't. Git arrived; the decisions stayed where they always were — in terminals, in heads, in habit.

What the transformation actually looks like: the repo is the only way changes reach devices. Review gets the time the blast radius deserves. The pipeline tests the failure modes that have actually paged you. Branch flow is written down and boring. And rollback is a pipeline run, not a heroic memory.

Git stores your configs. It can't store your discipline. A transformation is measured by what changes at 2am — not by what moved into a repo.

Which sign stung? Be honest — ours was #3 for a while.

#NetDevOps #NetworkAutomation #GitOps
