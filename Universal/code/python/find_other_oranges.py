import re
import os
from collections import Counter

css_path = r"C:\Users\angam\Downloads\Leano Website V1\Index\code\css\induyst.webflow.shared.cac7390ce.css"
with open(css_path, 'r', encoding='utf-8') as f:
    content = f.read()

colors = re.findall(r'#([0-9a-fA-F]{6})\b', content)
counts = Counter(colors)

print("Colors in new CSS (looking for orange-ish):")
for color, count in counts.items():
    r = int(color[0:2], 16)
    g = int(color[2:4], 16)
    b = int(color[4:6], 16)
    if r > 200 and g > 50 and g < 180 and b < 100:
        print(f"  #{color} (used {count} times)")
        
# Also check for rgb/rgba
rgba_colors = re.findall(r'rgba?\s*\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)', content)
for r, g, b in rgba_colors:
    r, g, b = int(r), int(g), int(b)
    if r > 200 and g > 50 and g < 180 and b < 100:
        print(f"  rgba({r}, {g}, {b})")
