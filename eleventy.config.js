import { HtmlBasePlugin } from "@11ty/eleventy";
import pluginRss from "@11ty/eleventy-plugin-rss";
import syntaxHighlight from "@11ty/eleventy-plugin-syntaxhighlight";

// Unique legacy Community Server (.aspx) paths for a post.
function legacyPaths(urls) {
  const paths = new Set();
  for (const u of urls || []) {
    try {
      const p = decodeURI(new URL(u).pathname).replace(/^\/CS\/blogs\//, "/blogs/");
      if (p.endsWith(".aspx")) paths.add(p);
    } catch {}
  }
  return [...paths];
}

export default function (eleventyConfig) {
  // Prefixes root-relative URLs in HTML output with pathPrefix (e.g. /cromwellhaus-site/ on github.io).
  eleventyConfig.addPlugin(HtmlBasePlugin);
  eleventyConfig.addPlugin(pluginRss);
  // Build-time Prism highlighting for ```lang fences; no client JS.
  eleventyConfig.addPlugin(syntaxHighlight, { preAttributes: { tabindex: 0 } });
  eleventyConfig.addPassthroughCopy("src/images");
  eleventyConfig.addPassthroughCopy("src/css");

  // Newest first.
  eleventyConfig.addCollection("posts", (api) =>
    api.getFilteredByGlob("src/posts/*.md").sort((a, b) => b.date - a.date)
  );

  // { "Agile": [posts...], ... } sorted by name.
  eleventyConfig.addCollection("categories", (api) => {
    const map = new Map();
    for (const post of api.getFilteredByGlob("src/posts/*.md").sort((a, b) => b.date - a.date)) {
      for (const cat of post.data.categories || []) {
        if (!map.has(cat)) map.set(cat, []);
        map.get(cat).push(post);
      }
    }
    return [...map.entries()]
      .sort(([a], [b]) => a.localeCompare(b, undefined, { sensitivity: "base" }))
      .map(([name, posts]) => ({ name, posts }));
  });

  // [{ year, posts }] newest year first.
  eleventyConfig.addCollection("postsByYear", (api) => {
    const years = new Map();
    for (const post of api.getFilteredByGlob("src/posts/*.md").sort((a, b) => b.date - a.date)) {
      const y = post.date.getUTCFullYear();
      if (!years.has(y)) years.set(y, []);
      years.get(y).push(post);
    }
    return [...years.entries()].map(([year, posts]) => ({ year, posts }));
  });

  eleventyConfig.addFilter("readableDate", (d) =>
    new Intl.DateTimeFormat("en-US", { dateStyle: "long", timeZone: "UTC" }).format(d)
  );
  eleventyConfig.addFilter("head", (arr, n) => arr.slice(0, n));
  eleventyConfig.addFilter("isoDate", (d) => d.toISOString().slice(0, 10));
  // Plain-text teaser from rendered HTML.
  eleventyConfig.addFilter("summary", (html, n = 280) => {
    const text = String(html || "")
      .replace(/<(script|style|pre)[\s\S]*?<\/\1>/gi, " ")
      .replace(/<[^>]+>/g, " ")
      .replace(/&#(\d+);/g, (_, n) => String.fromCodePoint(Number(n)))
      .replace(/&#x([0-9a-f]+);/gi, (_, n) => String.fromCodePoint(parseInt(n, 16)))
      .replace(/&(nbsp|lt|gt|quot|apos|amp);/g, (_, e) => ({ nbsp: " ", lt: "<", gt: ">", quot: '"', apos: "'", amp: "&" })[e])
      .replace(/\s+/g, " ")
      .replace(/\s+([.,;:!?)])/g, "$1")
      .trim();
    return text.length > n ? text.slice(0, text.lastIndexOf(" ", n)) + "…" : text;
  });
  eleventyConfig.addFilter("legacyPaths", legacyPaths);

  // [{ from, to }] for every old URL; rendered as _redirects and as HTML stubs (GitHub Pages ignores _redirects).
  eleventyConfig.addCollection("redirects", (api) => {
    const map = new Map([
      ["/feed/", "/feed.xml"],
      ["/feed/atom/", "/feed.xml"],
      ["/blogs/ryanc/rss.aspx", "/feed.xml"],
    ]);
    const posts = api.getFilteredByGlob("src/posts/*.md").filter((p) => p.url);
    for (const post of posts) {
      for (const from of [...(post.data.redirect_from || []), ...legacyPaths(post.data.original_urls)]) {
        map.set(from, post.url);
      }
    }
    // WordPress /tag/x/ archives -> the category of the same name, where there is one.
    const slugify = eleventyConfig.getFilter("slugify");
    for (const cat of new Set(posts.flatMap((p) => p.data.categories || []))) {
      map.set(`/tag/${slugify(cat)}/`, `/category/${slugify(cat)}/`);
    }
    return [...map].map(([from, to]) => ({ from, to }));
  });
  // Output file for a redirect stub: /a/b.aspx -> /a/b.aspx/index.html (Pages 301s /a/b.aspx to the slash form).
  eleventyConfig.addFilter("stubPath", (from) => (from.endsWith("/") ? from : from + "/") + "index.html");

  eleventyConfig.amendLibrary("md", (md) => md.set({ html: true, linkify: false, typographer: false }));

  return {
    dir: { input: "src", output: "_site", includes: "_includes", data: "_data" },
    // CI sets PATH_PREFIX from the Pages base path; "/" once a custom domain is in place.
    pathPrefix: process.env.PATH_PREFIX || "/",
    // Recovered posts contain code samples with {{ }} / {% %}; never run them through a template engine.
    markdownTemplateEngine: false,
    htmlTemplateEngine: "njk",
  };
}
