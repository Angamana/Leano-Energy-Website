import os
import re

about_us_path = r"C:\Users\angam\Downloads\Leano Website V1\About Us\website\About Us.html"

with open(about_us_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update main headings
text = text.replace('<div class="subtitle-head">our Testimonials</div>', '<div class="subtitle-head">Our Future</div>')
text = text.replace('<h2 class="heading-title">What Our Clients Say?</h2>', '<h2 class="heading-title">Mission, Vision and values</h2>')

# 2. Remove quote images, author images, and designations
text = re.sub(r'<div class="testimonial-quote-wrap">.*?</div>', '', text, flags=re.DOTALL)
text = re.sub(r'<div class="testimonial-one-image-wrap">.*?</div>', '', text, flags=re.DOTALL)
text = re.sub(r'<div class="testimonial-one-designation">.*?</div>', '', text, flags=re.DOTALL)

# 3. Change the author names to VISION, MISSION, VALUES
# The names are inside <div class="text-style-h5">
# We have 3 slides, so let's replace the first 3 occurrences
parts = text.split('<div class="text-style-h5">')
if len(parts) >= 4:
    parts[1] = "VISION</div>" + parts[1].split('</div>', 1)[1]
    parts[2] = "MISSION</div>" + parts[2].split('</div>', 1)[1]
    parts[3] = "VALUES</div>" + parts[3].split('</div>', 1)[1]
    text = '<div class="text-style-h5">'.join(parts)

# 4. Replace the testimonial descriptions with the provided content (no quotes)
new_texts = [
    "Developed on sustainable values and creating empowerment opportunities in South Africa, whilst striving to promote sustainable energy.",
    "Leano Energy aims to enter the green energy market by promoting renewable energy together with high quality and affordable services.",
    "We conduct our business with integrity and are committed to meeting and exceeding customer expectations to ensure client retention."
]

def replace_desc(match):
    if not hasattr(replace_desc, 'counter'):
        replace_desc.counter = 0
    idx = replace_desc.counter
    replace_desc.counter += 1
    new_text = new_texts[idx] if idx < len(new_texts) else ""
    return f'<div class="testimonial-one-desc">{new_text}</div>'

text = re.sub(r'<div class="testimonial-one-desc">.*?</div>', replace_desc, text, flags=re.DOTALL)

# 5. Remove the stars
# They are inside <div class="star-wrap">
text = re.sub(r'<div\s*class="star-wrap">.*?</div>\s*</div>', '', text, flags=re.DOTALL)

with open(about_us_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Updates complete!")
