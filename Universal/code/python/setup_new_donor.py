import os
import re

services_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html"

with open(services_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Asset Paths to match local architecture

# CSS (point all webflow shared CSS to the single CSS file we copied)
content = re.sub(r'https://cdn\.prod\.website-files\.com/[^/]+/css/[^"]+', '../code/css/Services%20CSS%20Code.css', content)

# JS (preserve filename for webflow chunks, update path)
content = re.sub(r'https://d3e54v103j8qbb\.cloudfront\.net/js/([^"]+)', r'../code/js/\1', content)
content = re.sub(r'https://cdn\.prod\.website-files\.com/[^/]+/js/([^"]+)', r'../code/js/\1', content)

# Images (point any cdn.prod... to ../images/)
# E.g. https://cdn.prod.website-files.com/68ec88daad774d7bbc39b02e/68ec88daad774d642339b0d1_staticbox-01.jpg
content = re.sub(r'https://cdn\.prod\.website-files\.com/[^/]+/([^"\'\s>]+)', r'../images/\1', content)

# Fonts
content = re.sub(r'https://fonts\.googleapis\.com/[^"]+', 'https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap', content)

# 2. Strip integrity and crossorigin
content = re.sub(r'\s+integrity="[^"]+"', '', content)
content = re.sub(r'\s+crossorigin="anonymous"', '', content)

with open(services_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Services HTML properly configured for images, CSS and JS links!")
