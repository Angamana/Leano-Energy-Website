import os
import re

services_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html"

with open(services_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Change the main headline
text = re.sub(
    r'<h2 class="heading-title service-heading white-text">Smart Processes And Stronger Outcomes</h2>',
    r'<h2 class="heading-title service-heading white-text">Premium Petroleum Products For Your Every Need</h2>',
    text,
    flags=re.IGNORECASE
)

# 2. Remove the images from the tabs in the Products Detail Section
section_match = re.search(r'(<div class="subtitle-head white-text">Products Detail Section</div>.*?)</section>', text, flags=re.DOTALL)
if section_match:
    section_html = section_match.group(1)
    
    # Remove the img tags with class staticbox-image
    new_section_html = re.sub(r'<img[^>]*class="staticbox-image"[^>]*>', '', section_html, flags=re.IGNORECASE)
    
    text = text.replace(section_html, new_section_html)

with open(services_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Fixed headline and removed images!")
