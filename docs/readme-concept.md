# Hellenic ASCII — design specification

## Decision

Select **Marble / Ultramarine: the engraved study** as the primary direction. A detailed Hermes bust is the sole major decorative gesture. Its texture supplies the richness; a single-column editorial README supplies clarity. Adapt this composition deliberately for dark mode using the tonal treatment of **Obsidian / Aegean: the nocturnal plate**.

This document is a design specification, not a claim that rendering or visual validation has already passed. Professional facts come only from the supplied brief and the current README. References below were opened directly from `ref/` with the available local image viewer; no vault was used. There is no tool named Read in this environment.

## Reading the five references

| Local reference | Observed quality | Translation into this design |
| --- | --- | --- |
| `photo_2026-10-26_00-31-08.jpg` | Dense ivory halftone against saturated blue; a large circular form remains clear despite granular detail. | Preserve broad light/shadow masses underneath the smallest marks. Use ultramarine decisively, not as a glow. |
| `photo_2026-10-26_00-31-20.jpg` | A winged figure emerges from near-black through small square marks; diagonal wings and drapery carry the silhouette. | Use articulated feather detail and isolated highlight clusters in dark mode. Do not reproduce the figure, screen-noise streaks, or multicolor pixels. |
| `photo_2026-10-26_00-31-24.jpg` | A compact mounted figure has a strong silhouette inside unusually generous white space. | Keep substantial untouched space around Hermes; avoid a full-bleed wall of characters. Do not add a horse merely to include every reference motif. |
| `photo_2026-10-26_00-31-26.jpg` | Close sculptural portrait; curls, brow, nose and neck have convincing volume beneath a regular character-like grid. | This is the strongest structural guide for the hero: a recognizable face, resolved curls, neck and shoulder planes, then computational texture. No copied background lettering. |
| `photo_2026-10-26_00-31-29.jpg` | Slender columns, quiet blue engraving, fine parallel lines, measured spacing. | Borrow the discipline of fine rules and aligned spacing. A single small engraved rule may close the page; no repeated temple ornament. |

These are visual observations, not historical identifications of the supplied subjects. Their creators and licenses were not supplied. Treat them as direction only; do not embed, trace, or sample them into production artwork.

## Two differentiated concepts

### A — Marble / Ultramarine: the engraved study

An ivory print plate, approximately 1200 × 560, with a substantial three-quarter Hermes bust toward the right and an open field to the left. The head turns inward. A subtly winged headpiece identifies the messenger motif requested in the brief; avoid angel wings attached to the torso. Curl clusters, the brow, eye socket, nose, cheek, jaw and collarbone must resolve as anatomy before texture is applied. The lower shoulder dissolves sparingly into engraving marks instead of a hard rectangular crop.

Use marble ivory `#E6E8E0` for the ground, ultramarine `#1936C8` for dominant engraved strokes and Aegean navy `#10264A` for deep structural shadow. No gradient backdrop. A small plate caption is optional and decorative; no essential profile information belongs inside the illustration. Target roughly 55–65% art coverage, leaving purposeful breathing room. A small flat ultramarine registration rule can balance the open side.

**Rationale:** closest to a classical publication, strongest contrast with generic developer profiles, and naturally compatible with normal GitHub reading. Its quieter field allows the profile name and actual work to remain prominent.

### B — Obsidian / Aegean: the nocturnal plate

A more central and tightly cropped Hermes portrait, approximately 1200 × 560, with a clear winged headpiece silhouette and the face emerging from a near-black field. Dense engraved highlights trace the forehead, nose bridge and upper shoulder. Aegean blue carries broad middle tones; ivory is reserved for lit planes. Outer curls and shoulder edges partly merge into the ground. The texture should resemble ink or cut marks, never a luminous screen.

Use obsidian `#111319` as the ground, `#10264A` for low-contrast depth, restrained ultramarine for middle-tone marks, and `#E6E8E0` for selected high points. A muted blue such as `#8C9DC6` may bridge the middle values. No glow, scan lines or animation.

**Rationale:** closer to the second and fourth references' dramatic silhouette. It is compelling in dark mode but less suitable as the only profile appearance because dark fields can overwhelm otherwise restrained content.

### Selected synthesis

