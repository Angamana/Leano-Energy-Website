import os
import re

about_us_path = r"C:\Users\angam\Downloads\Leano Website V1\About Us\website\About Us.html"

with open(about_us_path, "r", encoding="utf-8") as f:
    text = f.read()

# Remove the inline style I added previously
text = text.replace(' style="padding-top: 100px; margin-top: 100px;"', '')

# To reduce the white space, we can either remove the 'section-margin' class from these sections,
# or we can apply an inline style overriding the top padding/margin.
# Let's add an inline style to override the top margin and padding to something smaller, like 40px, or 0.
# The user wants to "remove the padding", which might mean setting it to 0. Let's set padding-top and margin-top to 0.

# 1. For tab-image-section
text = re.sub(
    r'(<section class="tab-image-section.*?")',
    r'\1 style="padding-top: 0px; margin-top: 0px;"',
    text
)

# 2. For testimonial-section
text = re.sub(
    r'(<section class="testimonial-section.*?")',
    r'\1 style="padding-top: 0px; margin-top: 0px;"',
    text
)

with open(about_us_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Padding removed!")
