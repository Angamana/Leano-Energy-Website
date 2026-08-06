import os
import re

services_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html"
donor_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\Donor\induyst.webflow.io\induyst.webflow.io\services.html"

with open(services_path, "r", encoding="utf-8") as f:
    services_content = f.read()

with open(donor_path, "r", encoding="utf-8") as f:
    donor_content = f.read()

# Find </header> in Donor
header_end_donor = donor_content.find("</header>") + len("</header>")
# Find first </section> after header in Donor
section_end_donor = donor_content.find("</section>", header_end_donor)

donor_hero = donor_content[header_end_donor:section_end_donor]

# Replace CDN URLs in donor_hero
# Images
donor_hero = re.sub(r'https://cdn\.prod\.website-files\.com/[^/]+/', '../../Universal/images/', donor_hero)
# Links
donor_hero = donor_hero.replace('href="/contact"', 'href="../../Contact Us/website/Contact Us.html"')
donor_hero = donor_hero.replace('href="/"', 'href="../../Index/website/Index.html"')

# Find </header> in Services
header_end_services = services_content.find("</header>") + len("</header>")
# Find first </section> after header in Services
section_end_services = services_content.find("</section>", header_end_services)

# Replace the hero section
new_services_content = services_content[:header_end_services] + donor_hero + services_content[section_end_services:]

# Write back
with open(services_path, "w", encoding="utf-8") as f:
    f.write(new_services_content)

print("Hero section perfectly restored from Donor!")
