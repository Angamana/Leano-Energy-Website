import os
import re
import urllib.request
import urllib.parse

base_dir = r"C:\Users\angam\Downloads\Leano Website V1"
assets_dir = os.path.join(base_dir, "Universal", "webflow_assets")

dirs = {
    "css": os.path.join(assets_dir, "css"),
    "js": os.path.join(assets_dir, "js"),
    "images": os.path.join(assets_dir, "images"),
    "fonts": os.path.join(assets_dir, "fonts"),
    "misc": os.path.join(assets_dir, "misc")
}

for d in dirs.values():
    os.makedirs(d, exist_ok=True)

# URL matching pattern
pattern = re.compile(r'(https?://(?:cdn\.prod\.website-files\.com|assets\.website-files\.com|d3e54v103j8qbb\.cloudfront\.net|fonts\.googleapis\.com|fonts\.gstatic\.com)[^\s\x22\x27\)\>]+)')

url_map = {}

def get_local_path_and_rel_url(url, file_path):
    # Determine type based on extension or URL content
    url_lower = url.lower()
    
    # Extract filename
    parsed = urllib.parse.urlparse(url)
    filename = os.path.basename(parsed.path)
    if not filename:
        filename = "downloaded_asset"
        
    if ".css" in url_lower:
        category = "css"
        if not filename.endswith(".css"): filename += ".css"
    elif ".js" in url_lower:
        category = "js"
        if not filename.endswith(".js"): filename += ".js"
    elif any(ext in url_lower for ext in [".woff", ".woff2", ".ttf", ".eot", ".svg#", "fonts.googleapis"]):
        category = "fonts"
        if "fonts.googleapis" in url_lower: filename = "fonts.css"
    elif any(ext in url_lower for ext in [".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ico"]):
        category = "images"
    else:
        category = "misc"

    # Make filename unique to avoid collisions
    safe_filename = re.sub(r'[^a-zA-Z0-9_\-\.]', '_', filename)
    local_abs_path = os.path.join(dirs[category], safe_filename)
    
    # Handle collisions
    counter = 1
    base_name, ext = os.path.splitext(safe_filename)
    while os.path.exists(local_abs_path) and url_map.get(url, {}).get("abs_path") != local_abs_path:
        local_abs_path = os.path.join(dirs[category], f"{base_name}_{counter}{ext}")
        counter += 1

    return local_abs_path

def download_file(url, local_path):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(local_path, 'wb') as out_file:
            out_file.write(response.read())
        return True
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return False

# Step 1: Scan and map all URLs
files_to_process = []
for root, _, files in os.walk(base_dir):
    if "Donor" in root: continue
    for file in files:
        if file.endswith(('.html', '.css', '.js')):
            files_to_process.append(os.path.join(root, file))

for file_path in files_to_process:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    matches = pattern.findall(content)
    for url in matches:
        # Clean URL if it has trailing weird chars
        url = url.rstrip('\\"')
        if url not in url_map:
            local_abs_path = get_local_path_and_rel_url(url, file_path)
            url_map[url] = {
                "abs_path": local_abs_path,
                "downloaded": False
            }

print(f"Found {len(url_map)} unique URLs to download.")

# Step 2: Download all URLs
for url, data in url_map.items():
    if not os.path.exists(data["abs_path"]):
        success = download_file(url, data["abs_path"])
        data["downloaded"] = success
    else:
        data["downloaded"] = True

# Step 3: Replace URLs in files
def get_relative_path(from_file, to_file):
    from_dir = os.path.dirname(from_file)
    rel_path = os.path.relpath(to_file, from_dir)
    return rel_path.replace("\\", "/")

for file_path in files_to_process:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_content = content
        
        matches = pattern.findall(content)
        # Sort matches by length descending to replace longer URLs first (prevent partial replacements)
        matches.sort(key=len, reverse=True)
        
        for url in matches:
            url_clean = url.rstrip('\\"')
            if url_clean in url_map and url_map[url_clean]["downloaded"]:
                rel_path = get_relative_path(file_path, url_map[url_clean]["abs_path"])
                # Safe replace
                content = content.replace(url_clean, rel_path)
                
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

print("Successfully replaced URLs with local relative paths!")
