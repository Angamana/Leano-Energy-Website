import re

path = r'C:\Users\angam\Downloads\Leano Website V1\Contact Us\website\Contact Us.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

replacements = {
    '"85 Preston, Inglewood"': '"120 11th Street"',
    '"addressLocality": "Maine"': '"addressLocality": "Parkmore Sandton"',
    '"postalCode": "98380"': '"postalCode": "2196"',
    '"addressCountry": "US"': '"addressCountry": "ZA"',
    '"+1(212) 255-511"': '"010 442 4895"',
    '>+1(212) 255-511<': '>010 442 4895<',
    '"example@pbminfotech.com"': '"info@leanoenergy.com"',
    'no-reply@example.com<br/>example@pbminfotech.com': 'info@leanoenergy.com<br/>www.leanoenergy.com',
    'Phone: +001 236-895-4732<br/>Mobile: +93 895-4732-236': '010 442 4895<br/>061 427 6602',
    '85 Preston, Inglewood, Maine 98380, Hoofddorp Noord- 2132': '120 11th Street Parkmore Sandton 2196'
}

for old, new in replacements.items():
    text = text.replace(old, new)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated Contact Us page details.')
