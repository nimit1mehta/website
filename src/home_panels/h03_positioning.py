"""Product positioning - three paragraphs and a CTA, impact figures alongside.

Figures are the home set (3.5x / -84% / +45%), deliberately distinct from the
product page's set. They are placeholders until measured.
"""
ID, TITLE = "positioning", "Product positioning (3 paragraphs + impact)"

HEADING = "Agents are only as good as the context they can reach"

PARAS = [
    "Point an agent at one application and it performs. Point it at the enterprise and it "
    "starts guessing — because nothing tells it what a customer is, what a contract commits "
    "you to, or which rule applies.",

    "TQ Data Foundation is where that meaning lives. Your experts model the concepts, "
    "relationships, rules and processes your business actually runs on, approve them, and "
    "govern them in one place.",

    "That context is then served to every model, agent, application and analyst through MCP, "
    "SDKs and your existing stack — so the same question returns the same defensible answer, "
    "wherever it is asked.",
]

# Read along one horizontal axis - no tiles, no per-metric copy.
METRICS = [
    dict(value="3.5&times;", label="More accurate"),
    dict(value="&minus;84%", label="Fewer tokens"),
    dict(value="+45%",       label="More secure"),
]


def html(ctx):
    paras = "".join(f"<p>{p}</p>" for p in PARAS)
    marks = "".join(f'''
        <div class="nv-mark">
          <span class="nv-mark-v">{m['value']}</span>
          <span class="nv-mark-dot" aria-hidden="true"></span>
          <span class="nv-mark-l">{m['label']}</span>
        </div>''' for m in METRICS)

    return f'''
<section class="nv nv-light nv-block nv-pos-sec" id="nv-positioning">
  <div class="nv-container nv-pos-grid">
    <div class="nv-pos-copy">
      <h2 class="nv-h2">{HEADING}</h2>
      {paras}
      <a href="./product/" class="nv-btn nv-btn-solid">Explore TQ Data Foundation</a>
    </div>
    <div class="nv-impact">
      <span class="nv-kicker">Impact</span>
      <div class="nv-axis-graphic">
        <div class="nv-axis-rule" aria-hidden="true"></div>
        <div class="nv-marks">{marks}</div>
      </div>
    </div>
  </div>
</section>'''


CSS = """
.nv-pos-sec{padding:84px 0}
.nv-pos-grid{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);
  gap:56px;align-items:center}
.nv-pos-copy p{font-family:var(--nv-body);font-size:1.02rem;line-height:1.65;
  color:var(--nv-muted);margin:18px 0 0;max-width:60ch}
.nv-pos-copy .nv-h2{margin-bottom:6px}
.nv-btn-solid{background:var(--nv-ink);color:#fff;margin-top:30px}
.nv-btn-solid:hover{background:var(--nv-accent)}

/* one horizontal axis with the three numbers on it - no tiles, no sub-copy */
.nv-impact{padding-top:6px}
.nv-axis-graphic{position:relative;margin-top:26px}
.nv-axis-rule{position:absolute;left:0;right:0;top:50%;height:1px;background:var(--nv-line)}
.nv-marks{position:relative;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));
  align-items:center}
.nv-mark{display:flex;flex-direction:column;align-items:center;gap:10px;text-align:center}
.nv-mark-v{font-family:var(--nv-display);font-size:clamp(1.5rem,2.3vw,2rem);font-weight:700;
  letter-spacing:-.02em;color:var(--nv-ink);line-height:1}
.nv-mark-dot{width:9px;height:9px;background:var(--nv-accent);border-radius:50%;
  box-shadow:0 0 0 5px var(--nv-paper)}
.nv-mark-l{font-family:var(--nv-mono);font-size:10px;font-weight:600;letter-spacing:.12em;
  text-transform:uppercase;color:var(--nv-muted)}
@media (max-width:1040px){.nv-pos-grid{grid-template-columns:1fr;gap:38px}}
"""
