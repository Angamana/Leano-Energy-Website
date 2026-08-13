import os, glob
import re
html_files = glob.glob('**/*.html', recursive=True)
fix_css = '''
    @supports (-webkit-touch-callout: none) {
        .hero-one-section, .breadcrumb-section, .w-slider, .header, .header-main {
            transform: none !important;
            -webkit-transform: none !important;
            overflow: visible !important;
            clip-path: none !important;
        }
    }
'''
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'id=\"ios-nav-fullscreen-fix\"' in content:
        if '@supports (-webkit-touch-callout: none)' not in content:
            content = content.replace('/* Force Webflow mobile nav overlay', fix_css + '    /* Force Webflow mobile nav overlay')
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
print('iOS fix applied to all files')
