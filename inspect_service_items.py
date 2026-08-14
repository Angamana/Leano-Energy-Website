import re

with open(r'C:\Users\angam\Downloads\Leano Website V1\index.html', encoding='utf-8') as f:
    c = f.read()

# Find all service-one blocks
blocks = re.findall(r'<div class="service-one".*?data-w-id="service-one-\d\d".*?</div>\s*</div>\s*</div>\s*</div>\s*</div>', c, re.DOTALL)

print(f"Found {len(blocks)} service-one blocks")
for b in blocks:
    title_m = re.search(r'<div class="service-one-title">(.*?)</div>', b)
    num_m = re.search(r'<div class="service-one-number">(.*?)</div>', b)
    cats_m = re.findall(r'<div class="service-one-category">(.*?)</div>', b)
    desc_m = re.search(r'<div class="service-one-desc">(.*?)</div>', b, re.DOTALL)
    
    title = title_m.group(1) if title_m else ""
    num = num_m.group(1) if num_m else ""
    cats = ", ".join(cats_m)
    desc = desc_m.group(1).strip() if desc_m else ""
    
    print(f"\nItem {num}: {title}")
    print(f"  Categories: {cats}")
    print(f"  Description: {desc[:100]}...")
