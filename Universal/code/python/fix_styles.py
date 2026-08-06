import os
import re

about_us_path = r"C:\Users\angam\Downloads\Leano Website V1\About Us\website\About Us.html"

with open(about_us_path, "r", encoding="utf-8") as f:
    text = f.read()

# Find instances of: style="opacity:0" class="icon-style-four" style="..."
# and merge them.
# The user noticed it on the first tab.

def merge_styles(match):
    style1 = match.group(1) # e.g. "opacity:0"
    style2 = match.group(2) # e.g. "width: 50%;..."
    return f'class="icon-style-four" style="{style1}; {style2}"'

# Regex to match: style="something" class="icon-style-four" style="something_else"
text = re.sub(r'style="([^"]+)"\s*class="icon-style-four"\s*style="([^"]+)"', merge_styles, text)

# Just in case the order is different: class="icon-style-four" style="..." style="..."
text = re.sub(r'class="icon-style-four"\s*style="([^"]+)"\s*style="([^"]+)"', merge_styles, text)

with open(about_us_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Double styles merged!")
