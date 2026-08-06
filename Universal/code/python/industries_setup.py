import os
import re
import shutil
import urllib.request
import urllib.parse
from glob import glob

industries_dir = "Industries"
folders = [f for f in os.listdir(industries_dir) if os.path.isdir(os.path.join(industries_dir, f))]

def download_file(url, folder):
    filename = os.path.basename(urllib.parse.urlparse(url).path)
    if not filename:
        return url
    filepath = os.path.join(folder, filename)
    if not os.path.exists(filepath):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
                out_file.write(response.read())
        except Exception as e:
            print(f"Failed to download {url}: {e}")
            return url
    return f"../images/{filename}"

for folder_name in folders:
    base_path = os.path.join(industries_dir, folder_name)
    
    # 1. Create structure
    website_dir = os.path.join(base_path, "website")
    images_dir = os.path.join(base_path, "images")
    css_dir = os.path.join(base_path, "code", "css")
    js_dir = os.path.join(base_path, "code", "js")
    
    os.makedirs(website_dir, exist_ok=True)
    os.makedirs(images_dir, exist_ok=True)
    os.makedirs(css_dir, exist_ok=True)
    os.makedirs(js_dir, exist_ok=True)
    
    # 2. Find and move HTML file
    html_files = glob(os.path.join(base_path, "**", "*.html"), recursive=True)
    if not html_files:
        print(f"No HTML file found in {folder_name}")
        continue
        
    html_file = html_files[0]
    filename = os.path.basename(html_file)
    new_html_path = os.path.join(website_dir, filename)
    
    # Only move if it's not already in the right place
    if os.path.abspath(html_file) != os.path.abspath(new_html_path):
        shutil.move(html_file, new_html_path)
        
    # 3. Clean up induyst.webflow.io folders and zips
    for item in os.listdir(base_path):
        item_path = os.path.join(base_path, item)
        if item.startswith("induyst.webflow.io") or item.endswith(".zip"):
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)
                
    # 4. Process HTML
    with open(new_html_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Title & Badge
    content = re.sub(r'<title>.*?</title>', '<title>Leano Energy</title>', content, flags=re.IGNORECASE)
    if ".w-webflow-badge { display: none !important; }" not in content:
        content = content.replace("</head>", "\n    <style>.w-webflow-badge { display: none !important; }</style>\n</head>")
        
    # Remove integrity and crossorigin
    content = re.sub(r'\s+integrity="[^"]+"', '', content)
    content = re.sub(r'\s+crossorigin="[^"]+"', '', content)

    # Replace remote CSS with Universal CSS
    def css_replacer(match):
        url = match.group(1)
        fname = os.path.basename(urllib.parse.urlparse(url).path)
        return match.group(0).replace(url, f"../../../Universal/code/css/{fname}")
    content = re.sub(r'<link[^>]+href="(https://[^"]+\.css)"', css_replacer, content)
    
    # Replace remote JS with Universal JS
    def js_replacer(match):
        url = match.group(1)
        fname = os.path.basename(urllib.parse.urlparse(url).path)
        return match.group(0).replace(url, f"../../../Universal/code/js/{fname}")
    content = re.sub(r'<script[^>]+src="(https://[^"]+\.js)"', js_replacer, content)

    # Download Images and update src
    for match in re.finditer(r'src="(https://cdn\.prod\.website-files\.com/[^"]+\.(png|jpg|jpeg|gif|svg|webp))"', content):
        url = match.group(1)
        local_rel = download_file(url, images_dir)
        content = content.replace(url, local_rel)
        
    for match in re.finditer(r'content="(https://cdn\.prod\.website-files\.com/[^"]+\.(png|jpg|jpeg|gif|svg|webp))"', content):
        url = match.group(1)
        local_rel = download_file(url, images_dir)
        content = content.replace(url, local_rel)
        
    # Fix root links
    content = content.replace('href="/"', 'href="../../../Index/website/index.html"')
    content = content.replace('href="/about-us"', 'href="../../../About Us/website/about-us.html"')
    content = content.replace('href="/services"', 'href="../../../Services/website/services.html"')
    content = content.replace('href="/blog"', 'href="../../../Blog/website/blog.html"')
    content = content.replace('href="/contact-us"', 'href="../../../Contact Us/website/contact.html"')

    with open(new_html_path, "w", encoding="utf-8") as f:
        f.write(content)
        
print("Industries processing complete.")
