"""Extract blog posts from raw Wayback captures and write Markdown.

Usage: extract.py RAW_DIR OUT_DIR
Reads RAW_DIR/index.tsv (file, timestamp, original url).
"""
import json
import re
import sys
import textwrap
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


CODE_LINE = re.compile(
    r"(^\s*[{}()\]]+;?\s*$|;\s*$|^\s*</?[\w:.-]+[\s>/]|^\s*(public|private|protected|internal|static|using|namespace|"
    r"class|var|return|if|else|foreach|for|function|def|defmodule|end|Dim|End Sub|SELECT|FROM|WHERE|INSERT|"
    r"UPDATE|CREATE|\$\w+)\b|=>|\$\w+\s*=|\w+\(.*\)\s*\{?\s*$)"
)


def guess_language(text):
    t = text.strip()
    if not t:
        return ""
    if t.startswith("<"):
        return "xml"
    if re.search(r"\bdefmodule\b|\|>|\bdo\s*$|\bIO\.puts\b", t, re.M):
        return "elixir"
    if re.search(r"\b(Dim|End Sub|End Function|Sub \w+\()", t):
        return "vbnet"
    if re.search(r"\$\w+|\b\w+-object\b|-\w+ \$", t, re.I) and re.search(r"function |new-object|\$\w+\s*=|\| ?(%|foreach|where)", t, re.I):
        return "powershell"
    if re.search(r"\b(SELECT|INSERT INTO|UPDATE|CREATE (TABLE|PROC)|DECLARE @)\b", t) and not re.search(r"\b(public|class)\b", t):
        return "sql"
    if re.search(r"^\s*(\$ |brew |sudo |git |cd |npm |mix )", t, re.M):
        return "bash"
    if re.search(r"\bfunction\s*\w*\s*\(|\$\(|\bdocument\.|\bconsole\.log\b|\brequire\(|\bmodule\.exports\b", t):
        return "javascript"
    if re.search(r"\b(public|private|protected|namespace|using System|void|string|new \w+)\b|\bvar \w+ = |=>", t) and ";" in t:
        return "csharp"
    return ""


def line_text(el):
    """Text of an element with <br> and block boundaries as newlines, nbsp as spaces."""
    for br in el.find_all("br"):
        br.replace_with("\n")
    for blk in el.find_all(["p", "div", "li"]):
        blk.insert_after("\n")
    return el.get_text().replace("\xa0", " ")


def new_pre(soup, text):
    text = textwrap.dedent("\n".join(l.rstrip() for l in text.strip("\n").split("\n")))
    pre = soup.new_tag("pre")
    code = soup.new_tag("code")
    code.string = text
    pre.append(code)
    lang = guess_language(text)
    if lang:
        pre["data-lang"] = lang
    return pre


