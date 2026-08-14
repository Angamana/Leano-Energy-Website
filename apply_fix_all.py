import os
import glob
import re

workspace_root = r'C:\Users\angam\Downloads\Leano Website V1'

pe_fix_css = """<style id="fuel-widget-pointer-events-fix">
/* Allow clicks to pass through the empty space of the fixed widget container */
.fuel-side-tabs {
    pointer-events: none !important;
}
/* Re-enable clicks on the actual visible button and panel */
.fuel-main-tab-btn, .fuel-panel-container {
    pointer-events: auto !important;
}
</style>"""

all_files = glob.glob(os.path.join(workspace_root, '**', '*.html'), recursive=True)

count = 0
for fpath in all_files:
    if 'Cookie System' in fpath or 'Donor' in fpath or 'Archived' in fpath:
        continue
    
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # 1. Add fuel-widget-pointer-events-fix if missing
    if 'fuel-widget-pointer-events-fix' not in content:
        if '<style id="universal-side-widget-toggle-css">' in content:
            content = content.replace('<style id="universal-side-widget-toggle-css">', pe_fix_css + '\n<style id="universal-side-widget-toggle-css">')
            modified = True
        elif '</head>' in content:
            content = content.replace('</head>', pe_fix_css + '\n</head>')
            modified = True
    
    # 2. Compute correct relative path to Order/website/Order.html
    rel_dir = os.path.relpath(os.path.dirname(fpath), workspace_root)
    # count levels
    if rel_dir == '.':
        order_rel_path = 'Order/website/Order.html'
    else:
        depth = len(rel_dir.replace('\\', '/').split('/'))
        order_rel_path = '../' * depth + 'Order/website/Order.html'
    
    # Update href in order-side-tab-container
    def replace_order_href(match):
        return f'class="order-side-tab-container" href="{order_rel_path}"'
    
    new_content = re.sub(r'class=["\']order-side-tab-container["\']\s+href=["\'][^"\']*["\']', replace_order_href, content)
    if new_content != content:
        content = new_content
        modified = True
    
    if modified:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f"Updated {fpath} -> Order link: {order_rel_path}")

print(f"\nDone! Updated {count} files.")
