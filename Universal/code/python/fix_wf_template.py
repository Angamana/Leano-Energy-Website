import os
import re
import urllib.parse
import urllib.request
from glob import glob

root_dir = r"C:\Users\angam\Downloads\Leano Website V1"
html_files = glob(os.path.join(root_dir, "**", "*.html"), recursive=True)

def download_file(url, dest_dir):
    filename = os.path.basename(urllib.parse.urlparse(url).path)
    if not filename: return None
    filepath = os.path.join(dest_dir, filename)
    if not os.path.exists(filepath):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
                out_file.write(response.read())
            print(f"Downloaded {filename}")
        except Exception as e:
            print(f"Failed to download {url}: {e}")
            return None
    return filename

for html_file in html_files:
    if "Old Leano Website" in html_file or "Backup" in html_file:
        continue
        
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()
        
    html_dir = os.path.dirname(html_file)
    
    def template_replacer(match):
        script_tag = match.group(0)
        encoded_html = match.group(1)
        decoded = urllib.parse.unquote(encoded_html)
        
        # Remove srcset and sizes
        decoded = re.sub(r'\s+srcset="[^"]+"', '', decoded)
        decoded = re.sub(r'\s+sizes="[^"]+"', '', decoded)
        
        # Find all src="https://..."
        def img_src_replacer(img_match):
            url = img_match.group(1)
            # We'll just put all wf-template images into the local images folder for the page
            # unless we know it belongs to Universal. It's safer to just put them in the page's images folder.
            dest_dir = os.path.abspath(os.path.join(html_dir, "../images"))
            os.makedirs(dest_dir, exist_ok=True)
            
            filename = download_file(url, dest_dir)
            if filename:
                return f'src="../images/{filename}"'
            return img_match.group(0)
            
        decoded = re.sub(r'src="(https://cdn\.prod\.website-files\.com/[^"]+)"', img_src_replacer, decoded)
        
        # Also check for background-image: url('...')
        def bg_replacer(bg_match):
            url = bg_match.group(1)
            dest_dir = os.path.abspath(os.path.join(html_dir, "../images"))
            os.makedirs(dest_dir, exist_ok=True)
            filename = download_file(url, dest_dir)
            if filename:
                return f"background-image: url('../images/{filename}')"
            return bg_match.group(0)
            
        decoded = re.sub(r"background-image:\s*url\(['\"]?(https://cdn\.prod\.website-files\.com/[^'\"]+)['\"]?\)", bg_replacer, decoded)
        
        re_encoded = urllib.parse.quote(decoded)
        # webflow often leaves some characters unquoted or uses specific casing, but quote() is generally safe
        # but let's just replace the inner content
        return script_tag.replace(encoded_html, re_encoded)
        
    new_content = re.sub(r'(?s)(<script type="text/x-wf-template"[^>]*>)(.*?)(</script>)', lambda m: m.group(1) + urllib.parse.quote(re.sub(r'\s+srcset="[^"]+"', '', re.sub(r'\s+sizes="[^"]+"', '', re.sub(r'src="(https://cdn\.prod\.website-files\.com/[^"]+)"', lambda im: f'src="../images/{download_file(im.group(1), os.path.abspath(os.path.join(html_dir, "../images")))}"' if download_file(im.group(1), os.path.abspath(os.path.join(html_dir, "../images"))) else im.group(0), urllib.parse.unquote(m.group(2)))))) + m.group(3), content)
    
    # Wait, the above one-liner is messy. Let's use a simpler loop to avoid lambda issues.
    
    def process_script_match(m):
        prefix = m.group(1)
        encoded_str = m.group(2)
        suffix = m.group(3)
        
        decoded = urllib.parse.unquote(encoded_str)
        decoded = re.sub(r'\s+srcset="[^"]+"', '', decoded)
        decoded = re.sub(r'\s+sizes="[^"]+"', '', decoded)
        
        def do_download(src_match):
            url = src_match.group(1)
            dest = os.path.abspath(os.path.join(html_dir, "../images"))
            os.makedirs(dest, exist_ok=True)
            fname = download_file(url, dest)
            if fname: return f'src="../images/{fname}"'
            return src_match.group(0)
            
        decoded = re.sub(r'src="(https://cdn\.prod\.website-files\.com/[^"]+)"', do_download, decoded)
        return prefix + urllib.parse.quote(decoded) + suffix
        
    new_content = re.sub(r'(?s)(<script type="text/x-wf-template"[^>]*>)(.*?)(</script>)', process_script_match, content)

    if new_content != content:
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(new_content)

print("Processed wf-templates.")
