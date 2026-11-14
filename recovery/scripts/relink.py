"""Rewrite links between recovered posts to root-relative /YYYY/MM/slug/ permalinks.

Usage: relink.py OUT_DIR
"""
import json
import re
import sys
from pathlib import Path

OUT = Path(sys.argv[1])
posts = sorted((OUT / "posts").glob("*.md"))

permalink = {}  # lowercase slug -> /YYYY/MM/slug/
for p in posts:
    fm = dict(re.findall(r"^(\w+): (.*)$", p.read_text().split("\n---\n", 1)[0], re.M))
    slug, date = json.loads(fm["slug"]), json.loads(fm["date"])
    link = f"/{date[:4]}/{date[5:7]}/{slug}/"
    for u in json.loads(fm["original_urls"]):
        m = re.search(r"/(\d{4})/(\d{2})/[^/]+?/?$", u) or re.search(r"/(\d{4})/(\d{2})/\d{2}/[^/]+$", u)
        if m and "/blogs/" not in u:
            link = f"/{m.group(1)}/{m.group(2)}/{slug}/"
            break
    permalink[slug.lower()] = link
    for u in json.loads(fm["original_urls"]):
        m = re.search(r"/([^/]+?)(?:\.aspx)?/?$", u)
        if m and not m.group(1).isdigit():
            permalink.setdefault(m.group(1).lower(), link)

LINK = re.compile(
    r"\((?:https?://(?:www\.|blog\.)?cromwellhaus\.com(?::80)?)(?:/index\.php|/CS)?"
    r"(?:/blogs/ryanc/archive)?/\d{4}/\d{2}/(?:\d{2}/)?([A-Za-z0-9%\-_.]+?)(?:\.aspx)?/?([#?][^)\s]*)?(\s+\"[^\"]*\")?\)"
)
changed = 0
for p in posts + sorted((OUT / "pages").glob("*.md")):
    s = p.read_text()
    head, body = s.split("\n---\n", 1)

    def sub(m):
        global changed
        target = permalink.get(m.group(1).lower())
        if not target:
            return m.group(0)
        changed += 1
        return f"({target}{m.group(3) or ''})"

    body2 = LINK.sub(sub, body)
    if p.parent.name == "posts" and "\npermalink:" not in head:
        slug = json.loads(re.search(r"^slug: (.*)$", head, re.M).group(1))
        head += f"\npermalink: {json.dumps(permalink[slug.lower()])}"
    p.write_text(head + "\n---\n" + body2)
print(f"rewrote {changed} internal links")
