import os
import re
import urllib.request
import urllib.parse
from html.parser import HTMLParser

# Map of local HTML file paths to their live Webflow URLs
page_mapping = {
    r"Index\website\index.html": "https://induyst.webflow.io/",
    r"About Us\website\about-us.html": "https://induyst.webflow.io/about-us",
    r"Services\website\services.html": "https://induyst.webflow.io/services",
    r"Blog\website\blog.html": "https://induyst.webflow.io/blog",
    r"Contact Us\website\contact.html": "https://induyst.webflow.io/contact-us",
    r"Industries\Industries Main Page\website\projects.html": "https://induyst.webflow.io/projects",
    r"Industries\Industries Sub Page 1\website\technological-solutions-for-factories.html": "https://induyst.webflow.io/projects/technological-solutions-for-factories",
    r"Industries\Industries Sub Page 2\website\clean-energy-efficiency-development.html": "https://induyst.webflow.io/projects/clean-energy-efficiency-development",
    r"Industries\Industries Sub Page 3\website\industrial-technology-research.html": "https://induyst.webflow.io/projects/industrial-technology-research",
    r"Industries\Industries Sub Page 4\website\sustainable-process-design-concept.html": "https://induyst.webflow.io/projects/sustainable-process-design-concept",
    r"Industries\Industries Sub Page 5\website\automated-robot-setup-integration.html": "https://induyst.webflow.io/projects/automated-robot-setup-integration",
    r"Industries\Industries Sub Page 6\website\renewable-energy-improvement-models.html": "https://induyst.webflow.io/projects/renewable-energy-improvement-models"
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
        self.images = {} # Mapping of src filename -> (srcset, sizes)

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            attrs_dict = dict(attrs)
            if 'src' in attrs_dict and 'srcset' in attrs_dict:
                src_url = attrs_dict['src']
                src_filename = os.path.basename(urllib.parse.urlparse(src_url).path)
                self.images[src_filename] = (attrs_dict.get('srcset', ''), attrs_dict.get('sizes', ''))

for local_path, url in page_mapping.items():
    if not os.path.exists(local_path):
        print(f"File not found locally: {local_path}")
        continue
        
    print(f"Fetching {url}")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        continue
        
    parser = ImgParser()
    parser.feed(html)
    
    # Now read local HTML
    with open(local_path, "r", encoding="utf-8") as f:
        local_html = f.read()
        
    # Determine the folder for local images based on the file
    # If the image src in local HTML is ../../Universal/images/..., it belongs in Universal.
    # Otherwise, ../images/... it belongs in os.path.join(os.path.dirname(local_path), "../images")
    
    def img_replacer(match):
        img_tag = match.group(0)
        src_attr = re.search(r'src="([^"]+)"', img_tag)
        if not src_attr: return img_tag
        
        src_val = src_attr.group(1)
        src_filename = os.path.basename(src_val)
        
        if src_filename in parser.images:
            srcset_orig, sizes_orig = parser.images[src_filename]
            if not srcset_orig: return img_tag
            
            # Determine destination directory
            if "Universal" in src_val:
                dest_dir = os.path.abspath("Universal/images")
                relative_prefix = src_val.split("Universal/images")[0] + "Universal/images/"
            else:
                dest_dir = os.path.abspath(os.path.join(os.path.dirname(local_path), "../images"))
                relative_prefix = "../images/"
                
            os.makedirs(dest_dir, exist_ok=True)
            
            new_srcset_parts = []
            for part in srcset_orig.split(","):
                part = part.strip()
                if not part: continue
                url_part, width_part = part.split(" ", 1)
                
                # download url_part
                new_filename = download_file(url_part, dest_dir)
                if new_filename:
                    new_srcset_parts.append(f"{relative_prefix}{new_filename} {width_part}")
                else:
                    new_srcset_parts.append(f"{relative_prefix}{os.path.basename(urllib.parse.urlparse(url_part).path)} {width_part}")
            
            new_srcset = ", ".join(new_srcset_parts)
            
            # Reconstruct the img tag to include srcset and sizes
            # Insert right before the closing > or />
            if "/>" in img_tag:
                new_img_tag = img_tag.replace("/>", f' srcset="{new_srcset}" sizes="{sizes_orig}" />')
            else:
                new_img_tag = img_tag.replace(">", f' srcset="{new_srcset}" sizes="{sizes_orig}">')
                
            return new_img_tag
            
        return img_tag

    # We need to replace <img> tags without breaking HTML.
    # Regular expressions for HTML tags can be tricky, but we know Webflow outputs fairly standard <img> tags.
    new_local_html = re.sub(r'<img[^>]+>', img_replacer, local_html)
    
    with open(local_path, "w", encoding="utf-8") as f:
        f.write(new_local_html)

print("Done restoring and localizing responsive images.")
