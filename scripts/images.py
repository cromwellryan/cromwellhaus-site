"""Fetch self-hosted images referenced by recovered posts and rewrite links.

Usage: images.py OUT_DIR
Downloads to OUT_DIR/images/<original path>, rewrites posts to /images/<path>.
"""
import re
import sys
import time
import urllib.request
from pathlib import Path
from urllib.parse import unquote, urlparse

OUT = Path(sys.argv[1])
IMG_RE = re.compile(r"!\[[^\]]*\]\((\S+?)(?:\s+\"[^\"]*\")?\)|\]\((\S+?\.(?:png|jpe?g|gif|bmp))\)", re.I)
OWN = re.compile(r"^https?://([a-z0-9-]+\.)?cromwellhaus\.com(:80)?/", re.I)

posts = sorted((OUT / "posts").glob("*.md"))
urls = set()
for p in posts:
    for m in IMG_RE.finditer(p.read_text()):
        u = m.group(1) or m.group(2)
        if u.startswith("http") and "feedburner.com" not in u:
            urls.add(u)

print(f"{len(urls)} image urls", flush=True)
mapping, failed = {}, []
for u in sorted(urls):
    pu = urlparse(u)
    path = unquote(pu.path).lstrip("/")
    if not OWN.match(u):
        path = f"external/{pu.netloc}/{path}"
    dest = OUT / "images" / path
    local = "/images/" + path
    if dest.exists():
        mapping[u] = local
        continue
    wb = f"https://web.archive.org/web/2019im_/{u}"
    for attempt in range(4):
        try:
            req = urllib.request.Request(wb, headers={"User-Agent": "cromwellhaus-recovery/1.0 (personal archive restore)"})
            with urllib.request.urlopen(req, timeout=60) as r:
                ctype, data = r.headers.get("Content-Type", ""), r.read()
            if not ctype.startswith("image/"):
                raise ValueError(f"not an image: {ctype}")
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
            mapping[u] = local
            break
        except urllib.error.HTTPError as e:
            if e.code == 404:
                break
            time.sleep(60 * (attempt + 1))
        except ValueError:
            break
        except Exception:  # noqa: BLE001
            time.sleep(60 * (attempt + 1))
    else:
        pass
    if u not in mapping:
        failed.append(u)
    time.sleep(4.5)

for p in posts:
    s = p.read_text()
    for u, local in mapping.items():
        s = s.replace(u, local)
    p.write_text(s)

(OUT / "images-missing.txt").write_text("\n".join(failed) + "\n")
print(f"recovered {len(mapping)}, missing {len(failed)}")
