#!/usr/bin/env python3
"""Build the static demo site for The Plastering and Rendering Group.

Usage (from the repo root):  python3 src/build.py
Writes every .html page to the repo root. Shared styles and scripts live in
assets/site.css and assets/site.js; page content lives in src/content.py.
"""
import html
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import (GROUPS, SERVICES, TESTIMONIALS, ENQUIRY_TYPES, JOBS, HOME_JOBS,  # noqa: E402
                     INSTAGRAM_TILES, COST_A, GUARANTEE, PHONE, WHATSAPP, EMAIL)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_NAME = "The Plastering and Rendering Group"

try:
    from PIL import Image
except ImportError:  # sizes are a nicety, not a requirement
    Image = None
_sizes = {}


def e(s):
    return html.escape(str(s), quote=True)


def img_size(name):
    if Image is None:
        return ""
    if name not in _sizes:
        try:
            with Image.open(os.path.join(ROOT, "assets", name)) as im:
                _sizes[name] = ' width="%d" height="%d"' % im.size
        except OSError:
            _sizes[name] = ""
    return _sizes[name]


def img(name, alt, cls="", lazy=True):
    c = f' class="{cls}"' if cls else ""
    lz = ' loading="lazy" decoding="async"' if lazy else ""
    return f'<img{c} src="assets/{name}" alt="{e(alt)}"{img_size(name)}{lz}>'


def group_of(slug):
    for g in GROUPS:
        if slug in g["services"]:
            return g
    raise KeyError(slug)


def menu_name(slug):
    s = SERVICES[slug]
    return s.get("menu", s["name"])


# ---------------------------------------------------------------- icons
ICON_CHEV = '<svg class="chev" aria-hidden="true" width="12" height="8" viewBox="0 0 12 8" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M1 1.5l5 5 5-5"></path></svg>'
ICON_MENU = '<svg aria-hidden="true" width="18" height="14" viewBox="0 0 18 14" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M0 1h18M0 7h18M0 13h18"></path></svg>'
ICON_PHONE = '<svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"></path></svg>'
ICON_CHAT = '<svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20l1.4-4.2A8 8 0 1 1 8.3 18.7z"></path></svg>'
ICON_LEFT = '<svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M15 5l-7 7 7 7"></path></svg>'
ICON_RIGHT = '<svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M9 5l7 7-7 7"></path></svg>'
ICON_DRAG = '<svg aria-hidden="true" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 6l-6 6 6 6M15 6l6 6-6 6"></path></svg>'
ARROW = '<span aria-hidden="true">&rarr;</span>'


# ---------------------------------------------------------------- shared parts
class Ctx:
    def __init__(self, fname, current=None, svc=None):
        self.fname = fname
        self.current = current
        self.svc = svc

    @property
    def is_home(self):
        return self.fname == "index.html"

    def home(self, anchor=None):
        if anchor is None:
            return "./"
        return f"#{anchor}" if self.is_home else f"index.html#{anchor}"

    def cur(self, key):
        return ' aria-current="page"' if self.current == key else ""


def topbar():
    return f'''<div class="topbar">
<div class="wrap topbar-row">
<span class="tb-long">Plastering, rendering and decorative finishes in Cheshire</span><span class="tb-short">Plastering &middot; Rendering &middot; Decorative finishes</span>
<div class="top-extra">
<a href="#contact">{e(PHONE)}</a>
<a href="#contact">{e(EMAIL)}</a>
</div>
</div>
</div>'''


def service_links(ctx, cls=""):
    out = []
    for g in GROUPS:
        items = []
        for s in g["services"]:
            cur = ' aria-current="page"' if s == ctx.svc else ""
            items.append(f'<li><a href="{s}.html"{cur}><span>{e(menu_name(s))}</span>{ARROW}</a></li>')
        out.append((g, "\n".join(items)))
    return out


