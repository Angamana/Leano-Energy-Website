import re
import urllib.parse

path = r'C:\Users\angam\Downloads\Leano Website V1\Contact Us\website\Contact Us.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the iframe src, aria-label, and title
# Old: <iframe aria-label="jersery city new york" height="100%" loading="lazy" src="https://maps.google.com/maps?q=jersery%20city%20new%20york&amp;t=m&amp;z=15&amp;output=embed&amp;iwloc=near" title="jersery city new york" width="100%">

address = "120 11th Street Parkmore Sandton 2196"
encoded_address = urllib.parse.quote(address)

new_src = f"https://maps.google.com/maps?q={encoded_address}&amp;t=m&amp;z=15&amp;output=embed&amp;iwloc=near"

# Replace src
text = re.sub(r'src="https://maps\.google\.com/maps\?q=[^"]+"', f'src="{new_src}"', text)

# Replace aria-label
text = re.sub(r'aria-label="jersery city new york"', 'aria-label="Leano Energy Office Location"', text)

# Replace title
text = re.sub(r'title="jersery city new york"', 'title="Leano Energy Office Location"', text)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated Google Maps iframe!')
