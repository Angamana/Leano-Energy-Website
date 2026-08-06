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
    
    # Add cache buster to CSS link
    # <link href="../code/css/induyst.webflow.shared.cac7390ce.css" rel="stylesheet" type="text/css"/>
    content = re.sub(r'(\.css)(["\'])', r'\1?v=2\2', content)
                     
    if original != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        modified_count += 1

print(f"Updated {modified_count} HTML files with cache busters.")
