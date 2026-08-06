import os

services_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html"
index_path = r"C:\Users\angam\Downloads\Leano Website V1\Index\website\Index.html"

# Fix Services.html
with open(services_path, "r", encoding="utf-8") as f:
    services_content = f.read()

# 1. Change page ID to Index's page ID for animations to work
services_content = services_content.replace('data-wf-page="68ec88daad774d7bbc39b100"', 'data-wf-page="68ec88daad774d7bbc39b02d"')

# 2. Swap back to Index's JS script to get the animations
services_content = services_content.replace('webflow.d0509937.b285daf4e1885937.js', 'webflow.f73038d4.86e8628c28dd3a64.js')

# 3. Add black spacer before footer
if '<div style="background-color: #0b0b0f; width: 100%; height: 120px;"></div>\n<footer class="footer">' not in services_content:
    services_content = services_content.replace('<footer class="footer">', '<div style="background-color: #0b0b0f; width: 100%; height: 120px;"></div>\n<footer class="footer">')

with open(services_path, "w", encoding="utf-8") as f:
    f.write(services_content)


# Fix Index.html
with open(index_path, "r", encoding="utf-8") as f:
    index_content = f.read()

# Replace footer text
index_content = index_content.replace("Ready to Power Your Journey?", "Let’s Talk")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_content)

print("Fixed animations and added spacing to Services.html, and updated Index.html footer!")
