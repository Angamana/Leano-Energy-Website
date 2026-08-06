import os
import shutil
import re
from glob import glob

root_dir = r"C:\Users\angam\Downloads\Leano Website V1"
universal_css = os.path.join(root_dir, "Universal", "code", "css")
universal_js = os.path.join(root_dir, "Universal", "code", "js")

html_files = glob(os.path.join(root_dir, "**", "*.html"), recursive=True)

for filepath in html_files:
    if "Old Leano Website" in filepath or "Backup" in filepath or "Universal" in filepath:
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Find the module directory. It is the parent of the 'website' directory.
    # e.g. C:\...\Index\website\Index.html -> C:\...\Index
    module_dir = os.path.dirname(os.path.dirname(filepath))
    
    local_css_dir = os.path.join(module_dir, "code", "css")
    local_js_dir = os.path.join(module_dir, "code", "js")
    
    os.makedirs(local_css_dir, exist_ok=True)
    os.makedirs(local_js_dir, exist_ok=True)
    
    # We want to replace paths pointing to Universal with local paths
    # They could be something like href="../../Universal/code/css/..." or src="../../../Universal/code/js/..."
    
    def css_replacer(match):
        filename = match.group(2)
        # copy file from universal
        src_file = os.path.join(universal_css, filename)
        if os.path.exists(src_file):
            shutil.copy2(src_file, os.path.join(local_css_dir, filename))
        return f'{match.group(1)}="../code/css/{filename}"'
        
    def js_replacer(match):
        filename = match.group(2)
        # copy file from universal
        src_file = os.path.join(universal_js, filename)
        if os.path.exists(src_file):
            shutil.copy2(src_file, os.path.join(local_js_dir, filename))
        return f'{match.group(1)}="../code/js/{filename}"'

    # Match href="..." or src="..." pointing to Universal CSS
    content = re.sub(r'(href|src)="[^"]*Universal/code/css/([^"]+)"', css_replacer, content)
    # Match href="..." or src="..." pointing to Universal JS
    content = re.sub(r'(href|src)="[^"]*Universal/code/js/([^"]+)"', js_replacer, content)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        
print("Distributed CSS and JS into local folders.")
