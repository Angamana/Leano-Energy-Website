import os
import re
from glob import glob

root_dir = r"C:\Users\angam\Downloads\Leano Website V1"
html_files = glob(os.path.join(root_dir, "**", "*.html"), recursive=True)

renamed_count = 0
updated_html_count = 0

old_css_name = "induyst.webflow.shared.cac7390ce.css"

for filepath in html_files:
    if "Old Leano Website" in filepath or "Backup" in filepath or "Universal" in filepath:
        continue
        
    # Get the base name without extension for the page
    page_name = os.path.splitext(os.path.basename(filepath))[0]
    new_css_name = f"{page_name} CSS Code.css"
    
    # Path to the CSS file
    # Assuming HTML is at .../Index/website/Index.html
    # And CSS is at .../Index/code/css/induyst.webflow.shared.cac7390ce.css
    # Let's dynamically find the code/css folder in the same parent directory as the website folder
    website_dir = os.path.dirname(filepath)
    parent_dir = os.path.dirname(website_dir)
    css_dir = os.path.join(parent_dir, "code", "css")
    old_css_path = os.path.join(css_dir, old_css_name)
    new_css_path = os.path.join(css_dir, new_css_name)
    
    if os.path.exists(old_css_path):
        os.rename(old_css_path, new_css_path)
        renamed_count += 1
        
    # Now update the HTML file to point to the new CSS file
    # The link in HTML looks like href="../code/css/induyst.webflow.shared.cac7390ce.css?v=2"
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    original = content
    # We will use regex to replace induyst.webflow.shared.cac7390ce.css (with optional ?v=x)
    # with the new name (but URL encoded if there are spaces, wait, spaces in href are usually fine in modern browsers, or we can use %20)
    # Actually, Web browsers handle spaces in href just fine locally, but %20 is safer. Let's use %20.
    new_css_url = new_css_name.replace(" ", "%20")
    
    # Replace the old css name in the href
    content = re.sub(r'induyst\.webflow\.shared\.cac7390ce\.css(?:\?v=\d+)?', new_css_url, content)
                     
    if original != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        updated_html_count += 1

print(f"Renamed {renamed_count} CSS files.")
print(f"Updated {updated_html_count} HTML files.")
