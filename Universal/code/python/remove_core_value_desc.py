import os
import re

html_path = r"C:\Users\angam\Downloads\Leano Website V1\About Us\website\About Us.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Remove the description divs that I added
# They look like: <div class="accordian-style-one-desc" style="color:var(--text-color); font-size:15px;">...</div>
content = re.sub(r'<div class="accordian-style-one-desc" style="color:var\(--text-color\); font-size:15px;">.*?</div>', '', content)
# Just in case it was added with the other string:
content = re.sub(r'<div class="accordian-style-one-desc" style="color:#aaa; font-size:14px;">.*?</div>', '', content)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Removed extra text successfully!")
