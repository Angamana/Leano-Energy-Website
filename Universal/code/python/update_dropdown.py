import re

path = r'C:\Users\angam\Downloads\Leano Website V1\Contact Us\website\Contact Us.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

old_options = r'<option value="CNC Turning">CNC Turning</option><option value="Robot Installation">Robot Installation</option><option value="Renewable energy">Renewable energy</option><option value="Gas &amp; oil industry">Gas &amp; oil industry</option>'
new_options = r'<option value="Petrol Unleaded">Petrol Unleaded</option><option value="Diesel">Diesel</option><option value="Illuminating Paraffin">Illuminating Paraffin</option><option value="Oils &amp; Lubricants">Oils &amp; Lubricants</option><option value="Biofuel">Biofuel</option>'

if old_options in text:
    text = text.replace(old_options, new_options)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print('Updated dropdown options!')
else:
    print('Old options not found.')
