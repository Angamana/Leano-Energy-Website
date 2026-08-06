import os
import re

services_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html"

with open(services_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix CSS Link
# The link currently points to `../code/css/induyst.webflow.shared.cac7390ce.css`
content = content.replace('../code/css/induyst.webflow.shared.cac7390ce.css', '../code/css/Services%20CSS%20Code.css')

with open(services_path, "w", encoding="utf-8") as f:
    f.write(content)

print("CSS link properly renamed!")
