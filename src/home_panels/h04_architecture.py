"""The architecture, full size, under its own heading."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from panels import arch

ID, TITLE = "architecture", "A platform that makes your context authoritative"

HEADING = "A platform that makes your context authoritative"
LEDE = ("TQ sits between your source systems and your AI: modelling, governing and serving "
        "context so every downstream answer is accurate, explainable and trusted at scale.")


def html(ctx):
    return f'''
<section class="nv nv-dark nv-block nv-archsec" id="nv-architecture">
  <div class="nv-container">
    <div class="nv-head-full">
      <h2 class="nv-h2">{HEADING}</h2>
      <p class="nv-lede nv-lede-wide">{LEDE}</p>
    </div>
    <div class="nv-archwrap">{arch.render("nv-arch-main", mode="static")}</div>
  </div>
</section>'''


CSS = """
.nv-archsec{padding:88px 0}
/* this is the full picture, not the hero silhouette: open every layer */
.nv-archwrap .nv-slot{max-height:900px;opacity:1}
.nv-archwrap .nv-layer-body{max-height:420px;opacity:1;margin-top:11px}
.nv-archwrap .nv-slot[data-slot="data"] .nv-logos{max-height:130px;opacity:1}
.nv-archwrap{margin-top:36px}
.nv-archsec .nv-head-full{margin-bottom:0}
"""
