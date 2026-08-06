import os
import glob
import re

base_dir = r'C:\Users\angam\Downloads\Leano Website V1'
html_files = glob.glob(os.path.join(base_dir, '**', '*.html'), recursive=True)

count = 0
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # We are looking for the contact info line:
    # <div class="footer-line contact-info"><a class="footer-contact-text" href="tel:+1-234-567-89">+1-234-567-89 </a><a class="footer-contact-text" href="mailto:example@pbminfotech.com">example@pbmit.com</a></div>
    
    # To be safe against minor whitespace differences, we can use a regex that targets the specific placeholder text
    # Let's target the exact string first
    
    old_html = r'<div class="footer-line contact-info"><a class="footer-contact-text" href="tel:\+1-234-567-89">\+1-234-567-89 </a><a class="footer-contact-text" href="mailto:example@pbminfotech.com">example@pbmit.com</a></div>'
    new_html = r'<div class="footer-line contact-info"><a class="footer-contact-text" href="tel:0104424895">010 442 4895</a><a class="footer-contact-text" href="tel:0614276602">061 427 6602</a><a class="footer-contact-text" href="mailto:info@leanoenergy.com">info@leanoenergy.com</a></div>'
    
    if re.search(old_html, text):
        new_text = re.sub(old_html, new_html, text)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_text)
        count += 1

print(f"Updated footer contact information in {count} files.")
