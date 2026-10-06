```text
////////////////////////////////////////////////////////////////////////////////
//
//   A R N A U D   L E R O Y   +   S T U D I O
//   =========================================
//   system_ver: 1.1.0 [signal restored]
//   build_date: dec 29 2025 + rev oct 06 2026
//   auth: [a.l.]
//
////////////////////////////////////////////////////////////////////////////////

      /++++++  /++        
     /++__  ++| ++        
    | ++  \ ++| ++        
    | ++++++++| ++        
    | ++__  ++| ++        
    | ++  | ++| ++        
    | ++  | ++| ++++++++  
    |__/  |__/|________/  
                          

[ 01 ] SYSTEM ARCHITECTURE + PHILOSOPHY
--------------------------------------------------------------------------------
The studio is not just a website; it is an interactive OS built on "Silence."
It rejects modern frameworks (React, Vue) in favor of raw, timeless code.

> index.html ........... [root] the manifesto entry point          index 01
> projects.html ........ [list] the archive of works                index 02
> studio.html .......... [core] the identity / philosophy           index 03
> journal.html ......... [log] thoughts + sealed entries            index 04
> contact.html ......... [signal] the way in                        index 05
> game.html ............ [module] the interactive defense system    index 06
> blog/ ................ [notes] technical writing                  index 07
> project-*.html ....... [works] one page per project (01 + 11)
> 404.html ............. [error] "signal lost" custom page (noindex)
> secret.html .......... [hidden] the backstage (noindex)
> style.css ............ [skin] visual syntax / glass panels / grain engine
> components.js ........ [logic] auto-header / auto-footer / favicon-switcher
> humans.txt ........... [credits] who built the machine

* PATHS: every internal link + asset is root-absolute (/style.css, /projects.html)
  so the 404 page and /blog/ render correctly at any depth.
* HEAD: every page carries the same block: title + description + canonical +
  og + twitter + theme-color + icons + fonts. 404 + secret are noindex.
* THEME: a one-line script right after <body> applies dark mode before paint
  (no flash). components.js then wires the toggle.

* MATERIALITY: The interface mimics "digital glass." Panels use backdrop-filter 
  to blur the noise behind them, creating depth without solidity.
* SCROLLBAR: Custom thin-line track. It is barely there, prioritizing content.


[ 02 ] VISUAL IDENTITY + ASSETS
--------------------------------------------------------------------------------
The brand is defined by high contrast and strict typographic rules.

* COLORS:
  - Navy Blue .......... #002366 (The Void)
  - Cream White ........ #FAEBD7 (The Signal)

* DYNAMIC ICONS (Favicons):
  - Logic handled by 'components.js'.
  - Light Mode ......... Blue '+' on Cream Background.
  - Dark Mode .......... Cream '+' on Navy Background (Inverse).

* MOBILE PRESENCE (iOS):
  - App Name ........... "+" (Discrete, abstract, functional).
  - Home Icon .......... Navy Square with Cream '+' (apple-touch-icon.png).
  - Status Bar ......... Matches the theme color dynamically.

* SOCIAL CARD (OpenGraph):
  - File ............... share-image.jpg (1200x630).
  - Visual ............. Giant Cream '+' on Navy Void.


[ 03 ] THE SYSTEM MODULE (GAME ENGINE)
--------------------------------------------------------------------------------
A hidden arcade engine embedded in the site. "Silence is a material, Noise is the enemy."

* ACCESS POINTS:
  1. URL ............... /game.html
  2. KONAMI CODE ....... Type "p-l-a-y" on the homepage. Screen inverts & redirects.

* DUAL-MODE MECHANIC:
  The game physically changes based on the website's lighting mode.

  [MODE A] SYSTEM EVASION (Light Mode)
  - Visual ............. Clean, bright, visible.
  - Life ............... 3 Hearts.
  - Goal ............... Avoid the # / X / NOISE characters.

  [MODE B] NIGHTMARE DRIVE (Dark Mode)
  - Visual ............. Pitch black.
  - Mechanic ........... "Dynamic Flashlight" (light follows the player).
  - Physics ............ Speed increased.
  - Atmosphere ......... Grain intensity reduced for "Deep Black" OLED feel.

* SHARED MECHANICS:
  - Hearts ............. Fall in both modes. Restore one life (max 5).
  - Focus [SPACE] ...... Slows time + dampens the audio. Fed by blue [+].
  - Combo .............. x2 + x4 + x8 on consecutive catches. A hit resets it.
  - Glitch storm ....... Every 30s for 5s. Colors invert + noise floods in +
                         survival points are doubled.
  - Auto pause ......... Leaving the tab pauses the system.

* SCORE MEMORY:
  - Best score saved locally (localStorage key: al_arcade_best).


[ 04 ] INTERACTION + SECRET LAYERS
--------------------------------------------------------------------------------
The system rewards curiosity. There is a hidden layer beneath the content.

* THE FLASHLIGHT (Dark Mode Only):
  - When the lights go out (Moon Icon), the cursor becomes a light source.
  - It reveals hidden text elements that have 'display: none' in light mode.
  - It uses a 'radial-gradient' mask to "cut" through the darkness layer.

* THE FULL MAP OF SECRETS:
  - Dark mode ........... cursor becomes a lantern + hidden text on every page
  - "play" .............. typed on the homepage opens the arcade
  - ( r o r r i m ) ..... bottom right of studio in the dark + leads to secret.html
  - [ ALT ] ............. hold anywhere for x-ray blueprint mode
  - Ghost title ......... leave the tab + the title becomes " + "
  - Console ............. the system says hello
  - Copy stamp .......... copying 20+ characters signs the clipboard
  - Print ............... any page prints as a framed archive document
  - Manifesto ........... project-birth-studio.html downloads manifesto.txt
  - Uptime .............. the studio counts its own age since 2024
  - Oracle .............. tap the phone on project-the-oracle.html
  - 404 ................. dark mode reveals the signal-lost matrix
  - Backstage ........... secret.html counts your visits (this browser only)

* ADDING SECRETS:
  <div class="easter-egg">
      your_secret_text_here
  </div>
  (These elements sit at z-index: 5, technically *below* the dark overlay, 
   only visible when illuminated).


[ 05 ] ADDING A NEW PROJECT
--------------------------------------------------------------------------------
1. Duplicate an existing project file (data projects: project-coffeetrove.html
   / project-benchgecko.html + concept projects: project-maison-automata.html).
2. Rename it (e.g., project-new-concept.html). Update the axis label number.
3. Open 'projects.html' and add a row at the TOP (newest first):

   <a href="/project-new-concept.html" class="project-row" data-category="digital data">
       <span class="p-id">12</span>
       <div class="p-content">
           <h2 class="p-title">project name</h2>
           <div class="tag-container"><span class="tag-pill tag-digi">web</span></div>
           <span class="p-desc">subtitle <span class="plus-spin">+</span> subtitle</span>
       </div>
       <span class="p-year">2026</span>
   </a>

4. Add the page to the head metadata table (title + description) and to
   sitemap.xml. Filters: architecture + digital + data + game + fashion + research.


[ 05.5 ] MAINTENANCE TOOLS (_tools/ + not served by github pages)
--------------------------------------------------------------------------------
> python3 _tools/head.py ...... rebuilds every <head> from ONE table: title +
                                description + canonical + og + json-ld. New page?
                                add a row there first.
> python3 _tools/links.py ..... rewrites the "next project" trail on every
                                project page (order lives in the script).
> python3 _tools/og.py ........ renders /og/<slug>.jpg share cards (1200x630)
                                in rockwell + courier on the void.
> sh _tools/indexnow.sh ....... after a deploy: tells bing + yandex every url
                                in the sitemap changed.
* Header + footer are prerendered in each page for crawlers that skip js.
  components.js re-injects them, so after changing HEADER_HTML / FOOTER_HTML
  paste the same markup into the pages (or ask the machine to).


[ 06 ] SYNTAX RULES (STRICT)
--------------------------------------------------------------------------------
1. NO COMMAS ........... Replace with <span class="plus">+</span>
2. LOWERCASE ........... All brand text must be lowercase (humility).
3. IMAGES .............. Use .image-frame for the standard border/filter.
4. LINKS ............... Use .big-link for emphasis, .back-link for nav.
5. SITEMAP ............. Excludes 'secret.html' + '404.html' (both noindex).
6. NUMBERS ............. Figures carry a date ("graph snapshot + march 2026").
                         Never invent a metric. A redacted block beats a fake one.


## DropThe

This project is part of the [DropThe](https://dropthe.org) data platform — a media network tracking 1.83 million entities across movies, games, companies, people, crypto, and countries, connected by 2.18 million knowledge graph links.

- [dropthe.org](https://dropthe.org)
- [Data Insights](https://dropthe.org/data/)
- [Statistics](https://dropthe.org/data/statistics/movies/)
- [@dropthehq](https://x.com/dropthehq)



////////////////////////////////////////////////////////////////////////////////
// END OF FILE
// "curating ideas + designing emotions + crafting the intangible"
////////////////////////////////////////////////////////////////////////////////