def normalize_code(soup):
    """Repair code samples mangled by Live Writer / CopySourceAsHtml style markup."""
    # 0. <br> line breaks inside <pre>; empty <pre>.
    for pre in soup.find_all("pre"):
        for br in pre.find_all("br"):
            br.replace_with("\n")
    for pre in soup.find_all("pre"):
        if pre.parent is not None and not pre.get_text().strip():
            pre.decompose()
    # 1. <pre> wrapping one <pre> per line.
    #    Only the leading run of line-<pre>s is code: an unclosed outer <pre> can swallow
    #    the rest of the post, which gets moved back out after the merged block.
    for outer in soup.find_all("pre"):
        if outer.parent is None or not outer.find("pre", recursive=False):
            continue
        kids, lines, rest = list(outer.contents), [], []
        for i, k in enumerate(kids):
            if getattr(k, "name", None) == "pre":
                lines.append(k.get_text().replace("\xa0", " ").rstrip("\n"))
            elif not (isinstance(k, str) and not k.strip()):
                rest = kids[i:]
                break
        if not lines:
            continue
        anchor = new_pre(soup, "\n".join(lines))
        outer.replace_with(anchor)
        for k in rest:
            k.extract()
            anchor.insert_after(k)
            anchor = k
    # 2. Runs of sibling <pre> elements (one per line) -> one block.
    for pre in soup.find_all("pre"):
        if pre.parent is None:
            continue
        run = [pre]
        sib = pre.next_sibling
        while sib is not None and (sib.name == "pre" or (isinstance(sib, str) and not sib.strip())):
            if sib.name == "pre":
                run.append(sib)
            sib = sib.next_sibling
        if len(run) > 1 and all(len(p.get_text().strip("\n").split("\n")) <= 2 for p in run):
            merged = new_pre(soup, "\n".join(p.get_text().replace("\xa0", " ").rstrip("\n") for p in run))
            run[0].replace_with(merged)
            for p in run[1:]:
                p.decompose()
    # 3. Code formatted as quotes / monospace divs.
    for el in soup.find_all(["blockquote", "div"]):
        if el.parent is None or el.find("pre"):
            continue
        style = (el.get("style") or "").lower()
        cls = " ".join(el.get("class") or []).lower()
        mono = any(f in style for f in ("consolas", "courier", "monospace")) or any(
            c in cls for c in ("csharpcode", "code", "wlwritereditablesmartcontent"))
        if el.name == "div" and not mono:
            continue
        if el.find(["blockquote", "img", "table", "ul", "ol"]):
            continue
        text = line_text(BeautifulSoup(str(el), "lxml"))
        lines = [l for l in text.split("\n") if l.strip()]
        if len(lines) < 2:
            continue
        codey = sum(1 for l in lines if CODE_LINE.search(l))
        if codey / len(lines) >= (0.4 if mono else 0.6):
            el.replace_with(new_pre(soup, text))
    # 4. A blockquote that only wraps a code block is presentation, not a quote.
    squash = lambda s: re.sub(r"\s+", "", s)
    for bq in soup.find_all("blockquote"):
        pres = bq.find_all("pre")
        if pres and squash(bq.get_text()) == "".join(squash(p.get_text()) for p in pres):
            bq.unwrap()
    # 5. Tag remaining <pre> with a guessed language.
    for pre in soup.find_all("pre"):
        if not pre.get("data-lang"):
            lang = guess_language(pre.get_text())
            if lang:
                pre["data-lang"] = lang
    # 6. Literal "<tag>" and "\" in prose must survive Markdown. Placeholders are swapped
    #    back after conversion by unplaceholder() (markdownify would mangle real entities).
    for s in soup.find_all(string=lambda t: "<" in t or "\\" in t):
        if not s.find_parent(["pre", "code"]) and s.parent is not None and s.__class__.__name__ == "NavigableString":
            s.replace_with(s.replace("\\", PH_BS).replace("<", PH_LT))


PH_LT, PH_BS = "\ue000", "\ue001"  # private-use placeholders


def unplaceholder(md):
    return md.replace(PH_BS, "\\\\").replace(PH_LT, "&lt;")


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

def code_breaks(html):
    """Line breaks inside <pre>: some re-imported copies flattened code onto one line."""
    soup = BeautifulSoup(html, "lxml")
    return sum(p.get_text().count("\n") + len(p.find_all("br")) for p in soup.find_all("pre"))


def pick_best(cands):
    full = [c for c in cands if not c["excerpt"]] or cands
    top = max(c["len"] for c in full)
    near = [c for c in full if c["len"] >= 0.85 * top]
    return max(near, key=lambda c: (code_breaks(c["html"]) > 0, c["len"]))


# Fold excerpt-only groups into the full post they were cut from (retitled across eras).
def opening(cands):
    best = pick_best(cands)
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
    best = pick_best(cands)
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
    normalize_code(body)
    md = markdownify(str(body.body or body), heading_style="ATX", bullets="-",
                     code_language_callback=lambda el: el.get("data-lang") or "").strip()
    md = unplaceholder(md)
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
