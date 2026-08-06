import os
import re

about_us_path = r"C:\Users\angam\Downloads\Leano Website V1\About Us\website\About Us.html"

with open(about_us_path, "r", encoding="utf-8") as f:
    text = f.read()

# Fix the logo and home links
# Index.html -> ../../Index/website/Index.html
# href="/" -> href="../../Index/website/Index.html"
text = re.sub(r'href="Index\.html"', 'href="../../Index/website/Index.html"', text)
text = re.sub(r'href="/"', 'href="../../Index/website/Index.html"', text)

# Fix Services links
# /services -> ../../Services/website/Services.html
text = re.sub(r'href="/services"', 'href="../../Services/website/Services.html"', text)

# Fix Contact links
# /contact -> ../../Contact Us/website/Contact Us.html
text = re.sub(r'href="/contact"', 'href="../../Contact Us/website/Contact Us.html"', text)

# Fix Pricing plan (if it exists, maybe just point to Contact for now, or just leave it)
# Let's map it to contact just in case
text = re.sub(r'href="/pricing-plan"', 'href="../../Contact Us/website/Contact Us.html"', text)

with open(about_us_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Links fixed!")
