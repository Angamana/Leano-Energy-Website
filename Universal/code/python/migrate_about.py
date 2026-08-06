import os
import re

about_us_path = r"C:\Users\angam\Downloads\Leano Website V1\About Us\website\About Us.html"
donor_path = r"C:\Users\angam\Downloads\Leano Website V1\About Us\Donor\induyst.webflow.io\induyst.webflow.io\about-us.html"

with open(about_us_path, "r", encoding="utf-8") as f:
    about_content = f.read()

with open(donor_path, "r", encoding="utf-8") as f:
    donor_content = f.read()

# --- 1. Hero Section ---
# Replace Headline
about_content = about_content.replace(
    '<h2 class="heading-title white-text">Powering South Africa Since 2016</h2>',
    '<h2 class="heading-title white-text" style="font-size: 3rem; line-height: 1.2;">Youth-Owned. Level 1 BBBEE. Driven by Innovation.</h2>'
)
# Replace Description
old_desc = 'Leano Energy (Pty) Ltd was established with a singular mission: to provide reliable, high-quality, and cost-effective fuel distribution solutions across South Africa. As a Level 1 BBBEE Contributor and a 100% Black Youth-Owned company, we pride ourselves on delivering excellence, agility, and innovation to our clients.'
new_desc = "Leano Energy was founded with a clear mission: empower South African youth through innovation and deliver reliable, sustainable energy solutions to industries across the nation. As a 100% black youth-owned Level 1 BBBEE contributor, we bring fresh thinking to the fuel industry. We believe that a country's future is in the hands of its youth, and we're committed to opening doors, creating opportunities, and driving economic growth. We're licensed wholesalers and distributors of bulk fuels, diesel, paraffin, oils, and various lubricants. We serve clients across Gauteng, Mpumalanga, Limpopo, and the North West, providing energy solutions to mining, agriculture, logistics, airports, factories, and municipalities."
about_content = about_content.replace(old_desc, new_desc)


# --- 2. Mission/Vision (Company Overview) ---
about_content = about_content.replace(
    '<div class="subtitle-head">Company Overview / History</div>',
    '<div class="subtitle-head">Our Purpose</div>'
)
about_content = about_content.replace(
    '<h2 class="heading-title">Redefining Bulk Fuel Supply</h2>',
    '<h2 class="heading-title">Sustainable Values. Empowerment. Excellence.</h2>'
)
old_ov_desc = 'Starting with a vision to redefine bulk fuel supply, we have grown into a trusted partner for industries ranging from mining to agriculture and logistics. We are an authorized distributor for major refineries including Sasol, Shell, BP, Engen, and Chevron, guaranteeing the highest quality product with every drop.'
new_ov_desc = '<strong>Vision:</strong> Developed on sustainable values and creating empowerment opportunities in South Africa, whilst striving to promote sustainable energy.<br><br><strong>Mission:</strong> Leano Energy aims to enter the green energy market by promoting renewable energy together with high quality and affordable services.'
about_content = about_content.replace(old_ov_desc, new_ov_desc)


# --- 3. Extract & Inject "Working Process" ---
# Extract Working Process from donor
match = re.search(r'(<section class="tab-image-section section-margin">.*?<div class="subtitle-head">Working Process</div>.*?</section>)', donor_content, re.DOTALL)
if match:
    working_process_html = match.group(1)
    
    # Update Tab Menu Names
    working_process_html = working_process_html.replace('<div>Consultation</div>', '<div>Objectives</div>')
    working_process_html = working_process_html.replace('<div>Design</div>', '<div>Products & Services</div>')
    working_process_html = working_process_html.replace('<div>Fabrication</div>', '<div>Fuel Management</div>')
    working_process_html = working_process_html.replace('<div>Delivery</div>', '<div>Comparative Advantages</div>')
    working_process_html = working_process_html.replace('<div>Setup</div>', '<div>Supportive Culture</div>')
    
    # Update Tab 1 Content (Objectives)
    working_process_html = re.sub(
        r'(<div data-w-tab="Tab 1" class="tab-image-wrap _01 w-tab-pane w--tab-active">.*?<p>).*?(</p>)',
        r'\g<1>Leano Energy aims to enter the green energy market by promoting renewable energy together with high quality and affordable services. We aim to empower the youth and create opportunities in South Africa.\g<2>',
        working_process_html, flags=re.DOTALL
    )
    
    # Update Tab 2 Content (Products & Services)
    working_process_html = re.sub(
        r'(<div data-w-tab="Tab 2" class="tab-image-wrap _02 w-tab-pane">.*?<p>).*?(</p>)',
        r'\g<1>We are licensed wholesalers and distributors of bulk fuels, diesel, paraffin, oils, and various lubricants. We also provide on-site storage solutions and Biofuel options.\g<2>',
        working_process_html, flags=re.DOTALL
    )
    
    # Update Tab 3 Content (Fuel Management)
    working_process_html = re.sub(
        r'(<div data-w-tab="Tab 3" class="tab-image-wrap _03 w-tab-pane">.*?<p>).*?(</p>)',
        r'\g<1>Stop Fuel Theft. Reduce Costs. Gain Control. Our fuel management solution provides clear, quantifiable benefits: Live Monitoring, Theft Prevention, Cost Reduction, and Reporting with 99% accuracy.\g<2>',
        working_process_html, flags=re.DOTALL
    )
    
    # Update Tab 4 Content (Comparative Advantages)
    working_process_html = re.sub(
        r'(<div data-w-tab="Tab 4" class="tab-image-wrap _04 w-tab-pane">.*?<p>).*?(</p>)',
        r'\g<1>We are a 100% black youth-owned Level 1 BBBEE contributor with direct relationships with major refineries (Sasol, Shell, BP, Engen, Chevron) ensuring reliable supply at competitive prices.\g<2>',
        working_process_html, flags=re.DOTALL
    )
    
    # Update Tab 5 Content (Supportive Culture)
    working_process_html = re.sub(
        r'(<div data-w-tab="Tab 5" class="tab-image-wrap _05 w-tab-pane">.*?<p>).*?(</p>)',
        r'\g<1>Giving back to the youth and empowering the African child is one of Leano\'s deepest desires. We are developing an education fund to aid students in chemical engineering, mining, and construction.\g<2>',
        working_process_html, flags=re.DOTALL
    )
    
    # Inject it directly after the Mission/Vision section
    # The Mission/Vision section ends with </div></div></div></div></div></section>
    insert_point = '</div></div></div></div></div></section>'
    parts = about_content.split(insert_point)
    if len(parts) >= 2:
        # Reconstruct with the Working Process section injected
        about_content = parts[0] + insert_point + "\n\n" + working_process_html + parts[1]
    
with open(about_us_path, "w", encoding="utf-8") as f:
    f.write(about_content)

print("Migration completed!")
