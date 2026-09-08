"""Hero - dark, category headline, architecture silhouette top right."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from panels import arch

ID, TITLE = "hero", "Hero (H1 + H2 + architecture)"

H1_LEAD = "The Context Management Platform to master your"
H1_ACCENT = "Ground Truth"
H2 = ("Your ground truth is your IP. Your agents need it to earn your trust. "
      "TopQuadrant consolidates that truth so agents are safe, repeatable and "
      "decision-grade.")


def html(ctx):
    return f'''
<section class="nv nv-dark nv-hero" id="nv-hero">
  <div class="nv-container nv-hero-grid">
    <div class="nv-hero-copy">
      <span class="nv-eyebrow">TopQuadrant</span>
      <h1 class="nv-h1">{H1_LEAD} <span class="nv-accent">{H1_ACCENT}</span></h1>
      <p class="nv-hero-sub">{H2}</p>
      <div class="nv-actions">
        <a href="#" class="nv-btn nv-btn-primary">Get a Demo</a>
        <a href="#nv-architecture" class="nv-btn nv-btn-ghost">See the platform</a>
      </div>
    </div>
    <div class="nv-hero-vis" aria-hidden="true">{arch.render("nv-arch-hero", mode="static")}</div>
  </div>
</section>'''


CSS = """
/* The first screen is nav + hero + logo strip. Size the hero off the viewport so
   the logos are always above the fold instead of depending on how the headline
   happens to wrap. --nv-nav-h and --nv-logostrip-h are declared in build_home. */
.nv-hero{padding:40px 0;overflow:hidden;display:flex;align-items:center;
  min-height:calc(100svh - var(--nv-nav-h,68px) - var(--nv-logostrip-h,136px))}
.nv-hero-grid{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,1fr);
  gap:44px;align-items:center;width:100%}
.nv-hero-copy{max-width:46ch}
/* smaller than the product hero: this headline is long and must not wrap to six lines */
.nv-hero .nv-h1{font-size:clamp(1.9rem,3.1vw,3.05rem);line-height:1.08}
.nv-hero-sub{font-family:var(--nv-body);font-size:1rem;line-height:1.58;
  color:var(--nv-d-muted);margin:18px 0 0;max-width:52ch}
.nv-actions{display:flex;flex-wrap:wrap;gap:12px;margin-top:24px}
.nv-hero-vis .nv-arch{transform:scale(.86);transform-origin:center right}
@media (max-width:1040px){
  .nv-hero{min-height:0;padding:56px 0}
  .nv-hero-grid{grid-template-columns:1fr;gap:40px}
  .nv-hero-copy{max-width:none}
  .nv-hero-vis .nv-arch{transform:none}
}
"""
