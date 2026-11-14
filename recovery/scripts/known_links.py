"""List every post permalink referenced in raw captures, normalized to /YYYY/MM/slug.

Usage: known_links.py RAW_DIR
"""
import re
import sys
from pathlib import Path

RAW = Path(sys.argv[1])
LINK = re.compile(
    rb"(?:https?:)?//(?:web\.archive\.org/web/\d+[a-z_]*/)?(?:https?://)?(?:www\.|blog\.)?cromwellhaus\.com(?::80)?"
    rb"(/(?:index\.php/|CS/)?(?:blogs/ryanc/archive/)?\d{4}/\d{2}/(?:\d{2}/)?[a-z0-9%\-_.]+?)(?:\.aspx)?/?[\"'#?<\s]",
    re.I,
)
seen = {}
for f in RAW.iterdir():
    if f.name == "index.tsv":
        continue
    for m in LINK.finditer(f.read_bytes()):
        p = m.group(1).decode("utf-8", "replace").lower()
        p = re.sub(r"^/(index\.php|cs)/", "/", p)
        p = re.sub(r"^/blogs/ryanc/archive", "", p)
        if re.search(r"/(feed|trackback|comment-page-\d+|page)$", p) or re.search(r"\.(png|jpe?g|gif|zip)$", p):
            continue
        seen[p] = seen.get(p, 0) + 1
for p in sorted(seen):
    print(p)
