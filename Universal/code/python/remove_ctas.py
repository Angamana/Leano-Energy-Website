import re

services_path = r'C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html'
with open(services_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Remove the CTA spans and their <br> tags
# The span looks like: <span onclick="window.location.href='../../Contact Us/website/Contact Us.html'" style='color: var(--theme-color); text-decoration: underline; font-weight: bold; cursor: pointer;'>Request a Quote</span>
pattern = r'<br><br><span[^>]*>[^<]+</span>(?:<div style="height: 30px;"></div>)?'
text = re.sub(pattern, '', text, flags=re.IGNORECASE)

with open(services_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Removed CTA buttons and spacers from Services.html')
