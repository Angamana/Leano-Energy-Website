import os
import re

about_us_path = r"C:\Users\angam\Downloads\Leano Website V1\About Us\website\About Us.html"

with open(about_us_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update CSS path
# Replace the Webflow CSS link with the local one
text = re.sub(
    r'href="https://cdn\.prod\.website-files\.com/[^"]+\.css"',
    r'href="../code/css/About Us CSS Code.css"',
    text
)

# 2. Update JS paths
def replace_js(match):
    url = match.group(1)
    # Extract filename
    filename = url.split('/')[-1].split('?')[0] # removes ?site=...
    return f'src="../code/js/{filename}"'

text = re.sub(r'src="(https://[^"]+\.js(?:\?[^"]*)?)"', replace_js, text)

# 3. Update Image paths
def replace_img(match):
    url = match.group(1)
    # Extract filename
    filename = url.split('/')[-1]
    return f'src="../images/{filename}"'

text = re.sub(r'src="(https://[^"]+\.(?:jpg|png|svg|webp|jpeg))"', replace_img, text)

# Let's also catch srcset if it exists (webflow often uses srcset)
def replace_srcset(match):
    srcset = match.group(1)
    new_srcset = []
    for part in srcset.split(','):
        part = part.strip()
        if not part: continue
        parts = part.split(' ')
        url = parts[0]
        filename = url.split('/')[-1]
        parts[0] = f'../images/{filename}'
        new_srcset.append(' '.join(parts))
    return f'srcset="{", ".join(new_srcset)}"'

text = re.sub(r'srcset="([^"]+)"', replace_srcset, text)

with open(about_us_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Architecture paths updated successfully!")
