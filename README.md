# cromwellhaus.com

Markdown blog built with [Eleventy](https://www.11ty.dev/) 3. Content before 2021 was recovered from the Wayback Machine and the 2021 posts from the Contentful-backed site; the captures and scripts that produced `src/posts` live in `recovery/` (see `recovery/README.md`).

## Run

```
npm install
npm start          # dev server with live reload at http://localhost:8080
npm run build      # static output in _site/
npm run check-links  # fail on broken internal links/images in _site/
```

## Layout

```
src/
  posts/YYYY-MM-DD-slug.md   179 posts; URL comes from `permalink` (/YYYY/MM/slug/, same as WordPress)
  pages/*.md                 About, Presentations, etc. (each sets its own `permalink`)
  images/                    recovered images, referenced as /images/...
  _includes/layouts/         base, post, page (Nunjucks)
  _data/site.json            title, description, URL, nav
  css/style.css              the only stylesheet (light + dark)
  index.njk                  home, 10 per page (/page/N/)
  archive.njk, categories.njk, category.njk
  feed.njk                   Atom feed at /feed.xml
  redirects.njk              _redirects: /feed/ and old Community Server .aspx URLs -> new permalinks
scripts/check-links.mjs      internal link checker (run in CI)
recovery/                    Wayback captures + extraction scripts; not part of the build
.github/workflows/build.yml  CI: npm ci, build, check-links on every push and PR
```

## Writing a new post

Create `src/posts/2026-11-20-my-post.md`:

```markdown
---
title: "My post"
date: 2026-11-20
categories: ["Leadership"]
permalink: /2026/11/my-post/
---

Write here.
```

Optional front matter: `redirect_from: ["/old-path"]` adds 301s to `_redirects`; `external_url` (with `permalink: false`) makes a listing-only entry that links to something published elsewhere.

`permalink` is optional; without it Eleventy uses `/posts/2026-11-20-my-post/`. Markdown is not run through a template engine, so `{{ }}` in code samples is safe.

Recovered posts carry extra front matter (`original_urls`, `wayback_source`, `excerpt_only`). The post layout uses the last two to show a provenance link and an "excerpt only" notice; delete them from a post once you've restored or rewritten it.

## Deploying

Every push to `main` builds and deploys to GitHub Pages (`.github/workflows/build.yml`); pull requests build and link-check only. Live at https://cromwellryan.github.io/cromwellhaus-site/ until the custom domain is set.

- `PATH_PREFIX` / `SITE_URL` come from the Pages config, so the github.io build is served under `/cromwellhaus-site/`. Locally both default to `/` and https://cromwellhaus.com.
- GitHub Pages ignores `_redirects`, so every old URL also gets an HTML stub (`src/redirect-stubs.njk`, from the `redirects` collection) that meta-refreshes to the new permalink. `_redirects` is still emitted for Netlify / Cloudflare Pages.
- Feed readers don't follow meta refresh: subscribers on `/feed/` or `rss.aspx` need a real 301, which Pages can't do.

### Switching cromwellhaus.com to Pages

1. Repo Settings → Pages → Custom domain: `cromwellhaus.com` (enable Enforce HTTPS once the certificate is issued).
2. In DNSimple, replace the Heroku records: apex `A` records 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153 (and `AAAA` 2606:50c0:8000::153 … 8003::153), `www` `CNAME` cromwellryan.github.io.
3. Re-run the workflow (Actions → Build and deploy → Run workflow) so the build picks up the empty base path.

## Known gaps from the recovery

- 6 posts are excerpt-only (they show a notice).
- 173 images were never archived; those `<img>` tags still point at the dead original URLs. List: `recovery/content/images-missing.txt`.
- No comments.
