"""Customer logo wall, high on the page. Story cards deliberately not included."""
F = "./TQ Data Foundation — Power the Context Your AI Needs _ TopQuadrant_files/"

ID, TITLE = "logos", "Customer logos (above the fold)"

HEADING = "Trusted by organizations who can't afford to get it wrong"

LOGOS = [
    ("Thomson Reuters",      "6a740fee4b76f158a11f12d1_thomson-reuters.svg"),
    ("Salesforce",           "6a740ffaf0ddc643dc9fff3a_salesforce.svg"),
    ("Bristol Myers Squibb", "6a740fd7c6abf33d9d06c32b_bristol-myers-squibb.svg"),
    ("Google",               "6a740ff4856d6637d893198a_google.svg"),
    ("Spotify",              "6a740ff1b8c91cb4acf0d006_spotify.svg"),
    ("Johnson & Johnson",    "6a740fda8e417cf7525e2f61_johnson-and-johnson.svg"),
    ("Adobe",                "6a740ff700918759f9dcb84a_adobe.svg"),
    ("Novo Nordisk",         "6a740fe0b8c91cb4acf0c1e7_novo-nordisk.svg"),
    ("Mayo Clinic",          "6a740fe485d0e1ece0c58425_mayo-clinic.svg"),
    ("Bayer",                "6a740fdcf0ddc643dc9fe40b_bayer.svg"),
]


def html(ctx):
    cells = "".join(
        f'<span class="nv-logocell"><img src="{F}{f}" alt="{n}" loading="lazy"></span>'
        for n, f in LOGOS)
    return f'''
<section class="nv nv-light nv-logos-sec" id="nv-logos">
  <div class="nv-container">
    <p class="nv-logos-head">{HEADING}</p>
    <div class="nv-logowall">{cells}</div>
  </div>
</section>'''


CSS = """
/* fixed strip height so the hero above can subtract it from the viewport */
.nv-logos-sec{height:var(--nv-logostrip-h,136px);display:flex;align-items:center;
  border-bottom:1px solid var(--nv-line)}
.nv-logos-sec > .nv-container{width:100%}
.nv-logos-head{font-family:var(--nv-mono);font-size:10.5px;font-weight:600;
  letter-spacing:.13em;text-transform:uppercase;color:var(--nv-muted);
  margin:0 0 18px;text-align:center}
.nv-logowall{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));
  gap:0 24px;align-items:center}
.nv-logocell{display:grid;place-items:center;height:34px}
.nv-logocell img{max-height:26px;max-width:100%;width:auto;object-fit:contain;
  filter:grayscale(1);opacity:.62;transition:filter .2s ease,opacity .2s ease}
.nv-logocell:hover img{filter:none;opacity:1}
@media (max-width:900px){
  .nv-logos-sec{height:auto;padding:36px 0}
  .nv-logowall{grid-template-columns:repeat(3,minmax(0,1fr));gap:22px}}
@media (max-width:560px){.nv-logowall{grid-template-columns:repeat(2,minmax(0,1fr))}}
"""
