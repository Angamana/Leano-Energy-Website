import os
import re
import urllib.request
from urllib.parse import urlparse

base_dir = r"C:\Users\angam\Downloads\Leano Website V1\About Us"
html_path = os.path.join(base_dir, "website", "About Us.html")

with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

# Directories
img_dir = os.path.join(base_dir, "images")
css_dir = os.path.join(base_dir, "code", "css")
js_dir = os.path.join(base_dir, "code", "js")
fonts_dir = os.path.join(base_dir, "fonts")
for d in [img_dir, css_dir, js_dir, fonts_dir]:
    os.makedirs(d, exist_ok=True)

# Find all external URLs
# For Webflow files: cdn.prod.website-files.com
# For fonts: fonts.googleapis.com or fonts.gstatic.com
urls = re.findall(r'(https?://(?:cdn\.prod\.website-files\.com|fonts\.googleapis\.com|fonts\.gstatic\.com)[^\x22\x27\s\>]+)', text)
urls = list(set(urls))

print(f"Found {len(urls)} external URLs to localize.")

def download_file(url, folder, prefix=""):
    try:
        # Some URLs might have query strings, strip for filename
        parsed = urlparse(url)
        filename = os.path.basename(parsed.path)
        if not filename:
            filename = "downloaded_file"
        
        filepath = os.path.join(folder, prefix + filename)
        if not os.path.exists(filepath):
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
                out_file.write(response.read())
        return filename
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return None

for url in urls:
    if '.css' in url or 'fonts.googleapis.com' in url:
        # If it's the google fonts CSS, download it
        if 'fonts.googleapis.com' in url:
            # It's a CSS file from google fonts
            filename = download_file(url, css_dir, prefix="google_fonts_")
            if filename:
                text = text.replace(url, f'../code/css/{filename}')
        else:
            filename = download_file(url, css_dir)
            if filename:
                text = text.replace(url, f'../code/css/{filename}')
    elif '.js' in url:
        filename = download_file(url, js_dir)
        if filename:
            text = text.replace(url, f'../code/js/{filename}')
    elif 'fonts.gstatic.com' in url or '.woff' in url or '.ttf' in url:
        filename = download_file(url, fonts_dir)
        if filename:
            text = text.replace(url, f'../fonts/{filename}')
    else:
        # Treat as image/media
        filename = download_file(url, img_dir)
        if filename:
            text = text.replace(url, f'../images/{filename}')

with open(html_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Localization complete!")
