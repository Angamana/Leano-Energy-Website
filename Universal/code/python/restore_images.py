import os
import re
import shutil

services_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html"
universal_images_dir = r"C:\Users\angam\Downloads\Leano Website V1\Universal\images"
services_images_dir = r"C:\Users\angam\Downloads\Leano Website V1\Services\images"

if not os.path.exists(services_images_dir):
    os.makedirs(services_images_dir)

with open(services_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find all image filenames used in the HTML that start with ../images/
matches = re.findall(r'\.\./images/([^"\'\s>]+)', content)

# Copy them to Services/images
count = 0
for filename in set(matches):
    src = os.path.join(universal_images_dir, filename)
    dst = os.path.join(services_images_dir, filename)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        count += 1
    else:
        print(f"Warning: {filename} not found in Universal/images")

print(f"Copied {count} images to Services/images!")
