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
# It starts at the top and goes until the end of the <section class="marquee-section">
marquee_end = about_content.find('</section>', about_content.find('<section class="marquee-section"')) + 10
top_part = about_content[:marquee_end]

# 4. Extract Services Section from Index
# It's <section class="service-section section-gap section-margin"> ... </section>
service_start = index_content.find('<section class="service-section')
service_end = index_content.find('</section>', service_start) + 10
services_part = index_content[service_start:service_end]

# 5. Extract Footer from Index or About
footer_start = index_content.find('<footer class="footer">')
footer_part = index_content[footer_start:]

# 6. Combine them
reconstructed_services = top_part + "\n" + services_part + "\n" + footer_part

# 7. Fix the Hero text in the Breadcrumb
# About Us had "About Us" and "Powering South Africa Since 2016" (or Home > About Us)
reconstructed_services = reconstructed_services.replace(">About Us<", ">Services<")
reconstructed_services = reconstructed_services.replace(">About Leano Energy<", ">Our Services<")
reconstructed_services = reconstructed_services.replace(">Powering South Africa Since 2016<", ">Comprehensive Fuel Solutions for Every Industry<")

# Fix the marquee text from About to "Fuel up for the journey ahead" or similar, 
# wait, the about page marquee probably says something like "quality industy is the better future"
# I'll just change any marquee text to "Comprehensive Fuel Solutions"
reconstructed_services = re.sub(r'<div class="marquee-text">.*?</div>', '<div class="marquee-text">Comprehensive Fuel Solutions</div>', reconstructed_services)

# 8. Fix the intro text in the Services section from Index
# The Index services section has "our Services" and "quality industy is the better future"
# (Wait, I replaced it in index? Yes, I replaced it to "Comprehensive Fuel Solutions for Every Industry" in Index?)
# Let's just make sure it's correct.
reconstructed_services = re.sub(
    r'>quality industy is the better future<',
    '>Comprehensive Fuel Solutions for Every Industry<',
    reconstructed_services,
    flags=re.IGNORECASE
)
# Ensure intro is there:
# "At Leano Energy, we go beyond mere delivery. We offer a full suite of services designed to optimize your operations, reduce costs, and ensure a steady supply of energy whenever and wherever you need it."
reconstructed_services = re.sub(
    r'<div class="heading-subheading-desc">.*?</div>',
    '<div class="heading-subheading-desc">At Leano Energy, we go beyond mere delivery. We offer a full suite of services designed to optimize your operations, reduce costs, and ensure a steady supply of energy whenever and wherever you need it.</div>',
    reconstructed_services
)

# 9. Update the <title> tag
reconstructed_services = re.sub(r'<title>.*?</title>', '<title>Services | Leano Energy</title>', reconstructed_services)

# Save the restored Services.html
with open(services_path, "w", encoding="utf-8") as f:
    f.write(reconstructed_services)

print("Services page successfully reconstructed from components!")
