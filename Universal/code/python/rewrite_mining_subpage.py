import re

path = r'C:\Users\angam\Downloads\Leano Website V1\Industries\Industries Sub Page 1\website\Industries Sub Page 1.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove the left column "PROJECT INFORMATION"
# We match from <div class="project-detail-left to the closing </div> of that column.
# The structure is <div class="project-detail-left ..."> ... <div class="project-social-icons"> ... </div> </div> </div> </div>
# The left column is `<div class="project-detail-left column-767-padding-0 w-col w-col-4 w-col-stack">`
# Let's replace the whole `project-detail-left` div up to its closing tag. Since there are nested divs, we use a targeted regex.
# Looking at the file, the left column ends right before `<div class="project-details-right-column`

pattern_left = r'<div class="project-detail-left.*?(?=<div class="project-details-right-column)'
text = re.sub(pattern_left, '', text, flags=re.DOTALL)

# 2. Change right column to full width
text = text.replace('w-col-8', 'w-col-12')

# 3. Replace the inner content of the right column
# From `<div class="project-details-inner">` to its matching closing tag.
# We know the content ends just before `</div>` then `</div>` then `</div>` then `</section>` then `<section class="project-section section-margin project-detail">` (or similar)
# Let's just find the `project-details-inner` div and replace its contents.
# Wait, the easiest way is to use regex to capture everything from `<div class="project-details-inner">` to `</section>` and replace the inner content.

new_inner = """<div class="project-details-inner">
<div class="white-desc-text w-richtext" data-w-id="e8c1471f-7458-799f-7436-d60cb904e86a">
<h5>Mining & Civil Engineering</h5>
<p>Efficient fuel management is critical in mining and civil engineering operations. Leano Energy reduces fuel wastage through IoT-driven monitoring systems and strategic bulk supply, lowering operational costs for heavy plant machinery and large-scale construction projects.</p>
</div>

<div class="white-desc-text w-richtext" style="margin-top: 40px;">
<ul role="list">
<li><strong style="color: #f6722b;">Precision Fuel Management :</strong> accurate tracking and automated reporting</li>
<li><strong style="color: #f6722b;">Bulk Diesel Supply :</strong> high-volume, cost-effective deliveries</li>
<li><strong style="color: #f6722b;">Operational Efficiency :</strong> minimising downtime and maximising productivity</li>
</ul>
</div>
</div>
</div>
</div>
</section>"""

# Find where it starts
start_tag = '<div class="project-details-inner">'
end_tag = '</section>'
# We want to replace from start_tag up to the FIRST </section> after it.
pattern_inner = r'<div class="project-details-inner">.*?</section>'
text = re.sub(pattern_inner, new_inner, text, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated Mining sub page!')
