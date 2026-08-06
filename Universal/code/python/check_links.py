import os
import re

def check_html_links():
    html_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
                
    broken_links = 0
    total_links = 0
    
    for html_file in html_files:
        html_dir = os.path.dirname(html_file)
        with open(html_file, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Check all src attributes
        for match in re.finditer(r'src="([^"]+)"', content):
            src = match.group(1)
            # Ignore remote URLs and anchor links
            if src.startswith("http") or src.startswith("data:") or src.startswith("#"):
                continue
                
            total_links += 1
            # Resolve relative path
            target_path = os.path.normpath(os.path.join(html_dir, src))
            if not os.path.exists(target_path):
                print(f"Broken link in {html_file}: {src} -> resolves to {target_path}")
                broken_links += 1

    print(f"Checked {total_links} links. {broken_links} are broken.")

check_html_links()
