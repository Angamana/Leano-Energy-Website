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
    
    # 1. Replace Logo Image File Name
    content = content.replace("691eba39ae0e886ef9df3bba_logo-white.svg", "leano-energy-logo.png")
    
    # 2. Replace the word "Induyst" with "Leano Energy"
    content = content.replace("Induyst", "Leano Energy")
    # Also catch all-caps if it exists
    content = content.replace("INDUYST", "LEANO ENERGY")
    
    if original != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        modified_count += 1
        
print(f"Rebranded {modified_count} HTML files.")
