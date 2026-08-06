import os
import re

about_us_path = r"C:\Users\angam\Downloads\Leano Website V1\About Us\website\About Us.html"

with open(about_us_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Remove the 0px padding/margin styles
text = text.replace(' style="padding-top: 0px; margin-top: 0px;"', '')

# 2. Put back the 100px padding/margin on testimonial-section
text = re.sub(
    r'(<section class="testimonial-section.*?")',
    r'\1 style="padding-top: 100px; margin-top: 100px;"',
    text
)

with open(about_us_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Undone!")
