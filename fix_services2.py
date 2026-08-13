import re
with open(r'C:\Users\angam\Downloads\Leano Website V1\Services\Services Main Page\website\Services Main Page.html', 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace(r'src=\"../../../Index', 'src=\"../../../Index')
with open(r'C:\Users\angam\Downloads\Leano Website V1\Services\Services Main Page\website\Services Main Page.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Services images fixed')
