"""From the blog. Three posts, titles and blurbs carried over verbatim."""
ID, TITLE = "blog", "From the blog"

HEADING = "From the blog"

POSTS = [
    dict(tag="AI & context", date="June 30, 2026", read="6 min read",
         title="Do You Already Have a Context Layer? You May Be Closer Than You Think",
         blurb="AI fails when it doesn't know your business. Most organizations already have "
               "the context they need — it just isn't linked, governed, or reusable yet."),
    dict(tag="AI & context", date="April 9, 2026", read="",
         title="All Data Is Referential. Here's Why That Changes Everything.",
         blurb="Enterprises spend millions on master data management, data catalogs and AI "
               "infrastructure — and still can't get their systems to agree on what the data "
               "means. The missing piece is a governed reference data layer."),
    dict(tag="AI & context", date="March 17, 2026", read="8 min read",
         title="Gartner D&A Declares Context is King: Context Layers as the New Critical "
               "Infrastructure for AI",
         blurb="At the Gartner Data & Analytics Summit, context was named critical "
               "infrastructure for AI. Here is what that shift means for enterprise data "
               "leaders."),
]


def html(ctx):
    cards = "".join(f'''
      <article class="nv-post">
        <span class="nv-post-tag">{p['tag']}</span>
        <h3 class="nv-h3">{p['title']}</h3>
        <p>{p['blurb']}</p>
        <span class="nv-post-meta">{p['date']}{' &middot; ' + p['read'] if p['read'] else ''}</span>
      </article>''' for p in POSTS)
    return f'''
<section class="nv nv-light nv-block nv-blog-sec" id="nv-blog">
  <div class="nv-container">
    <div class="nv-uc-head">
      <h2 class="nv-h2">{HEADING}</h2>
      <a href="#" class="nv-btn nv-btn-outline">Read the blog</a>
    </div>
    <div class="nv-postgrid">{cards}</div>
  </div>
</section>'''


CSS = """
.nv-blog-sec{padding:84px 0}
.nv-btn-outline{border-color:var(--nv-line);color:var(--nv-ink)}
.nv-btn-outline:hover{border-color:var(--nv-accent);color:var(--nv-accent)}
.nv-postgrid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px}
.nv-post{border:1px solid var(--nv-line);background:#fff;padding:26px;
  display:flex;flex-direction:column;transition:border-color .2s ease}
.nv-post:hover{border-color:#d9d4c8}
.nv-post-tag{font-family:var(--nv-mono);font-size:9.5px;font-weight:600;letter-spacing:.12em;
  text-transform:uppercase;color:var(--nv-accent)}
.nv-post .nv-h3{margin:12px 0 10px;font-size:1.08rem;line-height:1.3}
.nv-post p{font-family:var(--nv-body);font-size:.9rem;line-height:1.55;
  color:var(--nv-muted);margin:0 0 18px}
.nv-post-meta{margin-top:auto;font-family:var(--nv-mono);font-size:10px;letter-spacing:.08em;
  text-transform:uppercase;color:var(--nv-muted)}
@media (max-width:1040px){.nv-postgrid{grid-template-columns:1fr}}
"""
