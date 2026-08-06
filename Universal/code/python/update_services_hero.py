import os
import re

services_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html"

with open(services_path, "r", encoding="utf-8") as f:
    text = f.read()

# Replace Subtitle
text = re.sub(
    r'<div class="breadcrumb-subtitle-head service-page">Our Services</div>',
    r'<div class="breadcrumb-subtitle-head service-page">Our Products</div>',
    text
)

# Replace Headline
text = re.sub(
    r'<h2 class="breadcrumb-heading-title service-page">Comprehensive Fuel Solutions</h2>',
    r'<h2 class="breadcrumb-heading-title service-page">Premium Fuel Products for Every Industry</h2>',
    text
)

# Replace Description
text = re.sub(
    r'<p class="white-text"[^>]*>At Leano Energy, we go beyond mere delivery. We offer a full suite of services designed to optimize your operations, reduce costs, and ensure a steady supply of energy whenever and wherever you need it.</p>',
    r'<p class="white-text" style="margin-top: 20px; margin-bottom: 30px; font-size: 18px; max-width: 800px; line-height: 1.6;">Leano Energy supplies high-quality petroleum products across Gauteng, Mpumalanga, Limpopo, and the North West. We partner with major refineries to ensure consistent quality and competitive pricing.</p>',
    text
)

with open(services_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Services hero updated!")
