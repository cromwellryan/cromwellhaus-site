"""Extract blog posts from raw Wayback captures and write Markdown.

Usage: extract.py RAW_DIR OUT_DIR
Reads RAW_DIR/index.tsv (file, timestamp, original url).
"""
import json
import re
import sys
from datetime import datetime
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup
from markdownify import markdownify

RAW, OUT = Path(sys.argv[1]), Path(sys.argv[2])

CONTENT_SEL = [
    ".entry-content", ".post-content", ".postcontent", ".storycontent",
    ".entry", ".post-body", ".content", ".PostContent", ".postbody",
]
MORE_RE = re.compile(r"(continue reading[^.]{0,40}$|read more\W*$|read the rest[^.]{0,40}$|\[(\.\.\.|…|&hellip;)\]\W*$|…\s*$)", re.I)


def norm_title(t):
    t = re.sub(r"&\w+;|&#\d+;", "", t or "")
    return re.sub(r"[^a-z0-9]+", "", t.lower())


def clean_path(url):
    p = urlparse(url)
    path = re.sub(r"^/(index\.php|CS)(?=/)", "", p.path)
    path = re.sub(r"^/index\.php/?$", "/", path)
    if p.query and re.fullmatch(r"p=\d+", p.query):
        path += "?" + p.query
    return path


def slug_from(path):
    m = re.search(r"/(\d{4})/(\d{2})/(?:(\d{2})/)?([^/?#]+?)(?:\.aspx)?/?$", path)
    if not m:
        return None, None
    y, mo, d, slug = m.groups()
    return slug, (y, mo, d)


def wb_original(href, base):
    """Undo Wayback URL rewriting if present, resolve relative links."""
    if not href:
        return href
    m = re.match(r"^(?:https?://web\.archive\.org)?/web/\d+[a-z_]*/(.+)$", href)
    if m:
        href = m.group(1)
        if href.startswith("http:/") and not href.startswith("http://"):
            href = href.replace("http:/", "http://", 1)
    return urljoin(base, href)


def text_len(html):
    return len(BeautifulSoup(html, "lxml").get_text(" ", strip=True))


def parse_date(s):
    if not s:
        return None
    s = s.strip()
    for fn in (
        lambda x: datetime.fromisoformat(x.replace("Z", "+00:00")),
        parsedate_to_datetime,
        lambda x: datetime.strptime(re.sub(r"(\d)(st|nd|rd|th)", r"\1", x), "%B %d, %Y"),
        lambda x: datetime.strptime(x, "%A, %B %d, %Y"),
        lambda x: datetime.strptime(x, "%b %d, %Y"),
        lambda x: datetime.strptime(x, "%d %B %Y"),
        lambda x: datetime.strptime(x, "%m/%d/%Y"),
    ):
        try:
            return fn(s).date().isoformat()
        except Exception:  # noqa: BLE001
            pass
    m = re.search(r"([A-Z][a-z]+ \d{1,2}(?:st|nd|rd|th)?,? \d{4})", s)
    if m:
        return parse_date(m.group(1).replace(",", ",") if "," in m.group(1) else m.group(1).replace(" 20", ", 20"))
    return None


posts = []  # raw candidates


def add(title, link, date, html, cats, tags, source, kind):
    if not title or not html or title.strip().startswith("Comment on "):
        return
    posts.append(dict(title=title.strip(), link=link, date=date, html=html, cats=cats or [],
                      tags=tags or [], source=source, kind=kind))


def from_feed(data, src, base):
    soup = BeautifulSoup(data, "xml")
    for it in soup.find_all(["item", "entry"]):
        title = it.find("title")
        link = it.find("link")
        href = (link.get("href") or link.get_text(strip=True)) if link else None
        orig = it.find("feedburner:origLink") or it.find("origLink")
        if orig:
            href = orig.get_text(strip=True)
        body = it.find("content:encoded") or it.find("encoded") or it.find("content") or it.find("description") or it.find("summary")
        date = it.find("pubDate") or it.find("published") or it.find("updated") or it.find("dc:date")
        cats = [c.get("term") or c.get_text(strip=True) for c in it.find_all("category")]
        add(title.get_text(strip=True) if title else None, href,
            parse_date(date.get_text()) if date else None,
            body.get_text() if body else None, cats, [], src, "feed")


