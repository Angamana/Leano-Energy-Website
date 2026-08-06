import os
import re

html_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove irrelevant sections
# The staticbox tabbed section: starts at `<section class="staticbox-section section-gap">` line 304
# The 4-icon grid is right after it, ending before `<section class="service-section section-gap section-margin">` line 421
# We can use regex to remove from `<section class="staticbox-section` to just before `<section class="service-section`
content = re.sub(r'<section class="staticbox-section.*?</section>', '', content, flags=re.DOTALL)

# 2. Hero & Intro
content = re.sub(
    r'>quality industy is the better future<',
    '>Comprehensive Fuel Solutions for Every Industry<',
    content,
    flags=re.IGNORECASE
)
content = re.sub(
    r'>We support the gas and oil sector with high-precision engineered solutions designed to perform under extreme pressure, and load condition.<',
    '>At Leano Energy, we go beyond mere delivery. We offer a full suite of services designed to optimize your operations, reduce costs, and ensure a steady supply of energy whenever and wherever you need it.<',
    content
)

# 3. Service Listings
# Let's extract the 4 service blocks and replace them.
# The structure inside service-one-desc-wrap is:
# <div class="service-one-desc">...</div>
# We can just do a sequential replacement of titles, categories, and descriptions.

services_data = [
    {
        "title": "Bulk Fuel Supply & Distribution",
        "cats": ("Distribution", "Supply"),
        "desc": "Supplying high-quality fuels—including Petrol, Diesel, Paraffin, Oils, and Biofuel—across Gauteng, Mpumalanga, Limpopo, and the North West. We cater to wholesale, retail, and commercial sectors.",
        "features": "Reliable delivery schedules, certified fuel quality, competitive pricing."
    },
    {
        "title": "Fuel Management Solutions",
        "cats": ("Management", "Monitoring"),
        "desc": "Protect your business from fuel theft and mismanagement. Our advanced systems include on-site storage solutions, monthly consumption monitoring, and real-time reporting.",
        "features": "Smart meters, secure storage tanks, detailed analytics."
    },
    {
        "title": "Lubricants & Oils",
        "cats": ("Lubricants", "Industrial"),
        "desc": "A comprehensive range of industrial lubricants to keep your machinery running smoothly, reducing wear and extending equipment lifespan.",
        "features": "High-performance formulas, diverse applications, technical support."
    },
    {
        "title": "Logistics & Temporary Sites",
        "cats": ("Biofuel", "Sustainable"), # Actually the tags from index were different but these are fine or I can use ("Logistics", "Temporary")
        "desc": "Need fuel at a remote mining site or a temporary construction project? We specialize in setting up rapid-deployment fuel stations tailored to your project’s duration.",
        "features": "Mobile tanks, rapid setup, strict compliance."
    }
]

# We need to replace the Titles
# In the template, titles are like <div class="service-one-title">CNC Turning</div>
old_titles = ["CNC Turning", "Robot Installation", "Renewable energy", "Gas &amp; oil industry"]
for i, old_t in enumerate(old_titles):
    content = content.replace(f'<div class="service-one-title">{old_t}</div>', f'<div class="service-one-title">{services_data[i]["title"]}</div>')
    # Replace the HTML entity version just in case
    content = content.replace(f'<div class="service-one-title">{old_t.replace("&amp;", "&")}</div>', f'<div class="service-one-title">{services_data[i]["title"]}</div>')

# We need to replace Categories
pattern_cats = re.compile(r'(<div class="service-one-category-list">\s*<div class="service-one-category">)(.*?)(</div>\s*<div class="service-one-category">)(.*?)(</div>\s*</div>)')
def repl_cats(match):
    global cat_idx
    tag = services_data[cat_idx % 4]["cats"]
    cat_idx += 1
    return match.group(1) + tag[0] + match.group(3) + tag[1] + match.group(5)
cat_idx = 0
content = pattern_cats.sub(repl_cats, content)

# We need to replace Descriptions and add features
# Structure: <div class="service-one-desc">...</div>
pattern_desc = re.compile(r'(<div class="service-one-desc">)(.*?)(</div>)')
def repl_desc(match):
    global desc_idx
    data = services_data[desc_idx % 4]
    desc_idx += 1
    # Add features bolded underneath the description
    new_html = f'{match.group(1)}{data["desc"]}<br><br><strong>Features:</strong> {data["features"]}{match.group(3)}'
    return new_html
desc_idx = 0
content = pattern_desc.sub(repl_desc, content)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Services page successfully migrated! Replaced {cat_idx} categories and {desc_idx} descriptions.")
