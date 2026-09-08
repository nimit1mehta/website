"""Closing demo CTA."""
ID, TITLE = "cta", "Demo CTA"

HEADING = "Give your AI the context it's been missing"
LEDE = ("See how TopQuadrant turns your enterprise knowledge into trusted, AI-ready context.")


def html(ctx):
    return f'''
<section class="nv nv-dark nv-cta-sec" id="nv-cta">
  <div class="nv-container nv-cta-inner">
    <h2 class="nv-h2">{HEADING}</h2>
    <p class="nv-lede nv-lede-wide">{LEDE}</p>
    <div class="nv-actions"><a href="#" class="nv-btn nv-btn-primary">Get a Demo</a></div>
  </div>
</section>'''


CSS = """
.nv-cta-sec{padding:96px 0}
.nv-cta-inner{text-align:center;display:flex;flex-direction:column;align-items:center}
.nv-cta-inner .nv-lede{margin-top:16px}
.nv-cta-inner .nv-actions{justify-content:center;margin-top:28px}
"""
