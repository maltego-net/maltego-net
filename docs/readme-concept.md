# README concept: Obsidian / Aegean blue

Text spec only. No code, no generators. Facts come from the current `README.md`; nothing is invented. Items in [README] must be copied from it.

## 1. What the references show

| Ref | Observation | Rule taken |
| :-- | :-- | :-- |
| `00-31-08` hermit with ring, white dots on flat ultramarine | Two-tone, square dots on a ~4 px grid. Dot density carries all tone: dense = ivory mass, sparse = cloth and shadow, empty = ground. Figure fades into ground without an outline. About 40% of the frame is empty ground. | Stipple tone from dot density, no outline, silhouette dissolves at the edges. |
| `00-31-20` winged figure on black | Square pixels with a dark gap, 8-10 px cells. Blue ramp from deep blue to pale ivory-yellow only on wing edges and brow. Large black areas, horizontal glitch streaks. | Obsidian ground, ramp from Aegean to ultramarine to ivory. Ivory only on highlights. No glitch streaks. |
| `00-31-24` winged rider on white | Very fine stipple (2-3 px), navy only, one figure at about 40% of frame width, lots of white around it. | Light theme: one navy figure, large empty ivory field. |
| `00-31-26` classical bust, halftone grid | Visible grid of dots over the whole frame, cyan and navy bands, deep shadow side. Vertical script texture behind. | Take the grid and the hard light/shadow split. Drop the cyan and the script texture. |
| `00-31-29` Corinthian columns, ink on paper | Single-hue blue line engraving on white, vertical hatching, nothing else. | Light theme reads as engraving: one ink colour on ivory paper. Vertical hatching for the rule/divider. |

Common to all: one subject, one hue family, density instead of colour for tone, generous empty ground, no text inside the picture.

## 2. Palette and roles

| Token | Hex | Role |
| :-- | :-- | :-- |
| Obsidian | `#111319` | Dark page ground in assets, light-theme text and darkest ink. |
| Aegean | `#10264A` | Hero top ground (dark), mid-tone dots and linework (light), panels. |
| Ultramarine | `#1936C8` | Dots, rules, one accent object. In light theme also links and numerals (7.0:1 on ivory). Never text on dark (2.0:1 on obsidian). |
| Ivory | `#E6E8E0` | Text on dark, highlight dots on dark, ground in light. |

Dark: ground gradient Aegean (top) to obsidian (bottom). Dots: ultramarine for shadow, ivory at 55% opacity for mid-tone, ivory 100% for highlights. At most 3 dot tones per asset.
Light: flat ivory ground. Dots: Aegean 35% / Aegean 70% / obsidian. Not an inversion: engraving on paper, not stipple on night.
GitHub canvas colour differs from both, so every SVG carries its own full-size background rect. No transparent assets.
Contrast: ivory on obsidian about 15:1, ivory on Aegean about 11.7:1, obsidian on ivory about 15:1, ultramarine on ivory 7.0:1.

## 3. Hero imagery

- Subject: one winged classical figure (statue), three-quarter or profile, as in `00-31-20` and `00-31-24`. The caduceus is an optional small detail. Pegasus rider and bust are fallback subjects, not additions.
- Placement: figure on the right 55% of the frame, cropped by the right or bottom edge. Left 40% is empty ground. Nothing sits behind the title area.
- Stipple density (dark): shadow 0-15% dot coverage, mid 30-50%, highlight 70-90%. Cell 6 px at 1200 px width (about 200 columns), square dots 4 px, 2 px gap. Fewer than 3 tones per region.
- Silhouette edge: ordered dither falling to empty ground. No outline, no glow.
- Light: same figure, finer cell (4 px), Aegean and obsidian dots on ivory, figure at about 40% of frame width with at least 25% empty ground on each side.
- Forbidden: glow, scanlines, glitch streaks, gradients on dots, texture behind the figure, text in the image.

## 4. Typography and hierarchy

GitHub renders its own fonts. Hierarchy is made with Markdown only.
- Title: `<h1 align="center">` with name [README] and one-line descriptor [README: IT Operations, Infrastructure and Automation, Hamburg]. The hero SVG holds no text.
- Section titles: `##`, plain words, no emoji.
- Body: 2 sentences per paragraph at most, one bold term at most.
- Lists and tables: at most 4 rows, one line each. Inline `code` only for repository and tool names.
- In SVG text (footer only): `ui-sans-serif, system-ui, sans-serif`, 14 px, ivory on dark, obsidian on light, one line.

