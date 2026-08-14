import re

def get_style_ids(filepath):
    with open(filepath, encoding='utf-8') as f:
        content = f.read()
    return re.findall(r'<style\s+id=["\'](.*?)["\']', content)

print('INDEX style IDs:', get_style_ids(r'C:\Users\angam\Downloads\Leano Website V1\index.html'))
print('SMAIN style IDs:', get_style_ids(r'C:\Users\angam\Downloads\Leano Website V1\Services\Services Main Page\website\Services Main Page.html'))
print('SSUB1 style IDs:', get_style_ids(r'C:\Users\angam\Downloads\Leano Website V1\Services\Services Sub Page 1\website\Services Sub Page 1.html'))
print('NMAIN style IDs:', get_style_ids(r'C:\Users\angam\Downloads\Leano Website V1\News\News Main Page\website\News Main Page.html'))
