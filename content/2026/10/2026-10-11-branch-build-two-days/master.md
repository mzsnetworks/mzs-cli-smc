# Master — branch-build-two-days

**Preset:** Business (LinkedIn company page + Facebook + Instagram + X, all on the MZS account)
**Date:** 2026-10-11
**Thesis:** A two-week branch build is almost never two weeks of work. It is two days of work distributed across three teams with no agreed interface, and the fix is standardizing four things rather than buying anything.
**Pillar:** Enterprise Network Operations — provisioning
**Source:** ideas-2026-08-30 #3
**Stats:** none stated as fact. The "two days / two weeks" figures describe a shape of work, not a measured client outcome.

---

A branch build should take two days. In most organizations it takes two weeks.

The gap is almost never engineering time. It is waiting.

Here is where the two weeks actually go. Someone requests addressing and waits for a reply. Someone else asks which switch model is standard this quarter and gets two answers. The config gets written from the last site's config, which was itself written from the site before it, carrying a typo that has propagated through four buildings. The circuit arrives and nobody knows who tests it, so it is tested twice or not at all.

None of that is difficult. All of it is undecided.

Four things collapse it, and none of them require buying anything.

One template, parameterized. Not a document describing the standard — an actual file with variables, where building a new site means filling in values rather than copying and editing. The moment a config is copied, it inherits every decision nobody remembers making.

One addressing scheme, allocated from a system. Not a spreadsheet. Something that hands out the next block and records who holds it, so the request stops being a conversation.

One staging step. The equipment is configured, powered, and validated before it ships, not in a closet at the site with someone on speakerphone.

One acceptance test, written down. A short list of things that must be true before the site is called done, including at least one that proves traffic actually takes the path you intended.

What makes this work is not the automation. It is that four decisions get made once instead of being renegotiated at every site.

The second branch is where you find out whether you built a template or just another config.

How long does your fortieth site take compared to your fourth?
