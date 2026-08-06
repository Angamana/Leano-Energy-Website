import re

services_path = r'C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html'
with open(services_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the style we added previously
old_style = "style='color: var(--theme-color); text-decoration: underline; font-weight: bold; cursor: pointer; display: inline-block; margin-bottom: 30px;'"
new_style = "style='color: var(--theme-color); text-decoration: underline; font-weight: bold; cursor: pointer;'"

# Replace it back
text = text.replace(old_style, new_style)

# Add a spacer div after Request a Quote</span> and Learn About Biofuel</span>
text = re.sub(r'(Request a Quote</span>)', r'\1<div style="height: 30px;"></div>', text)
text = re.sub(r'(Learn About Biofuel</span>)', r'\1<div style="height: 30px;"></div>', text)

with open(services_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Added spacer div below CTAs.')
