import os
import re

services_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html"
donor_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\induyst.webflow.io\induyst.webflow.io\services.html"

# Load the current services file
with open(services_path, "r", encoding="utf-8") as f:
    text = f.read()

# Load the original donor file
with open(donor_path, "r", encoding="utf-8") as f:
    donor_text = f.read()

# Products data with SPAN instead of A tags!
products = [
    {
        "title": "Petrol Unleaded (93, 95ULP)",
        "desc": "High-quality unleaded petrol for automotive and industrial applications. Available in 93 and 95 octane ratings.<br><br><strong>Supplied By:</strong> Sasol, Shell, BP, Engen, Chevron<br><br><span onclick=\\\"window.location.href='../../Contact Us/website/Contact Us.html'\\\" style='color: var(--theme-color); text-decoration: underline; font-weight: bold; cursor: pointer;'>Request a Quote</span>"
    },
    {
        "title": "Diesel (50, 500PPM)",
        "desc": "Premium diesel fuel for commercial and industrial use. Available in 50PPM and 500PPM sulfur content.<br><br><strong>Application:</strong> Mining, agriculture, logistics, factories<br><br><span onclick=\\\"window.location.href='../../Contact Us/website/Contact Us.html'\\\" style='color: var(--theme-color); text-decoration: underline; font-weight: bold; cursor: pointer;'>Request a Quote</span>"
    },
    {
        "title": "Illuminating Paraffin",
        "desc": "Quality paraffin for heating, lighting, and industrial applications.<br><br><span onclick=\\\"window.location.href='../../Contact Us/website/Contact Us.html'\\\" style='color: var(--theme-color); text-decoration: underline; font-weight: bold; cursor: pointer;'>Request a Quote</span>"
    },
    {
        "title": "Oils &amp; Lubricants",
        "desc": "Complete range of engine oils, gear oils, hydraulic oils, compressor oils, and industrial lubricants.<br><br><strong>Brands:</strong> Premium Partner Brands<br><br><span onclick=\\\"window.location.href='../../Contact Us/website/Contact Us.html'\\\" style='color: var(--theme-color); text-decoration: underline; font-weight: bold; cursor: pointer;'>Request a Quote</span>"
    },
    {
        "title": "Biofuel",
        "desc": "Blended biofuel, cleaner, safer, and more sustainable. Less harmful to the environment and better for engine performance.<br><br><span onclick=\\\"window.location.href='../../Contact Us/website/Contact Us.html'\\\" style='color: var(--theme-color); text-decoration: underline; font-weight: bold; cursor: pointer;'>Learn About Biofuel</span>"
    }
]

# 1. Extract the original section from donor
donor_match = re.search(r'(<div class="subtitle-head white-text">Why Choose us</div>.*?</section>)', donor_text, flags=re.DOTALL)
if donor_match:
    original_section = donor_match.group(1)
    
    # 2. Modify titles and descriptions in the original section
    # Extract the 4 original tabs
    tabs = re.findall(r'(<a data-w-tab="Tab [1-4]" class="staticbox-one.*?</a>)', original_section, flags=re.DOTALL)
    
    new_tabs = []
    for i in range(4):
        tab = tabs[i]
        prod = products[i]
        tab = re.sub(r'<div class="staticbox-title text-style-h3">.*?</div>', f'<div class="staticbox-title text-style-h3">{prod["title"]}</div>', tab)
        tab = re.sub(r'<div class="text-style-h2 white-text">.*?</div>', f'<div class="text-style-h2 white-text">{prod["title"]}</div>', tab)
        tab = re.sub(r'<div class="staticbox-text">.*?</div>', f'<div class="staticbox-text">{prod["desc"]}</div>', tab)
        new_tabs.append(tab)
    
    # 3. Create Tab 5 from the new Tab 4
    tab5 = new_tabs[3]
    tab5 = tab5.replace('Tab 4', 'Tab 5')
    tab5 = tab5.replace('>04<', '>05<')
    tab5 = tab5.replace('w--current', '') # ensure not active
    
    prod5 = products[4]
    tab5 = re.sub(r'<div class="staticbox-title text-style-h3">.*?</div>', f'<div class="staticbox-title text-style-h3">{prod5["title"]}</div>', tab5)
    tab5 = re.sub(r'<div class="text-style-h2 white-text">.*?</div>', f'<div class="text-style-h2 white-text">{prod5["title"]}</div>', tab5)
    tab5 = re.sub(r'<div class="staticbox-text">.*?</div>', f'<div class="staticbox-text">{prod5["desc"]}</div>', tab5)
    
    new_tabs.append(tab5)
    
    # Rebuild the section html
    new_section_html = original_section
    for i in range(4):
        new_section_html = new_section_html.replace(tabs[i], new_tabs[i])
        
    # Inject Tab 5 after Tab 4
    new_section_html = new_section_html.replace(new_tabs[3], new_tabs[3] + '\n' + tab5)
    
    # Also inject the w-tab-pane for Tab 5
    pane4 = '<div data-w-tab="Tab 4" class="w-tab-pane w--tab-active"></div>'
    pane4_inactive = '<div data-w-tab="Tab 4" class="w-tab-pane"></div>'
    
    # donor section might have pane4 with or without w--tab-active
    if pane4 in new_section_html:
        new_section_html = new_section_html.replace(pane4, pane4 + '\n<div data-w-tab="Tab 5" class="w-tab-pane"></div>')
    elif pane4_inactive in new_section_html:
        new_section_html = new_section_html.replace(pane4_inactive, pane4_inactive + '\n<div data-w-tab="Tab 5" class="w-tab-pane"></div>')
        
    # Update section headers
    new_section_html = new_section_html.replace('Why Choose us', 'Products Detail Section')
    new_section_html = re.sub(
        r'<h2 class="heading-title service-heading white-text">.*?</h2>',
        r'<h2 class="heading-title service-heading white-text">Premium Petroleum Products For Your Every Need</h2>',
        new_section_html,
        flags=re.IGNORECASE
    )
    
    # 4. Replace the old broken section in current Services.html with the new_section_html
    # We find the current section. It might have Products Detail Section
    curr_match = re.search(r'(<div class="subtitle-head white-text">Products Detail Section</div>.*?</section>)', text, flags=re.DOTALL)
    if not curr_match:
        # Fallback if it was named something else
        curr_match = re.search(r'(<div class="subtitle-head white-text">Why Choose us</div>.*?</section>)', text, flags=re.DOTALL)
        
    if curr_match:
        text = text.replace(curr_match.group(1), new_section_html)
        
        # Also remove the CSS hack we added earlier to bypass the crash, as the crash is now fixed!
        if '/* Override for Webflow IX2 crash caused by adding a 5th tab */' in text:
            text = re.sub(r'<style>\s*/\* Override for Webflow IX2 crash.*?</style>', '', text, flags=re.DOTALL)
            
        with open(services_path, "w", encoding="utf-8") as f:
            f.write(text)
        print("Successfully rebuilt the tabs with span elements!")
    else:
        print("Could not find current section to replace.")
else:
    print("Could not find original section in donor file.")
