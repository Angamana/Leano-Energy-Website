import re
import os

services_path = r'C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html'
with open(services_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Split by '<section'
sections = re.split(r'(?=<section)', text)

# Filter out the team section
new_sections = []
for sec in sections:
    if 'team-slider' in sec and 'Our Team' in sec:
        print("Removing section:", sec[:100].strip(), "...")
    else:
        new_sections.append(sec)

new_text = "".join(new_sections)

with open(services_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Team section removed.")
