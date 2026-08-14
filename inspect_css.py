import re
import glob

files_to_check = [
    r'C:\Users\angam\Downloads\Leano Website V1\index.html',
    r'C:\Users\angam\Downloads\Leano Website V1\Services\Services Main Page\website\Services Main Page.html',
    r'C:\Users\angam\Downloads\Leano Website V1\Services\Services Sub Page 1\website\Services Sub Page 1.html',
    r'C:\Users\angam\Downloads\Leano Website V1\News\News Main Page\website\News Main Page.html',
    r'C:\Users\angam\Downloads\Leano Website V1\About Us\website\About Us.html',
    r'C:\Users\angam\Downloads\Leano Website V1\Contact Us\website\Contact Us.html'
]

print("Checking differences in CSS rules containing order-side-tab-container or z-index or pointer-events...")

for fpath in files_to_check:
    with open(fpath, encoding='utf-8') as f:
        content = f.read()
    
    print(f"\n================ FILE: {fpath} ================")
    # find all style tags
    styles = re.findall(r'<style.*?>.*?</style>', content, re.DOTALL)
    print(f"Total style tags: {len(styles)}")
    
    # check for pointer-events: none
    pe_matches = re.findall(r'[^{}]*pointer-events:[^{}]*', content)
    print(f"pointer-events rules count: {len(pe_matches)}")
    for m in pe_matches[:5]:
        print("   PE:", m.strip()[:100])
        
    # check order-side-tab-container hover rule
    hover_matches = re.findall(r'[^{}]*order-side-tab-container:hover[^{}]*\{[^}]*\}', content)
    print(f"Hover rules count: {len(hover_matches)}")
    for hm in hover_matches:
        print("   HOVER:", hm.strip().replace('\n', ' '))
