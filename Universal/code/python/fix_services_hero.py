import os
import re

services_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html"

with open(services_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Fix the double "Services" in Navbar
# We want to find the LAST occurrence of <div class="nav-text">Services</div> and replace it with Contact
# It's inside <a ... href="../../Contact Us/website/Contact Us.html">
pattern_nav = re.compile(r'(<a[^>]+href="\.\./\.\./Contact Us/website/Contact Us\.html"[^>]*>.*?)>Services<', re.DOTALL)
content = pattern_nav.sub(r'\1>Contact<', content)

# 2. Fix subtitle "Selected Work" to "FORGING THE FUTURE"
content = content.replace('Selected Work', 'FORGING THE FUTURE')

# 3. Fix Title "Get in touch" to "SERVICE DETAIL"
content = content.replace('Get in touch', 'SERVICE DETAIL')

# 4. Add the button "DISCOVER MORE" right below the title
button_html = """
<div style="margin-top: 30px;">
  <a class="button-link w-inline-block" href="#">
    <div class="button-arrow-bg-color">
      <div class="button-arrow-wrap">
        <img alt="right-arrow" class="button-arrow" loading="lazy" src="../../Universal/images/6933c0d28e5f2dde71dad538_right-arrow.svg"/>
        <img alt="right-arrow" class="button-arrow-hover" loading="lazy" src="../../Universal/images/6933c0d28e5f2dde71dad538_right-arrow.svg"/>
      </div>
    </div>
    <div class="button-text-wrapper">
      <div class="button-text-wrap">
        <p class="button-text">DISCOVER MORE</p>
        <p class="button-text-hover">DISCOVER MORE</p>
      </div>
      <div class="button-text-bg-color"></div>
    </div>
  </a>
</div>
"""

# Find where to insert the button
pattern_title = re.compile(r'(<h2 class="breadcrumb-heading-title">SERVICE DETAIL</h2>\s*</div>)')
if "DISCOVER MORE" not in content:
    content = pattern_title.sub(r'\1' + button_html, content)

# 5. Change the background image to the slider image as a fallback (since we don't have the man image)
# We will use slider-01-01.jpg which is a hero image
content = content.replace('691edc4e31661c6f978eaa61_titlebar-bg.jpg', '../../Index/images/6933ca91c0f1dc94d644face_slider-01-01.jpg')

with open(services_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed hero section of Services.html!")
