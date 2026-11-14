# cromwellhaus.com

Markdown blog built with [Eleventy](https://www.11ty.dev/) 3. Content was recovered from the Wayback Machine (see `~/projects/cromwellhaus-recovery`).

## Run

```
npm install
npm start          # dev server with live reload at http://localhost:8080
npm run build      # static output in _site/
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

`permalink` is optional; without it Eleventy uses `/posts/2026-11-20-my-post/`. Markdown is not run through a template engine, so `{{ }}` in code samples is safe.

Recovered posts carry extra front matter (`original_urls`, `wayback_source`, `excerpt_only`). The post layout uses the last two to show a provenance link and an "excerpt only" notice; delete them from a post once you've restored or rewritten it.

## Deploying

Any static host works: build command `npm run build`, publish directory `_site`. `_site/_redirects` is in Netlify / Cloudflare Pages format; on other hosts, translate it or drop it.

## Known gaps from the recovery

- 6 posts are excerpt-only (they show a notice).
- 173 images were never archived; those `<img>` tags still point at the dead original URLs. List: `~/projects/cromwellhaus-recovery/content/images-missing.txt`.
- No comments.
