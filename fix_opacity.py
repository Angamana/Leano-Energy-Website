import re
with open(r'C:\Users\angam\Downloads\Leano Website V1\Services\Services Sub Page 4\website\Services Sub Page 4.html', 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('style=\"width: 100%; height: 100%; object-fit: cover; object-position: center 60%; transform: translateY(-20px);\"', 'style=\"width: 100%; height: 100%; object-fit: cover; object-position: center 60%; transform: translateY(-20px); opacity: 0.2;\"')
with open(r'C:\Users\angam\Downloads\Leano Website V1\Services\Services Sub Page 4\website\Services Sub Page 4.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Opacity updated')
