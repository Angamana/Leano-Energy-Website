import os
import re

about_us_path = r"C:\Users\angam\Downloads\Leano Website V1\About Us\website\About Us.html"

with open(about_us_path, "r", encoding="utf-8") as f:
    text = f.read()

# Fix Tab Content text and add CSS for the 50/50 split
# We will match the tab panes
tab_contents = {
    "Tab 1": "Leano Energy aims to enter the green energy market by promoting renewable energy together with high quality and affordable services. We aim to empower the youth and create opportunities in South Africa.",
    "Tab 2": "We are licensed wholesalers and distributors of bulk fuels, diesel, paraffin, oils, and various lubricants. We also provide on-site storage solutions and Biofuel options.",
    "Tab 3": "Stop Fuel Theft. Reduce Costs. Gain Control. Our fuel management solution provides clear, quantifiable benefits: Live Monitoring, Theft Prevention, Cost Reduction, and Reporting with 99% accuracy.",
    "Tab 4": "We are a 100% black youth-owned Level 1 BBBEE contributor with direct relationships with major refineries (Sasol, Shell, BP, Engen, Chevron) ensuring reliable supply at competitive prices.",
    "Tab 5": "Giving back to the youth and empowering the African child is one of Leano's deepest desires. We are developing an education fund to aid students in chemical engineering, mining, and construction."
}

for tab_id, content in tab_contents.items():
    # Find the <p> tag inside the tab pane
    pattern = r'(<div data-w-tab="' + tab_id + r'".*?class="tab-image-wrap.*?<p>).*?(</p>)'
    text = re.sub(pattern, r'\g<1>' + content + r'\g<2>', text, flags=re.DOTALL)
    
    # Let's add styling to make the text box fill the left half
    # 1. Expand the container so it doesn't limit width
    # 2. Make icon-style-four 50% width, 100% height, solid background
    # Actually, we can just replace 'class="icon-style-four"' with 'class="icon-style-four" style="width: 50%; max-width: 50%; height: 100%; min-height: 600px; background-color: #ffffff; padding: 40px; margin: 0; display: flex; flex-direction: column; justify-content: center;"'
    
    # We will just inject this style directly into the icon-style-four of this tab.
    # To do this safely, we will find icon-style-four inside this tab.
    # We'll use a function to process each tab individually.
    pass

def process_tab(match):
    tab_html = match.group(0)
    # Inject styles into icon-style-four
    # It currently has style="opacity:0" class="icon-style-four"
    # We append our styles to it.
    tab_html = re.sub(
        r'(class="icon-style-four")',
        r'\1 style="width: 50%; max-width: 50%; height: 100%; min-height: 500px; background-color: #ffffff; padding: 50px; margin: 0; display: flex; flex-direction: column; justify-content: center;"',
        tab_html
    )
    # Also, the container class `w-layout-blockcontainer container tab-container w-container` might limit width to 1200px and center it.
    # We want it to be 100% width and left aligned so the box touches the left edge.
    tab_html = re.sub(
        r'(class="w-layout-blockcontainer container tab-container w-container")',
        r'\1 style="max-width: 100%; padding: 0; margin: 0;"',
        tab_html
    )
    return tab_html

text = re.sub(r'<div data-w-tab="Tab \d".*?</div>\s*</div>\s*</div>\s*</div>', process_tab, text, flags=re.DOTALL)

with open(about_us_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Split layout complete!")
