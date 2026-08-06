import re
import os
from glob import glob
from collections import Counter

old_css_files = glob(r"C:\Users\angam\Downloads\Leano Website V1\Old Leano Website\**\*.css", recursive=True)
all_colors = []

for filepath in old_css_files:
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        colors = re.findall(r'#([0-9a-fA-F]{6})\b', content)
        all_colors.extend(colors)
    except:
        pass

counts = Counter(all_colors)
print("Most common colors in old website CSS:")
for color, count in counts.most_common(20):
    print(f"  #{color.lower()} (used {count} times)")
