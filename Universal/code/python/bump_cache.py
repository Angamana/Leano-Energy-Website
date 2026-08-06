import os
import re
from glob import glob

root_dir = r"C:\Users\angam\Downloads\Leano Website V1"
html_files = glob(os.path.join(root_dir, "**", "*.html"), recursive=True)

for filepath in html_files:
    if "Old Leano Website" in filepath or "Backup" in filepath or "Universal" in filepath:
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Bump cache buster to v=3
    content = re.sub(r'(\.css\?v=)2', r'\g<1>3', content)
                     
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