def header(ctx):
    mega_cols = "\n".join(
        f'<div class="mega-col">\n<p class="mega-title">{e(g["name"])}</p>\n<ul>\n{items}\n</ul>\n</div>'
        for g, items in service_links(ctx))
    m_groups = "\n".join(
        f'<p class="mnav-group">{e(g["name"])}</p>\n<ul>\n{items}\n</ul>'
        for g, items in service_links(ctx))
    svc_cls = ' is-current' if ctx.current == "services" else ""
    return f'''<header class="site-header">
<div class="wrap header-row">
<a class="logo" href="./" aria-label="{SITE_NAME}, home"><img src="assets/logo-ink.png" alt="{SITE_NAME}"{img_size("logo-ink.png")}></a>
<nav class="nav" aria-label="Main">
<div class="nav-item" data-mega-wrap>
<button class="nav-btn{svc_cls}" type="button" aria-expanded="false" aria-controls="mega" data-mega-btn>Services {ICON_CHEV}</button>
<div class="mega" id="mega" hidden>
<div class="wrap">
<div class="mega-grid">
{mega_cols}
</div>
<div class="mega-foot"><span>Not sure which service you need?</span><a href="#contact">Get a free quote {ARROW}</a></div>
</div>
</div>
</div>
<a href="jobs.html"{ctx.cur("jobs")}>Jobs we&rsquo;re proud of</a>
<a href="reviews.html"{ctx.cur("reviews")}>Reviews</a>
<a href="{ctx.home("about")}">About</a>
</nav>
<div class="header-actions">
<a class="btn btn-ink btn-sm head-cta" href="#contact">Get a free quote</a>
<button class="menu-btn" type="button" aria-expanded="false" aria-controls="mnav" data-menu-btn>{ICON_MENU}<span class="menu-label">Menu</span></button>
</div>
</div>
<nav class="mnav" id="mnav" aria-label="Mobile" hidden>
<div class="wrap">
<button class="mnav-acc" type="button" aria-expanded="false" aria-controls="mnav-services" data-acc>Services {ICON_CHEV}</button>
<div class="mnav-services" id="mnav-services" hidden>
{m_groups}
</div>
<a href="jobs.html"{ctx.cur("jobs")}>Jobs we&rsquo;re proud of</a>
<a href="reviews.html"{ctx.cur("reviews")}>Reviews</a>
<a href="{ctx.home("about")}">About</a>
<a href="#contact">Get a free quote</a>
</div>
</nav>
</header>'''


def footer(ctx):
    groups = "\n".join(f'<a href="{ctx.home("services")}">{e(g["name"])}</a>' for g in GROUPS)
    return f'''<footer class="site-footer">
<div class="wrap">
<div class="foot-grid">
<div class="foot-brand">
<img src="assets/logo-light.png" alt="{SITE_NAME}"{img_size("logo-light.png")} loading="lazy">
<span class="gold-rule" aria-hidden="true"></span>
</div>
<div class="foot-col">
<p class="foot-title">Services</p>
{groups}
</div>
<div class="foot-col">
<p class="foot-title">Explore</p>
<a href="jobs.html">Jobs we&rsquo;re proud of</a>
<a href="reviews.html">Reviews</a>
<a href="{ctx.home("about")}">About</a>
<a href="#contact">Contact</a>
</div>
<div class="foot-col">
<p class="foot-title">Find us online</p>
<span>theplasteringandrenderinggroup.co.uk</span>
<span>plastererscheshire.co.uk</span>
<span>rendererscheshire.co.uk</span>
<span>[INSTAGRAM AND SOCIAL LINKS]</span>
</div>
<div class="foot-col">
<p class="foot-title">Company</p>
<span>The Plastering and Rendering Group Ltd</span>
<span>Company no. 17507346</span>
<span>Registered address: 4 Henbury Gardens, Appleton, WA4 5GH</span>
<span>Health &amp; safety: [ACCREDITATION, ONCE CONFIRMED]</span>
</div>
</div>
<div class="foot-base">
<span>&copy; 2026 The Plastering and Rendering Group Ltd</span>
<span>Plastering &middot; Rendering &middot; Decorative finishes</span>
</div>
</div>
</footer>'''


def mobile_bar():
    return '''<div class="mobile-bar">
<a href="#contact">Call</a>
<a href="#contact">WhatsApp</a>
<a class="mb-quote" href="#contact">Free quote</a>
</div>'''


