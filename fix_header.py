import glob
sub_pages = glob.glob(r'C:\Users\angam\Downloads\Leano Website V1\Services\Services Sub Page *\website\*.html')
for page in sub_pages:
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('style=\"position: absolute; top: 0; left: 0; width: 100%; z-index: 100; background-color: transparent !important; border-bottom: none !important;\"', 'style=\"position: absolute; top: 0; left: 0; width: 100%; z-index: 100; background-color: transparent !important; border-bottom: 1px solid rgba(255, 255, 255, 0.2) !important;\"')
    with open(page, 'w', encoding='utf-8') as f:
        f.write(content)
print('Updated headers on sub pages')
