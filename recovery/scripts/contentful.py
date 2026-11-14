"""Convert the 2021 Contentful-backed site (Next.js) into Markdown posts.

Usage: contentful.py SNAPSHOT_DIR OUT_DIR [--skip SLUG ...]
SNAPSHOT_DIR holds saved pages from https://cromwellhaus.com (archive + one per post);
each embeds its Contentful entries as __NEXT_DATA__, so no API token is needed.
Writes OUT_DIR/posts/*.md and downloads embedded assets to OUT_DIR/images/contentful/.
"""
import json
import re
import sys
import urllib.request
from pathlib import Path

SNAP, OUT = Path(sys.argv[1]), Path(sys.argv[2])
SKIP = set(sys.argv[sys.argv.index("--skip") + 1:]) if "--skip" in sys.argv else set()


def next_data(path):
    m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', path.read_text())
    return json.loads(m.group(1))["props"]["pageProps"] if m else {}


def guess_language(code):
    if re.search(r'^\s*(resource|locals|variable|module|provider)\b.*\{', code, re.M):
        return "hcl"
    if code.lstrip().startswith("<"):
        return "xml"
    return ""


def is_code(par):
    texts = [n for n in par.get("content", []) if n["nodeType"] == "text" and n["value"].strip()]
    return par["nodeType"] == "paragraph" and texts and all(
        n["nodeType"] == "text" and (not n["value"].strip() or any(m["type"] == "code" for m in n["marks"]))
        for n in par["content"])


def inline(nodes):
    out = []
    for n in nodes:
        if n["nodeType"] == "text":
            v = n["value"].replace("\xa0", " ")
            if not v.strip():
                out.append(v)
                continue
            lead, core, trail = re.match(r"(\s*)(.*?)(\s*)$", v, re.S).groups()
            for m in n["marks"]:
                core = {"bold": f"**{core}**", "italic": f"*{core}*", "code": f"`{core}`"}.get(m["type"], core)
            out.append(lead + core + trail)
        elif n["nodeType"] == "hyperlink":
            text = inline(n["content"]).strip()
            if text:
                out.append(f"[{text}]({n['data']['uri']})")
    return "".join(out)


def blocks(nodes, assets, depth=0):
    out, code = [], []

    def flush():
        if code:
            body = "\n".join(code).rstrip("\n")
            out.append(f"```{guess_language(body)}\n{body}\n```")
            code.clear()

    for n in nodes:
        t = n["nodeType"]
        if is_code(n):
            code.append("".join(c["value"] for c in n["content"]))
            continue
        flush()
        if t == "paragraph":
            text = inline(n["content"]).strip()
            if text:
                out.append(text)
        elif t.startswith("heading-"):
            out.append("#" * int(t[-1]) + " " + inline(n["content"]).strip())
        elif t in ("ordered-list", "unordered-list"):
            items = []
            for i, li in enumerate(n["content"], 1):
                bullet = f"{i}." if t == "ordered-list" else "-"
                body = "\n\n".join(blocks(li["content"], assets, depth + 1))
                items.append(f"{bullet} " + body.replace("\n", "\n" + " " * (len(bullet) + 1)))
            out.append("\n".join(items))
        elif t == "blockquote":
            out.append("\n".join("> " + l for l in "\n\n".join(blocks(n["content"], assets)).split("\n")))
        elif t == "hr":
            out.append("---")
        elif t == "embedded-asset-block":
            a = assets.get(n["data"]["target"]["sys"]["id"])
            if a:
                out.append(f"![{a['alt']}]({a['local']})")
    flush()
    return out


def fetch_asset(asset):
    f = asset["fields"]
    url = "https:" + f["file"]["url"] if f["file"]["url"].startswith("//") else f["file"]["url"]
    name = f"{asset['sys']['id']}-{f['file']['fileName']}".replace(" ", "-")
    dest = OUT / "images" / "contentful" / name
    if not dest.exists():
        dest.parent.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(url, timeout=60) as r:
            dest.write_bytes(r.read())
    return {"local": f"/images/contentful/{name}", "alt": f.get("description") or f.get("title") or ""}


def front(fm):
    return "---\n" + "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in fm.items()) + "\n---\n\n"


entries, includes = {}, {}
for page in sorted(SNAP.glob("*.html")):
    props = next_data(page)
    for it in props.get("publications", []) + props.get("recentContent", []):
        entries.setdefault(it["sys"]["id"], it)
    if "post" in props:
        entries[props["post"]["sys"]["id"]] = props["post"]  # full entry beats the listing copy
        for a in (props.get("includes") or {}).get("Asset", []):
            includes[a["sys"]["id"]] = a

(OUT / "posts").mkdir(parents=True, exist_ok=True)
for e in sorted(entries.values(), key=lambda e: e["sys"]["createdAt"]):
    f, kind, date = e["fields"], e["sys"]["contentType"]["sys"]["id"], e["sys"]["createdAt"][:10]
    if kind == "post":
        slug = f["slug"]
        if slug in SKIP:
            print(f"skip {slug}")
            continue
        if "body" not in f:
            print(f"WARN {slug}: no body in snapshots; save https://cromwellhaus.com/{slug}", file=sys.stderr)
            continue
        assets = {i: fetch_asset(a) for i, a in includes.items()}
        fm = {"title": f["title"], "date": date, "slug": slug, "categories": [], "tags": [],
              "abstract": f.get("abstract", ""), "original_urls": [f"https://cromwellhaus.com/{slug}"],
              "redirect_from": [f"/{slug}"], "contentful_id": e["sys"]["id"],
              "permalink": f"/{date[:4]}/{date[5:7]}/{slug}/"}
        body = "\n\n".join(blocks(f["body"]["content"], assets))
    elif kind == "externalContent":
        slug = re.sub(r"[^a-z0-9]+", "-", f["title"].lower()).strip("-")
        fm = {"title": f["title"], "date": date, "slug": slug, "categories": [], "tags": [],
              "external_url": f["url"], "contentful_id": e["sys"]["id"], "permalink": False}
        body = "\n\n".join(blocks(f["abstract"]["content"], {}))
    else:
        print(f"WARN unknown content type {kind}", file=sys.stderr)
        continue
    path = OUT / "posts" / f"{date}-{slug}.md"
    path.write_text(front(fm) + body + "\n")
    print(f"wrote {path.name}")
