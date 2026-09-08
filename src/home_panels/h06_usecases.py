"""Use cases. Six cards, copy carried over verbatim from the live homepage."""
ID, TITLE = "usecases", "Use cases for every data team"

HEADING = "Use cases for every data team"
LEDE = ("TopQuadrant applies governed context dynamically at query-time, surfacing the meaning "
        "and relationships that turn scattered data into decisions you can defend.")

CASES = [
    ("Ontology governance", "Manage ontologies as governed, versioned assets with owners, "
     "change control, and impact analysis."),
    ("Taxonomy management", "Concept schemes with a named owner and a change process, so six "
     "systems stop holding six versions."),
    ("Metadata management", "Every table with an agreed definition, a named steward, and a "
     "date it was last confirmed true."),
    ("Reference data", "One agreed list of codes, with every past version still answerable."),
    ("Semantic layer", "One agent-ready layer that tells your query engine what the data "
     "actually means."),
    ("AI governance", "Give agents context they can cite, and the controls to keep them "
     "inside policy."),
]


def html(ctx):
    cards = "".join(f'''
      <article class="nv-uc"><h3 class="nv-h3">{t}</h3><p>{d}</p></article>'''
      for t, d in CASES)
    return f'''
<section class="nv nv-dark nv-block nv-uc-sec" id="nv-usecases">
  <div class="nv-container">
    <div class="nv-uc-head">
      <div>
        <h2 class="nv-h2">{HEADING}</h2>
        <p class="nv-lede nv-lede-wide">{LEDE}</p>
      </div>
      <a href="#" class="nv-btn nv-btn-ghost">Explore use cases</a>
    </div>
    <div class="nv-ucgrid">{cards}</div>
  </div>
</section>'''


CSS = """
.nv-uc-sec{padding:88px 0}
.nv-uc-head{display:flex;justify-content:space-between;align-items:flex-end;gap:32px;
  flex-wrap:wrap;margin-bottom:38px}
.nv-ucgrid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));
  border-top:1px solid var(--nv-d-line);border-left:1px solid var(--nv-d-line)}
.nv-uc{padding:30px 26px;border-right:1px solid var(--nv-d-line);
  border-bottom:1px solid var(--nv-d-line);transition:background .2s ease}
.nv-uc:hover{background:rgba(255,255,255,.03)}
.nv-uc .nv-h3{margin:0 0 10px;color:#fff}
.nv-uc p{font-family:var(--nv-body);font-size:.94rem;line-height:1.55;
  color:var(--nv-d-muted);margin:0}
@media (max-width:1040px){.nv-ucgrid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:640px){.nv-ucgrid{grid-template-columns:1fr}}
"""
