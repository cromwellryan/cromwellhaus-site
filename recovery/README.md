# cromwellhaus.com recovery

Blog content recovered from the Wayback Machine (captures 2006 – Aug 2019), converted to Markdown for a static-site relaunch.

## What's here

- `content/posts/` — 179 posts as `YYYY-MM-DD-slug.md`, with front matter: `title`, `date`, `slug`, `permalink` (original `/YYYY/MM/slug/` URL), `categories`, `tags`, `original_urls`, `wayback_source`, `excerpt_only`.
- `content/pages/` — 6 static pages (Bio, Presentations, Presentation Abstracts, Dayton Code & Coffee, Lap Around WPF, Missing Pieces abstract).
- `content/images/` — 53 recovered images. Posts reference them as `/images/<original path>` (external ones under `/images/external/<host>/`).
- `content/INDEX.md` — every post with excerpt and missing-image flags.
- `content/images-missing.txt` — 173 image URLs that Wayback never captured; `content/posts_missing_imgs.txt` lists the affected posts.
- `raw/` — the 1,028 untouched Wayback captures (`raw/index.tsv` maps file → timestamp → URL). Keep this; it's the source of truth.
- `cdx/` — Wayback CDX inventories used to choose captures.
- `scripts/` — the pipeline.

## Coverage

The 2019 site paginated 5 posts/page across 36 pages (~176–180 posts). 179 posts were recovered, including a few Community Server–era (2006–2008) posts that never made it into WordPress. Archive-widget month counts (2005-12 through 2012-02) match exactly.

Gaps:
- 6 posts survive only as listing-page excerpts (no full capture exists anywhere): Notes, WPF Bootcamp Day 1 – DataTemplates, Personal Backup with Mozy, "We're Agile, We do Scrum", Easy Github Code Reviews with diffgist in PsGist, Crickets: Messages Are Only Useful If Received.
- 173 images were never archived (mostly 2010–2013 Windows Live Writer screenshots and Community Server attachments). Those links still point at the dead original URLs.
- Comments and file downloads (`/files/...` attachments such as code samples) were not recovered.
- Days on a few listing-only posts default to `-01` when the page didn't show a day.

## Re-running

Run from this `recovery/` directory. The output lands in `content/`; copy `content/posts`, `content/pages` and `content/images` into `../src/` to update the site. `../src/posts` is the source of truth once you start editing posts there; re-extracting would overwrite those edits, so diff before copying.

```
python3 -I scripts/select_captures.py cdx/domain.txt cdx/feedburner.txt > cdx/fetch.tsv
python3 -I scripts/fetch.py cdx/fetch.tsv raw          # ~75 min; Wayback rate-limits hard
uv run --no-project --with beautifulsoup4 --with lxml --with markdownify python -I scripts/extract.py raw content
uv run --no-project python -I scripts/images.py content
python3 -I scripts/relink.py content
```

## 2021 site (Contentful)

The 2021 Next.js site (`cromwellryan/cromwellhaus-com`) read 4 Contentful entries: 2 posts and 2 links to work published elsewhere. Next.js embeds each page's entries as `__NEXT_DATA__`, so the snapshots in `contentful/` (saved 2026-11-14 from https://cromwellhaus.com) hold them in full; no API token was needed. `/the-wpf-mindset` was a re-paste of the 2008 post and is skipped in favour of the original, which carries a `redirect_from` for it. The About page was hard-coded in that repo (`pages/about.js`) and was copied into `../src/pages/about.md` by hand.

```
python3 -I scripts/contentful.py contentful content --skip the-wpf-mindset
```
