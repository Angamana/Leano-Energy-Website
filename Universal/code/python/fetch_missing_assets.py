import os
import re
import urllib.request
from glob import glob

root_dir = r"C:\Users\angam\Downloads\Leano Website V1"
html_files = glob(os.path.join(root_dir, "**", "*.html"), recursive=True)

css_dir = os.path.join(root_dir, "Universal", "code", "css")
js_dir = os.path.join(root_dir, "Universal", "code", "js")
os.makedirs(css_dir, exist_ok=True)
os.makedirs(js_dir, exist_ok=True)

def download_file(url, dest_path):
    if not os.path.exists(dest_path):
        try:
            print(f"Downloading {url}")
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response, open(dest_path, 'wb') as out_file:
                out_file.write(response.read())
            print(f"Saved to {dest_path}")
        except Exception as e:
            print(f"Failed to download {url}: {e}")

site_id = "68ec88daad774d7bbc39b02e"

for html_file in html_files:
    if "Old Leano Website" in html_file or "Backup" in html_file:
        continue
        
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Check CSS
    for match in re.finditer(r'href="[^"]+Universal/code/css/([^"]+)"', content):
        filename = match.group(1)
        dest_path = os.path.join(css_dir, filename)
        if not os.path.exists(dest_path):
            url = f"https://cdn.prod.website-files.com/{site_id}/css/{filename}"
            download_file(url, dest_path)
            
    # Check JS
    for match in re.finditer(r'src="[^"]+Universal/code/js/([^"]+)"', content):
        filename = match.group(1)
        dest_path = os.path.join(js_dir, filename)
        if not os.path.exists(dest_path):
            if "jquery" in filename:
                url = f"https://d3e54v103j8qbb.cloudfront.net/js/{filename}?site={site_id}"
            else:
                url = f"https://cdn.prod.website-files.com/{site_id}/js/{filename}"
            download_file(url, dest_path)
            
    changed_state = {"changed": False}
    
    # Fix missed jQuery links
    def jq_replacer(match):
        url = match.group(1)
        filename = "jquery-3.5.1.min.dc5e7f18c8.js"
        dest_path = os.path.join(js_dir, filename)
        if not os.path.exists(dest_path):
            download_file(url, dest_path)
            
        html_dir = os.path.dirname(html_file)
        rel_path = os.path.relpath(dest_path, html_dir).replace("\\", "/")
        changed_state["changed"] = True
        return f'src="{rel_path}"'
        
    content = re.sub(r'src="(https://d3e54v103j8qbb\.cloudfront\.net/js/jquery-[^"]+)"', jq_replacer, content)
    
    if changed_state["changed"]:
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(content)
            
print("Missing JS and CSS downloaded.")
