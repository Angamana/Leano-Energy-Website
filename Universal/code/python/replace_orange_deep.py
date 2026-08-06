import os
import re
from glob import glob

root_dir = r"C:\Users\angam\Downloads\Leano Website V1"

files_to_check = glob(os.path.join(root_dir, "**", "*.css"), recursive=True)

modified_count = 0
file_mod_count = 0

logo_orange = "#c03629"

for filepath in files_to_check:
    if "Old Leano Website" in filepath or "Backup" in filepath:
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        try:
            content = f.read()
        except UnicodeDecodeError:
            continue
            
    original = content
    
    # Replace #f56e28 (the old website orange I just put in) with #c03629 (the deep red-orange from the logo)
    content, count = re.subn(r'#f56e28', logo_orange, content, flags=re.IGNORECASE)
    modified_count += count
                     
    if original != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        file_mod_count += 1

print(f"Replaced {modified_count} instances across {file_mod_count} files.")
