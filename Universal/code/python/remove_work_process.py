import os
import re

about_us_path = r"C:\Users\angam\Downloads\Leano Website V1\About Us\website\About Us.html"

with open(about_us_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Replace \' with '
text = text.replace(r"\'", "'")

# 2. Remove the Efficient Work Process block from the Hero section
# The block is inside <div class="about-inner">
# We want to remove it up to the end of the container div that it is inside, but keeping the closing tags of the section intact.
# To be safe, we can find `<div class="about-inner">` and remove it and all its children up to the </div> that closes it.
# Actually, it's easier to find the exact substring since it ends right before the closing of the main container.

idx_start = text.find('<div class="about-inner">')
if idx_start != -1:
    idx_end = text.find('<section class="tab-image-section', idx_start)
    if idx_end != -1:
        # We need to backtrack to the closing tag of the previous section
        idx_end = text.rfind('</section>', idx_start, idx_end) + len('</section>')
        
        # Let's see what we are deleting.
        # We want to keep the closing divs of the `w-layout-blockcontainer container w-container` and `about-staticbox-one-flex`.
        # To be precise, let's just use regex to remove `<div class="about-inner">` up to the last `</div>` before `</section>`.
        chunk = text[idx_start:idx_end]
        # Remove everything starting from about-inner up to the closing divs.
        # Actually, let's just find the exact string "Efficient Work Process" and delete the about-inner div.
        
        # Instead of parsing, let's remove exactly: <div class="about-inner"> ... </div>
        # Looking at the original donor file, about-inner has 2 closing divs after it?
        # Let's just do a greedy match up to the end of the section, and replace it with the closing tags:
        text = text[:idx_start] + '    </div>\n        </div>\n    </section>' + text[idx_end:]


with open(about_us_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Updates complete!")
