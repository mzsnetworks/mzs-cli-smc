# Shared Rules (all platforms)

These apply to every post regardless of platform. Platform files layer formatting on top; they never override these.

**Two lanes.** Posts live in one of two trees, and the lane changes which rule files apply:

| Lane | Tree | Ends on | Extra rules |
|------|------|---------|-------------|
| Thought leadership | `content/` | a question, no company ask | — |
| Marketing | `marketing/` | a CTA, names an MZS product or service | `rules/MARKETING.md` · `rules/SPANISH.md` |

Everything in this file applies to both, with one narrow exception noted under Fact Discipline.

---

## Niche & Audience

- **Niche:** network engineering, infrastructure, automation, AIOps, operations.
- **Audience:** practitioners and technical leaders — but reach-oriented. A post should be sharp enough that a senior engineer respects it and accessible enough that a mid-level engineer shares it.

## Voice

- Opinionated senior engineer who actually builds. Strong point of view, stated as a claim.
- First person is allowed and encouraged ("here's what I concluded after building in this space").
- A strong hook in the first line is mandatory on every platform.
- Concrete over abstract. Name real technologies, failure modes, and numbers.
- Confident, not hype. The credibility comes from specifics, not adjectives.

### Author Voice Layer (`rules/VOICE.md`)

If `rules/VOICE.md` exists, it is the **author's** voice profile and it is **mandatory** — every agent that writes or edits copy (Writer, Adapter, Editor, Formatter, Hook, Ideation, Reels) must read it and apply it: the author's pillars, defended opinions, signature openings/landings, word list, and war stories. It *adds specificity* on top of these shared rules; it never overrides fact discipline or the banned list. If `rules/VOICE.md` is absent, fall back to this shared voice. Build it with the Voice agent.

## Length Targets (recommended, per platform)

Hooks always sit above the platform "fold." Stay near the sweet spot, not the hard cap.

**These targets are calibrated to English.** Spanish runs roughly 15–25% longer for the same content — see `rules/SPANISH.md` for the ES numbers. The *fold* does not scale in either language.

| Platform | Sweet spot | Hard cap | Fold (hook must land before) |
|----------|-----------|----------|------------------------------|
| LinkedIn | ~1,300–2,000 chars (~200–350 words) | ~3,000 chars | ~210 chars (~3 lines) |
| Facebook | ~400–800 chars | none (63k) | ~477 chars desktop (~400 mobile) |
| Instagram | ~125–220 chars caption (more if carousel) | ~2,200 chars | ~125 chars (first line) |
| X — single | ~240–270 chars | 280 chars | whole post visible |
| X — thread | each tweet ≤280, one idea per tweet | 280/tweet | tweet 1 is the hook |

The Editor tightens to these; the Scorer's "platform fit" dimension checks them. **`python3 tools/check-renders.py <postdir>` verifies them mechanically** — run it before publish, always.

**Draft to the middle of the band, not the cap.** The numbers above are limits. Writing to the limit and trimming afterward wastes a pass and reliably overshoots: Facebook exceeded 800 on six of six Business posts written on 2026-09-20, each needing two rounds of cuts. Draft targets that hold: LinkedIn ~1,500–1,800 · **Facebook ~550–700** · Instagram ~600–900 caption · Spanish LinkedIn ~1,700–2,000.

## Fact Discipline (Non-Negotiable)

This is the one rule that does not loosen.

- **Every statistic, percentage, or forecast must trace to a real, citable source.** No invented precision.
- If a number can't be sourced, cut it or reframe it as judgment ("most teams," "in my experience").
- Vendor forecasts (Gartner, IDC, etc.) must name the source and the year.
- The Factcheck agent enforces this. A post with an uncited stat does not ship.

**The one exception, `marketing/` lane only:** an uncited number passes when the copy frames it as the *reader's* hypothetical scenario ("a template update that reached 38 of 40 sites") and never as something MZS measured ("we found drift at 38 of 40 client sites"). Credentials and proof points are excluded from the exception — they are claims and need attribution or a source. Full table in `rules/MARKETING.md`; enforced by `agents/FACTCHECK.md`. This exception does not exist for `content/` posts.

## Renders Are Plain Text (every platform)

**No platform in this system renders markdown.** LinkedIn, Facebook, Instagram and X all publish `*asterisks*`, `**bold**`, `_underscores_` and `` `backticks` `` as literal characters. A render is the exact string that will appear in the feed.

- Never use markdown emphasis in a render. Carry emphasis with sentence structure and line breaks instead.
- The one place asterisks are correct is `carousel.json`, where `*word*` is the renderer's own syntax for the red accent. Those files never publish.
- **A `#` followed by digits becomes a hashtag.** "change window #47" and "reason #3" linkify and count against the platform's tag limit. Write "window 47" or "the third reason".

This has shipped twice — markdown to LinkedIn in the Sep 6–18 batch, and in every Instagram caption in the Oct 11 batch — so it is checked mechanically: `python3 tools/check-renders.py <postdir>`.

## Always Banned (every platform)

- Fabricated or unsourced numbers
- Claims about technology behavior that are factually wrong
- Consultant fluff with no operational substance ("synergy," "leverage best-in-class")
- Pure hype with no specifics ("revolutionary game-changer")

## Allowed Here (unlike LinkedIn-LPM)

- Emojis — per platform policy
- CTAs and closing questions
- Personal anecdote openings
- Threads, carousels, and long form where the platform supports them

## The Spine

Most strong posts in this system share a structure:

1. **Hook** — a claim or tension in the first line
2. **POV** — your take on it
3. **Data** — cited numbers that back the take
4. **Judgment** — what it means, the part only an experienced engineer can say
5. **Landing** — a memorable close (often a triad or a question)

The reference posts use: "The CLI made us operators. Code made us engineers. AI is about to make us judges." That triad is the landing. Aim for that.
