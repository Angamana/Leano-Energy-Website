import os
import re
import shutil

css_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\code\css\Services CSS Code.css"
images_dir = r"C:\Users\angam\Downloads\Leano Website V1\Services\images"
universal_images_dir = r"C:\Users\angam\Downloads\Leano Website V1\Universal\images"

with open(css_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find all CDN links in CSS
matches = re.findall(r'https://cdn\.prod\.website-files\.com/[^/]+/([^"\')\s>]+)', content)

# Copy them to Services/images
for filename in set(matches):
    src = os.path.join(universal_images_dir, filename)
    dst = os.path.join(images_dir, filename)
    if os.path.exists(src):
        shutil.copy2(src, dst)
    else:
        print(f"Warning: {filename} not found in Universal/images")

# Update CSS to point to ../../images/ (since CSS is in code/css/)
content = re.sub(r'https://cdn\.prod\.website-files\.com/[^/]+/([^"\')\s>]+)', r'../../images/\1', content)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(content)

print("CSS updated to use local images!")
