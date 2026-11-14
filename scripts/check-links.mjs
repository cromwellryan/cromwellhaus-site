// Fail if any internal href/src/meta-refresh in the built site points at a file that doesn't exist.
// Usage: node scripts/check-links.mjs [_site] [pathPrefix]
import { existsSync, readdirSync, readFileSync, statSync } from "node:fs";
import { join } from "node:path";

const root = process.argv[2] || "_site";
const prefix = (process.argv[3] || "/").replace(/\/?$/, "/");
const REF = /\s(?:href|src)="([^"#?]*)|http-equiv="refresh" content="\d+; url=([^"#?]*)/g;

function* htmlFiles(dir) {
  for (const name of readdirSync(dir)) {
    const p = join(dir, name);
    if (statSync(p).isDirectory()) yield* htmlFiles(p);
    else if (p.endsWith(".html")) yield p;
  }
}

const resolves = (url) => {
  const p = join(root, decodeURI(url));
  return existsSync(p) && (statSync(p).isFile() || existsSync(join(p, "index.html")));
};

let refs = 0;
const broken = [];
for (const file of htmlFiles(root)) {
  for (const [, attr, refresh] of readFileSync(file, "utf8").matchAll(REF)) {
    const url = attr ?? refresh;
    if (!url.startsWith("/") || url.startsWith("//")) continue;
    refs++;
    if (!url.startsWith(prefix) || !resolves(url.slice(prefix.length - 1))) broken.push(`${file.slice(root.length)} -> ${url}`);
  }
}

console.log(`${refs} internal refs, ${broken.length} broken`);
if (broken.length) {
  console.log(broken.join("\n"));
  process.exit(1);
}
