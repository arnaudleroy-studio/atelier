/**
 * /////////////////////////////////////////////////////////////////////////////
 * //
 * //   L O G I C   C O N T R O L L E R
 * //   ===============================
 * //   file: components.js
 * //   tasks:
 * //     [1] auto-inject header/footer
 * //     [2] manage dual-mode favicons
 * //     [3] detect konami code sequences
 * //
 * /////////////////////////////////////////////////////////////////////////////
 * 
 *     /++++++  /++       
 *    /++__  ++| ++       
 *   | ++  \ ++| ++       
 *   | ++++++++| ++       
 *   | ++__  ++| ++        
 *   | ++  | ++| ++       
 *   | ++  | ++| ++++++++ 
 *   |__/  |__/|________/ 
 * 
 */
// =============================================================================
// [ 01 ] FAVICON ENGINE (Refined)
// =============================================================================
function updateFavicon(isDarkMode) {
    // 1. Define Colors
    const bgColor = isDarkMode ? "#FAEBD7" : "#002366"; // Cream vs Blue
    const textColor = isDarkMode ? "#002366" : "#FAEBD7"; // Blue vs Cream

    // 2. Define the SVG String (The Mechanical Plus)
    const svgString = `
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
      <rect width="64" height="64" fill="${bgColor}"/>
      <text x="50%" y="55%" 
            dominant-baseline="middle" 
            text-anchor="middle" 
            font-family="monospace" 
            font-size="42" 
            font-weight="bold" 
            fill="${textColor}">+</text>
    </svg>`.trim();

    // 3. Convert to Base64
    const base64Icon = btoa(svgString);
    const dataURI = `data:image/svg+xml;base64,${base64Icon}`;

    // 4. Inject
    let link = document.querySelector("link[rel*='icon']");
    if (link) {
        document.head.removeChild(link);
    }
    
    link = document.createElement('link');
    link.rel = 'icon';
    link.type = 'image/svg+xml';
    link.href = dataURI;
    document.head.appendChild(link);
}

// =============================================================================
// [ 02 ] HEADER COMPONENT (UPDATED WITH HAMBURGER)
// =============================================================================
const HEADER_HTML = `
    <div class="brand-container">
        <a href="index.html" class="brand-link">
            <span class="brand-name">arnaud leroy</span>
        </a>
    </div>

    <div class="mobile-toggle">
        <span></span>
        <span></span>
    </div>

    <nav class="mono-font">
        <ul>
            <li><a href="projects.html">projects</a></li>
            <li><a href="studio.html">studio</a></li>
            <li><a href="journal.html">journal</a></li>
            <li><a href="contact.html">contact</a></li>
        </ul>
    </nav>
`;

// =============================================================================
// [ 03 ] FOOTER COMPONENT
// =============================================================================
const FOOTER_HTML = `
    <div>c 2024 arnaud leroy</div>
    
    <div class="footer-center"> 
        multidisciplinary design<br>
        studio based in lisbon <span class="plus">+</span> paris <span class="plus">+</span> tokyo
    </div>
    
    <div style="text-align: right; color: var(--accent-blue); display: flex; align-items: center; justify-content: flex-end;">
        a l <span class="plus">+</span> studio
        
        <div id="mode-toggle" title="Toggle Theme">
            <svg class="sun-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="5"></circle>
                <line x1="12" y1="1" x2="12" y2="3"></line>
                <line x1="12" y1="21" x2="12" y2="23"></line>
                <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
                <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
                <line x1="1" y1="12" x2="3" y2="12"></line>
                <line x1="21" y1="12" x2="23" y2="12"></line>
                <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
                <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
            </svg>
            
            <svg class="moon-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
            </svg>
        </div>
    </div>
`;


// =============================================================================
// [ 04 ] ANALYTICS SENSOR (GoatCounter)
// =============================================================================
// "Measuring the signal without the noise."
// Privacy-friendly, no cookies, no banners.
function injectAnalytics() {
    // Only run on the live site (prevents tracking your local edits)
    if (window.location.hostname === "arnaudleroy.com") {
        const script = document.createElement('script');
        script.async = true;
        script.dataset.goatcounter = 'https://arnaudleroy.goatcounter.com/count';
        script.src = '//gc.zgo.at/count.js';
        document.head.appendChild(script);
        console.log("System: Signal sensor active.");
    }
}

