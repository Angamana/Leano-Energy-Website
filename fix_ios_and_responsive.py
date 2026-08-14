import os
import glob
import re

# ── iOS Nav Fix (JavaScript-based) ──
# The CSS-only approach doesn't fully work on iOS because position:fixed
# elements get trapped inside containers with overflow:hidden or transforms.
# Webflow's .w-nav-overlay is deeply nested inside .w-nav > header > hero/breadcrumb.
# The only reliable iOS fix is to use JS to move .w-nav-overlay to <body> when it opens.
#
# ── Responsive Squishing Fix ──
# Add a min-width to body so content never gets squished below the smallest
# designed breakpoint. The browser will add a horizontal scrollbar gracefully
# instead of distorting the layout.

IOS_NAV_JS = '''
<script id="ios-nav-body-portal">
(function() {
    // Detect iOS devices (iPhone, iPad, iPod) - all iOS browsers use WebKit
    var isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent) ||
                (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
    if (!isIOS) return;

    // Wait for DOM and Webflow to initialize
    function initIOSNavFix() {
        var navOverlay = document.querySelector('.w-nav-overlay');
        if (!navOverlay) return;

        var originalParent = navOverlay.parentNode;
        var moved = false;

        // Create a MutationObserver to watch for the overlay becoming visible
        var observer = new MutationObserver(function(mutations) {
            mutations.forEach(function(mutation) {
                if (mutation.type === 'attributes') {
                    var display = window.getComputedStyle(navOverlay).display;
                    var height = navOverlay.style.height || navOverlay.getAttribute('data-height');

                    if (display !== 'none' && !moved) {
                        // Move overlay to body so it escapes all containing contexts
                        document.body.appendChild(navOverlay);
                        moved = true;

                        // Force fullscreen on iOS
                        navOverlay.style.position = 'fixed';
                        navOverlay.style.top = '0';
                        navOverlay.style.left = '0';
                        navOverlay.style.right = '0';
                        navOverlay.style.bottom = '0';
                        navOverlay.style.width = '100vw';
                        navOverlay.style.height = '100vh';
                        navOverlay.style.height = '100dvh';
                        navOverlay.style.zIndex = '9999999';
                        navOverlay.style.background = 'rgba(0, 0, 0, 0.75)';
                        navOverlay.style.webkitBackdropFilter = 'blur(14px)';
                        navOverlay.style.backdropFilter = 'blur(14px)';
                        navOverlay.style.overflowY = 'auto';
                        navOverlay.style.webkitOverflowScrolling = 'touch';
                    } else if (display === 'none' && moved) {
                        // Move it back when closed so Webflow can manage it
                        originalParent.appendChild(navOverlay);
                        moved = false;
                    }
                }
            });
        });

        observer.observe(navOverlay, {
            attributes: true,
            attributeFilter: ['style', 'data-height', 'class']
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            setTimeout(initIOSNavFix, 500);
        });
    } else {
        setTimeout(initIOSNavFix, 500);
    }
})();
</script>
'''

RESPONSIVE_CSS = '''
<style id="responsive-min-width-fix">
/* Prevent content squishing when browser window is narrower than design minimum */
/* This adds smooth horizontal scroll instead of distorting the layout */
@media screen and (min-width: 992px) {
    body {
        min-width: 992px;
    }
}
@media screen and (max-width: 991px) and (min-width: 768px) {
    body {
        min-width: 768px;
    }
}
@media screen and (max-width: 767px) and (min-width: 480px) {
    body {
        min-width: 480px;
    }
}
@media screen and (max-width: 479px) {
    body {
        min-width: 320px;
    }
}
</style>
'''

# Get all HTML files (excluding Reference and Cookie System)
html_files = glob.glob('**/*.html', recursive=True)
html_files = [f for f in html_files if 'Reference' not in f and 'Cookie System' not in f]

ios_count = 0
responsive_count = 0

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # 1. Add iOS nav JS if not already present
    if 'ios-nav-body-portal' not in content:
        # Insert before </body>
        if '</body>' in content:
            content = content.replace('</body>', IOS_NAV_JS + '</body>')
            ios_count += 1
            modified = True
    
    # 2. Add responsive min-width CSS if not already present
    if 'responsive-min-width-fix' not in content:
        # Insert before </head>
        if '</head>' in content:
            content = content.replace('</head>', RESPONSIVE_CSS + '</head>')
            responsive_count += 1
            modified = True
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print(f'iOS nav JS fix added to {ios_count} files')
print(f'Responsive min-width fix added to {responsive_count} files')
