import os
import re
from glob import glob

root_dir = r"C:\Users\angam\Downloads\Leano Website V1"

pages = {
    "/contact": "Contact Us/website/contact.html",
    "/project/technological-solutions-for-factories": "Industries/Industries Sub Page 1/website/technological-solutions-for-factories.html",
    "/project/clean-energy-efficiency-development": "Industries/Industries Sub Page 2/website/clean-energy-efficiency-development.html",
    "/project/industrial-technology-research": "Industries/Industries Sub Page 3/website/industrial-technology-research.html",
    "/project/sustainable-process-design-concept": "Industries/Industries Sub Page 4/website/sustainable-process-design-concept.html",
    "/project/automated-robot-setup-integration": "Industries/Industries Sub Page 5/website/automated-robot-setup-integration.html",
    "/project/renewable-energy-improvement-models": "Industries/Industries Sub Page 6/website/renewable-energy-improvement-models.html"
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

print("Additional navigation links updated.")
