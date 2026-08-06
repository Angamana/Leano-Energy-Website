import os
import re

services_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html"

with open(services_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix the missed links
content = content.replace('href="/services"', 'href="../../Services/website/Services.html"')
content = content.replace('href="/blog"', 'href="../../Our Blog/website/Our Blog.html"')

# Just to be sure about dropdown Home links, if any point to "/" it was replaced to Index.html, which is correct.
# Let's also check if there are any other absolute paths
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

with open(services_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Links fixed!")
