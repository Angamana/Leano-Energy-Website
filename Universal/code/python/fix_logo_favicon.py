import os
import re
from glob import glob

root_dir = r"C:\Users\angam\Downloads\Leano Website V1"
html_files = glob(os.path.join(root_dir, "**", "*.html"), recursive=True)

modified_count = 0

for filepath in html_files:
    if "Old Leano Website" in filepath or "Backup" in filepath or "Universal" in filepath:
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    original = content
    
    # Calculate relative path to Universal/images
    file_dir = os.path.dirname(filepath)
    rel_path_to_images = os.path.relpath(os.path.join(root_dir, "Universal", "images"), file_dir).replace("\\", "/")
    
    # 1. Update logo image name and add max-height
    # The current tag looks like: <img alt="logo-white" class="logo" src="../../Universal/images/leano-energy-logo.png"/>
    
    def logo_replacer(match):
        return f'<img alt="Leano Energy Logo" class="logo" style="max-height: 50px; width: auto; object-fit: contain;" src="{rel_path_to_images}/leano energy logo + Tagline.png"/>'
        
    content = re.sub(r'<img[^>]*class="logo"[^>]*src="[^"]*images/leano-energy-logo.png"[^>]*>', logo_replacer, content)
    
    # Also catch cases where it still points to the SVG (just in case)
    content = re.sub(r'<img[^>]*class="logo"[^>]*src="[^"]*images/[^"]*_logo-white.svg"[^>]*>', logo_replacer, content)
    
    # 2. Update Favicons
    # <link href="https://cdn...favicon-small.png" rel="shortcut icon" type="image/x-icon"/>
    content = re.sub(r'<link[^>]*href="[^"]*favicon-small\.png"[^>]*rel="shortcut icon"[^>]*>', 
                     f'<link href="{rel_path_to_images}/Leano Energy Logo.png" rel="shortcut icon" type="image/x-icon"/>', content)
                     
    content = re.sub(r'<link[^>]*href="[^"]*favicon\.png"[^>]*rel="apple-touch-icon"[^>]*>', 
                     f'<link href="{rel_path_to_images}/Leano Energy Logo.png" rel="apple-touch-icon"/>', content)
                     
    if original != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        modified_count += 1

print(f"Updated {modified_count} HTML files.")
