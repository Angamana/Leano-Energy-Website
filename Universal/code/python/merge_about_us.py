import os
import re

about_us_path = r"C:\Users\angam\Downloads\Leano Website V1\About Us\website\About Us.html"

with open(about_us_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Extract the Testimonial Section
testi_match = re.search(r'(<section class="testimonial-section section-margin bg-white">.*?</section>)', text, re.DOTALL)
if testi_match:
    testi_html = testi_match.group(1)
    text = text.replace(testi_html, "")
else:
    print("Could not find testimonial section")

# 2. Extract the Tabs Wrapper from Part 5
# It looks like: <div data-current="Tab 2" data-easing="ease" data-duration-in="300" data-duration-out="100" class="tab-image w-tabs" style="margin-bottom: 80px;"> ... </div></section>
tabs_wrapper_match = re.search(r'(<div data-current="Tab 2".*?class="tab-image w-tabs".*?</div>\s*</div>\s*</div>\s*)</div></section>', text, re.DOTALL)
if not tabs_wrapper_match:
    # Try a more generic match
    tabs_wrapper_match = re.search(r'(<div data-current="Tab 2".*?class="tab-image w-tabs".*?)(</section>)', text, re.DOTALL)

if tabs_wrapper_match:
    tabs_html = tabs_wrapper_match.group(1)
else:
    print("Could not find tabs wrapper")
    
# 3. Delete Part 5 completely (the second tab-image-section)
# We'll just find it and remove it.
# It starts with <section class="tab-image-section section-margin"> and has <div class="subtitle-head">About Us</div>
part5_match = re.search(r'<section class="tab-image-section section-margin">.*?<div class="subtitle-head">About Us</div>.*?</section>', text, re.DOTALL)
if part5_match:
    text = text.replace(part5_match.group(0), "")

# 4. Modify Part 1 (Our Purpose) and inject the tabs
# Replace subtitle
text = text.replace('<div class="subtitle-head">Our Purpose</div>', '<div class="subtitle-head">About Us</div>')

# Clear the right side text (Mission/Vision)
# It's inside <div class="tab-image-right">
# We want to keep the structure but empty the text, or just remove the <div class="tab-image-right"> entirely.
# Let's just remove the text inside heading-subheading-desc
text = re.sub(r'(<div class="heading-subheading-desc">).*?(</div>)', r'\g<1>\g<2>', text, flags=re.DOTALL)

# Now inject the tabs_html right before the closing </section> of Part 1.
# Since we deleted Part 5, the first </section> after "Sustainable Values" should be Part 1's end.
part1_end_match = re.search(r'(<h2 class="heading-title">Sustainable Values.*?)</section>', text, re.DOTALL)
if part1_end_match:
    # Find the last </div> before </section> in Part 1 to insert tabs
    # The end of Part 1 looks like: </div></div></div></div></div></section>
    # We can just replace </section> with the tabs_html + </section>
    
    # Wait, we need to be careful. Let's just do a specific replace on the first tab-image-section's end.
    pass

# A safer way to inject into Part 1:
# Find the exact string that ends Part 1.
# It ends with: </div>\n  </div>\n  </div>\n  </div>\n  </div></section>
# Let's replace the first </section> that comes after "Sustainable Values"
def inject_tabs(match):
    return match.group(1) + "\n" + tabs_html + "\n</section>"

text = re.sub(r'(<h2 class="heading-title">Sustainable Values.*?)(\n\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*)</section>', inject_tabs, text, flags=re.DOTALL)

# 5. Inject Testimonials Section right after the combined Part 1
# We just append testi_html after the </section> of Part 1.
def inject_testi(match):
    return match.group(0) + "\n\n" + testi_html + "\n\n"

text = re.sub(r'<h2 class="heading-title">Sustainable Values.*?</section>', inject_testi, text, flags=re.DOTALL)

with open(about_us_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Update successful!")
