import os
import re
from glob import glob

root_dir = r"C:\Users\angam\Downloads\Leano Website V1"

files_to_check = glob(os.path.join(root_dir, "**", "*.css"), recursive=True)

modified_count = 0
file_mod_count = 0

old_orange = "#f56e28"
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
    
    # Revert #c03629 to #f56e28
    content, count = re.subn(r'#c03629', old_orange, content, flags=re.IGNORECASE)
    modified_count += count
                     
    if original != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        file_mod_count += 1

print(f"Reverted {modified_count} instances across {file_mod_count} files.")
