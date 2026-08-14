import re

def get_style_by_id(filepath, style_id):
    with open(filepath, encoding='utf-8') as f:
        content = f.read()
    match = re.search(fr'<style\s+id=["\']{style_id}["\'].*?>.*?</style>', content, re.DOTALL)
    return match.group(0) if match else None

index_path = r'C:\Users\angam\Downloads\Leano Website V1\index.html'

for sid in ['fuel-widget-pointer-events-fix', 'fuel-widget-zindex-fix', 'universal-side-widget-toggle-css', 'order-fuel-widget-css', 'fuel-prices-widget-styles']:
    print(f"=== Style ID: {sid} in index.html ===")
    print(get_style_by_id(index_path, sid))
    print("\n")
