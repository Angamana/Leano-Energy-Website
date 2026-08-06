import os
import re
import urllib.request
import urllib.parse
from html.parser import HTMLParser
from glob import glob

sub5_backup = glob(r"C:\Users\angam\Downloads\Leano Website V1\Industries\Industries Sub Page 5\Backup Sub Page 5\**\*.html", recursive=True)[0]
sub6_backup = glob(r"C:\Users\angam\Downloads\Leano Website V1\Industries\Industries Sub Page 6\Backup Sub Page 6\**\*.html", recursive=True)[0]

mapping = {
    r"C:\Users\angam\Downloads\Leano Website V1\Industries\Industries Sub Page 5\website\automated-robot-setup-integration.html": sub5_backup,
    r"C:\Users\angam\Downloads\Leano Website V1\Industries\Industries Sub Page 6\website\renewable-energy-improvement-models.html": sub6_backup
}

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

class ImgParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = {}

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            attrs_dict = dict(attrs)
            if 'src' in attrs_dict and 'srcset' in attrs_dict:
                src_url = attrs_dict['src']
                src_filename = os.path.basename(urllib.parse.urlparse(src_url).path)
                self.images[src_filename] = (attrs_dict.get('srcset', ''), attrs_dict.get('sizes', ''))

for local_path, backup_path in mapping.items():
    if not os.path.exists(local_path) or not os.path.exists(backup_path):
        continue
        
    with open(backup_path, "r", encoding="utf-8") as f:
        html = f.read()
        
    parser = ImgParser()
    parser.feed(html)
    
    with open(local_path, "r", encoding="utf-8") as f:
        local_html = f.read()
        
    def img_replacer(match):
        img_tag = match.group(0)
        src_attr = re.search(r'src="([^"]+)"', img_tag)
        if not src_attr: return img_tag
        
        src_val = src_attr.group(1)
        src_filename = os.path.basename(src_val)
        
        if src_filename in parser.images:
            srcset_orig, sizes_orig = parser.images[src_filename]
            if not srcset_orig: return img_tag
            
            if "Universal" in src_val:
                dest_dir = r"C:\Users\angam\Downloads\Leano Website V1\Universal\images"
                relative_prefix = "../../../Universal/images/"
            else:
                dest_dir = os.path.abspath(os.path.join(os.path.dirname(local_path), "../images"))
                relative_prefix = "../images/"
                
            os.makedirs(dest_dir, exist_ok=True)
            
            new_srcset_parts = []
            for part in srcset_orig.split(","):
                part = part.strip()
                if not part: continue
                if " " in part:
                    url_part, width_part = part.rsplit(" ", 1)
                else:
                    url_part = part
                    width_part = ""
                    
                # Fix Webflow srcset parsing
                url_part = url_part.strip()
                if url_part.startswith("../") or url_part.startswith("images/"):
                    url_part = "https://cdn.prod.website-files.com/68ec88daad774d7bbc39b02e/" + os.path.basename(url_part)
                elif not url_part.startswith("http"):
                    continue
                    
                new_filename = download_file(url_part, dest_dir)
                if new_filename:
                    new_srcset_parts.append(f"{relative_prefix}{new_filename} {width_part}")
            
            new_srcset = ", ".join(new_srcset_parts)
            
            if "/>" in img_tag:
                new_img_tag = img_tag.replace("/>", f' srcset="{new_srcset}" sizes="{sizes_orig}" />')
            else:
                new_img_tag = img_tag.replace(">", f' srcset="{new_srcset}" sizes="{sizes_orig}">')
                
            return new_img_tag
            
        return img_tag

    new_local_html = re.sub(r'<img[^>]+>', img_replacer, local_html)
    
    with open(local_path, "w", encoding="utf-8") as f:
        f.write(new_local_html)

print("Restored backup files.")
