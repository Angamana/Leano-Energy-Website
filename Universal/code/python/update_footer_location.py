import os
import glob
import re

base_dir = r'C:\Users\angam\Downloads\Leano Website V1'
html_files = glob.glob(os.path.join(base_dir, '**', '*.html'), recursive=True)

count = 0
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # We want to find the section with Newsletter Subscription and replace it
    # Pattern: 
    # <div class="footer-title">Newsletter Subscription</div>\s*</div>\s*<div class="footer-line contact-info">.*?</div>
    
    old_pattern = r'<div class="footer-title">Newsletter Subscription</div>\s*</div>\s*<div class="footer-line contact-info">.*?</div>'
    
    # We replace it with:
    new_html = (
        '<div class="footer-title">LOCATION</div>\n'
        '</div>\n'
        '<div class="footer-line contact-info">\n'
        '<a class="footer-contact-text" href="https://maps.google.com/?q=120+11th+Street+Parkmore+Sandton+2196" target="_blank">\n'
        '120 11th Street<br>Parkmore Sandton 2196\n'
        '</a>\n'
        '</div>'
    )
    
    if re.search(old_pattern, text):
        new_text = re.sub(old_pattern, new_html, text)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_text)
        count += 1

print(f"Updated Newsletter Subscription to Location in {count} files.")
