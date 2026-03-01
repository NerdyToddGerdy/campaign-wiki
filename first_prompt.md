Build me a D&D campaign wiki as a Docusaurus site to be hosted on GitHub Pages.
World & Campaign Structure
The wiki covers a single shared world with two separate campaigns running in it. Content should be organized as:

World-level content (shared between both campaigns): locations, NPCs, factions, deities, lore, items
Campaign-specific content: session logs, party members, plot threads — but fully visible to both campaigns

Content Types & Templates
Create markdown templates for each of the following:

NPC — name, race, class/role, location, faction affiliation, physical description, personality, player-known history, DM notes (hidden/excluded from public build)
Location — name, region, description, notable NPCs, connected locations, campaign appearances
Faction — name, goals, leadership, members, allied/rival factions
Deity — name, domain, symbol, worshippers, temple locations
Item — name, type, description, current owner, history
Session Log — session number, campaign name, date played, players present, summary, key events, NPCs encountered, loot gained, cliffhanger/next session hook
Plot Thread — name, campaign, status (active/resolved), related NPCs, related locations, summary

Proper Noun Auto-Linking
Build a Docusaurus plugin that scans all markdown content at build time and automatically converts any proper noun that matches an existing page title into an internal hyperlink. This should work across all content types and both campaigns.
Navigation Structure
Sidebar should be organized as:

World

Locations
NPCs
Factions
Deities
Lore
Items


Campaign 1 (placeholder name "Campaign One" for now)

Sessions
Party
Plot Threads


Campaign 2 (placeholder name "Campaign Two" for now)

Sessions
Party
Plot Threads



Search
Enable Docusaurus's built-in search so players can look up any proper noun quickly.
Public Deployment

Configure for GitHub Pages deployment
Set up a GitHub Actions workflow that automatically builds and deploys on every push to main
DM notes fields on any template should be excluded from the public build via a build-time content filter

Visual Style
Give it a fantasy/medieval aesthetic — dark background, parchment-style content cards, a serif or fantasy-style font for headings. Should feel like a living tome rather than a tech docs site.
Starter Content
Populate each template type with one example entry using placeholder fantasy content so I can see how everything renders and links together before I start adding real campaign content.