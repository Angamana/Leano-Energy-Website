import os
import re

about_us_path = r"C:\Users\angam\Downloads\Leano Website V1\About Us\website\About Us.html"

with open(about_us_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Remove the section-margin class from the two sections to eliminate the extra spacing
# The first section is the tab-image-section
text = text.replace('<section class="tab-image-section section-margin">', '<section class="tab-image-section">')

# The second section is the testimonial-section
text = re.sub(
    r'<section class="testimonial-section section-margin bg-white".*?>',
    '<section class="testimonial-section bg-white">',
    text
)

# 2. Remove all star-wrap divs
text = re.sub(r'<div\s*class="star-wrap">.*?</div>\s*</div>', '</div>', text, flags=re.DOTALL)

# 3. Replace the testimonial descriptions with Mission, Vision, Values
new_texts = [
    "Leano Energy aims to enter the green energy market by promoting renewable energy together with high quality and affordable services.",
    "Developed on sustainable values and creating empowerment opportunities in South Africa, whilst striving to promote sustainable energy.",
    "Sustainable Values. Empowerment. Excellence."
]

def replace_desc(match):
    if not hasattr(replace_desc, 'counter'):
        replace_desc.counter = 0
    
    idx = replace_desc.counter
    replace_desc.counter += 1
    
    # If there are more than 3 slides, just leave them empty or repeat
    new_text = new_texts[idx] if idx < len(new_texts) else ""
    return f'<div class="testimonial-one-desc">{new_text}</div>'

text = re.sub(r'<div class="testimonial-one-desc">.*?</div>', replace_desc, text, flags=re.DOTALL)

# 4. In case I messed up star-wrap removal because of nested divs, let's just do a greedy replace for the stars
text = re.sub(r'<div\s+class="star-wrap">.*?</div>\s*</div>\s*</div>\s*</div>\s*</div>', '</div></div></div>', text, flags=re.DOTALL)
# Actually, the star-wrap was inside testimonial-one-content-group. 
# <div class="testimonial-one-content-group">
#    <div class="testimonial-one-desc">...</div>
#    <div class="star-wrap">...</div>
# </div>
# So we can just remove: <div class="star-wrap">...</div>
text = re.sub(r'<div\s*class="star-wrap">.*?</div>\s*</div>', '', text, flags=re.DOTALL)

with open(about_us_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Updates complete!")
