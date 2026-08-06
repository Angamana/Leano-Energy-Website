import os
import re
import shutil

pages = {
    "Index": "index.html",
    "About Us": "about-us.html",
    "Services": "services.html",
    "Blog": "blog.html",
    "Contact Us": "contact.html"
}

# Create Universal folders
os.makedirs("Universal/code/css", exist_ok=True)
os.makedirs("Universal/code/js", exist_ok=True)
os.makedirs("Universal/images", exist_ok=True)

# Create page folders
for page in pages.keys():
    os.makedirs(f"{page}/website", exist_ok=True)
    os.makedirs(f"{page}/images", exist_ok=True)
    os.makedirs(f"{page}/code/css", exist_ok=True)
    os.makedirs(f"{page}/code/js", exist_ok=True)

# Track usage of each asset
asset_usage = {} # path -> set of page names

for page, html_file in pages.items():
    if not os.path.exists(html_file):
        continue
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Find assets matching assets/...
    matches = re.finditer(r'(assets/(css|js|images)/[^"\'\s]+)', content)
    for match in matches:
        asset_path = match.group(1)
        if asset_path not in asset_usage:
            asset_usage[asset_path] = set()
        asset_usage[asset_path].add(page)

# Copy assets and determine their new paths
asset_new_paths = {} # old_path -> (new_filesystem_path, new_relative_path_from_website_folder)

for asset_path, used_in_pages in asset_usage.items():
    if not os.path.exists(asset_path):
        continue
        
    filename = os.path.basename(asset_path)
    
    # CSS and JS always go to Universal
    if asset_path.startswith("assets/css/"):
        new_fs = f"Universal/code/css/{filename}"
        new_rel = f"../../Universal/code/css/{filename}"
        shutil.copy(asset_path, new_fs)
        asset_new_paths[asset_path] = new_rel
    elif asset_path.startswith("assets/js/"):
        new_fs = f"Universal/code/js/{filename}"
        new_rel = f"../../Universal/code/js/{filename}"
        shutil.copy(asset_path, new_fs)
        asset_new_paths[asset_path] = new_rel
    elif asset_path.startswith("assets/images/"):
        if len(used_in_pages) > 1:
            new_fs = f"Universal/images/{filename}"
            new_rel = f"../../Universal/images/{filename}"
            shutil.copy(asset_path, new_fs)
            asset_new_paths[asset_path] = new_rel
        else:
            page = list(used_in_pages)[0]
            new_fs = f"{page}/images/{filename}"
            new_rel = f"../images/{filename}"
            shutil.copy(asset_path, new_fs)
            # We need a page-specific mapping for this asset
            if asset_path not in asset_new_paths:
                asset_new_paths[asset_path] = {}
            asset_new_paths[asset_path][page] = new_rel

# Rewrite HTML files and move them
for page, html_file in pages.items():
    if not os.path.exists(html_file):
        continue
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Replace links
    # Sort asset paths by length descending to prevent partial replacements
    for asset_path in sorted(asset_usage.keys(), key=len, reverse=True):
        if asset_path in asset_new_paths:
            new_rel = asset_new_paths[asset_path]
            if isinstance(new_rel, dict):
                # Page specific
                if page in new_rel:
                    content = content.replace(asset_path, new_rel[page])
            else:
                # Universal
                content = content.replace(asset_path, new_rel)
                
    # Additionally, fix root relative links like href="/about-us" to point to the new location
    content = content.replace('href="/"', 'href="../../Index/website/index.html"')
    content = content.replace('href="/about-us"', 'href="../../About Us/website/about-us.html"')
    content = content.replace('href="/services"', 'href="../../Services/website/services.html"')
    content = content.replace('href="/blog"', 'href="../../Blog/website/blog.html"')
    content = content.replace('href="/contact-us"', 'href="../../Contact Us/website/contact.html"')
                
    with open(f"{page}/website/{html_file}", "w", encoding="utf-8") as f:
        f.write(content)
        
    # Remove original html file
    os.remove(html_file)

# Remove the global assets folder now that everything is distributed
shutil.rmtree("assets")
print("Distribution complete.")