Use A's spacious composition in both modes for continuity, with B's independently tuned luminance hierarchy in the dark asset. Dark mode must preserve sculptural lighting rather than reversing lit and shaded planes. Both variants should read as two impressions of the same original plate. The implementation may adjust the nominal aspect ratio to keep the face recognizable at a 328px content width.

## Artwork engineering brief

1. Begin with an original, convincing sculptural image or original anatomical drawing. An AI-generated source is acceptable if its use is disclosed. Do not trace the supplied references or use an uncredited photograph. If a public-domain source is used instead, record the exact source URL, institution, work title and rights statement.
2. Convert luminance and local edges into a dense fixed-width character or engraving field. A short deterministic converter is appropriate because the mission explicitly requests procedural image-to-ASCII investigation and reproducible sources. Avoid a framework or an unnecessarily elaborate pipeline.
3. Use a coherent ASCII vocabulary such as `. : ; + x = # @` with distinct densities; choose characters from tonal information, not arbitrary decorative noise. Edge-aligned slash marks and compact stipple shapes may supplement the glyph field. Real glyphs can be stored as reusable SVG path definitions to avoid font dependence.
4. Preserve at least five useful tonal steps, including clear highlights. Render shape through density, not merely colored flat outlines. Inspect at native size and at the actual README width. A face that looks convincing only at 200% zoom fails.
5. Prefer referenced SVGs with a viewBox, explicit dimensions, a title and a concise description. Batch repeated geometry or reuse glyph definitions; avoid thousands of individually styled elements when paths or grouped rows suffice. Aim for each final SVG below 500 KB where visual quality permits; record actual size, not just this target.
6. Keep final assets self-contained: no remote fonts, scripts, external image links or filters that create fragile rendering. A raster source wrapped in SVG is not a substitute for the requested computational engraving.
7. Retain the minimum reproducible source and record the command, input provenance and tone mapping. Unused experiments need not ship.

## README hierarchy and typography

- **Identity:** actual Markdown `# Rostyslav Zhludko`, followed by `Infrastructure / Systems / Automation` and Hamburg. Place the hero close to the name, while keeping the name visible early on mobile. Use one `<picture>` with dark/light SVG sources and a normal light fallback image. Suggested alt text: “Hermes in three-quarter profile, rendered as a dense typographic engraving with a winged headpiece.” Adjust to the actual art.
- **About:** two short sentences about operating deployment infrastructure, Linux systems, applications and automation. Do not add a mythology metaphor to every section.
- **Experience:** compact prose covering Notebook-Pro, leadership, PXE/MDT and Proxmox, followed by existing practical delivery/background facts. Existing metrics can be preserved only with their existing scope; do not upgrade a registration count into active users or production reach.
- **Selected work:** four stacked entries with real linked repository names and short descriptions. A small inline monospace index is optional. No two-column image cards, logo wall or fixed-width table. State the application/infrastructure relationships and identify `k8s-neko` as a learning project.
- **Toolkit:** four compact labeled paragraphs, using the existing domains and technologies. This wraps better than a wide table at 360px.
- **Currently building:** Kityz explicitly marked “In progress”; retain the actual TypeScript/Fastify, WebSocket, MCP, isolated execution and human approval scope. Preserve the Linux server work without inventing availability claims.
- **Footer:** LinkedIn, email and repository navigation as text links, with at most one small classical rule. Languages/background may remain in semantic `<details>` if necessary.

GitHub controls body fonts and heading scale. Rely on its native readable typography; use monospace only for short labels and the artwork. Do not simulate a bespoke website through image text. Important facts must remain selectable and accessible when images are unavailable. Use native heading spacing, a small number of horizontal rules and a consistent left alignment.

## Review gates

Inspect the integrated README at desktop and approximately 360px viewport widths in light and dark modes. Verify the appropriate picture source, no horizontal overflow, a readable face silhouette, non-clipped asset boundaries, usable project links, sensible alt text and all factual distinctions. Look for moiré or visual mud when the fine marks scale down. If needed, simplify middle-tone texture while keeping the anatomical edges. Record screenshots and distinguish a local GitHub-style preview from a verified GitHub render.

No external art was researched or adopted for this specification. The visual recommendation is grounded in the five supplied references and the user's stated Hermes direction.
