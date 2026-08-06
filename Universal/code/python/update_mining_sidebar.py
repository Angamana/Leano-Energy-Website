import re

path = r'C:\Users\angam\Downloads\Leano Website V1\Industries\Industries Sub Page 1\website\Industries Sub Page 1.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

replacements = {
    '>PROJECT INFORMATION<': '>INDUSTRY INFORMATION<',
    '>CLIENT :<': '>CLIENTS :<',
    '>Mary Kent<': '>Mines<',
    '>CATEGORY :<': '>SECTOR :<'
}

for old, new in replacements.items():
    text = text.replace(old, new)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated Sidebar Information in Mining Sub Page!')
