"""Pick which Wayback captures to download.

Input: CDX lines (urlkey timestamp original mimetype status digest).
Output: TSV of timestamp<TAB>original to fetch.
"""
import re
import sys
from collections import defaultdict

SKIP = re.compile(
    r"/(media|members|user|login\.aspx|photos|wp-json|wp-includes|wp-content|"
    r"wp-admin|wp-login|utility|search|error\.htm|files|groups|wikis|xmlrpc|"
    r"themes|tags?/[^/]+/feed|trackback|comment-page|rsd\.ashx|wlwmanifest|"
    r"opml|rsscomments|events)(/|$|\?|\.)",
    re.I,
)
# Listing-ish pages whose content changes over time: keep many captures.
MULTI = re.compile(r"\)(/|/index\.php/?|/feed/?|/feed/atom/?|/ryancromwell|/blogs/?|"
                   r"/blogs/(ryanc/)?(default\.aspx|rss\.aspx|mainfeed\.aspx)|"
                   r"/cs/blogs/ryanc/rss\.aspx|/page/\d+/?)$", re.I)

rows = defaultdict(list)
for path in sys.argv[1:]:
    for line in open(path):
        parts = line.split()
        if len(parts) < 6:
            continue
        urlkey, ts, orig, mime, status, digest = parts[:6]
        if status != "200" or not re.search(r"html|xml|rss|atom", mime):
            continue
        key = re.sub(r"\?(?!p=\d+$).*$", "", urlkey)  # drop query except ?p=N
        if SKIP.search(key.split(")", 1)[1]):
            continue
        # comment feeds of individual posts carry comments only
        if re.search(r"/\d{4}/\d{2}/[^/]+/feed/?$", key):
            continue
        rows[key].append((ts, orig, digest))

out = []
for key, caps in rows.items():
    caps.sort()
    seen, uniq = set(), []
    for c in caps:
        if c[2] not in seen:
            seen.add(c[2])
            uniq.append(c)
    keep = uniq if MULTI.search(key) else uniq[-2:]
    out.extend(keep)

for ts, orig, _ in sorted(out):
    print(f"{ts}\t{orig}")
print(f"{len(out)} captures from {len(rows)} urls", file=sys.stderr)