def from_html(data, src, base):
    soup = BeautifulSoup(data, "lxml")
    blocks = soup.select('[id^="post-"]')
    blocks = [b for b in blocks if re.fullmatch(r"post-\d+", b.get("id", ""))]
    if not blocks:
        blocks = soup.select(".hentry") or soup.select("div.post") or soup.select(".BlogPostArea, .CommonContentArea .post")
    # drop blocks nested inside other blocks
    blocks = [b for b in blocks if not any(o is not b and b in o.descendants for o in blocks)]
    for b in blocks:
        h = b.select_one(".entry-title, .posttitle, .post-title, h1, h2, h3, h4")
        title = h.get_text(" ", strip=True) if h else None
        a = h.find("a", href=True) if h else None
        link = wb_original(a["href"], base) if a else base
        if not a and len(blocks) > 1:
            continue
        content = None
        for sel in CONTENT_SEL:
            content = b.select_one(sel)
            if content:
                break
        if content is None:
            content = b
        # date
        date = None
        t = b.select_one("time[datetime], abbr.published, .published, .entry-date, .date, .postdate, .post-date")
        if t:
            date = parse_date(t.get("datetime") or t.get("title") or t.get_text(" ", strip=True))
        if not date:
            prev = b.find_previous(class_=re.compile("date", re.I))
            if prev and len(blocks) > 1:
                date = parse_date(prev.get_text(" ", strip=True))
        cats = [x.get_text(strip=True) for x in b.select('a[rel~="category"]')]
        tags = [x.get_text(strip=True) for x in b.select('a[rel~="tag"]') if 'category' not in x.get('rel', [])]
        for junk in content.select(".sharedaddy, .jp-relatedposts, .wp-socializer, .addtoany_share_save_container, "
                                   ".postmetadata, .entry-meta, .meta-list, .entry-footer, .cat-links, .tags-links, "
                                   ".post-meta, .entry-utility, .postfoot, .posthead, script, style, noscript, "
                                   "iframe[src*='facebook'], .navigation, #comments, .commentlist, form"):
            junk.decompose()
        if h and content is b:
            h.decompose()
        for img in content.find_all("img"):
            if img.get("src"):
                img["src"] = wb_original(img["src"], base)
        for lk in content.find_all("a", href=True):
            lk["href"] = wb_original(lk["href"], base)
        add(title, link, date, str(content), cats, tags, src, "page" if len(blocks) == 1 else "listing")


index = [l.rstrip("\n").split("\t") for l in open(RAW / "index.tsv")]
for fname, ts, url in index:
    data = (RAW / fname).read_bytes()
    src = f"https://web.archive.org/web/{ts}/{url}"
    head = data[:600].lstrip().lower()
    try:
        if head.startswith(b"<?xml") or b"<rss" in head or b"<feed" in head:
            from_feed(data, src, url)
        else:
            from_html(data, src, url)
    except Exception as e:  # noqa: BLE001
        print(f"ERR {fname} {url}: {e}", file=sys.stderr)

# merge
merged = {}
for p in posts:
    path = clean_path(p["link"] or "")
    slug, ymd = slug_from(path)
    p["slug"], p["ymd"], p["len"] = slug, ymd, text_len(p["html"])
    p["excerpt"] = p["len"] < 1500 and bool(MORE_RE.search(BeautifulSoup(p["html"], "lxml").get_text(" ", strip=True)[-200:]))
    key = norm_title(p["title"])
    if not key or key in {"pagenotfound", "notfound", "archives", "about"} and not slug:
        continue
    merged.setdefault(key, []).append(p)

OUT.mkdir(parents=True, exist_ok=True)
(OUT / "posts").mkdir(exist_ok=True)
(OUT / "pages").mkdir(exist_ok=True)

# Fold excerpt-only groups into the full post they were cut from (retitled across eras).
def opening(cands):
    best = max(cands, key=lambda c: (not c["excerpt"], c["len"]))
    return best, norm_title(BeautifulSoup(best["html"], "lxml").get_text(" ", strip=True)[:150])[:80]


openings = {k: opening(c) for k, c in merged.items()}
for key, (best, op) in list(openings.items()):
    if not best["excerpt"] or len(op) < 40:
        continue
    for other, (obest, oop) in openings.items():
        if other != key and other in merged and not obest["excerpt"] and oop.startswith(op[:60]):
            merged[other].extend(merged.pop(key))
            break

report = []
for key, cands in merged.items():
    best = max(cands, key=lambda c: (not c["excerpt"], c["len"]))
    slug = next((c["slug"] for c in cands if c["slug"] and not c["slug"].isdigit()), None) \
        or re.sub(r"[^a-z0-9]+", "-", best["title"].lower()).strip("-")[:80]
    date = next((c["date"] for c in cands if c["date"]), None)
    if not date:
        ymd = next((c["ymd"] for c in cands if c["ymd"]), None)
        if ymd:
            date = f"{ymd[0]}-{ymd[1]}-{ymd[2] or '01'}"
    cats = sorted({x for c in cands for x in c["cats"]})
    tags = sorted({x for c in cands for x in c["tags"]})
    links = sorted({c["link"] for c in cands if c["link"]})
    body = BeautifulSoup(best["html"], "lxml")
    for el in body.select('img[src*="feedburner.com"], a[href*="feedburner.com"], img[src*="feeds.wordpress.com"], img[src*="aggbug"]'):
        el.decompose()
    md = markdownify(str(body.body or body), heading_style="ATX", bullets="-", code_language="").strip()
    md = re.sub(r"\n{3,}", "\n\n", md)
    fm = {
        "title": best["title"],
        "date": date,
        "slug": slug,
        "categories": cats,
        "tags": tags,
        "original_urls": links,
        "wayback_source": best["source"],
        "excerpt_only": best["excerpt"],
    }
    fname = f"{date}-{slug}.md" if date else f"{slug}.md"
    front = "---\n" + "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in fm.items()) + "\n---\n\n"
    (OUT / ("posts" if date else "pages") / fname).write_text(front + md + "\n")
    report.append(dict(file=fname, title=best["title"], date=date, chars=best["len"], excerpt=best["excerpt"],
                       kind=best["kind"], n_sources=len(cands)))

report.sort(key=lambda r: r["date"] or "")
(OUT / "report.json").write_text(json.dumps(report, indent=1))
full = sum(1 for r in report if not r["excerpt"])
print(f"{len(posts)} candidates -> {len(report)} posts ({full} full, {len(report)-full} excerpt-only)")
