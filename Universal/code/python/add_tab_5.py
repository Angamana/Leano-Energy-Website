import os
import re

services_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html"

with open(services_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Replace "Why Choose us" with "Products Detail Section"
text = re.sub(
    r'<div class="subtitle-head white-text">Why Choose us</div>',
    r'<div class="subtitle-head white-text">Products Detail Section</div>',
    text,
    flags=re.IGNORECASE
)

# 2. Duplicate the Tab 4 link in the menu
# We need to find the full <a data-w-tab="Tab 4" ...>...</a> block.
m_link = re.search(r'(<a data-w-tab="Tab 4"[^>]*>.*?</a>)', text, flags=re.DOTALL)
if m_link:
    tab4_link = m_link.group(1)
    
    # Create tab5_link by modifying tab4_link
    tab5_link = tab4_link.replace('Tab 4', 'Tab 5')
    tab5_link = tab5_link.replace('>04<', '>05<')
    tab5_link = tab5_link.replace('w--current', '') # Remove active state so both aren't open by default
    
    # Insert tab5_link after tab4_link
    text = text.replace(tab4_link, tab4_link + '\n' + tab5_link)

# 3. Duplicate the Tab 4 pane
m_pane = re.search(r'(<div data-w-tab="Tab 4"[^>]*>.*?</div>)', text, flags=re.DOTALL)
if m_pane:
    tab4_pane = m_pane.group(1)
    
    # Create tab5_pane
    tab5_pane = tab4_pane.replace('Tab 4', 'Tab 5')
    tab5_pane = tab5_pane.replace('w--tab-active', '')
    
    # Insert tab5_pane after tab4_pane
    text = text.replace(tab4_pane, tab4_pane + '\n' + tab5_pane)

with open(services_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Added Tab 5 successfully!")
