import os
import re

about_us_path = r"C:\Users\angam\Downloads\Leano Website V1\About Us\website\About Us.html"
donor_path = r"C:\Users\angam\Downloads\Leano Website V1\About Us\Donor\induyst.webflow.io\induyst.webflow.io\about-us.html"

with open(about_us_path, "r", encoding="utf-8") as f:
    about_content = f.read()

with open(donor_path, "r", encoding="utf-8") as f:
    donor_content = f.read()

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
    
    # Let's inject by finding the end of the first tab-image-section.
    # We can split by `<section class="testimonial-section section-margin bg-white">`
    # and insert our new section right before it.
    
    split_str = '<section class="testimonial-section section-margin bg-white">'
    parts = about_content.split(split_str)
    if len(parts) >= 2:
        about_content = parts[0] + working_process_html + "\n\n" + split_str + parts[1]
        
    with open(about_us_path, "w", encoding="utf-8") as f:
        f.write(about_content)
        
    print("Injection complete!")
else:
    print("Could not find Working Process in donor HTML")
