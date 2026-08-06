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
    
    # Revert policy links to #
    content = re.sub(r'href="\.\./\.\./Policies/[^"]+"', 'href="#"', content)
    
    # Change footer logo to the requested one
    content = re.sub(r'src="\.\./\.\./Universal/images/leano-energy-logo\.png[^"]*"', 'src="../../Universal/images/Logo/Logo/Leano%20Energy-02.png"', content)
                     
    if original != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        modified_count += 1

print(f"Updated {modified_count} HTML files (Reverted Policy links and updated footer logo).")
