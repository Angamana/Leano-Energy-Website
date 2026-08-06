import os

about_us_path = r"C:\Users\angam\Downloads\Leano Website V1\About Us\website\About Us.html"

with open(about_us_path, "r", encoding="utf-8") as f:
    text = f.read()

# Find the Our Team text
idx_our_team = text.find('<div class="subtitle-head white-text">Our Team</div>')
if idx_our_team == -1:
    idx_our_team = text.lower().find('our team', text.lower().find('our team') + 1)

# Backtrack to the <section ...
sec_start = text.rfind('<section', 0, idx_our_team)
# Find the end of this section
sec_end = text.find('</section>', sec_start) + len('</section>')

# Remove this chunk
text = text[:sec_start] + text[sec_end:]

with open(about_us_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Our Team section removed!")
