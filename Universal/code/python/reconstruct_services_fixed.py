import os
import re

about_us_path = r"C:\Users\angam\Downloads\Leano Website V1\About Us\website\About Us.html"
index_path = r"C:\Users\angam\Downloads\Leano Website V1\Index\website\Index.html"
services_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html"

# 1. Get the About Us content
with open(about_us_path, "r", encoding="utf-8") as f:
    about_content = f.read()

# 2. Get the Index content
with open(index_path, "r", encoding="utf-8") as f:
    index_content = f.read()

# 3. Extract Head + Navbar + Breadcrumb from About Us
# It starts at the top and goes until the end of the <section class="breadcrumb-section">
# Wait, let's find the end of breadcrumb-section
breadcrumb_start = about_content.find('<section class="breadcrumb-section">')
breadcrumb_end = about_content.find('</section>', breadcrumb_start) + 10
top_part = about_content[:breadcrumb_end]

# Ensure we use Services specific CSS link
# About Us has: <link href="../code/css/About Us CSS Code.css" rel="stylesheet" type="text/css"/>
# We need: <link href="../code/css/Services%20CSS%20Code.css" rel="stylesheet" type="text/css"/>
top_part = top_part.replace('href="../code/css/About Us CSS Code.css"', 'href="../code/css/Services%20CSS%20Code.css"')
# And correct the wf-page attribute for Services page:
top_part = re.sub(r'data-wf-page="[a-z0-9]+"', 'data-wf-page="68ec88daad774d7bbc39b100"', top_part)

# 4. Extract Services Section from Index
service_start = index_content.find('<section class="service-section')
service_end = index_content.find('</section>', service_start) + 10
services_part = index_content[service_start:service_end]

# 5. Extract Footer from Index
footer_start = index_content.find('<footer class="footer">')
footer_part = index_content[footer_start:]

# 6. Combine them
reconstructed_services = top_part + "\n" + services_part + "\n" + footer_part

# 7. Fix the Hero text in the Breadcrumb
reconstructed_services = reconstructed_services.replace(">About Us<", ">Services<")
reconstructed_services = reconstructed_services.replace(">About Leano Energy<", ">Our Services<")
reconstructed_services = reconstructed_services.replace(">Powering South Africa Since 2016<", ">Comprehensive Fuel Solutions for Every Industry<")

# 8. Fix the intro text in the Services section from Index
reconstructed_services = re.sub(
    r'>quality industy is the better future<',
    '>Comprehensive Fuel Solutions for Every Industry<',
    reconstructed_services,
    flags=re.IGNORECASE
)
reconstructed_services = re.sub(
    r'<div class="heading-subheading-desc">.*?</div>',
    '<div class="heading-subheading-desc">At Leano Energy, we go beyond mere delivery. We offer a full suite of services designed to optimize your operations, reduce costs, and ensure a steady supply of energy whenever and wherever you need it.</div>',
    reconstructed_services
)

# 9. Update the <title> tag
reconstructed_services = re.sub(r'<title>.*?</title>', '<title>Services | Leano Energy</title>', reconstructed_services)

# 10. Re-append features since we are pulling from Index again
services_features = [
    "Reliable delivery schedules, certified fuel quality, competitive pricing.",
    "Smart meters, secure storage tanks, detailed analytics.",
    "High-performance formulas, diverse applications, technical support.",
    "Mobile tanks, rapid setup, strict compliance."
]
pattern_desc = re.compile(r'(<div class="service-one-desc">)(.*?)(</div>)')
def repl_desc(match):
    global desc_idx
    feats = services_features[desc_idx % 4]
    desc_idx += 1
    if "<strong>Features:</strong>" not in match.group(2):
        return f'{match.group(1)}{match.group(2)}<br><br><strong>Features:</strong> {feats}{match.group(3)}'
    return match.group(0)

desc_idx = 0
reconstructed_services = pattern_desc.sub(repl_desc, reconstructed_services)

# Save the restored Services.html
with open(services_path, "w", encoding="utf-8") as f:
    f.write(reconstructed_services)

print("Services page successfully reconstructed with full CSS and header!")
