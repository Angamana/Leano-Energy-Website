import os
import re
import urllib.request
import urllib.parse

html_files = ["index.html", "about-us.html", "services.html", "blog.html", "contact.html"]
os.makedirs("assets/css", exist_ok=True)
os.makedirs("assets/js", exist_ok=True)
os.makedirs("assets/images", exist_ok=True)

def download_file(url, folder):
    filename = os.path.basename(urllib.parse.urlparse(url).path)
    if not filename:
        return url
    filepath = os.path.join(folder, filename)
    if not os.path.exists(filepath):
        try:
            print(f"Downloading {url} to {filepath}")
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
                out_file.write(response.read())
        except Exception as e:
            print(f"Failed to download {url}: {e}")
            return url
    return f"{folder}/{filename}".replace("\\", "/")

for html_file in html_files:
    if not os.path.exists(html_file):
        continue
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Find and download CSS
    for match in re.finditer(r'<link[^>]+href="(https://[^"]+\.css)"', content):
        url = match.group(1)
        local_path = download_file(url, "assets/css")
        content = content.replace(url, local_path)

    # Find and download JS
    for match in re.finditer(r'<script[^>]+src="(https://[^"]+\.js)"', content):
        url = match.group(1)
        local_path = download_file(url, "assets/js")
        content = content.replace(url, local_path)

    # Find and download Images
    for match in re.finditer(r'src="(https://cdn\.prod\.website-files\.com/[^"]+\.(png|jpg|jpeg|gif|svg|webp))"', content):
        url = match.group(1)
        local_path = download_file(url, "assets/images")
        content = content.replace(url, local_path)
        
    for match in re.finditer(r'content="(https://cdn\.prod\.website-files\.com/[^"]+\.(png|jpg|jpeg|gif|svg|webp))"', content):
        url = match.group(1)
        local_path = download_file(url, "assets/images")
        content = content.replace(url, local_path)

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(content)
        
print("Localization complete.")
