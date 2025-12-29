```text
////////////////////////////////////////////////////////////////////////////////
//
//   A R N A U D   L E R O Y   +   S T U D I O
//   =========================================
//   system_ver: 1.0.5 [golden_master]
//   build_date: dec 29 2025
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

> index.html ........... [root] the manifesto entry point
> studio.html .......... [core] the identity / philosophy
> projects.html ........ [list] the archive of works
> game.html ............ [module] the interactive defense system
> 404.html ............. [error] "signal lost" custom page
> secret.html .......... [hidden] non-indexed easter egg
> style.css ............ [skin] visual syntax / glass panels / grain engine
> components.js ........ [logic] auto-header / auto-footer / favicon-switcher

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
  - Mechanic ........... "Dynamic Flashlight" (Light follows the player cursor).
  - Physics ............ Speed increased.
  - Loot ............... "Hearts" fall from the sky to restore life.
  - Atmosphere ......... Grain intensity reduced for "Deep Black" OLED feel.

* SCORE MEMORY:
  - High scores are saved to the user's local machine (localStorage).


[ 04 ] INTERACTION + SECRET LAYERS
--------------------------------------------------------------------------------
The system rewards curiosity. There is a hidden layer beneath the content.

* THE FLASHLIGHT (Dark Mode Only):
  - When the lights go out (Moon Icon), the cursor becomes a light source.
  - It reveals hidden text elements that have 'display: none' in light mode.
  - It uses a 'radial-gradient' mask to "cut" through the darkness layer.

* ADDING SECRETS:
  <div class="easter-egg">
      your_secret_text_here
  </div>
  (These elements sit at z-index: 5, technically *below* the dark overlay, 
   only visible when illuminated).


[ 05 ] ADDING A NEW PROJECT
--------------------------------------------------------------------------------
1. Duplicate an existing project file (e.g., project-maison-automata.html).
2. Rename it (e.g., project-new-concept.html).
3. Open 'projects.html' and add a new entry to the list:

   <a href="project-new-concept.html" class="project-row">
       <span>0X</span>
       <span>
           project name <span class="plus">+</span> subtitle
           <span class="status-badge status-ongoing">ongoing</span>
       </span>
       <span>DATE</span>
   </a>


[ 06 ] SYNTAX RULES (STRICT)
--------------------------------------------------------------------------------
1. NO COMMAS ........... Replace with <span class="plus">+</span>
2. LOWERCASE ........... All brand text must be lowercase (humility).
3. IMAGES .............. Use .image-frame for the standard border/filter.
4. LINKS ............... Use .big-link for emphasis, .back-link for nav.
5. SITEMAP ............. Excludes 'secret.html' to prevent Google indexing.


////////////////////////////////////////////////////////////////////////////////
// END OF FILE
// "curating ideas + designing emotions + crafting the intangible"
////////////////////////////////////////////////////////////////////////////////