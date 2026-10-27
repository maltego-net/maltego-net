"""Generate the two character-engraving plates. Requires Python + Pillow only."""
from html import escape
from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets/source/hermes.png"
COLS, ROWS = 224, 140
X, Y, W, H = 594, 12, 536, 536
RAMP = ".,:;i1tfLCG08@"


def plate(dark: bool, mobile: bool = False) -> str:
    image = Image.open(SOURCE).convert("LA").resize((COLS, ROWS), Image.Resampling.LANCZOS)
    lum, alpha = image.split()
    lum = ImageEnhance.Contrast(ImageOps.autocontrast(lum, cutoff=1)).enhance(1.20)
    bg = "#111319" if dark else "#E6E8E0"
    ink = "#E6E8E0" if dark else "#10264A"
    muted = "#8C9DC6" if dark else "#1936C8"
    colors = ["#536B9B", "#9DAFD0", "#E6E8E0"] if dark else ["#1936C8", "#1936C8", "#10264A"]
    mode = "Obsidian impression" if dark else "Marble impression"
    width, viewbox = (600, "570 0 600 560") if mobile else (1200, "0 0 1200 560")
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="560" viewBox="{viewbox}" role="img" aria-labelledby="title desc">',
           '<title id="title">Hermes — a study in characters</title>',
           f'<desc id="desc">{mode}. An original winged Hermes bust, its curls, face and shoulders built from thousands of monospaced ASCII marks.</desc>',
           f'<rect width="1200" height="560" fill="{bg}"/>']
    if not mobile:
        out += [f'<path d="M58 58H112M58 502H112" fill="none" stroke="{muted}" stroke-width="2"/>',
           f'<g fill="{muted}" font-family="Courier New,monospace" font-size="13" letter-spacing="2">',
           '<text x="58" y="88">STUDY / 01</text>',
           '<text x="58" y="478">FORM THROUGH CHARACTERS</text></g>',
           f'<text x="55" y="270" fill="{ink}" font-family="Georgia,serif" font-size="70" letter-spacing="3">Hermes</text>',
           f'<path d="M58 305H460" fill="none" stroke="{muted}" stroke-width=".6"/>']
    out += [f'<g font-family="Courier New,monospace" font-size="{W/COLS/0.6:.4f}" font-weight="700">']
    for row in range(ROWS):
        layers = [[" "] * COLS for _ in colors]
        for col in range(COLS):
            a = alpha.getpixel((col, row)) / 255
            if a < .3:
                continue
            l = lum.getpixel((col, row)) / 255
            # Light marks describe shadow; dark marks describe illuminated stone.
            # Their distinct contrast curves preserve light direction in both modes.
            density = (l ** .8) if dark else ((1 - l) ** .68)
            density *= a
            if density < .035:
                continue
            index = min(len(RAMP) - 1, int(density * len(RAMP)))
            layer = min(2, int((l if dark else 1-l) * 3))
            layers[layer][col] = RAMP[index]
        for color, chars in zip(colors, layers):
            if all(c == " " for c in chars):
                continue
            occupied = [(col, char) for col, char in enumerate(chars) if char != " "]
            positions = " ".join(f"{X + col*W/COLS:.2f}" for col, _ in occupied)
            marks = "".join(char for _, char in occupied)
            out.append(f'<text x="{positions}" y="{Y+(row+1)*H/ROWS:.3f}" fill="{color}">{escape(marks)}</text>')
    out += ["</g>", "</svg>"]
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    for mobile in (False, True):
        for dark in (False, True):
            path = ROOT / f'assets/hermes-{"dark" if dark else "light"}{"-mobile" if mobile else ""}.svg'
            path.write_text(plate(dark, mobile), encoding="utf-8", newline="\n")
            print(f"{path.relative_to(ROOT)}: {path.stat().st_size:,} bytes")
