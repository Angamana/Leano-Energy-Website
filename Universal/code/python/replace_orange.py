import os
import re
from glob import glob

root_dir = r"C:\Users\angam\Downloads\Leano Website V1"

files_to_check = glob(os.path.join(root_dir, "**", "*.html"), recursive=True) + glob(os.path.join(root_dir, "**", "*.css"), recursive=True)

modified_count = 0
file_mod_count = 0

# The old orange is #f56e28
# The new template orange is #ff7618
old_orange = "#f56e28"

for filepath in files_to_check:
    if "Old Leano Website" in filepath or "Backup" in filepath or "Universal" in filepath:
        # Wait, the shared CSS might be in a Universal folder if we didn't modularize it properly, 
        # but we DID modularize it to each page's code/css folder. 
        # But maybe we should also replace it in Universal just in case it's used as a base.
        if "Universal" not in filepath: # let's skip Old and Backup
            pass
    if "Old Leano Website" in filepath or "Backup" in filepath:
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        try:
            content = f.read()
        except UnicodeDecodeError:
            continue
            
    original = content
    
    # Case insensitive replacement of #ff7618 to #f56e28
    # Using regex to ensure we catch #FF7618 as well
    content, count = re.subn(r'#ff7618', old_orange, content, flags=re.IGNORECASE)
    modified_count += count
                     
    if original != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        file_mod_count += 1

print(f"Replaced {modified_count} instances across {file_mod_count} files.")
