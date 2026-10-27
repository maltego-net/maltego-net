# Independent README review

Reviewer: `content_review`, who audited content but did not implement the README, artwork, generator, or preview tooling. Review date: 2026-10-27. This is the review phase of the existing content task, not a separate agent task.

## Evidence and scope

- Compared the implemented README with the baseline README and `docs/content-audit.md`.
- Read `docs/artwork.md`, `scripts/generate-hermes.py`, `scripts/preview_readme.py`, and the generated HTML.
- Parsed both final SVG files with Python's XML parser; examined their element types and asset references.
- Examined desktop/light and mobile/dark initial screenshots directly. Corrected four-theme/width screenshots are pending final visual review.
- Read the preview measurement JSON. It describes GitHub Markdown API output rendered locally with `github-markdown-css`, not a screenshot of the live GitHub profile.

## Defects and correction pass

1. **Blocking visual defect, initially found by lead and independently confirmed:** SVG character layers collapsed whitespace and stretched each row into a rectangle. The hero had no recognizable face or silhouette. The developer changed the converter to explicit per-character x positions, removing whitespace-dependent positioning and `textLength`. Final visual confirmation is pending.
2. **Blocking content defect, found independently here:** the README contained UTF-8 mojibake: 29 U+00C2 characters and two U+00E2 characters corrupted separators and dash punctuation. Python `ascii()` exposed the actual decoded characters, ruling out a console-only display issue. The developer repaired the file with explicit UTF-8 handling. Recheck found zero of either corruption marker, and the team range is correctly U+2013. Preview generation must use this corrected source.

## Checks passed

- All four existing repository targets, LinkedIn, email, and repository navigation links are preserved. Each project repository was independently checked with successful `gh repo view` during the audit.
- Original facts and scope distinctions are preserved: team of 3–4; co-built deployment platform; 10,800+ wallet registrations; Kubernetes learning project; Kityz in progress; original client/startup delivery, server operations, studies, and languages. No new employment, degree, product-launch, or production-deployment claims were introduced.
- Every original toolkit technology remains in actual text. The added Kubernetes learning qualifier is supported by the original project description and brief.
- Identity, headings, descriptions, and links are selectable Markdown/HTML text. Artwork is not the sole source of professional information.
- The picture has light and dark SVG sources and a light fallback; its image has meaningful alt text. SVGs have title/description metadata.
- Both SVGs parse as XML. Their element set is limited to `svg`, `title`, `desc`, `rect`, `path`, `g`, and `text`; no scripts, external image links, fonts, animation, or embedded raster appear.
- All three README `src`/`srcset` paths exist. The source PNG hash matches the provenance record: `6060bdef8dfe703eff34d4e2615374a7faedf66e02b7c2ae0474533535e977c4`.
- The first local measurements reported correct image source selection and successful loads for both themes at 1440 px and 360 px, with no horizontal overflow. These mechanical checks did **not** catch the initial visual defect, which required image inspection.

## Remaining validation

Final visual verdict is pending corrected screenshots and updated measurements. Do not treat the earlier screenshot files as accepted evidence.

## Limits

The review does not establish exact live GitHub appearance, browser-wide glyph consistency, LinkedIn availability, or mailbox deliverability. Courier fallback glyph shapes may differ by system. The preview script currently uses a Windows Chrome installation path and requires development-only Python Playwright and GitHub CLI; these are not README runtime dependencies.
