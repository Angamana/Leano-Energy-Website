import os
import re
import urllib.request
import urllib.parse
from glob import glob

root_dir = r"C:\Users\angam\Downloads\Leano Website V1"
blog_htmls = glob(os.path.join(root_dir, "Blog", "Blog Sub Page *", "website", "*.html"))

def download_file(url, folder):
    filename = os.path.basename(urllib.parse.urlparse(url).path)
    if not filename: return None
    filepath = os.path.join(folder, filename)
    if not os.path.exists(filepath):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
                out_file.write(response.read())
            print(f"Downloaded {filename} to {folder}")
        except Exception as e:
            print(f"Failed to download {url}: {e}")
            return None
    return filename

for html_file in blog_htmls:
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()
        
    html_dir = os.path.dirname(html_file)
    images_dir = os.path.join(html_dir, "../images")
    
    # 1. Strip integrity and crossorigin
    content = re.sub(r'\s+integrity="[^"]+"', '', content)
    content = re.sub(r'\s+crossorigin="[^"]+"', '', content)
    
    # 2. Fix normal script links that are remote Webflow CDN
    def js_replacer(match):
        url = match.group(1)
        fname = os.path.basename(urllib.parse.urlparse(url).path)
        return f'src="../../../Universal/code/js/{fname}"'
    content = re.sub(r'src="(https://cdn\.prod\.website-files\.com/[^"]+\.js)"', js_replacer, content)
    
    # 3. Replace all https images
    def img_replacer(match):
        url = match.group(1)
        ext = match.group(2)
        fname = download_file(url, images_dir)
        if fname:
            return f'src="../images/{fname}"'
        return match.group(0)
        
    content = re.sub(r'src="(https://cdn\.prod\.website-files\.com/[^"]+\.(png|jpg|jpeg|gif|svg|webp))"', img_replacer, content)
    
    # Also strip srcset because we want them to fall back to the src image, OR run the srcset restorer
    # Let's just strip srcset for now so they don't break. The user already said the extra space was okay but 
    # we don't have the 404 versions so strip is better for the Blog pages since they might 404 on Webflow's end
    content = re.sub(r'\s+srcset="[^"]+"', '', content)
    
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(content)
        
print("Processed Blog Sub Pages.")
