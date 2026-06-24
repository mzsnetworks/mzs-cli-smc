# Shared Rules (all platforms)

These apply to every post regardless of platform. Platform files layer formatting on top; they never override these.

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

| Platform | Sweet spot | Hard cap | Fold (hook must land before) |
|----------|-----------|----------|------------------------------|
| LinkedIn | ~1,300–2,000 chars (~200–350 words) | ~3,000 chars | ~210 chars (~3 lines) |
| Instagram | ~125–220 chars caption (more if carousel) | ~2,200 chars | ~125 chars (first line) |
| X — single | ~240–270 chars | 280 chars | whole post visible |
| X — thread | each tweet ≤280, one idea per tweet | 280/tweet | tweet 1 is the hook |

The Editor tightens to these; the Scorer's "platform fit" dimension checks them.

## Fact Discipline (Non-Negotiable)

This is the one rule that does not loosen.

- **Every statistic, percentage, or forecast must trace to a real, citable source.** No invented precision.
- If a number can't be sourced, cut it or reframe it as judgment ("most teams," "in my experience").
- Vendor forecasts (Gartner, IDC, etc.) must name the source and the year.
- The Factcheck agent enforces this. A post with an uncited stat does not ship.

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
