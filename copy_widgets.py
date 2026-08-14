import re
import glob

# 1. Read Services Main Page.html
services_path = r'C:\Users\angam\Downloads\Leano Website V1\Services\Services Main Page\website\Services Main Page.html'
with open(services_path, 'r', encoding='utf-8') as f:
    services_content = f.read()

# Define regex patterns for the 4 blocks
# 1. toggle CSS
toggle_css_pattern = re.compile(r'<style id="universal-side-widget-toggle-css">.*?</style>', re.DOTALL)
# 2. order widget (includes its CSS)
order_widget_pattern = re.compile(r'<div id="order-fuel-side-widget">.*?</style>', re.DOTALL)
# 3. toggle script
toggle_script_pattern = re.compile(r'<script id="mobile-widget-toggle-script">.*?</script>', re.DOTALL)
# 4. fuel panel
fuel_panel_pattern = re.compile(r'<div class="fuel-side-tabs" id="fuel-side-panel">.*?(?=<script id="fuel-api-script">|</script>\s*</body>)', re.DOTALL)

toggle_css_match = toggle_css_pattern.search(services_content)
order_widget_match = order_widget_pattern.search(services_content)
toggle_script_match = toggle_script_pattern.search(services_content)
fuel_panel_match = fuel_panel_pattern.search(services_content)

if not all([toggle_css_match, order_widget_match, toggle_script_match, fuel_panel_match]):
    print("Error: Could not find all blocks in Services Main Page.html")
    exit(1)

toggle_css_str = toggle_css_match.group(0)
order_widget_str = order_widget_match.group(0)
toggle_script_str = toggle_script_match.group(0)
fuel_panel_str = fuel_panel_match.group(0)

# The user explicitly said: "update the links"
# We know News pages (both main and sub) are 4 levels deep (e.g. News/News Main Page/website/News Main Page.html)
# So the path to Order should be ../../../Order/website/Order.html
order_widget_str = re.sub(r'href="[^"]*Order/website/Order.html"', 'href="../../../Order/website/Order.html"', order_widget_str)


# 2. Process all News pages
news_files = glob.glob(r'C:\Users\angam\Downloads\Leano Website V1\News\**\website\*.html', recursive=True)
count = 0

for filepath in news_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the blocks
    content = toggle_css_pattern.sub(toggle_css_str, content)
    content = order_widget_pattern.sub(order_widget_str, content)
    content = toggle_script_pattern.sub(toggle_script_str, content)
    
    # For fuel panel, we also need to be careful with the positive lookahead
    # It's better to just replace the old block entirely
    content = fuel_panel_pattern.sub(fuel_panel_str, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    count += 1
    print(f"Updated {filepath}")

print(f"Successfully updated {count} files.")
