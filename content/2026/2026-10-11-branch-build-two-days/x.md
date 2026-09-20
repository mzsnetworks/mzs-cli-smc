# X — branch-build-two-days


## Single (publish this)

A branch build should take two days. Most take two weeks.

The gap is almost never engineering time — it's waiting. Addressing, the standard switch model, who owns the test.

None of it is difficult. All of it is undecided.

#NetworkAutomation #NetOps

---

## Thread

1/ A branch build should take two days.

In most organizations it takes two weeks.

The gap is almost never engineering time. It's waiting. 🧵

2/ Where the two weeks actually go:

Someone requests addressing and waits for a reply. Someone asks which switch model is standard this quarter and gets two answers.

3/ The config gets written from the last site's config — which was written from the site before it, carrying a typo that has now propagated through four buildings.

The circuit arrives and nobody knows who tests it.

4/ None of that is difficult.

All of it is undecided.

5/ Four things collapse it, and none require buying anything:

• One parameterized template
• One addressing scheme allocated from a system
• One staging step before equipment ships
• One written acceptance test

6/ The template matters most. Not a document describing the standard — an actual file with variables.

The moment a config is copied, it inherits every decision nobody remembers making.

7/ What makes this work isn't the automation. It's that four decisions get made once instead of being renegotiated at every site.

The second branch tells you whether you built a template or just another config.

#NetworkAutomation #NetOps
