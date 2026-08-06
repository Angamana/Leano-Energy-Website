import os
import re
from glob import glob

root_dir = r"C:\Users\angam\Downloads\Leano Website V1"
html_files = glob(os.path.join(root_dir, "**", "*.html"), recursive=True)

modified_count = 0

utility_pattern = re.compile(r'<div class="footer-title">\s*Utility Page\s*</div>.*?<div class="footer-line">.*?</div\s*>\s*</div\s*>', re.DOTALL)

utility_replacement = """<div class="footer-title">Policies</div>
</div>
<div class="footer-line">
<a class="footer-link w-inline-block" href="../../Policies/Quality Policy/website/Quality Policy.html">
<div class="footer-link-text" href="#">Quality Policy</div>
</a>
<a class="footer-link w-inline-block" href="../../Policies/Environmental Policy/website/Environmental Policy.html">
<div class="footer-link-text" href="#">Environmental Policy</div>
</a>
<a class="footer-link w-inline-block" href="../../Policies/Health & Safety Policy/website/Health & Safety Policy.html">
<div class="footer-link-text" href="#">Health &amp; Safety Policy</div>
</a>
<a class="footer-link w-inline-block" href="../../Policies/Privacy Policy/website/Privacy Policy.html">
<div class="footer-link-text" href="#">Privacy Policy</div>
</a>
<a class="footer-link w-inline-block" href="../../Policies/Terms and Conditions/website/Terms and Conditions.html">
<div class="footer-link-text" href="#">Terms and Conditions</div>
</a>
</div>"""

logo_pattern = re.compile(r'<img[^>]*src="[^"]*692a8d5bf0caac22cab26bd7_footer-logo\.svg"[^>]*>', re.IGNORECASE)
logo_replacement = '<img alt="Leano Energy Logo" class="footer-logo" loading="lazy" src="../../Universal/images/leano-energy-logo.png?v=2" style="max-height: 85px;"/>'

copyright_pattern = re.compile(r'<div class="footer-small-link-text-wrap">Copyright © 2025 <a[^>]*>Leano Energy</a>.*?</div>', re.DOTALL | re.IGNORECASE)
copyright_replacement = '<div class="footer-small-link-text-wrap">Copyright © 2025 <a class="footer-small-link-text-link" href="../../Index/website/Index.html">Leano Energy</a></div>'

for filepath in html_files:
    if "Old Leano Website" in filepath or "Backup" in filepath or "Universal" in filepath:
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    original = content
    
    # 1. Replace Utility block
    # Note: my regex for utility_pattern captures an extra </div> but wait, the original html is:
    # <div class="footer-title">Utility Page</div>
    # </div>
    # <div class="footer-line">...</div>
    # so:
    content = re.sub(r'<div class="footer-title">\s*Utility Page\s*</div>\s*</div>\s*<div class="footer-line">.*?<div class="footer-link-text" href="#">404 Page</div>\s*</a>\s*</div>', utility_replacement, content, flags=re.DOTALL)
    
    # 2. Replace Footer Logo
    content = logo_pattern.sub(logo_replacement, content)
    
    # 3. Replace Copyright string
    content = copyright_pattern.sub(copyright_replacement, content)
                     
    if original != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        modified_count += 1

print(f"Updated {modified_count} HTML files (Footer updates).")
