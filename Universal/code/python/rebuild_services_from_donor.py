import os
import re

services_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html"

with open(services_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Asset Paths
# CSS
content = re.sub(r'https://cdn\.prod\.website-files\.com/[^/]+/css/[^"]+', '../code/css/Services%20CSS%20Code.css', content)
# JS
content = re.sub(r'https://d3e54v103j8qbb\.cloudfront\.net/js/jquery-[^"]+', '../code/js/jquery-3.5.1.min.dc5e7f18c8.js', content)
content = re.sub(r'https://cdn\.prod\.website-files\.com/[^/]+/js/webflow\.[^"]+', '../code/js/webflow.f73038d4.86e8628c28dd3a64.js', content)
# Images
content = re.sub(r'https://cdn\.prod\.website-files\.com/[^/]+/', '../../Universal/images/', content)
# Fonts
content = re.sub(r'https://fonts\.googleapis\.com/[^"]+', 'https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap', content)

# 2. Fix Links
content = content.replace('href="/"', 'href="../../Index/website/Index.html"')
content = content.replace('href="/contact"', 'href="../../Contact Us/website/Contact Us.html"')
content = content.replace('href="/about-us"', 'href="../../About Us/website/About Us.html"')

# Ensure Navbar links are correct
# Home
content = re.sub(r'<a href="[^"]+" class="nav-link w-inline-block">.*?<div class="nav-text">Home</div>.*?</a>', r'<a href="../../Index/website/Index.html" class="nav-link w-inline-block"><div class="nav-text-wrap"><div class="nav-text">Home</div></div></a>', content, flags=re.DOTALL)
# Services
content = re.sub(r'<a href="[^"]+" aria-current="page" class="nav-link w-inline-block w--current">.*?<div class="nav-text">Services</div>.*?</a>', r'<a href="../../Services/website/Services.html" aria-current="page" class="nav-link w-inline-block w--current"><div class="nav-text-wrap"><div class="nav-text">Services</div></div></a>', content, flags=re.DOTALL)
# Contact
content = re.sub(r'<a href="[^"]+" class="nav-link w-inline-block">.*?<div class="nav-text">Contact</div>.*?</a>', r'<a href="../../Contact Us/website/Contact Us.html" class="nav-link w-inline-block"><div class="nav-text-wrap"><div class="nav-text">Contact</div></div></a>', content, flags=re.DOTALL)


# 3. Change "Selected Work" to "FORGING THE FUTURE"
content = content.replace('>Selected Work<', '>Forging the Future<')

# 4. Remove "Process" and "Our Team" sections
# These correspond to "staticbox-section section-gap" (the second one) and "section-gap padding-bottom-0"

# Remove Process
process_start = content.find('<section class="staticbox-section section-gap">')
# the first one is the hero, we want to find the second one which contains "staticbox-two-wrapper"
if process_start != -1:
    process_start = content.find('<section class="section-gap section-margin">', process_start + 10)
    if process_start != -1:
        process_end = content.find('</section>', process_start) + 10
        content = content[:process_start] + content[process_end:]

# Remove Our Team
team_start = content.find('<section class="section-gap padding-bottom-0">')
if team_start != -1:
    team_end = content.find('</section>', team_start) + 10
    content = content[:team_start] + content[team_end:]

# 5. Fix Page ID so animations work (use Index page ID)
content = re.sub(r'data-wf-page="[a-z0-9]+"', 'data-wf-page="68ec88daad774d7bbc39b02d"', content)

# 6. Change Footer text to "Let's Talk"
content = content.replace('Ready to Power Your Journey?', "Let’s Talk")

# 7. Add black spacer before footer
content = content.replace('<footer class="footer">', '<div style="background-color: #0b0b0f; width: 100%; height: 120px;"></div>\n<footer class="footer">')

with open(services_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Services page correctly built from pure donor file!")
