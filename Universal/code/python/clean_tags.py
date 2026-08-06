import os

about_us_path = r"C:\Users\angam\Downloads\Leano Website V1\About Us\website\About Us.html"

with open(about_us_path, "r", encoding="utf-8") as f:
    text = f.read()

# The string to remove
bad_string = """<section class="testimonial-section section-margin bg-white" style="padding-top: 100px;">
        
            </div>
            <div class="testimonial-triangle display-none-767"></div>
        </div>"""

good_string = """<section class="testimonial-section section-margin bg-white" style="padding-top: 100px;">"""

# In case there are differences in whitespace
import re
text = re.sub(
    r'<section class="testimonial-section section-margin bg-white" style="padding-top: 100px;">\s*</div>\s*<div class="testimonial-triangle display-none-767"></div>\s*</div>',
    good_string,
    text
)

# Also let's change padding-top to margin-top to see if it spaces them better.
text = text.replace('style="padding-top: 100px;"', 'style="padding-top: 100px; margin-top: 100px;"')

with open(about_us_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Cleanup and spacing applied!")