def quote_section(ctx):
    opts = ['<option value="" disabled selected>Choose one</option>'] + [
        f'<option>{e(t)}</option>' for t in ENQUIRY_TYPES]
    svc_opts = [f'<option value=""{"" if ctx.svc else " selected"} disabled>Choose a service</option>']
    for g in GROUPS:
        inner = "".join(
            f'<option value="{s}"{" selected" if s == ctx.svc else ""}>{e(menu_name(s))}</option>'
            for s in g["services"])
        svc_opts.append(f'<optgroup label="{e(g["name"])}">{inner}</optgroup>')
    svc_opts.append('<option value="not-sure">Not sure yet</option>')
    rows = [("Phone", PHONE), ("WhatsApp", WHATSAPP), ("Email", EMAIL),
            ("Rav", "[RAV'S EMAIL]")]
    contact = "\n".join(
        f'<a href="#contact"><span class="k">{e(k)}</span><span class="v">{e(v)}</span></a>' for k, v in rows)
    return f'''<section class="section bg-dark" id="contact">
<div class="wrap quote-grid">
<div class="quote-copy">
<span class="gold-rule" aria-hidden="true"></span>
<h2 class="h2 h2-xl">Get a free quote</h2>
<p class="lead-dark">Tell us about the job and we will come back to you to arrange a site visit. Photos and drawings help if you have them.</p>
<div class="contact-list">
{contact}
</div>
</div>
<form class="quote-form" data-quote-form novalidate>
<div class="form-row">
<div class="field"><label for="q-name">Name</label><input id="q-name" type="text" autocomplete="name"></div>
<div class="field"><label for="q-phone">Phone</label><input id="q-phone" type="tel" autocomplete="tel"></div>
</div>
<div class="form-row">
<div class="field"><label for="q-email">Email</label><input id="q-email" type="email" autocomplete="email"></div>
<div class="field"><label for="q-postcode">Postcode</label><input id="q-postcode" type="text" autocomplete="postal-code"></div>
</div>
<div class="form-row">
<div class="field"><label for="q-type">Type of enquiry</label><select id="q-type">{"".join(opts)}</select></div>
<div class="field"><label for="q-service">Service</label><select id="q-service">{"".join(svc_opts)}</select></div>
</div>
<div class="field"><label for="q-msg">About the job</label><textarea id="q-msg" rows="4"></textarea></div>
<button class="btn btn-ink" type="submit">Request my free quote</button>
<p class="form-status" role="status" hidden>This is a preview, so nothing was sent. On the live site this form goes to {e(EMAIL)}.</p>
</form>
</div>
</section>'''


def page(ctx, title, desc, main):
    return f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="icon" href="assets/favicon.png" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&amp;family=Montserrat:wght@400;500;600&amp;display=swap">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{topbar()}
{header(ctx)}
<main id="main">
{main}
{quote_section(ctx)}
</main>
{footer(ctx)}
{mobile_bar()}
<script src="assets/site.js" defer></script>
</body>
</html>
'''


def car(inner, cls, cid=None):
    i = f' id="{cid}"' if cid else ""
    return f'<div class="car-wrap">\n<div class="{cls} carousel"{i}>\n{inner}\n</div>\n</div>'


def ba(job, live):
    svc = SERVICES[job["service"]]
    name = svc["name"]
    knob = f'<span class="ba-knob">{ICON_DRAG}</span>' if live else ""
    rng = (f'<input class="ba-range" type="range" min="0" max="100" value="50" '
           f'aria-label="Before and after, {e(name)}. Use the arrow keys to compare.">') if live else ""
    cls = "ba ba-live" if live else "ba"
    data = " data-ba" if live else ""
    return f'''<div class="{cls}"{data}>
{img(job["after"], f"After: {name} (placeholder image)")}
<div class="ba-before">{img(job["before"], f"Before: {name} (placeholder image)")}</div>
<span class="ba-tag ba-tag-before">Before</span><span class="ba-tag ba-tag-after">After</span>
<span class="ba-line" aria-hidden="true">{knob}</span>
<span class="tag">Placeholder images</span>
{rng}
</div>'''


def job_meta(job, tag="h3"):
    svc = SERVICES[job["service"]]
    return (f'<div class="job-meta"><span class="eyebrow">{e(svc["name"])} &middot; [TOWN]</span>'
            f'<{tag} class="job-title">[JOB NAME]</{tag}></div>')


def review_card(name, role, compact=False):
    role_html = f'<span class="role">{e(role)}</span>' if role else ""
    return f'''<figure class="review">
