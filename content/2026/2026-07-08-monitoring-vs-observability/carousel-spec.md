# Carousel build spec — monitoring-vs-observability

8 slides · 1080×1350 (4:5).

## How to generate (read first — paste this whole file)

Generate these as individual images — one separate image per slide, each portrait 1080×1350 (4:5). Do NOT combine them into a grid, collage, or contact sheet. Generate one slide at a time; wait for "next" between slides. Keep identical style, palette, and fonts across all slides. Proof every slide's text against this spec before using.

**Brand**
- **Colors:** navy `#161a45` (background/base ~60%) · cream `#F4EFE3` (headlines + body text ~30%, not stark white) · red `#eb2027` (accent ~10% — one word/rule/number per slide, never more).
- **Palette rule:** rich dark navy field, soft cream text, one restrained red accent. Never red full-bleed backgrounds, never color-on-color. Cover + CTA may invert for punch.
- **Fonts:** Cormorant Garamond Medium (500) — titles (~32pt+). Lato Regular (400) — body (~18pt).
- **Identity:** MZS Networks · mzsnetworks.com · handle @mzsnetworks.
- **Slide mark:** no logo image — set the `@mzsnetworks` text small, in cream, as the mark. CTA slide also shows mzsnetworks.com.

| # | Type | Title (Cormorant) | Body (Lato) | Notes |
|---|------|--------------------|-------------|-------|
| 1 | Cover | Your monitoring stack is a **museum**. | It shows what broke. At 2am it tells you nothing you can act on. | "museum" red · @handle mark bottom |
| 2 | Body | Two words, mistaken for one | Monitoring answers *what*. Observability answers *why*. | italic what/why |
| 3 | Body | Monitoring | The questions you knew to ask in advance. CPU. BGP. A latency threshold. | plain |
| 4 | Body | Observability | The question you **didn't** pre-plan — asked mid-outage, without shipping a new sensor. | "didn't" red |
| 5 | Body | The tell is the war room | Still SSH-ing into boxes for context the dashboards never caught? That was monitoring. | plain |
| 6 | Body | Green wall, **down** service | Every part read "up" while the service was down. Nobody instrumented the relationship. | "down" red |
| 7 | Triad | What you actually bought | Monitoring: it's down. → Observability: the **why**. → Judgment: knowing **which one**. | step 3 red |
| 8 | CTA | Which one is your team running? | Follow **@mzsnetworks** · mzsnetworks.com | inverted/punch · handle red |

**Layout system:** body slides — navy field, cream title top third, cream body below, `@mzsnetworks` cream mark bottom-left. One red accent per slide max. Cover + CTA are visually distinct (heavier title, may invert to a red block). No stats anywhere — this is a judgment post; never fabricate a number.
