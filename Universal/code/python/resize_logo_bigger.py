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
    
    # Increase max-height from 50px to 65px (30% increase)
    content = content.replace("max-height: 50px;", "max-height: 65px;")
                     
    if original != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        modified_count += 1

print(f"Updated {modified_count} HTML files.")