<span class="qmark" aria-hidden="true">&ldquo;</span>
<blockquote>[TESTIMONIAL TEXT TO BE ADDED]</blockquote>
<figcaption><span class="who">{e(name)}</span>{role_html}</figcaption>
</figure>'''


# ---------------------------------------------------------------- home
def home_page():
    ctx = Ctx("index.html")
    cards = []
    for g in GROUPS:
        links = "\n".join(
            f'<li><a href="{s}.html"><span>{e(menu_name(s))}</span>{ARROW}</a></li>' for s in g["services"])
        cards.append(f'''<article class="svc-card">
<div class="media">{img(g["image"], f"Placeholder image for {g['name'].lower()}")}<span class="tag">Placeholder image</span></div>
<div class="svc-body">
<h3>{e(g["name"])}</h3>
<p>{e(g["blurb"])}</p>
<ul class="link-list">
{links}
</ul>
</div>
</article>''')
    jobs_by_id = {j["id"]: j for j in JOBS}
    job_cards = "\n".join(
        f'<a class="job-card" href="jobs.html#{j}">\n{ba(jobs_by_id[j], live=False)}\n{job_meta(jobs_by_id[j])}\n</a>'
        for j in HOME_JOBS)
    reviews = "\n".join(review_card(n, r) for n, r in TESTIMONIALS)
    insta = "\n".join(
        f'<div class="media">{img(t, "Placeholder for an Instagram post")}</div>' for t in INSTAGRAM_TILES)
    main = f'''<section class="hero" id="top">
{img("hero.jpg", "", "bg-img", lazy=False)}
<div class="wrap hero-grid">
<div class="hero-copy">
<p class="kicker">Cheshire &middot; Domestic &amp; commercial</p>
<h1 class="display">Plastering, rendering and decorative finishes</h1>
<p class="lead">One team for every surface of the building. External render, internal plastering and drylining, and hand-finished microcement, Venetian and marble plaster.</p>
<div class="btn-row">
<a class="btn btn-ink btn-wide" href="#contact">Get a free quote</a>
<a class="btn btn-line btn-case" href="#contact">{ICON_PHONE}<span>Call<span class="lbl-l"> {e(PHONE)}</span></span></a>
<a class="btn btn-line btn-case" href="#contact">{ICON_CHAT}<span>WhatsApp</span></a>
</div>
</div>
<div class="hero-tiles">
<figure class="tile">{img("lime.jpg", "Sample of a rendered exterior finish", lazy=False)}<figcaption>01 Render</figcaption></figure>
<figure class="tile">{img("microcement.jpg", "Sample of a smooth internal plaster finish", lazy=False)}<figcaption>02 Plaster</figcaption></figure>
<figure class="tile">{img("venetian.jpg", "Sample of a polished Venetian plaster finish", lazy=False)}<figcaption>03 Decorative</figcaption></figure>
</div>
</div>
</section>

<section class="band">
<div class="wrap band-row">
<h2>Most firms render and dryline, or do decorative finishes. We do the lot.</h2>
<p>That means one quote, one schedule and one standard of finish, from the insulation behind the wall to the polished plaster on the face of it. No handovers between trades and no gaps for things to go wrong in.</p>
</div>
</section>

<section class="section bg-paper" id="services">
<div class="wrap stack">
<div class="sec-head">
<span class="eyebrow">What we do</span>
<h2 class="h2">Three trades, one team</h2>
</div>
{car(chr(10).join(cards), "grid-3")}
</div>
</section>

<section class="section bg-paper2" id="jobs">
<div class="wrap stack">
<div class="sec-head-row">
<div class="sec-head">
<span class="eyebrow">Recent work</span>
<h2 class="h2">Jobs we&rsquo;re proud of</h2>
</div>
<a class="btn btn-line btn-md to-end" href="jobs.html">See all jobs</a>
</div>
{car(job_cards, "grid-3")}
</div>
</section>

