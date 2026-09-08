#!/usr/bin/env python3
"""
Assemble the TopQuadrant homepage mockup - a standalone side page for design handoff.

    python3 build_home.py                      -> home_restructured.html
    python3 inline_build.py home_restructured.html home-v2.html

This shares no markup with the live Webflow site and cannot affect it. Copy is
carried over verbatim from the live homepage; styling is the same nv design
system used for the product page (panels/base.py, panels/arch.py).

Reorder the page by reordering MANIFEST. Edit one section by editing only its
module in home_panels/.
"""
import importlib
import sys

from panels import base, arch

MANIFEST = [
    "h01_hero",          # H1/H2 + architecture silhouette
    "h02_logos",         # customer logos, high, no story cards
    "h03_positioning",   # 3 paragraphs + CTA, impact figures right
    "h04_architecture",  # "makes your context authoritative" + full architecture
    "h05_quote",         # Expedia customer story
    "h06_usecases",      # six use cases
    "h07_blog",          # three posts
    "h08_faq",           # five questions
    "h09_cta",           # demo CTA
]

# Live homepage sections deliberately not carried over.
RETIRED = [
    "Agents are more than copilots",
    "Why is AI failing? It's missing your context  (the scrolly)",
    "Not all context is built the same",
    "A platform behind accurate, repeatable, cheaper AI",
    "The only data foundation built entirely on knowledge graphs",
    "From raw data to agent-ready context, in five connected steps",
]

OUT = "home_restructured.html"

# The Google Fonts stylesheet is referenced through the saved-page path purely so
# inline_build.py swaps it for embedded woff2. Nothing else from Webflow is used.
FONTS = ('<link rel="stylesheet" media="all" href="./TQ Data Foundation '
         '&mdash; Power the Context Your AI Needs _ TopQuadrant_files/css">')
FONTS = FONTS.replace("&mdash;", "—")

NAV = """
<header class="nv nv-dark nv-nav">
  <div class="nv-container nv-nav-inner">
    <span class="nv-brand">TopQuadrant</span>
    <nav class="nv-navlinks">
      <a href="./product/">Product</a>
      <a href="#nv-usecases">Use cases</a>
      <a href="#nv-quote">Customers</a>
      <a href="#nv-blog">Resources</a>
      <a href="#nv-faq">FAQ</a>
    </nav>
    <a href="#nv-cta" class="nv-btn nv-btn-primary nv-nav-cta">Get a Demo</a>
  </div>
</header>"""

FOOTER = """
<footer class="nv nv-dark nv-foot">
  <div class="nv-container nv-foot-inner">
    <span class="nv-brand">TopQuadrant</span>
    <p>Operationalizing complex data into AI-ready data foundations for the world's
      leading enterprises.</p>
    <span class="nv-foot-meta">&copy; 2026 TopQuadrant, Inc. &middot; Raleigh, NC
      &middot; Homepage concept &mdash; not the live site</span>
  </div>
</footer>"""

SHELL_CSS = """
:root{--nv-nav-h:68px;--nv-logostrip-h:136px}
html,body{margin:0;padding:0;background:#fdfcf9}
.nv-nav{position:sticky;top:0;z-index:50;border-bottom:1px solid rgba(255,255,255,.1)}
.nv-nav-inner{display:flex;align-items:center;gap:32px;height:var(--nv-nav-h,68px)}
.nv-brand{font-family:var(--nv-display);font-weight:700;font-size:1.05rem;color:#fff;
  letter-spacing:-.01em}
.nv-navlinks{display:flex;gap:26px;margin-left:auto}
.nv-navlinks a{font-family:var(--nv-body);font-size:.92rem;color:var(--nv-d-muted);
  text-decoration:none;transition:color .18s ease}
.nv-navlinks a:hover{color:#fff}
.nv-nav-cta{padding:10px 18px;font-size:.88rem}
.nv-foot{padding:56px 0;border-top:1px solid rgba(255,255,255,.1)}
.nv-foot-inner{display:flex;flex-direction:column;gap:12px}
.nv-foot p{font-family:var(--nv-body);font-size:.94rem;color:var(--nv-d-muted);margin:0;
  max-width:52ch}
.nv-foot-meta{font-family:var(--nv-mono);font-size:10px;letter-spacing:.09em;
  text-transform:uppercase;color:var(--nv-d-muted)}
@media (max-width:900px){.nv-navlinks{display:none}}
"""


def main():
    panels = [importlib.import_module("home_panels." + n) for n in MANIFEST]

    ctx = {"note": lambda *a: None, "icon": lambda *a: ""}

    body, css, js = [], [base.CSS, arch.CSS, SHELL_CSS], [base.JS]
    for p in panels:
        body.append(f"\n<!-- ===== panel: {p.ID} - {p.TITLE} ===== -->")
        body.append(p.html(ctx))
        if getattr(p, "CSS", None):
            css.append(f"/* ---- {p.ID} ---- */\n{p.CSS}")
        if getattr(p, "JS", None):
            js.append(f"/* ---- {p.ID} ---- */\n{p.JS}")

    page = f"""<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>TopQuadrant &mdash; homepage concept</title>
<meta name="robots" content="noindex,nofollow,noarchive">
{FONTS}
<style>:root{{color-scheme:light}}</style>
</head>
<body>
{NAV}
{''.join(body)}
{FOOTER}
<style id="nv-styles">{''.join(css)}</style>
<script id="nv-behaviour">{''.join(js)}</script>
</body>
</html>"""

    open(OUT, "w", encoding="utf-8").write(page)

    print(f"\n  {len(panels)} panels assembled -> {OUT}  ({len(page)/1024:.0f} KB)\n")
    for i, p in enumerate(panels, 1):
        print(f"   {i}. {p.TITLE}")
    print("\n  not carried over from the live homepage:")
    for r in RETIRED:
        print("      -", r)
    print()
    for p in panels:
        n = page.count(f"panel: {p.ID} ")
        print(f"      {'ok' if n == 1 else '!! ' + str(n):5s} {p.ID}")


if __name__ == "__main__":
    main()
