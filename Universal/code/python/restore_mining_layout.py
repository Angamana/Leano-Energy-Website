import re

# We will read from Sub Page 2 which is pristine
src_path = r'C:\Users\angam\Downloads\Leano Website V1\Industries\Industries Sub Page 2\website\Industries Sub Page 2.html'
dest_path = r'C:\Users\angam\Downloads\Leano Website V1\Industries\Industries Sub Page 1\website\Industries Sub Page 1.html'

with open(src_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Fix the title and breadcrumb heading to match Sub Page 1 (Mining)
text = re.sub(r'<title>Leano Energy \| Agriculture</title>', '<title>Leano Energy | Mining</title>', text)
text = re.sub(r'<h2 class="breadcrumb-heading-title">.*?</h2>', '<h2 class="breadcrumb-heading-title">Reliable fuel supply and management solutions to keep heavy mining machinery running. </h2>', text)

# Sidebar fixes:
# Change Category value from Agriculture to Mining
text = re.sub(r'(<div class="meta-data-title">Category :</div>\s*<div class="project-meta-value">).*?(</div>)', r'\g<1>Mining\g<2>', text)

# Remove Date
text = re.sub(r'<div class="meta-data"[^>]*>\s*<div class="meta-data-title">Date :</div>\s*<div class="project-meta-value">.*?</div>\s*</div>', '', text, flags=re.DOTALL)

# Remove Website
text = re.sub(r'<div class="meta-data">\s*<div class="meta-data-title">Website :</div>\s*<div class="project-meta-value">.*?</div>\s*</div>', '', text, flags=re.DOTALL)

# Main Content Fixes:
# An overview of our project -> Mining & Civil Engineering Solutions
text = re.sub(r'<h5>An overview of our project</h5>', '<h5>Mining & Civil Engineering Solutions</h5>', text)

# Overview text replacement
old_overview_pattern = r'<p>Industry the summer, starting in mid-May.*?evaluate the attractiveness\.</p>'
new_overview = '<p>Efficient fuel management is critical in mining and civil engineering operations. Leano Energy reduces fuel wastage through IoT-driven monitoring systems and strategic bulk supply, lowering operational costs for heavy plant machinery and large-scale construction projects.</p>'
text = re.sub(old_overview_pattern, new_overview, text, flags=re.DOTALL)

# Rebrand "The process we follow" -> "Our Delivery Process"
text = re.sub(r'<h5>The process we follow</h5>', '<h5>Our Delivery Process</h5>', text)

# Rebrand "What We Did" -> "Key Value Drivers"
text = re.sub(r'<h5>What We Did</h5>', '<h5>Key Value Drivers</h5>', text)
text = re.sub(r'<p>Working with team was a seamless experience from start to finish.*?</p>', '<p>We bring unparalleled efficiency to mining and civil engineering operations through precise, data-backed solutions that scale with your project needs.</p>', text, flags=re.DOTALL)

# Replace the bullet points
new_bullets = """<ul role="list">
<li><strong>Precision Fuel Management :</strong> accurate tracking and automated reporting</li>
<li><strong>Bulk Diesel Supply :</strong> high-volume, cost-effective deliveries</li>
<li><strong>Operational Efficiency :</strong> minimising downtime and maximising productivity</li>
</ul>"""
text = re.sub(r'<ul role="list">.*?</ul>', new_bullets, text, flags=re.DOTALL)

with open(dest_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Restored and updated Mining sub page!')
