import os
import glob
import re

base_dir = r'C:\Users\angam\Downloads\Leano Website V1'
html_files = glob.glob(os.path.join(base_dir, '**', '*.html'), recursive=True)

old_inserted_html = """<div class="footer-line contact-info" style="display: flex; flex-direction: column; gap: 15px;">
    <div style="display: flex; flex-wrap: wrap; gap: 20px;">
        <a class="footer-contact-text" href="tel:0104424895" style="display: flex; align-items: center; gap: 10px; min-width: 150px;"><div class="icon" style="color: #f6722b; font-size: 20px;"></div> 010 442 4895</a>
        <a class="footer-contact-text" href="tel:0614276602" style="display: flex; align-items: center; gap: 10px; min-width: 150px;"><div class="icon" style="color: #f6722b; font-size: 20px;"></div> 061 427 6602</a>
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 20px;">
        <a class="footer-contact-text" href="mailto:info@leanoenergy.com" style="display: flex; align-items: center; gap: 10px; min-width: 150px;"><div class="icon" style="color: #f6722b; font-size: 20px;"></div> info@leanoenergy.com</a>
        <a class="footer-contact-text" href="https://www.leanoenergy.com" style="display: flex; align-items: center; gap: 10px; min-width: 150px;"><div class="icon" style="color: #f6722b; font-size: 20px;"></div> www.leanoenergy.com</a>
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 20px;">
        <a class="footer-contact-text" href="#" style="display: flex; align-items: center; gap: 10px;"><div class="icon" style="color: #f6722b; font-size: 20px;"></div> 120 11th Street Parkmore Sandton 2196</a>
    </div>
</div>"""

original_html = '<div class="footer-line contact-info"><a class="footer-contact-text" href="tel:+1-234-567-89">+1-234-567-89 </a><a class="footer-contact-text" href="mailto:example@pbminfotech.com">example@pbmit.com</a></div>'

count = 0
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    if old_inserted_html in text:
        new_text = text.replace(old_inserted_html, original_html)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_text)
        count += 1
            
print(f'Reverted footer contact info in {count} files.')
