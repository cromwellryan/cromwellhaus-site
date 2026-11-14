// SITE_URL is set by CI to the GitHub Pages URL (no trailing slash); production default below.
export default {
  url: process.env.SITE_URL || "https://cromwellhaus.com",
  title: "Ryan Cromwell",
  description: "Software, teams, and the craft of building things — writing since 2005.",
  author: "Ryan Cromwell",
  intro: "I've been building software professionally for more than 20 years and leading the teams that build it for much of that. I write about engineering leadership, delivery, and the craft of making things.",
  nav: [
    { label: "Archive", url: "/archive/" },
    { label: "Categories", url: "/category/" },
    { label: "Presentations", url: "/presentations/" },
    { label: "About", url: "/about/" },
  ],
};