<section class="section bg-texture">
{img("dark.jpg", "", "bg-img")}
<div class="wrap stack">
<div class="sec-head">
<span class="eyebrow">Why choose us</span>
<h2 class="h2">Guaranteed, insured and approved</h2>
</div>
{car(chr(10).join([
        '<div><span class="num">01</span><h3>Workmanship guarantee</h3><p>[GUARANTEE LENGTH AND TERMS]</p></div>',
        '<div><span class="num">02</span><h3>Manufacturer approvals</h3><p>[APPROVALS HELD, e.g. K Rend approved installer]</p></div>',
        '<div><span class="num">03</span><h3>Accredited and insured</h3><p>[HEALTH &amp; SAFETY SCHEME, e.g. CHAS or SafeContractor] and [INSURANCE COVER]</p></div>',
        '<div><span class="num">04</span><h3>Homes and commercial sites</h3><p>Homeowners, developers, housebuilders and commercial clients.</p></div>',
    ]), "trust")}
</div>
</section>

<section class="section bg-paper" id="reviews">
<div class="wrap stack">
<div class="sec-head-row">
<div class="sec-head">
<span class="eyebrow">Reviews</span>
<h2 class="h2">What clients say</h2>
</div>
<div class="car-nav to-end">
<button class="car-btn" type="button" data-car-prev="reviews-car" aria-label="Previous reviews">{ICON_LEFT}</button>
<button class="car-btn" type="button" data-car-next="reviews-car" aria-label="Next reviews">{ICON_RIGHT}</button>
<a class="btn btn-line btn-md" href="reviews.html">All reviews</a>
</div>
</div>
{car(reviews, "car-always", "reviews-car")}
</div>
</section>

<section class="section bg-paper2" id="about">
<div class="wrap about-row">
<div class="people people-solo">
<figure class="person"><div class="ph-box">Photo of Rav</div><figcaption>Rav</figcaption></figure>
</div>
<div class="about-copy">
<span class="eyebrow">About us</span>
<h2 class="h2">Meet Rav</h2>
<p class="body-lg">[COMPANY STORY: how Rav started, years on the tools, the kind of projects he takes on.] You deal with Rav directly, from the first site visit to the final coat.</p>
<a class="btn btn-line btn-md" href="#contact">Get in touch</a>
</div>
</div>
</section>

<section class="section bg-paper" id="instagram">
<div class="wrap stack">
<div class="sec-head-row">
<div class="sec-head">
<span class="eyebrow">Instagram</span>
<h2 class="h2">@[INSTAGRAM HANDLE]</h2>
</div>
<a class="btn btn-line btn-md to-end" href="#instagram">Follow on Instagram</a>
</div>
<div class="insta-grid">
{insta}
</div>
<p class="note">The live Instagram feed appears here once the account is set up and posting.</p>
</div>
</section>'''
    return page(ctx, f"{SITE_NAME} | Plastering, rendering and decorative finishes in Cheshire",
                "Plastering, rendering and decorative finishes in Cheshire: external render, internal plastering and drylining, microcement, Venetian and marble plaster.",
                main)


# ---------------------------------------------------------------- service pages
def service_page(slug):
    s = SERVICES[slug]
    g = group_of(slug)
    ctx = Ctx(f"{slug}.html", current="services", svc=slug)
    benefits = "\n".join(
        f'<div class="benefit"><span class="num">{i:02d}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>'
        for i, (t, d) in enumerate(s["benefits"], 1))
    tags = ["[PROJECT PHOTO &middot; TOWN]", "[PROJECT PHOTO &middot; TOWN]", "[BEFORE / AFTER &middot; TOWN]"]
    photo_alt = "Placeholder for a %s project photo" % s["name"]
    photos = "\n".join(
        f'<figure class="photo">{img(w, photo_alt)}<figcaption class="tag">{t}</figcaption></figure>'
        for w, t in zip(s["work"], tags))
    chips = "\n".join(f'<li class="chip">{e(m)}</li>' for m in s["materials"])
    faqs = list(s["faqs"])
    faqs.append((f"How much does {s['cost_name']} cost?", COST_A))
    if not any(q == GUARANTEE[0] for q, _ in faqs):
        faqs.insert(len(faqs) - 1, GUARANTEE)
    faq_html = "\n".join(
        f'<details{" open" if i == 0 else ""}><summary>{e(q)}</summary><p>{e(a)}</p></details>'
        for i, (q, a) in enumerate(faqs))
    siblings = [x for x in g["services"] if x != slug]
    related = "\n".join(f'<li><a class="chip" href="{x}.html">{e(menu_name(x))}</a></li>' for x in siblings)

    light = iter(["bg-paper", "bg-paper2"] * 6)
    sec = lambda: next(light)  # noqa: E731

    pools = ""
    if "pools" in s:
        p = s["pools"]
        pts = "\n".join(f'<li><strong>{e(a)}</strong><span>{e(b)}</span></li>' for a, b in p["points"])
        pools_bg = None
    what_bg = sec()
    why_bg = sec()
    if "pools" in s:
        pools_bg = sec()
        pools = f'''<section class="section {pools_bg}" id="pools">
