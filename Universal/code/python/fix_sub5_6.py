import os
import re
import shutil
from glob import glob

root_dir = r"C:\Users\angam\Downloads\Leano Website V1"

pages = {
    "/project/automated-robot-setup-integration-project": "Industries/Industries Sub Page 5/website/automated-robot-setup-integration.html",
    "/project/renewable-energy-improvement-model": "Industries/Industries Sub Page 6/website/renewable-energy-improvement-models.html"
}

def get_relative_path(from_file, to_file):
    from_dir = os.path.dirname(os.path.abspath(from_file))
    to_abs = os.path.abspath(os.path.join(root_dir, to_file))
    rel_path = os.path.relpath(to_abs, from_dir)
    return rel_path.replace("\\", "/")

html_files = glob(os.path.join(root_dir, "**", "*.html"), recursive=True)

for html_file in html_files:
    if "Old Leano Website" in html_file or "Backup" in html_file:
        continue
        
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()
        
    for webflow_path, local_target in pages.items():
        pattern = rf'href="{webflow_path}/?"'
        rel_target = get_relative_path(html_file, local_target)
        content = re.sub(pattern, f'href="{rel_target}"', content)
        
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(content)

# Clean up Backup folders
backup5 = os.path.join(root_dir, "Industries", "Industries Sub Page 5", "Backup Sub Page 5")
backup6 = os.path.join(root_dir, "Industries", "Industries Sub Page 6", "Backup Sub Page 6")

for b in [backup5, backup6]:
    if os.path.exists(b):
        shutil.rmtree(b)
        print(f"Removed {b}")

print("Linked Sub Pages 5 & 6 and cleaned up architecture.")
