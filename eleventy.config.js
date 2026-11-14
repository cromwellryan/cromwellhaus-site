import pluginRss from "@11ty/eleventy-plugin-rss";
import syntaxHighlight from "@11ty/eleventy-plugin-syntaxhighlight";

export default function (eleventyConfig) {
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
  // Unique legacy Community Server (.aspx) paths for a post, for _redirects.
  eleventyConfig.addFilter("legacyPaths", (urls) => {
    const paths = new Set();
    for (const u of urls || []) {
      try {
        const p = decodeURI(new URL(u).pathname).replace(/^\/CS\/blogs\//, "/blogs/");
        if (p.endsWith(".aspx")) paths.add(p);
      } catch {}
    }
    return [...paths];
  });

  eleventyConfig.amendLibrary("md", (md) => md.set({ html: true, linkify: false, typographer: false }));

  return {
    dir: { input: "src", output: "_site", includes: "_includes", data: "_data" },
    // Recovered posts contain code samples with {{ }} / {% %}; never run them through a template engine.
    markdownTemplateEngine: false,
    htmlTemplateEngine: "njk",
  };
}
