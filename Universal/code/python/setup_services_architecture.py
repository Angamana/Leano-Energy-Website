import os
import re

services_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html"

with open(services_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Asset Paths
# CSS (point all webflow shared CSS to the single CSS file we copied)
content = re.sub(r'https://cdn\.prod\.website-files\.com/[^/]+/css/[^"]+', '../code/css/Services%20CSS%20Code.css', content)

# JS (preserve filename for webflow chunks, update path)
content = re.sub(r'https://d3e54v103j8qbb\.cloudfront\.net/js/([^"]+)', r'../code/js/\1', content)
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

with open(services_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Services HTML properly configured for new architecture!")