<div class="wrap feature">
<figure class="feature-media">{img("pool.jpg", "Placeholder image of a microcement pool surround")}<figcaption class="tag">Placeholder image</figcaption></figure>
<div class="feature-copy">
<span class="eyebrow">Pools</span>
<h2 class="h2 h2-sm">{e(p["title"])}</h2>
<p class="body-lg">{e(p["text"])}</p>
<ul class="ticks">
{pts}
</ul>
</div>
</div>
</section>'''
    work_bg = sec()
    faq_bg = sec()
    rel_bg = sec()
    main = f'''<section class="page-hero">
{img("hero.jpg", "", "bg-img", lazy=False)}
<div class="wrap">
<nav class="crumbs" aria-label="Breadcrumb"><ol>
<li><a href="./">Home</a></li>
<li><a href="{ctx.home("services")}">{e(g["name"])}</a></li>
<li><span aria-current="page">{e(s["name"])}</span></li>
</ol></nav>
<div class="page-hero-row">
<div class="page-hero-copy">
<p class="kicker">{e(g["name"])}</p>
<h1 class="display">{e(s["h1"])}</h1>
<p class="lead">{e(s["intro"])}</p>
<div class="btn-row">
<a class="btn btn-ink" href="#contact"><span class="lbl-l">Get a free quote</span><span class="lbl-s">Free quote</span></a>
<a class="btn btn-line btn-case" href="#contact">{ICON_PHONE}<span>Call<span class="lbl-l"> {e(PHONE)}</span></span></a>
</div>
</div>
<figure class="page-hero-media">{img(s["image"], f"Placeholder image for {s['name']}", lazy=False)}<figcaption class="tag">Placeholder image</figcaption></figure>
</div>
</div>
</section>

<section class="section {what_bg}">
<div class="wrap two-col">
<div class="col-head">
<span class="eyebrow">What it is</span>
<h2 class="h2 h2-sm">{e(s["what_title"])}</h2>
</div>
<div class="col-body">
{chr(10).join(f"<p>{e(par)}</p>" for par in s["what"])}
</div>
</div>
</section>

<section class="section {why_bg}">
<div class="wrap stack">
<div class="sec-head">
<span class="eyebrow">Why choose it</span>
<h2 class="h2 h2-sm">Why clients choose {e(s["name"] if slug != "insulation" else "Kingspan and Rockwool")}</h2>
</div>
{car(benefits, "grid-4")}
</div>
</section>

{pools}

<section class="section {work_bg}">
<div class="wrap stack">
<div class="sec-head-row">
<div class="sec-head">
<span class="eyebrow">Our work</span>
<h2 class="h2 h2-sm">{e(s["name"] if slug != "insulation" else "Insulation")} projects by our team</h2>
</div>
<a class="btn btn-line btn-md to-end" href="jobs.html">Jobs we&rsquo;re proud of</a>
</div>
{car(photos, "grid-photos")}
</div>
</section>

<section class="section bg-texture">
{img("dark.jpg", "", "bg-img")}
<div class="wrap split">
<div class="sec-head">
<span class="eyebrow">Brands and materials</span>
<h2 class="h2 h2-sm">What we use</h2>
<p class="muted-dark">Manufacturer logos sit here on the live site, alongside the approvals the team holds.</p>
</div>
<ul class="chip-list chip-grid">
{chips}
</ul>
</div>
</section>

<section class="section {faq_bg}">
<div class="wrap faq stack">
<div class="sec-head">
<span class="eyebrow">FAQs</span>
<h2 class="h2 h2-sm">{e(s["name"] if slug != "insulation" else "Insulation")} questions, answered</h2>
</div>
<div class="faq-list">
{faq_html}
</div>
</div>
</section>

