import os
import re

services_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html"

with open(services_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Change the main headline
text = re.sub(
    r'<h2 class="heading-title-two white-text">Smart Processes And Stronger Outcomes</h2>',
    r'<h2 class="heading-title-two white-text">Premium Petroleum Products For Your Every Need</h2>',
    text,
    flags=re.IGNORECASE
)

# Products data
products = [
    {
        "title": "Petrol Unleaded (93, 95ULP)",
        "desc": "High-quality unleaded petrol for automotive and industrial applications. Available in 93 and 95 octane ratings.<br><br><strong>Supplied By:</strong> Sasol, Shell, BP, Engen, Chevron<br><br><a href='../../Contact Us/website/Contact Us.html' style='color: var(--theme-color); text-decoration: underline; font-weight: bold;'>Request a Quote</a>"
    },
    {
        "title": "Diesel (50, 500PPM)",
        "desc": "Premium diesel fuel for commercial and industrial use. Available in 50PPM and 500PPM sulfur content.<br><br><strong>Application:</strong> Mining, agriculture, logistics, factories<br><br><a href='../../Contact Us/website/Contact Us.html' style='color: var(--theme-color); text-decoration: underline; font-weight: bold;'>Request a Quote</a>"
    },
    {
        "title": "Illuminating Paraffin",
        "desc": "Quality paraffin for heating, lighting, and industrial applications.<br><br><a href='../../Contact Us/website/Contact Us.html' style='color: var(--theme-color); text-decoration: underline; font-weight: bold;'>Request a Quote</a>"
    },
    {
        "title": "Oils &amp; Lubricants",
        "desc": "Complete range of engine oils, gear oils, hydraulic oils, compressor oils, and industrial lubricants.<br><br><strong>Brands:</strong> Premium Partner Brands<br><br><a href='../../Contact Us/website/Contact Us.html' style='color: var(--theme-color); text-decoration: underline; font-weight: bold;'>Request a Quote</a>"
    },
    {
        "title": "Biofuel",
        "desc": "Blended biofuel, cleaner, safer, and more sustainable. Less harmful to the environment and better for engine performance.<br><br><a href='../../Contact Us/website/Contact Us.html' style='color: var(--theme-color); text-decoration: underline; font-weight: bold;'>Learn About Biofuel</a>"
    }
]

# We need to extract the Products Detail Section to avoid modifying other tabs
section_match = re.search(r'(<div class="subtitle-head white-text">Products Detail Section</div>.*?)</section>', text, flags=re.DOTALL)
if section_match:
    section_html = section_match.group(1)
    
    # Extract the 5 tabs
    tabs = re.findall(r'(<a data-w-tab="Tab [1-5]" class="staticbox-one.*?</a>)', section_html, flags=re.DOTALL)
    
    if len(tabs) == 5:
        new_tabs = []
        for i, tab in enumerate(tabs):
            prod = products[i]
            # Replace small title
            tab = re.sub(r'<div class="staticbox-title text-style-h3">.*?</div>', f'<div class="staticbox-title text-style-h3">{prod["title"]}</div>', tab)
            # Replace large title inside pane
            tab = re.sub(r'<div class="text-style-h2 white-text">.*?</div>', f'<div class="text-style-h2 white-text">{prod["title"]}</div>', tab)
            # Replace description
            tab = re.sub(r'<div class="staticbox-text">.*?</div>', f'<div class="staticbox-text">{prod["desc"]}</div>', tab)
            new_tabs.append(tab)
            
        # Replace the old tabs with the new tabs in the section html
        new_section_html = section_html
        for i in range(5):
            new_section_html = new_section_html.replace(tabs[i], new_tabs[i])
            
        # Replace the old section with the new section in the full text
        text = text.replace(section_html, new_section_html)

with open(services_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Product details injected successfully!")
