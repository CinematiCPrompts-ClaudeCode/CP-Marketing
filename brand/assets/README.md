# Brand assets

Canonical marketing assets — use these files, don't redraw or approximate them.

| File | What it is | Source of truth |
|---|---|---|
| `app-icon-1024.png` | App icon (clapperboard + film reel, cream on deep navy) | `Marketing-Examples/Cinematic Prompts/Appstore /AppIcon-512@2x.png` |
| `app-store-badge.png` | Apple's official "Download on the App Store" badge | Apple Marketing Resources |

**Never redraw the App Store badge.** It's a trademarked lockup and Apple's guidelines
require the official artwork. Use this file.

## Design system

Full CI: `Marketing-Examples/Cinematic Prompts/cinematic-prompts-design-system.pdf`
(generated from the live codebase; source of truth is `src/index.css` + `tailwind.config.ts`).

**Colors**
| Role | Hex |
|---|---|
| Orange / Primary | `#f4aa33` |
| Cyan / Accent | `#22b5c3` |
| Petrol / Card | `#0b556a` |
| Deep Background | `#0f1119` |
| Foreground / Text | `#f4f3ef` |
| Red / Selected | `#c54929` |
| Muted | `#20222b` |
| Muted Foreground | `#808497` |
| Border | `#2b2d3a` |

**Type** — Playfair Display (400/500) for headers only; **Jost** for all UI text
(600 for the CINEMATIC PROMPTS wordmark, 500 for style/lighting names, 400 for
metadata and descriptions).
