---
name: ideate
description: Generate a content-idea matrix — 30+ specific post angles crossing the author's pillars with proven formats. Use when the user says "give me post ideas", "content ideas", "what should I post about", "ideate", "content matrix", "map out my content", or asks for a batch of things to write.
---

# Ideate

Run the **IDEATION agent**. Read `agents/IDEATION.md`, `rules/SHARED.md`, and `rules/VOICE.md` (if it exists — pull pillars from it), then execute:

1. Cross the author's content pillars with the 8 formats into a 30+ row table of *specific* angles (a real post, not a topic). Include a **Developed?** column (`—` / `drafting` / `SHIP` / `PUBLISHED`).
2. Flag which ideas will need a cited stat.
3. End with a "Top 5 to write now."
4. **Ask if the user wants to save the ideas.** If yes, write them to `ideas/ideas-<YYYY-MM-DD>.md` (create the `ideas/` directory if absent) — the full matrix (with the **Developed?** column) plus the Top 5.

If the user hands you a RESEARCH story list, use it as raw material. Do not draft full posts — when the user picks one, hand off to `/post`.
