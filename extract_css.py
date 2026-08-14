import re

def get_widget_css(filepath):
    with open(filepath, encoding='utf-8') as f:
        content = f.read()
    
    rules = []
    # find all style blocks
    styles = re.findall(r'<style.*?>.*?</style>', content, re.DOTALL)
    for s in styles:
        if any(k in s for k in ['order-side-tab', 'mobile-widget-toggle', 'fuel-side-tabs', 'order-fuel-side-btn']):
            rules.append(s)
    return "\n\n".join(rules)

index_css = get_widget_css(r'C:\Users\angam\Downloads\Leano Website V1\index.html')
sub1_css = get_widget_css(r'C:\Users\angam\Downloads\Leano Website V1\Services\Services Sub Page 1\website\Services Sub Page 1.html')

print("--- CSS IN INDEX BUT NOT IN SERVICES SUB PAGE 1 ---")
with open('index_widget_css.txt', 'w', encoding='utf-8') as f:
    f.write(index_css)

with open('sub1_widget_css.txt', 'w', encoding='utf-8') as f:
    f.write(sub1_css)

print("Saved css files to index_widget_css.txt and sub1_widget_css.txt")
