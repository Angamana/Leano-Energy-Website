import re
with open(r'C:\Users\angam\Downloads\Leano Website V1\Services\Services Main Page\website\Services Main Page.html', 'r', encoding='utf-8') as f:
    content = f.read()
content = re.sub(r'src=\"\.\./images/Fuel%20Management%20Solutions%201\.png\"', r'src=\"../../../Index/Index Main Page/images/Fuel Management Solutions 1.png\"', content)
content = re.sub(r'src=\"\.\./images/Fuel%20Management%20Solutions%202\.png\"', r'src=\"../../../Index/Index Main Page/images/Fuel Management Solutions 2.png\"', content)
content = re.sub(r'src=\"\.\./images/Oils%20and%20Lubricants%201\.jpg\" srcset=\".*?\"', r'src=\"../../../Index/Index Main Page/images/Lubricants%20%26%20Oils%201.jpg\"', content)
content = re.sub(r'src=\"\.\./images/Oils%20and%20Lubricants%202\.jpg\" srcset=\".*?\"', r'src=\"../../../Index/Index Main Page/images/Lubricants%20%26%20Oils%202.jpg\"', content)
with open(r'C:\Users\angam\Downloads\Leano Website V1\Services\Services Main Page\website\Services Main Page.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Services images updated')
