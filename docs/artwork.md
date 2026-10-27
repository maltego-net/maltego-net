# Hermes character engraving

## What ships

- `assets/hermes-light.svg` — ultramarine shadow marks on marble ivory.
- `assets/hermes-dark.svg` — independently mapped illuminated stone in muted blue and ivory on obsidian.
- `assets/hermes-light-mobile.svg` and `assets/hermes-dark-mobile.svg` — closer portrait-only framing below 600px, generated from the same character field. The mobile assets omit the decorative captions so the face remains legible at a 360px viewport.
- `assets/source/hermes.png` — original generated sculptural study, 768 × 768 grayscale plus alpha, 268,867 bytes. This is a generation input only, not embedded inside the SVG.
- `scripts/generate-hermes.py` — deterministic conversion, Python and Pillow only.

The illustration is built from actual monospaced characters, not a photograph wrapped in SVG. Each impression uses a 224 × 140 sampling grid and the density vocabulary `.,:;i1tfLCG08@`. The broad planes retain the sculpture's lighting; the marks resolve curls, eyes, feathers, cheek and neck. SVG text rows use local `Courier New, monospace` with explicit per-character x positions, requiring no downloadable fonts. Character shape can vary slightly with the viewer's installed fallback font. Explicit positions avoid the whitespace collapse that distorted the first preview; no SVG `textLength` stretching is used.

The README's identity, experience, project descriptions, toolkit and links remain native text. The plate's “Hermes” and specimen captions are decorative. SVGs contain their own title and description, and the README image has meaningful alternative text.

## Provenance

The source was created for this project on 2026-10-27 with the built-in imagegen tool and `transparent_background: true`. It is an AI-generated invented sculpture, not a photograph of a historical object. No reference image was supplied to the generation call, copied, traced, or sampled. The five files in `ref/` informed the art direction only; their unknown authorship or licenses are not asserted.

Source SHA-256:

```text
6060bdef8dfe703eff34d4e2615374a7faedf66e02b7c2ae0474533535e977c4
```

The generation prompt was:

> Use case: stylized-concept. Asset type: original grayscale source for a computational ASCII engraving of Hermes, for an engineering portfolio. Create a highly refined, anatomically convincing antique marble sculptural bust of Hermes, three-quarter view, head turned subtly toward viewer's left. Curled hair, calm classical face, a subtly winged petasos headpiece with two clearly articulated small feathered wings (wings on headpiece, never attached to body), neck, collarbones, shoulders and upper chest. Crop below upper chest as a sculpture bust, all hat/feather tips within frame. Square composition, bust centered and fills ~88% height with clear margins. Hard museum lighting from upper left, deeply resolved chiaroscuro, luminous marble forehead/nose/cheek against dark shadow eye socket/curls/neck, nuanced grayscale tonal planes and finely incised engraving detail, realistic classical proportions. Genuine transparent background, isolated sculpture. This is a new invented sculpture, do not reproduce known artwork. No text, no captions, no typography yet, no pedestal, no border, no scenery, no metallic sci-fi helmet, no glow, no neon, no cyberpunk, no colors. Need exceptionally detailed curls, facial anatomy, feather filaments and stone surface; sharp silhouette suitable for reduction to dense tiny ASCII characters. Quiet classical art publication quality.

The generated PNG was converted to grayscale with its alpha channel retained and reduced with Pillow's `thumbnail((768,768))`, then saved with PNG optimization. A few feathers reach the source's top edge; the SVG leaves a margin around the source rather than clipping the image further. Regenerating from the prompt is nondeterministic. The committed input makes the final SVG conversion reproducible.

## Reproduction

With Python and Pillow installed, run from the repository root:

```sh
python scripts/generate-hermes.py
```

Created with Python 3.14.5 and Pillow 12.2.0. There are no runtime dependencies for viewing the README. The converter resamples luminance and alpha, applies autocontrast and a controlled contrast curve, and groups rows by three ink tones. Light mode translates shadow into glyph density; dark mode translates illuminated stone into glyph density with a different gamma. This preserves the direction of light instead of simply inverting colors.

Desktop SVGs use a 1200 × 560 viewBox; mobile SVGs use a 600 × 560 portrait crop. Each corrected output is approximately 116–117 KB (light) or 145 KB (dark), below the design target of 500 KB. They contain no external images, scripts, animation, gradients, web fonts or external service calls. Only the source PNG and the short converter are needed to edit the artwork; preview tooling is separate and is not consumed by GitHub.