## 5. README layout (order fixed)

1. Hero: `hero` picture (full width), title, one centred link line: Explore my work, LinkedIn, Email [README URLs].
2. Intro: 2 short paragraphs [README]: Hamburg, leading the technical operations team at Notebook-Pro, PXE/MDT network OS deployment platform on Proxmox and Windows Server. Optional `highlights` strip only with the three facts already in the README (team of 3-4, 10,800+ NEKO wallet registrations, PXE/MDT).
3. Divider.
4. Selected work: the four projects, 2x2 on desktop, collapsing to one column at 390 px: AWS Infrastructure (`terraform-aws-mempoolio`), NEKO, Mempoolio, Kubernetes Lab (`k8s-neko`) [README names, descriptions and URLs]. Each card is one SVG linked to its repository.
5. Currently building: Kityz, in development, one sentence [README]. No percentages, dates, metrics.
6. Contacts: LinkedIn and Email as two list items on separate lines [README URLs], then `footer` picture.
Tools table and the collapsed background block stay as in the current README, below item 4, unchanged in content.

## 6. SVG assets (`assets/`)

Every asset: self-contained, no external fonts, scripts, filters or raster images, under 150 KB, `role="img"` with `<title>` and `<desc>`, own background rect. Each exists as a `-dark` and `-light` pair, embedded as:
`<picture><source media="(prefers-color-scheme: dark)" srcset="assets/X-dark.svg"><img src="assets/X-light.svg" alt="..." width="100%"></picture>`

| File | viewBox | Content |
| :-- | :-- | :-- |
| `hero-dark.svg`, `hero-light.svg` | 1200x420 | Stipple figure from section 3. No text. |
| `divider-dark.svg`, `divider-light.svg` | 800x8 | 1 px line, centred row of 5 ultramarine dots. Decorative, `alt=""`. |
| `project-<name>-dark.svg`, `-light.svg` (4) | 560x200 | Project name (18 px) and the [README] one-line description (13 px) on Aegean (dark) or ivory (light), 1 px ultramarine left rule, a small stipple fragment at the right 25%. No logos, no badges. |
| `footer-dark.svg`, `footer-light.svg` | 1200x120 | One text line [README: name, Hamburg, closing line], centred, with a stipple edge fading from the bottom. |

Light/dark: switched only by `prefers-color-scheme` in `<picture>`. A single-file SVG with an internal media query is not used, because GitHub's image proxy does not reliably pass the viewer's scheme to SVGs loaded via `<img>`.

## 7. Mobile (390 px)

- Hero scales to 390x136. It has no text, so nothing becomes unreadable. The figure stays in the right half and must still read at this size.
- Project cards: one column. At 390 px the card text is 13 px x 0.7 = about 9 px, which is too small. Use viewBox 560x200 with the description kept under 60 characters and the name at 22 px, or place the text in Markdown under each card. Decision: name and description go in Markdown beside the card at 390 px, the SVG carries only the mark. Dev checks readability before committing.
- Title and links are Markdown and wrap. Link lines use separate lines with padding for 44 px tap height. No code blocks, no wide tables beyond 2 columns: no horizontal scroll.

## 8. Restraint rules

- No neon, no cyan, no gradients beyond Aegean to obsidian. Ultramarine is an accent, never a fill larger than a dot row or a 1 px rule.
- No emoji, in headings, lists or alt text.
- No badge or shield walls, no stats widgets, no skill-icon grids, no visitor counters.
- No more than one figure per page and one image per section.
- No animated SVG, no GIF.
- No claims not in the current README: no invented years, employers, percentages or project status.

## 9. Accessibility

- Hero alt: "Stippled statue of a winged figure on a dark blue ground." Divider alt: "" (decorative).
- Cards and footer alt repeat their visible text.
- No meaning carried by colour alone. Link text is descriptive ("LinkedIn", "Email").
- Ultramarine text on dark is not allowed.

## 10. Acceptance for Dev

Both themes checked via `prefers-color-scheme` at 1280 and 390 px. No horizontal scroll, every `img` has alt, no raster files, each SVG under 150 KB, facts match the current README.
