import os
import re

html_path = r"C:\Users\angam\Downloads\Leano Website V1\About Us\website\About Us.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Introduction / Mission Statement
# Subtitle
content = content.replace(">Why Choose us<", ">About Leano Energy<")

# Main Headline
content = content.replace(
    ">We work for you\xa0since 1989.\xa0 Industrial around the world<",
    ">Powering South Africa Since 2016<"
)
content = content.replace(
    ">We work for you since 1989.  Industrial around the world<",
    ">Powering South Africa Since 2016<"
)
# And the other instance where it might have a zero-width space or just spaces
content = re.sub(
    r'>We work for you[\s\xa0]*since 1989.[\s\xa0]*Industrial around the world<',
    '>Powering South Africa Since 2016<',
    content
)

# Intro Paragraph
content = re.sub(
    r'>We provide precision-driven solutions across robotics setup, renewable energy, oil and gas, and CNC machining, delivering reliable performance and lasting impact for every industrial project. Our expertise is built to meet\s*complex requirements<',
    '>Leano Energy (Pty) Ltd was established with a singular mission: to provide reliable, high-quality, and cost-effective fuel distribution solutions across South Africa. As a Level 1 BBBEE Contributor and a 100% Black Youth-Owned company, we pride ourselves on delivering excellence, agility, and innovation to our clients.<',
    content
)

# 2. Update Core Values
# There is a grid of 4 items with class="icon-style-one-title text-style-h4"
# We need to replace the 4 titles, and since there is no description, we will append a description underneath the title.
# Wait, let's see how we can inject the description.
# <div class="icon-style-one-title text-style-h4">We are certified company</div>
# We can change it to:
# <div class="icon-style-one-title text-style-h4" style="margin-bottom: 10px;">Safety & Compliance</div><div class="accordian-style-one-desc">Adhering to the highest industry standards, ensuring safe transportation and storage.</div>

core_values = [
    ("Safety & Compliance", "Adhering to the highest industry standards, ensuring safe transportation and storage."),
    ("Customer Centricity", "Your operations are our priority. We deliver on time, every time."),
    ("Sustainability", "Committed to eco-friendly practices and providing sustainable energy solutions."),
    ("Integrity", "Transparent pricing and operations you can trust.")
]

old_titles = [
    "We are certified company",
    "We are bring quality services",
    "Engineering project study &amp; solution",
    "Raw Materials Transportation"
]

for i, (old, (new_title, new_desc)) in enumerate(zip(old_titles, core_values)):
    content = content.replace(
        f'>{old}<',
        f' style="margin-bottom: 10px;">{new_title}</div><div class="accordian-style-one-desc" style="color:#aaa; font-size:14px;">{new_desc}<'
    )
    # The above assumes it looks like: <div ...>We are certified company</div>
    # My replacement makes it: <div ... style="margin-bottom: 10px;">Safety & Compliance</div><div class="...">Adhering...</div>
    # To be safer with exact string replacement:
    content = content.replace(
        f'<div class="icon-style-one-title text-style-h4">{old}</div>',
        f'<div class="icon-style-one-title text-style-h4" style="margin-bottom: 10px;">{new_title}</div><div class="accordian-style-one-desc" style="color:var(--text-color); font-size:15px;">{new_desc}</div>'
    )

# 3. Restructure & Update Company Overview / History
# Replace "Working Process" with "Company Overview"
# Replace "quality industy is the better future" with "Redefining Bulk Fuel Supply"
# Replace the desc "Whether it’s robot setup..." with the company overview text.
# Remove the <div class="tab-image w-tabs" ...> block

content = content.replace(">Working Process<", ">Company Overview / History<")
content = re.sub(
    r'>quality industy is the better future<',
    '>Redefining Bulk Fuel Supply<',
    content,
    flags=re.IGNORECASE
)

content = re.sub(
    r'>Whether it’s robot setup, renewable energy, oil &amp; gas, or CNC machining, our work reflects precision, and lasting impact across every project.<',
    '>Starting with a vision to redefine bulk fuel supply, we have grown into a trusted partner for industries ranging from mining to agriculture and logistics. We are an authorized distributor for major refineries including Sasol, Shell, BP, Engen, and Chevron, guaranteeing the highest quality product with every drop.<',
    content
)

# Now, we need to completely remove the w-tabs element
tab_start = content.find('<div class="tab-image w-tabs"')
if tab_start != -1:
    tab_end = content.find('</section>', tab_start)
    if tab_end != -1:
        # We delete up to the closing section tag, but leave the closing section tag so the layout doesn't break
        content = content[:tab_start] + "</div>" + content[tab_end:]

# 4. Remove Irrelevant Sections
# 4a. Remove "Efficient Work Process" list
# <div class="about-inner">
# <div class="icon-style-three-heading">Efficient Work Process</div>
# ... </div>
# Wait, it is inside <div class="about-inner">
inner_start = content.find('<div class="about-inner">')
if inner_start != -1:
    # it ends at the matching </div> for about-inner. Let's find "</div>\n</div>\n</div>\n</div>\n<div class=\"w-layout-grid icon-style-one-grid about-page\">"
    grid_start = content.find('<div class="w-layout-grid icon-style-one-grid about-page">')
    if grid_start != -1:
        # We can just remove <div class="about-inner"> up to that grid
        # Actually about-inner has nested divs. 
        # But we know it's directly followed by the grid section closure and grid start.
        # It's safer to just regex out <div class="about-inner">.*?<div class="w-layout-grid' with DOTALL
        content = re.sub(r'<div class="about-inner">.*?</div>\s*</div>\s*</div>\s*</div>\s*<div class="w-layout-grid', '</div>\n</div>\n</div>\n<div class="w-layout-grid', content, flags=re.DOTALL)


# 4b. Remove "Our Team" slider section completely
team_sec_start = content.find('<section class="section-gap">')
# Actually, the team section has a unique class? No, "section-gap". Let's search for "The best of our capacity"
team_idx = content.find("The best of our capacity")
if team_idx != -1:
    team_start = content.rfind('<section', 0, team_idx)
    team_end = content.find('</section>', team_idx)
    if team_start != -1 and team_end != -1:
        team_end += len('</section>')
        content = content[:team_start] + content[team_end:]

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("About Us page successfully migrated!")
