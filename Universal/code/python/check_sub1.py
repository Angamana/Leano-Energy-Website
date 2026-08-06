import os
import re

html_file = r"C:\Users\angam\Downloads\Leano Website V1\Industries\Industries Sub Page 1\website\technological-solutions-for-factories.html"
html_dir = os.path.dirname(html_file)

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

for match in re.finditer(r'<img[^>]*src="([^"]+)"', content):
    src = match.group(1)
    if src.startswith("http") or src.startswith("data:"):
        continue
    target_path = os.path.normpath(os.path.join(html_dir, src))
    if not os.path.exists(target_path):
        print(f"BROKEN: {src} -> {target_path}")
    else:
        print(f"OK: {src} -> {target_path}")
