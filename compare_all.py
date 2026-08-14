import re
import glob

def get_blocks(filepath):
    with open(filepath, encoding='utf-8') as f:
        content = f.read()
    
    css = re.findall(r'<style id="universal-side-widget-toggle-css">.*?</style>', content, re.DOTALL)
    widget_html = re.findall(r'<div id="order-fuel-side-widget">.*?</style>', content, re.DOTALL)
    js = re.findall(r'<script id="mobile-widget-toggle-script">.*?</script>', content, re.DOTALL)
    fuel_panel = re.findall(r'<div class="fuel-side-tabs" id="fuel-side-panel">.*?(?=<script id="fuel-api-script">|</script>\s*</body>)', content, re.DOTALL)

    return {
        'css': css[0] if css else '',
        'widget_html': widget_html[0] if widget_html else '',
        'js': js[0] if js else '',
        'fuel_panel': fuel_panel[0] if fuel_panel else '',
        'full_content': content
    }

index_data = get_blocks(r'C:\Users\angam\Downloads\Leano Website V1\index.html')
smain_data = get_blocks(r'C:\Users\angam\Downloads\Leano Website V1\Services\Services Main Page\website\Services Main Page.html')

all_html_files = glob.glob(r'C:\Users\angam\Downloads\Leano Website V1\**\*.html', recursive=True)

print("Comparing index.html & Services Main Page.html with all other HTML files...")

for fpath in all_html_files:
    if 'index.html' in fpath and fpath.endswith('index.html') and 'Cookie System' not in fpath:
        continue
    if 'Services Main Page.html' in fpath:
        continue
    
    data = get_blocks(fpath)
    print(f"\n=== File: {fpath} ===")
    print("  CSS present:", bool(data['css']))
    print("  Widget HTML present:", bool(data['widget_html']))
    print("  JS present:", bool(data['js']))
    print("  Fuel Panel present:", bool(data['fuel_panel']))
    
    if data['js'] != index_data['js']:
        print("  [!] JS differs from index.html!")
    
    if data['css'] != index_data['css']:
        print("  [!] universal-side-widget-toggle-css differs from index.html!")