// =============================================================================
// [ 05 ] NAVIGATION LOGIC
// =============================================================================
function setActiveLink() {
    const path = window.location.pathname;
    const page = path.split("/").pop();
    
    document.querySelectorAll('nav a').forEach(link => {
        if(link.getAttribute('href') === page) {
            link.classList.add('active');
        }
    });
}

// =============================================================================
// [ 06 ] FLASHLIGHT ENGINE
// =============================================================================
function initFlashlight() {
    if (!document.getElementById('flashlight')) {
        const f = document.createElement('div');
        f.id = 'flashlight';
        document.body.appendChild(f);
    }

    const f = document.getElementById('flashlight');
    document.addEventListener('mousemove', (e) => {
        f.style.setProperty('--x', e.clientX + 'px');
        f.style.setProperty('--y', e.clientY + 'px');
    });
}

// =============================================================================
// [ 07 ] DARK MODE SYSTEM
// =============================================================================
function initDarkMode() {
    const btn = document.getElementById('mode-toggle');
    const body = document.body;

    const applyMode = (isDark) => {
        if (isDark) {
            body.classList.add('dark-mode');
            localStorage.setItem('theme', 'dark');
        } else {
            body.classList.remove('dark-mode');
            localStorage.setItem('theme', 'light');
        }
        updateFavicon(isDark);
    };

    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        applyMode(true);
    } else {
        applyMode(false);
    }

    if(btn) {
        btn.addEventListener('click', () => {
            const isCurrentlyDark = body.classList.contains('dark-mode');
            applyMode(!isCurrentlyDark);
        });
    }
}

// =============================================================================
// [ 08 ] MOBILE MENU LOGIC (ADDED)
// =============================================================================
function initMobileMenu() {
    const toggle = document.querySelector('.mobile-toggle');
    const nav = document.querySelector('nav');
    
    if(toggle && nav) {
        toggle.addEventListener('click', () => {
            toggle.classList.toggle('active');
            nav.classList.toggle('active');
            
            // Prevent scrolling when menu is open
            if(nav.classList.contains('active')) {
                document.body.style.overflow = 'hidden';
            } else {
                document.body.style.overflow = '';
            }
        });
    }
}

// =============================================================================
// [ 09 ] INITIALIZATION
// =============================================================================
document.addEventListener("DOMContentLoaded", function() {
    
    // Inject Header
    const headerContainer = document.querySelector('header');
    if(headerContainer) { 
        headerContainer.innerHTML = HEADER_HTML; 
        setActiveLink(); 
    }

    // Inject Footer
    const footerContainer = document.querySelector('footer');
    if(footerContainer) { 
        footerContainer.innerHTML = FOOTER_HTML; 
    }

    injectAnalytics();

    // Boot Systems
    initFlashlight();
    initDarkMode();
    initMobileMenu(); 
   
    console.log(
        "%c arnaud leroy + studio \n%c system: online \n%c silence is a material", 
        "font-family: 'Rockwell', serif; font-size: 20px; color: #002366; font-weight: bold;",
        "font-family: 'Courier New', monospace; font-size: 12px; color: #A0A0A0;",
        "font-family: 'Courier New', monospace; font-size: 12px; color: #002366;"
    );

});

document.addEventListener('copy', function(e) {
    const selection = window.getSelection().toString();
    // Only stamp if they copy more than 20 characters (prevents annoyance on small copies)
    if (selection.length > 20) {
        const stamp = `\n\n\n[offered with love by: arnaudleroy.com]`;
        e.clipboardData.setData('text/plain', selection + stamp);
        e.preventDefault(); // Prevent default copy to inject our version
    }
});


// =============================================================================
// [ 10 ] PAGE VISIBILITY LOGIC (Ghost Mode)
// =============================================================================
document.addEventListener('visibilitychange', function() {
    if (document.hidden) {
        document.title = " + ";
    } else {
        document.title = "a l + studio"; // Or restore original title
    }
});

// =============================================================================
// [ 11 ] GLOBAL X-RAY BLUEPRINT MODE
// =============================================================================
// Hold [ ALT ] (or Option on Mac) to reveal system architecture.

document.addEventListener('keydown', (e) => {
    if (e.key === 'Alt') {
        document.body.classList.add('blueprint-mode');
    }
});

document.addEventListener('keyup', (e) => {
    if (e.key === 'Alt') {
        document.body.classList.remove('blueprint-mode');
    }
});