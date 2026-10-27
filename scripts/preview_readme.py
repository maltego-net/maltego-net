"""Review-only preview: GitHub-rendered Markdown, GitHub-like CSS, local assets.

Requires Python Playwright and Chrome. Run from the repository root.
No dependency or remote service is used by the published README itself.
"""
import hashlib
import json
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import subprocess
from threading import Thread
import urllib.request

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "previews"
OUT.mkdir(parents=True, exist_ok=True)
cache = ROOT / ".preview-cache"
cache.mkdir(exist_ok=True)
payload = json.dumps({"text": (ROOT / "README.md").read_text(encoding="utf-8"),
                      "mode": "gfm", "context": "maltego-net/maltego-net"})
result = subprocess.run(["gh", "api", "-X", "POST", "markdown", "--input", "-"],
                        input=payload, text=True, encoding="utf-8", capture_output=True, check=True)
css_url = "https://raw.githubusercontent.com/sindresorhus/github-markdown-css/main/github-markdown.css"
css_path = cache / "github-markdown.css"
if not css_path.exists():
    css_path.write_bytes(urllib.request.urlopen(css_url, timeout=30).read())
css = css_path.read_text(encoding="utf-8")
html = '''<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Hellenic ASCII — README review</title><style>''' + css + '''
body { margin:0; background:#fff; }
.markdown-body { box-sizing:border-box; max-width:1012px; margin:32px auto; padding:32px; border:1px solid #d1d9e0; border-radius:6px; }
@media(prefers-color-scheme:dark) { body {background:#0d1117} .markdown-body {border-color:#3d444d} }
@media(max-width:767px) { .markdown-body {margin:0; padding:16px; border:0; border-radius:0} }
</style></head><body><article class="markdown-body">''' + result.stdout + '</article></body></html>'
(ROOT / "preview.html").write_text(html, encoding="utf-8")

class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass

server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(ROOT)))
Thread(target=server.serve_forever, daemon=True).start()
records = []
try:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, executable_path="C:/Program Files/Google/Chrome/Application/chrome.exe")
        for width, label in [(1440, "desktop"), (360, "mobile")]:
            for theme in ["light", "dark"]:
                page = browser.new_page(viewport={"width": width, "height": 1050}, color_scheme=theme, device_scale_factor=1)
                page.goto(f"http://127.0.0.1:{server.server_port}/preview.html", wait_until="networkidle")
                page.evaluate("document.fonts.ready")
                record = page.evaluate('''() => ({
                    viewport:innerWidth, documentWidth:document.documentElement.scrollWidth,
                    images:[...document.images].map(i=>({src:i.getAttribute('src'),selected:i.currentSrc.split('/').pop(),loaded:i.complete&&i.naturalWidth>0,alt:i.alt,width:i.width,height:i.height})),
                    headings:[...document.querySelectorAll('h1,h2,h3')].map(h=>h.textContent),
                    overflowing:[...document.querySelectorAll('.markdown-body *')].filter(e=>e.getBoundingClientRect().right>innerWidth+1).map(e=>e.tagName)
                })''')
                record.update(theme=theme, size=label)
                image = page.locator(".markdown-body img").first
                if record["images"] and record["images"][0]["selected"].endswith(".gif"):
                    first_frame = hashlib.sha256(image.screenshot()).hexdigest()
                    page.wait_for_timeout(650)
                    next_frame = hashlib.sha256(image.screenshot()).hexdigest()
                    record["animationFrameChanged"] = first_frame != next_frame
                page.screenshot(path=str(OUT / f"{label}-{theme}.png"), full_page=True)
                page.locator("details").evaluate_all("items => items.forEach(e => e.open = true)")
                record["expandedDetailsOverflow"] = page.evaluate("document.documentElement.scrollWidth > innerWidth")
                records.append(record)
                page.close()
                still = browser.new_page(viewport={"width": width, "height": 1050}, color_scheme=theme,
                                         reduced_motion="reduce", device_scale_factor=1)
                still.goto(f"http://127.0.0.1:{server.server_port}/preview.html", wait_until="networkidle")
                still_record = still.evaluate('''() => ({
                    viewport:innerWidth, documentWidth:document.documentElement.scrollWidth,
                    images:[...document.images].map(i=>({selected:i.currentSrc.split('/').pop(),loaded:i.complete&&i.naturalWidth>0})),
                    overflowing:[...document.querySelectorAll('.markdown-body *')].filter(e=>e.getBoundingClientRect().right>innerWidth+1).map(e=>e.tagName)
                })''')
                still_record.update(theme=theme, size=label, reducedMotion=True)
                records.append(still_record)
                still.close()
        browser.close()
finally:
    server.shutdown()
report = {"rendering":"GitHub Markdown API; local github-markdown-css approximation, not live GitHub UI",
          "css_source":css_url, "css_sha256":hashlib.sha256(css.encode()).hexdigest(), "checks":records}
(OUT / "validation.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
print(json.dumps(report, indent=2))
assert all(r["documentWidth"] == r["viewport"] and not r["overflowing"] for r in records), "Horizontal overflow"
assert all(i["loaded"] for r in records for i in r["images"]), "Broken asset"
assert all(r["theme"] in r["images"][0]["selected"] for r in records), "Incorrect theme source"
assert all(("mobile" in r["images"][0]["selected"]) == (r["size"] == "mobile") for r in records), "Incorrect responsive source"
assert not any(r["expandedDetailsOverflow"] for r in records if not r.get("reducedMotion")), "Expanded details overflow"
assert all(r["animationFrameChanged"] for r in records if not r.get("reducedMotion")), "Animated GIF did not change frames"
assert all(r["images"][0]["selected"].endswith(".svg") for r in records if r.get("reducedMotion")), "Reduced motion did not select static SVG"
