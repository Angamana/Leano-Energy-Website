import os
import re

html_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# We need to add features back to the 4 services.
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
    # Check if features are already there to prevent double appending
    if "<strong>Features:</strong>" not in match.group(2):
        new_html = f'{match.group(1)}{match.group(2)}<br><br><strong>Features:</strong> {feats}{match.group(3)}'
        return new_html
    return match.group(0)

desc_idx = 0
content = pattern_desc.sub(repl_desc, content)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Features appended successfully!")
