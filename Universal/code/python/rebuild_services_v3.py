import os
import re

services_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html"

with open(services_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Asset Paths
# CSS (preserve filename, just update path)
content = re.sub(r'https://cdn\.prod\.website-files\.com/[^/]+/css/([^"]+)', r'../code/css/\1', content)
# JS (preserve filename for webflow chunks, update path)
content = re.sub(r'https://d3e54v103j8qbb\.cloudfront\.net/js/jquery-[^"]+', '../code/js/jquery-3.5.1.min.dc5e7f18c8.js', content)
content = re.sub(r'https://cdn\.prod\.website-files\.com/[^/]+/js/([^"]+)', r'../code/js/\1', content)
# Images
content = re.sub(r'https://cdn\.prod\.website-files\.com/[^/]+/', '../../Universal/images/', content)
# Fonts
content = re.sub(r'https://fonts\.googleapis\.com/[^"]+', 'https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap', content)

# 2. Fix Links
content = content.replace('href="/"', 'href="../../Index/website/Index.html"')
content = content.replace('href="/contact"', 'href="../../Contact Us/website/Contact Us.html"')
content = content.replace('href="/about-us"', 'href="../../About Us/website/About Us.html"')
content = content.replace('href="/services"', 'href="../../Services/website/Services.html"')
content = content.replace('href="/blog"', 'href="../../Our Blog/website/Our Blog.html"')
content = content.replace('href="/industries"', 'href="../../Industries/website/Industries.html"')
content = content.replace('href="/services-detail"', 'href="../../Services/website/Services.html"')
content = content.replace('href="/team"', '#')
content = content.replace('href="/pricing"', '#')
content = content.replace('href="/faq"', '#')
content = content.replace('href="/404"', '#')
content = content.replace('href="/protected-page"', '#')
content = content.replace('href="/style-guide"', '#')
content = content.replace('href="/licensing"', '#')
content = content.replace('href="/changelog"', '#')

# Ensure Navbar links are correct
# Home
content = re.sub(r'<a href="[^"]+" class="nav-link w-inline-block">.*?<div class="nav-text">Home</div>.*?</a>', r'<a href="../../Index/website/Index.html" class="nav-link w-inline-block"><div class="nav-text-wrap"><div class="nav-text">Home</div></div></a>', content, flags=re.DOTALL)
# Services
content = re.sub(r'<a href="[^"]+" aria-current="page" class="nav-link w-inline-block w--current">.*?<div class="nav-text">Services</div>.*?</a>', r'<a href="../../Services/website/Services.html" aria-current="page" class="nav-link w-inline-block w--current"><div class="nav-text-wrap"><div class="nav-text">Services</div></div></a>', content, flags=re.DOTALL)
# Contact
content = re.sub(r'<a href="[^"]+" class="nav-link w-inline-block">.*?<div class="nav-text">Contact</div>.*?</a>', r'<a href="../../Contact Us/website/Contact Us.html" class="nav-link w-inline-block"><div class="nav-text-wrap"><div class="nav-text">Contact</div></div></a>', content, flags=re.DOTALL)

# 3. Strip integrity and crossorigin
content = re.sub(r'\s+integrity="[^"]+"', '', content)
content = re.sub(r'\s+crossorigin="anonymous"', '', content)

# 4. Change "Selected Work" to "FORGING THE FUTURE"
content = content.replace('>Selected Work<', '>Forging the Future<')

# 5. Remove "Process" and "Our Team" sections
# Remove Process
process_start = content.find('<section class="staticbox-section section-gap">')
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

# 6. Fix Page ID so animations work (use Index page ID)
content = re.sub(r'data-wf-page="[a-z0-9]+"', 'data-wf-page="68ec88daad774d7bbc39b02d"', content)

# 7. Change Footer text to "Let's Talk"
content = content.replace('Ready to Power Your Journey?', "Let’s Talk")

# 8. Add black spacer before footer
content = content.replace('<footer class="footer">', '<div style="background-color: #0b0b0f; width: 100%; height: 120px;"></div>\n<footer class="footer">')

with open(services_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Services page fully rebuilt with proper donor CSS/JS included!")
