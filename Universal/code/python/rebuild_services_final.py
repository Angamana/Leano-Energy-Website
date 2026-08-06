import os
import re

contact_path = r"C:\Users\angam\Downloads\Leano Website V1\Contact Us\website\Contact Us.html"
index_path = r"C:\Users\angam\Downloads\Leano Website V1\Index\website\Index.html"
services_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html"

# Read sources
with open(contact_path, "r", encoding="utf-8") as f:
    contact_content = f.read()

with open(index_path, "r", encoding="utf-8") as f:
    index_content = f.read()

# 1. Extract Head + Navbar + Breadcrumb from Contact Us
breadcrumb_start = contact_content.find('<section class="breadcrumb-section">')
breadcrumb_end = contact_content.find('</section>', breadcrumb_start) + 10
top_part = contact_content[:breadcrumb_end]

# Fix CSS link and Page ID
top_part = top_part.replace('Contact%20Us%20CSS%20Code.css', 'Services%20CSS%20Code.css')
top_part = top_part.replace('Contact Us CSS Code.css', 'Services%20CSS%20Code.css')
top_part = re.sub(r'data-wf-page="[a-z0-9]+"', 'data-wf-page="68ec88daad774d7bbc39b100"', top_part)

# Fix Title and Breadcrumb text
top_part = re.sub(r'<title>.*?</title>', '<title>Services | Leano Energy</title>', top_part)
top_part = top_part.replace('>Contact Us<', '>Our Services<')
top_part = top_part.replace('>Contact<', '>Services<')
# Sometimes it's Home > Contact Us
top_part = top_part.replace('Home > Contact Us', 'Home > Services')

# 2. Extract Services Section from Index
service_start = index_content.find('<section class="service-section')
service_end = index_content.find('</section>', service_start) + 10
services_part = index_content[service_start:service_end]

# Fix the intro text in the Services section from Index
services_part = re.sub(
    r'>quality industy is the better future<',
    '>Comprehensive Fuel Solutions for Every Industry<',
    services_part,
    flags=re.IGNORECASE
)
services_part = re.sub(
    r'<div class="heading-subheading-desc">.*?</div>',
    '<div class="heading-subheading-desc">At Leano Energy, we go beyond mere delivery. We offer a full suite of services designed to optimize your operations, reduce costs, and ensure a steady supply of energy whenever and wherever you need it.</div>',
    services_part
)

# Append features to services_part
services_features = [
    "Reliable delivery schedules, certified fuel quality, competitive pricing.",
    "Smart meters, secure storage tanks, detailed analytics.",
    "High-performance formulas, diverse applications, technical support.",
    "Mobile tanks, rapid setup, strict compliance."
]
pattern_desc = re.compile(r'(<div class="service-one-desc">)(.*?)(</div>)')
desc_idx = 0
def repl_desc(match):
    global desc_idx
    feats = services_features[desc_idx % 4]
    desc_idx += 1
    if "<strong>Features:</strong>" not in match.group(2):
        return f'{match.group(1)}{match.group(2)}<br><br><strong>Features:</strong> {feats}{match.group(3)}'
    return match.group(0)
services_part = pattern_desc.sub(repl_desc, services_part)

# 3. Extract Footer from Index
footer_start = index_content.find('<footer class="footer">')
footer_part = index_content[footer_start:]

# 4. Combine
final_html = top_part + "\n" + services_part + "\n" + footer_part

# Save the restored Services.html
with open(services_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print("Services page correctly reconstructed with Contact Us header!")
