import os
import re
from glob import glob

html_files = []
for root, dirs, files in os.walk("."):
    if "Old Leano Website" in root or "Universal" in root:
        continue
    for file in files:
        if file.endswith(".html"):
            html_files.append(os.path.join(root, file))

for html_file in html_files:
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Remove srcset and sizes attributes
    content = re.sub(r'\s+srcset="[^"]+"', '', content)
    content = re.sub(r'\s+sizes="[^"]+"', '', content)
    
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(content)

print("Removed srcset and sizes attributes.")
