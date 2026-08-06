import os
import shutil
import re
from glob import glob

root_dir = r"C:\Users\angam\Downloads\Leano Website V1"

def get_relative_path(from_file, to_file):
    from_dir = os.path.dirname(os.path.abspath(from_file))
    to_abs = os.path.abspath(to_file)
    rel_path = os.path.relpath(to_abs, from_dir)
    return rel_path.replace("\\", "/")

# 1. Structure the Blog Sub Pages first
for i in range(1, 7):
    blog_dir = os.path.join(root_dir, "Blog", f"Blog Sub Page {i}")
    website_dir = os.path.join(blog_dir, "website")
    images_dir = os.path.join(blog_dir, "images")
    code_dir = os.path.join(blog_dir, "code")
    
    os.makedirs(website_dir, exist_ok=True)
    os.makedirs(images_dir, exist_ok=True)
    os.makedirs(os.path.join(code_dir, "css"), exist_ok=True)
    os.makedirs(os.path.join(code_dir, "js"), exist_ok=True)
    
    htmls = glob(os.path.join(blog_dir, "**", "*.html"), recursive=True)
    # Exclude files already in website/
    htmls = [h for h in htmls if not h.startswith(website_dir)]
    
    if htmls:
        target_html = os.path.join(website_dir, f"Blog Sub Page {i}.html")
        shutil.move(htmls[0], target_html)
        
    # Clean up messy folders
    for f in os.listdir(blog_dir):
        path = os.path.join(blog_dir, f)
        if os.path.isdir(path) and f not in ["website", "images", "code"]:
            shutil.rmtree(path)

# 2. Rename existing HTML files
html_files = glob(os.path.join(root_dir, "**", "*.html"), recursive=True)

# Keep track of old -> new paths for linking
path_mapping = {}

for html_file in html_files:
    if "Old Leano Website" in html_file or "Backup" in html_file or "temp_restore" in html_file:
        continue
        
    dir_name = os.path.dirname(html_file) # e.g. .../Index/website
    parent_dir_name = os.path.basename(os.path.dirname(dir_name)) # e.g. Index
    
    # We want to name it ParentDirName.html
    new_filename = f"{parent_dir_name}.html"
    new_path = os.path.join(dir_name, new_filename)
    
    if html_file != new_path:
        shutil.move(html_file, new_path)
        path_mapping[html_file] = new_path
    else:
        path_mapping[html_file] = html_file

# Update html_files list with new paths
html_files = list(path_mapping.values())

# 3. Update all links
for new_path in html_files:
    with open(new_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # We need to find all href="..." and src="..." that end in .html and replace them.
    # Wait, earlier we were using exact relative paths. The safest way is to regex match
    # href="([^"]+\.html)" and compute if the target exists in our mapping.
    
    def replacer(match):
        rel_url = match.group(1)
        # ignore absolute URLs
        if rel_url.startswith("http") or rel_url.startswith("file://") or rel_url.startswith("#"):
            return match.group(0)
            
        # compute absolute path of the target
        # if the URL is root-relative (starts with /), this doesn't work easily here, but our links are all relative!
        if rel_url.startswith("/"):
            return match.group(0) # We shouldn't have any root-relative left
            
        target_abs = os.path.normpath(os.path.join(os.path.dirname(new_path), rel_url))
        
        # Check if this target was renamed
        # We look up in our mapping. But the target_abs is the old path!
        # Let's see if target_abs is a key in path_mapping
        
        for old_p, new_p in path_mapping.items():
            if os.path.abspath(old_p) == target_abs:
                # Yes! Calculate new relative path
                new_rel = get_relative_path(new_path, new_p)
                return f'href="{new_rel}"'
                
        return match.group(0)
        
    content = re.sub(r'href="([^"]+\.html)"', replacer, content)
    
    # Do the same for href that might be missing .html? 
    # All our internal links are currently pointing to .html because of fix_nav_links.py!
    
    with open(new_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Renaming and structuring complete.")
