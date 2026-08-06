import os

about_us_path = r"C:\Users\angam\Downloads\Leano Website V1\About Us\website\About Us.html"

with open(about_us_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix the Tab menu names
content = content.replace('<div class="tab-text">Robot Installation</div>', '<div class="tab-text">Objectives</div>')
content = content.replace('<div class="tab-text">Renewable energy</div>', '<div class="tab-text">Products & Services</div>')
content = content.replace('<div class="tab-text">Gas &amp; oil industry</div>', '<div class="tab-text">Fuel Management</div>')
content = content.replace('<div class="tab-text">CNC Turning</div>', '<div class="tab-text">Comparative Advantages</div>')
content = content.replace('<div class="tab-text">Automation</div>', '<div class="tab-text">Supportive Culture</div>')

with open(about_us_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Tabs fixed!")
