---
name: niche-research
description: Surface recent, dated, citable stories in the niche via WebSearch. Use when the user says "what's trending", "research my niche", "find stories", "this week's news", "what's happening in network engineering", or wants current events to post about. No scraping — WebSearch only.
---

# Niche Research

Run the **RESEARCH agent**. Read `agents/RESEARCH.md` and `rules/SHARED.md`, then execute:

1. Run targeted WebSearch queries across the niche (vendor news, outages, automation, AIOps, surveys) for the requested window (default last 14 days).
2. Return up to 20 stories, each with a real link, a verified date, a one-line why-it-matters, and a shareable angle.
3. Drop anything you can't date or link, and list what you dropped.

Every surfaced stat must name its source — you're feeding Factcheck downstream. Do not fabricate stories, dates, or numbers. Hand strong stories to the `ideate` skill or `/post`.
