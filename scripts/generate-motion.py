"""Render restrained feather-engraving loops as GitHub-compatible animated GIFs.

Requirements: Python Playwright, local Chrome, and ffmpeg. No runtime services.
The static SVG plates remain the reduced-motion and fallback versions.
"""
from pathlib import Path
import subprocess

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
TMP = ROOT / ".preview-cache" / "motion"
TMP.mkdir(parents=True, exist_ok=True)
FRAMES = 16

# Three restrained engraved strokes follow feather shafts on the cap's wing.
# Their ink is drawn and released once per loop; the sculpture itself stays still.
PATHS = (
    "M 741 105 C 731 82 716 57 691 39",
    "M 754 108 C 746 81 742 51 726 27",
    "M 767 111 C 763 84 766 60 757 40",
)


def overlay(t: float, color: str) -> str:
    # Open on a still plate, ink each feather in sequence, then let it settle.
    reveal = max(0.0, min(1.0, (t - 0.10) / 0.44))
    settle = max(0.0, min(1.0, (0.98 - t) / 0.25))
    alpha = 0.58 * min(reveal, settle)
    lines = []
    for idx, path in enumerate(PATHS):
        amount = max(0.0, min(1.0, (t - idx * 0.09) / 0.43))
        dash = max(0.01, 54 * amount)
        dashoffset = 54 * (1 - amount)
        lines.append(f'<path d="{path}" fill="none" stroke="{color}" stroke-width="1.7" '
                     f'stroke-linecap="round" stroke-dasharray="{dash:.2f} 90" '
                     f'stroke-dashoffset="{dashoffset:.2f}" opacity="{alpha:.3f}"/>')
    return '<g aria-hidden="true">' + "".join(lines) + "</g>"


def main() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, executable_path="C:/Program Files/Google/Chrome/Application/chrome.exe")
        for theme in ("light", "dark"):
            color = "#1936C8" if theme == "light" else "#E6E8E0"
            for mobile in (False, True):
                suffix = "-mobile" if mobile else ""
                stem = f"hermes-{theme}{suffix}"
                svg = (ROOT / "assets" / f"{stem}.svg").read_text(encoding="utf-8")
                width = 600 if mobile else 1200
                page = browser.new_page(viewport={"width": width, "height": 560}, device_scale_factor=1)
                for frame in range(FRAMES):
                    t = frame / (FRAMES - 1)
                    rendered = svg.replace("</svg>", overlay(t, color) + "</svg>")
                    page.set_content('<!doctype html><html><body style="margin:0">' + rendered + '</body></html>')
                    path = TMP / stem
                    path.mkdir(exist_ok=True)
                    page.screenshot(path=str(path / f"frame-{frame:02}.png"), animations="disabled")
                page.close()
                output = ROOT / "assets" / f"{stem}.gif"
                command = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-framerate", "10",
                           "-i", str(path / "frame-%02d.png"), "-filter_complex",
                           "[0:v]split[s0][s1];[s0]palettegen=max_colors=128[p];[s1][p]paletteuse=dither=none",
                           "-loop", "0", str(output)]
                subprocess.run(command, check=True)
                print(f"{output.relative_to(ROOT)}: {output.stat().st_size:,} bytes")
        browser.close()


if __name__ == "__main__":
    main()
