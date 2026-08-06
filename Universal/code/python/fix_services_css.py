import os
import re

services_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html"

with open(services_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix the CSS link
content = content.replace('href="../code/css/About%20Us%20CSS%20Code.css"', 'href="../code/css/Services%20CSS%20Code.css"')
content = content.replace('href="../code/css/About Us CSS Code.css"', 'href="../code/css/Services%20CSS%20Code.css"')

with open(services_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed CSS link in Services.html")
