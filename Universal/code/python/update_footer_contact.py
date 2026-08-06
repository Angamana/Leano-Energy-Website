import os
import glob
import re

base_dir = r'C:\Users\angam\Downloads\Leano Website V1'
html_files = glob.glob(os.path.join(base_dir, '**', '*.html'), recursive=True)

new_contact_html = """<div class="footer-line contact-info" style="display: flex; flex-direction: column; gap: 15px;">
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

count = 0
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Replace the old footer contact info
    # The old structure is typically <div class="footer-line contact-info">...</div>
    # or similar. We will find it and replace it.
    
    # We will use a regex to match from `<div class="footer-line contact-info"` up to the next `</div>` 
    # but since it might contain nested `<a>` tags, we'll match up to `</a></div>` or `</a>\s*</div>`
    
    pattern = r'<div class="footer-line contact-info">.*?</a>\s*</div>'
    if re.search(pattern, text, flags=re.DOTALL):
        new_text = re.sub(pattern, new_contact_html, text, flags=re.DOTALL)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_text)
        count += 1
    else:
        # Fallback: Maybe it's just missing the final space
        pattern2 = r'<div class="footer-line contact-info">.*?</a></div>'
        if re.search(pattern2, text, flags=re.DOTALL):
            new_text = re.sub(pattern2, new_contact_html, text, flags=re.DOTALL)
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_text)
            count += 1
            
print(f'Updated footer contact info in {count} files.')