<section class="section section-tight {rel_bg}">
<div class="wrap split">
<div class="sec-head">
<span class="eyebrow">Related services</span>
<h2 class="h2 h2-md">More {e(g["name"].lower())}</h2>
</div>
<ul class="chip-list chip-grid chip-grid-related">
{related}
<li><a class="chip chip-ink" href="{ctx.home("services")}">All services {ARROW}</a></li>
</ul>
</div>
</section>'''
    title = f"{s['name']} | {SITE_NAME}"
    return page(ctx, title, s["intro"], main)


# ---------------------------------------------------------------- jobs
def jobs_page():
    ctx = Ctx("jobs.html", current="jobs")
    chips = ['<button class="chip-btn" type="button" data-filter="all" aria-pressed="true">All</button>'] + [
        f'<button class="chip-btn" type="button" data-filter="{g["id"]}" aria-pressed="false">{e(g["short"])}</button>'
        for g in GROUPS]
    cards = "\n".join(
        f'<article class="job" id="{j["id"]}" data-cat="{group_of(j["service"])["id"]}">\n{ba(j, live=True)}\n{job_meta(j, "h2")}\n</article>'
        for j in JOBS)
    main = f'''<section class="page-hero page-hero-plain">
{img("hero.jpg", "", "bg-img", lazy=False)}
<div class="wrap">
<nav class="crumbs" aria-label="Breadcrumb"><ol>
<li><a href="./">Home</a></li>
<li><span aria-current="page">Jobs we&rsquo;re proud of</span></li>
</ol></nav>
<div class="page-hero-copy">
<p class="kicker">Our work</p>
<h1 class="display">Jobs we&rsquo;re proud of</h1>
<p class="lead">Before-and-after stills from selected jobs, with the location and the service on each. Every pair is shot from the same angle, in similar light, with no filters.</p>
</div>
</div>
</section>

<section class="section bg-paper">
<div class="wrap stack">
<div class="filter-row">
<p class="note">Drag the handle on each photo to compare before and after.</p>
<div class="chips" role="group" aria-label="Filter jobs by service">
{chr(10).join(chips)}
</div>
</div>
<div class="jobs-grid">
{cards}
</div>
</div>
</section>'''
    return page(ctx, f"Jobs we’re proud of | {SITE_NAME}",
                "Before-and-after stills from selected plastering, rendering and decorative finishes jobs.", main)


# ---------------------------------------------------------------- reviews
def reviews_page():
    ctx = Ctx("reviews.html", current="reviews")
    cards = "\n".join(review_card(n, r) for n, r in TESTIMONIALS)
    google = '''<div class="google-card">
<span class="eyebrow">Google reviews</span>
<p class="google-score">[RATING] out of 5</p>
<p>From [NUMBER] Google reviews. These show here once the Google Business Profile is live.</p>
<a class="btn btn-line btn-sm" href="#contact">Leave a review</a>
</div>'''
    main = f'''<section class="page-hero page-hero-plain">
{img("hero.jpg", "", "bg-img", lazy=False)}
<div class="wrap">
<nav class="crumbs" aria-label="Breadcrumb"><ol>
<li><a href="./">Home</a></li>
<li><span aria-current="page">Reviews</span></li>
</ol></nav>
<div class="page-hero-copy">
<p class="kicker">Reviews</p>
<h1 class="display">What clients say</h1>
<p class="lead">Testimonials from homeowners, builders and commercial clients, alongside our Google reviews.</p>
</div>
</div>
</section>

<section class="section bg-paper">
<div class="wrap">
<div class="reviews-grid">
{cards}
{google}
</div>
</div>
</section>'''
    return page(ctx, f"Reviews | {SITE_NAME}",
                "Testimonials and Google reviews from homeowners, builders and commercial clients.", main)


def main():
    pages = {"index.html": home_page(), "jobs.html": jobs_page(), "reviews.html": reviews_page()}
    for slug in SERVICES:
        pages[f"{slug}.html"] = service_page(slug)
    for name, content in pages.items():
        with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
            f.write(content)
    print(f"Built {len(pages)} pages")


if __name__ == "__main__":
    main()
