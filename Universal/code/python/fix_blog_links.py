import os
import re
from glob import glob

root_dir = r"C:\Users\angam\Downloads\Leano Website V1"

# 1. Fix relative depths inside all Blog files
blog_files = glob(os.path.join(root_dir, "Blog", "**", "*.html"), recursive=True)

for html_file in blog_files:
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()
        
    # The user moved these files one level deeper (from Blog/website/ to Blog/Blog Main Page/website/)
    # So any original relative links to Universal that were "../../Universal" are now broken.
    # We must change them to "../../../Universal"
    # But wait, my fetch_missing_assets.py already put "Universal" links in the new Blog Sub Pages.
    # Let's just blindly calculate the relative path from the current file to the Universal folders.
    
    css_dir = os.path.join(root_dir, "Universal", "code", "css")
    js_dir = os.path.join(root_dir, "Universal", "code", "js")
    img_dir = os.path.join(root_dir, "Universal", "images")
    
    def get_rel(target):
        return os.path.relpath(target, os.path.dirname(html_file)).replace("\\", "/")
        
    rel_css = get_rel(css_dir)
    rel_js = get_rel(js_dir)
    rel_img = get_rel(img_dir)
    
    # Replace any href or src pointing to Universal
    # It might look like href="../../Universal/code/css/..." or href="../../../Universal/code/css/..."
    content = re.sub(r'(href|src)="[^"]*Universal/code/css/([^"]+)"', rf'\1="{rel_css}/\2"', content)
    content = re.sub(r'(href|src)="[^"]*Universal/code/js/([^"]+)"', rf'\1="{rel_js}/\2"', content)
    content = re.sub(r'(href|src)="[^"]*Universal/images/([^"]+)"', rf'\1="{rel_img}/\2"', content)
    content = re.sub(r'srcset="[^"]*Universal/images/([^"]+)"', rf'srcset="{rel_img}/\1"', content)
    
    # Also if there are still https://cdn.prod.website-files.com/68ec88daad774d7bbc39b02e/css/...
    # Let's replace them to point to Universal
    def css_replace(m):
        fname = m.group(1)
        return f'href="{rel_css}/{fname}"'
    content = re.sub(r'href="https://cdn\.prod\.website-files\.com/[^/]+/css/([^"]+)"', css_replace, content)
    
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(content)

# 2. Fix the broken navigation links across the entire project
all_html = glob(os.path.join(root_dir, "**", "*.html"), recursive=True)

# Map of known bad links to correct local files
# We know the user has 6 Blog sub pages. Let's map them.
# The slugs from the Webflow export for the blog were:
# 1. creation-of-industrial-projects-around-the-world
# 2. manufacturing-research-in-kiev-regions-of-the-country
# 3. future-of-sustainable-industrial-development
# 4. enhancing-safety-protocols-in-heavy-industry
# 5. clean-energy-efficiency-development (wait, this is a project slug, but let's just map all /post/ links)

# We can dynamically find the right Blog Sub Page by reading the title or we can just map them.
# The user said "Blog Sub Page 1" etc. 

pages = {
    # The blog main page link was left as "../../Blog/website/blog.html" or "/blog"
    # We will match anything ending in /blog.html or /blog
    r"([^\"']*/Blog/website/blog\.html|/blog)": "Blog/Blog Main Page/website/Blog Main Page.html",
    
    # The blog sub pages were under /post/
    r"/post/creation-of-industrial-projects-around-the-world": "Blog/Blog Sub Page 1/website/Blog Sub Page 1.html",
    r"/post/manufacturing-research-in-kiev-regions-of-the-country": "Blog/Blog Sub Page 2/website/Blog Sub Page 2.html",
    r"/post/future-of-sustainable-industrial-development": "Blog/Blog Sub Page 3/website/Blog Sub Page 3.html",
    r"/post/enhancing-safety-protocols-in-heavy-industry": "Blog/Blog Sub Page 4/website/Blog Sub Page 4.html",
    r"/post/clean-energy-efficiency-development": "Blog/Blog Sub Page 5/website/Blog Sub Page 5.html",
    r"/post/sustainable-process-design-concept": "Blog/Blog Sub Page 6/website/Blog Sub Page 6.html",
}

for html_file in all_html:
    if "Old Leano Website" in html_file or "Backup" in html_file:
        continue
        
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()
        
    for pattern, target in pages.items():
        rel_path = os.path.relpath(os.path.join(root_dir, target), os.path.dirname(html_file)).replace("\\", "/")
        # Be careful not to replace things that don't look like hrefs
        content = re.sub(rf'href="{pattern}"', f'href="{rel_path}"', content)
        
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(content)

print("Fixed CSS depths and Blog navigation links.")
