"""FAQ. Questions and answers carried over verbatim from the live homepage."""
ID, TITLE = "faq", "Questions, answered"

HEADING = "Questions, answered"
LEDE = "What teams ask when they stop guessing and start governing."

QA = [
    ("What is a knowledge graph?",
     "A machine-readable model of the things your business runs on and the relationships "
     "between them, with meaning attached, so software can reason over your data instead of "
     "just retrieving it."),
    ("How does TopQuadrant make data AI-ready?",
     "It connects your structured and unstructured sources, standardises terms against your "
     "taxonomies and glossaries, and models the meaning your agents need. Your experts "
     "approve it, which is what makes it authoritative."),
    ("What types of data can you connect and govern?",
     "Structured data, unstructured content like documents and notes, business glossaries, "
     "taxonomies, ontologies, metadata and policies, in one governed place."),
    ("Who typically uses TopQuadrant?",
     "Enterprise architects, knowledge engineers and data platform leads build on it. The "
     "CDO, CTO or AI leader who owns the outcome sponsors it."),
    ("How quickly can we get started?",
     "Most organisations are connecting, governing and serving their first context within "
     "weeks, starting from one use case rather than a platform rollout."),
]


def html(ctx):
    items = "".join(f'''
      <details class="nv-faq"{' open' if i == 0 else ''}>
        <summary><span>{q}</span><span class="nv-faq-mark" aria-hidden="true"></span></summary>
        <p>{a}</p>
      </details>''' for i, (q, a) in enumerate(QA))
    return f'''
<section class="nv nv-light nv-block nv-faq-sec" id="nv-faq">
  <div class="nv-container nv-faq-grid">
    <div class="nv-faq-intro">
      <h2 class="nv-h2">{HEADING}</h2>
      <p class="nv-lede">{LEDE}</p>
    </div>
    <div class="nv-faq-list">{items}</div>
  </div>
</section>'''


CSS = """
.nv-faq-sec{padding:84px 0}
.nv-faq-grid{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);gap:56px;
  align-items:start}
.nv-faq{border-bottom:1px solid var(--nv-line)}
.nv-faq summary{display:flex;justify-content:space-between;align-items:center;gap:20px;
  padding:20px 0;cursor:pointer;list-style:none;
  font-family:var(--nv-display);font-size:1.05rem;font-weight:600;color:var(--nv-ink)}
.nv-faq summary::-webkit-details-marker{display:none}
.nv-faq-mark{position:relative;width:12px;height:12px;flex:none}
.nv-faq-mark::before,.nv-faq-mark::after{content:"";position:absolute;background:var(--nv-accent);
  transition:transform .25s ease}
.nv-faq-mark::before{top:5px;left:0;width:12px;height:1.5px}
.nv-faq-mark::after{top:0;left:5px;width:1.5px;height:12px}
.nv-faq[open] .nv-faq-mark::after{transform:scaleY(0)}
.nv-faq p{font-family:var(--nv-body);font-size:.97rem;line-height:1.62;color:var(--nv-muted);
  margin:0 0 22px;max-width:62ch}
@media (max-width:1040px){.nv-faq-grid{grid-template-columns:1fr;gap:28px}}
"""
