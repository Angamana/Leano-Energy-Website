import os

services_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html"

with open(services_path, "r", encoding="utf-8") as f:
    content = f.read()

# I will replace the tags based on their exact line number or sequence to ensure they match perfectly.
# Card 1 (Bulk Fuel Supply) tags: Equipment, Fabricators -> Supply, Distribution
content = content.replace('<div class="service-one-category">Equipment</div>\n                                    <div class="service-one-category">Fabricators</div>', '<div class="service-one-category">Supply</div>\n                                    <div class="service-one-category">Distribution</div>')
content = content.replace('<div class="service-one-category">Equipment</div>\n                                            <div class="service-one-category">Fabricators</div>', '<div class="service-one-category">Supply</div>\n                                            <div class="service-one-category">Distribution</div>')

# Card 2 (Fuel Management) tags: Automation, Engineering -> Management, Technology
content = content.replace('<div class="service-one-category">Automation</div>\n                                    <div class="service-one-category">Engineering</div>', '<div class="service-one-category">Management</div>\n                                    <div class="service-one-category">Technology</div>')
content = content.replace('<div class="service-one-category">Automation</div>\n                                            <div class="service-one-category">Engineering</div>', '<div class="service-one-category">Management</div>\n                                            <div class="service-one-category">Technology</div>')


# Card 3 (Lubricants) tags: Industrial, Equipment -> Lubricants, Maintenance
content = content.replace('<div class="service-one-category">Industrial</div>\n                                    <div class="service-one-category">Equipment</div>', '<div class="service-one-category">Lubricants</div>\n                                    <div class="service-one-category">Maintenance</div>')
content = content.replace('<div class="service-one-category">Industrial</div>\n                                            <div class="service-one-category">Equipment</div>', '<div class="service-one-category">Lubricants</div>\n                                            <div class="service-one-category">Maintenance</div>')

# Card 4 (Logistics) tags: Equipment, Engineering -> Logistics, Remote Sites
content = content.replace('<div class="service-one-category">Equipment</div>\n                                    <div class="service-one-category">Engineering</div>', '<div class="service-one-category">Logistics</div>\n                                    <div class="service-one-category">Remote Sites</div>')
content = content.replace('<div class="service-one-category">Equipment</div>\n                                            <div class="service-one-category">Engineering</div>', '<div class="service-one-category">Logistics</div>\n                                            <div class="service-one-category">Remote Sites</div>')

with open(services_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Tags updated.")
