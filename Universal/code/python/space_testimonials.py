import os
import re

about_us_path = r"C:\Users\angam\Downloads\Leano Website V1\About Us\website\About Us.html"

with open(about_us_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Add padding-top to testimonial-section to space it from About Us
# The class is "testimonial-section section-margin bg-white"
text = re.sub(
    r'(<section class="testimonial-section.*?")',
    r'\1 style="padding-top: 100px;"',
    text
)

# 2. Remove testimonial-section-one-inner completely.
# Let's find it. It starts with <div class="testimonial-section-one-inner"> and ends where the next major container starts.
# We'll use regex to remove it
text = re.sub(r'<div class="testimonial-section-one-inner">.*?</div>\s*</div>\s*</div>\s*</div>', '', text, flags=re.DOTALL)

# Let's be safer and match up to the end of testimonial-counter-flex's parent w-container, which is 3 divs up.
# Looking at my previous output:
# <div class="testimonial-section-one-inner">
#   <div class="testimonial-one-overlay-one"></div>
#   <div class="testimonial-one-overlay-two"></div>
#   <div class="w-layout-blockcontainer container w-container">
#       <div class="testimonial-counter-flex"> ... </div>
#   </div>
# </div>
# That's exactly one </div> for testimonial-counter-flex, one for w-container, one for testimonial-section-one-inner.
# Wait, let's verify if that's all.
# Yes, it looks like it.

with open(about_us_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Spacing and removal complete!")
