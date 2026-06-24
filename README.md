# Social Media Content System (claude-cli-smc)

A multi-platform editorial system for technical social content. Write one idea once, render it correctly for **LinkedIn, Instagram, and X** — each with its own voice, length, emoji policy, and hashtag rules.

Adapted from the LinkedIn-LPM editorial system. Same niche (network engineering, infrastructure, AIOps) and the same fact-checking discipline, but **engagement-oriented** rather than repel-mode: hooks, CTAs, questions, threads, and platform-appropriate emojis are allowed.

---

## How It Works

One core idea flows through a pipeline and comes out as three platform-native posts.

```
Writer --> Factcheck --> Platform Adapter --> per-platform Editor --> Hashtag
                              |
              +---------------+---------------+
              |               |               |
          LinkedIn        Instagram           X
```

1. **Writer** drafts the core post (the master version, usually LinkedIn-length)
2. **Factcheck** verifies every number and claim against a real source
3. **Platform Adapter** renders the core idea into LinkedIn, Instagram, and X versions following each platform's rule file
4. **Editor** tightens each rendered version
5. **Hashtag** applies per-platform hashtag rules

See `agents/PIPELINE.md` for run mechanics.

---

## Layout

```
rules/
  SHARED.md        # niche, audience, voice, fact discipline — applies everywhere
  LINKEDIN.md      # long-form, professional, minimal emoji, 2-3 hashtags
  INSTAGRAM.md     # caption + carousel, emoji-accented, 10-15 hashtag block
  X.md             # 280-char single or thread, concise, 1-2 hashtags
agents/
  WRITER.md
  FACTCHECK.md
  PLATFORM_ADAPTER.md
  EDITOR.md
  HASHTAG.md
  PIPELINE.md
content/             # generated posts (see Output Layout below)
  <year>/
    <YYYY-MM-DD>-<slug>/
      master.md  linkedin.md  instagram.md  x.md
```

## Output Layout

Generated posts are **idea-first**: the unit of work is one idea, rendered for three platforms. Each idea gets one dated folder holding all its versions.

```
content/<year>/<YYYY-MM-DD>-<slug>/
  master.md      # the fact-checked source (LinkedIn-length, full Sources block)
  linkedin.md    # publish-ready LinkedIn render
  instagram.md   # publish-ready Instagram render
  x.md           # publish-ready X render
```

- `<YYYY-MM-DD>` is the intended publish/creation date (sorts chronologically).
- `<slug>` is a short kebab-case handle for the idea, drawn from its landing or thesis (e.g. `ai-makes-us-judges`).
- `master.md` is what Factcheck gates on; the Adapter writes the other three from it.

The first idea — `content/2026/2026-06-24-ai-makes-us-judges/` — is the migrated reference set. The same idea across all three platforms; the calibration examples the rules and agents are tuned to.

---

## What Carries Over From LinkedIn-LPM (and What Doesn't)

**Carries over:**
- Network-engineering niche and senior-practitioner credibility
- Fact discipline — every statistic needs a cited source
- Operational grounding over hype; judgment over buzzwords

**Deliberately loosened:**
- Emojis allowed (platform-dependent; heavy on Instagram, sparing on X, near-zero on LinkedIn)
- CTAs and closing questions allowed
- Personal-brand voice allowed (first-person, "here's what I concluded")
- Long-form allowed where the platform supports it
