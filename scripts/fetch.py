"""Download Wayback captures in raw (id_) mode. Usage: fetch.py fetch.tsv outdir"""
import hashlib
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

tsv, outdir = sys.argv[1], Path(sys.argv[2])
outdir.mkdir(parents=True, exist_ok=True)
jobs = [l.rstrip("\n").split("\t") for l in open(tsv) if l.strip()]


def name(ts, url):
    return f"{ts}_{hashlib.sha1(url.encode()).hexdigest()[:12]}"


def get(job):
    ts, url = job
    dest = outdir / name(ts, url)
    if dest.exists():
        return "skip"
    wb = f"https://web.archive.org/web/{ts}id_/{url}"
    for attempt in range(6):
        try:
            req = urllib.request.Request(wb, headers={"User-Agent": "cromwellhaus-recovery/1.0 (personal archive restore)"})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            dest.write_bytes(data)
            (outdir / "index.tsv").open("a").write(f"{dest.name}\t{ts}\t{url}\n")
            time.sleep(4.5)
            return "ok"
        except Exception as e:  # noqa: BLE001
            err = e
            time.sleep(90 * (attempt + 1))
    print(f"FAIL {ts} {url} {err}", file=sys.stderr, flush=True)
    return "fail"


with ThreadPoolExecutor(1) as ex:
    for i, res in enumerate(ex.map(get, jobs), 1):
        if i % 25 == 0:
            print(f"{i}/{len(jobs)}", flush=True)
print("done", flush=True)
