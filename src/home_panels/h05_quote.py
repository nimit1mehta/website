"""Expedia customer story. Copy and attribution carried over verbatim."""
F = "./TQ Data Foundation — Power the Context Your AI Needs _ TopQuadrant_files/"
COVER = "6a7c03a5ddac10fbe108fb01_5bf6f10e9ac7dd8f15039f5a7c23babc_expedia_group_alt-1--cover.jpg"

ID, TITLE = "quote", "Expedia customer story"

QUOTE = ("We had a semantic problem. Getting governed definitions of every property, place "
         "and customer need helped us drive the uniform interpretation we needed to stay "
         "coordinated.")
NAME, ROLE, ORG = "Patrick Bradley", "Sr. Director of Engineering", "Expedia Group"
STATS = [("1", "Governed travel taxonomy across every brand"),
         ("Weeks", "To audit-ready lineage, source to model")]


def html(ctx):
    stats = "".join(f'<div class="nv-stat"><span class="nv-stat-v">{v}</span>'
                    f'<span class="nv-stat-l">{l}</span></div>' for v, l in STATS)
    return f'''
<section class="nv nv-light nv-block nv-quote-sec" id="nv-quote">
  <div class="nv-container nv-quote-plain">
    <div class="nv-quote-body">
      <span class="nv-kicker">Customer story &middot; Expedia Group</span>
      <blockquote><p>&ldquo;{QUOTE}&rdquo;</p></blockquote>
      <div class="nv-quote-who">
        <span class="nv-qname">{NAME}</span>
        <span class="nv-qrole">{ROLE} &middot; {ORG}</span>
      </div>
      <div class="nv-stats">{stats}</div>
    </div>
  </div>
</section>'''


CSS = """
.nv-quote-sec{padding:84px 0}
.nv-quote-plain{max-width:900px}
.nv-quote-body blockquote{margin:16px 0 0}
.nv-quote-plain blockquote p{font-family:var(--nv-display);font-weight:500;
  font-size:clamp(1.25rem,2.1vw,1.7rem);line-height:1.36;letter-spacing:-.012em;
  color:var(--nv-ink);margin:0;max-width:38ch}
.nv-quote-who{margin-top:22px;display:flex;flex-direction:column;gap:3px}
.nv-qname{font-family:var(--nv-body);font-size:.95rem;font-weight:600;color:var(--nv-ink)}
.nv-qrole{font-family:var(--nv-mono);font-size:10.5px;letter-spacing:.1em;
  text-transform:uppercase;color:var(--nv-muted)}
.nv-stats{display:flex;gap:44px;margin-top:30px;padding-top:24px;
  border-top:1px solid var(--nv-line);flex-wrap:wrap}
.nv-stat{display:flex;flex-direction:column;gap:6px}
.nv-stat-v{font-family:var(--nv-display);font-size:1.7rem;font-weight:700;color:var(--nv-ink)}
.nv-stat-l{font-family:var(--nv-body);font-size:.85rem;color:var(--nv-muted);max-width:26ch}

"""
