import os
import re

about_us_path = r"C:\Users\angam\Downloads\Leano Website V1\About Us\website\About Us.html"

with open(about_us_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update Hero
text = text.replace('<div class="subtitle-head white-text">About induyst</div>', '<div class="subtitle-head white-text">About Leano Energy</div>')
text = re.sub(
    r'<h2 class="heading-title white-text">.*?</h2>',
    '<h2 class="heading-title white-text" style="font-size: 3rem; line-height: 1.2;">Youth-Owned. Level 1 BBBEE. Driven by Innovation.</h2>',
    text
)
# The description in donor might be different. Let's find white-desc-text
text = re.sub(
    r'(<div class="heading-subheading-desc white-desc-text">).*?(</div>)',
    r'\g<1>Leano Energy was founded with a clear mission: empower South African youth through innovation and deliver reliable, sustainable energy solutions to industries across the nation. As a 100% black youth-owned Level 1 BBBEE contributor, we bring fresh thinking to the fuel industry. We believe that a country\'s future is in the hands of its youth, and we\'re committed to opening doors, creating opportunities, and driving economic growth. We\'re licensed wholesalers and distributors of bulk fuels, diesel, paraffin, oils, and various lubricants. We serve clients across Gauteng, Mpumalanga, Limpopo, and the North West, providing energy solutions to mining, agriculture, logistics, airports, factories, and municipalities.\g<2>',
    text, flags=re.DOTALL
)

# 2. Update Tabs Section (Working Process -> About Us)
# Find the tab-image-section
# Update subtitle
text = text.replace('<div class="subtitle-head">Working Process</div>', '<div class="subtitle-head">About Us</div>')
# Update Title
text = re.sub(
    r'(<div class="subtitle-head">About Us</div>\s*</div>\s*<div class="heading-title-animation">\s*<h2 class="heading-title">).*?(</h2>)',
    r'\g<1>Sustainable Values. Empowerment. Excellence.\g<2>',
    text, flags=re.DOTALL
)
# Clear right side text
text = re.sub(
    r'(<div class="tab-image-right">\s*<div class="heading-subheading-desc-wrap tab-heading-desc">\s*<div class="heading-subheading-desc">).*?(</div>)',
    r'\g<1>\g<2>',
    text, flags=re.DOTALL
)

# Flex wrap tabs
text = text.replace('<div class="tabs-image-menu w-tab-menu">', '<div class="tabs-image-menu w-tab-menu" style="flex-wrap: wrap;">')
text = re.sub(r'(<a data-w-tab="Tab \d" class="tab-image-link w-inline-block w-tab-link)', r'\1" style="width: 33.33%; min-width: 250px;', text)

# Tab Names
text = text.replace('<div class="tab-text">Robot Installation</div>', '<div class="tab-text">Objectives</div>')
text = text.replace('<div class="tab-text">Renewable energy</div>', '<div class="tab-text">Products & Services</div>')
text = text.replace('<div class="tab-text">Gas &amp; oil industry</div>', '<div class="tab-text">Fuel Management</div>')
text = text.replace('<div class="tab-text">CNC Turning</div>', '<div class="tab-text">Comparative Advantages</div>')
text = text.replace('<div class="tab-text">Automation</div>', '<div class="tab-text">Supportive Culture</div>')

# Tab Content
text = re.sub(
    r'(<div data-w-tab="Tab 1" class="tab-image-wrap _01 w-tab-pane w--tab-active">.*?<p>).*?(</p>)',
    r'\g<1>Leano Energy aims to enter the green energy market by promoting renewable energy together with high quality and affordable services. We aim to empower the youth and create opportunities in South Africa.\g<2>',
    text, flags=re.DOTALL
)
text = re.sub(
    r'(<div data-w-tab="Tab 2" class="tab-image-wrap _02 w-tab-pane">.*?<p>).*?(</p>)',
    r'\g<1>We are licensed wholesalers and distributors of bulk fuels, diesel, paraffin, oils, and various lubricants. We also provide on-site storage solutions and Biofuel options.\g<2>',
    text, flags=re.DOTALL
)
text = re.sub(
    r'(<div data-w-tab="Tab 3" class="tab-image-wrap _03 w-tab-pane">.*?<p>).*?(</p>)',
    r'\g<1>Stop Fuel Theft. Reduce Costs. Gain Control. Our fuel management solution provides clear, quantifiable benefits: Live Monitoring, Theft Prevention, Cost Reduction, and Reporting with 99% accuracy.\g<2>',
    text, flags=re.DOTALL
)
text = re.sub(
    r'(<div data-w-tab="Tab 4" class="tab-image-wrap _04 w-tab-pane">.*?<p>).*?(</p>)',
    r'\g<1>We are a 100% black youth-owned Level 1 BBBEE contributor with direct relationships with major refineries (Sasol, Shell, BP, Engen, Chevron) ensuring reliable supply at competitive prices.\g<2>',
    text, flags=re.DOTALL
)
text = re.sub(
    r'(<div data-w-tab="Tab 5" class="tab-image-wrap _05 w-tab-pane">.*?<p>).*?(</p>)',
    r'\g<1>Giving back to the youth and empowering the African child is one of Leano\'s deepest desires. We are developing an education fund to aid students in chemical engineering, mining, and construction.\g<2>',
    text, flags=re.DOTALL
)

# 3. Update Testimonials Section
text = text.replace('<div class="subtitle-head">our Testimonials</div>', '<div class="subtitle-head">Our Future</div>')
text = text.replace('<h2 class="heading-title">What Our Clients Say?</h2>', '<h2 class="heading-title">Mission, Vision and values</h2>')

# Remove Quotes, Author Images, Designations
text = re.sub(r'<div class="testimonial-quote-wrap">.*?</div>', '', text, flags=re.DOTALL)
text = re.sub(r'<div class="testimonial-one-image-wrap">.*?</div>', '', text, flags=re.DOTALL)
text = re.sub(r'<div class="testimonial-one-designation">.*?</div>', '', text, flags=re.DOTALL)

# Slide 1: Mission
text = re.sub(
    r'(<div class="testimonial-one-desc">)“Leano Energy has completely transformed our supply chain.*?</div>',
    r'\g<1>Leano Energy aims to enter the green energy market by promoting renewable energy together with high quality and affordable services.</div>',
    text, flags=re.DOTALL
)
# In donor file, the name might be "Alina Parker" or similar. Let's just find <div class="text-style-h5">...</div> inside testimonials and replace in order.
# Better to do a replace on all
parts = text.split('<div class="text-style-h5">')
if len(parts) >= 4: # at least 3 names
    parts[1] = "Mission</div>" + parts[1].split('</div>', 1)[1]
    parts[2] = "Vision</div>" + parts[2].split('</div>', 1)[1]
    parts[3] = "Values</div>" + parts[3].split('</div>', 1)[1]
    text = '<div class="text-style-h5">'.join(parts)

# Fix Slide 2 text
text = re.sub(
    r'(<div class="testimonial-one-desc">)“In the mining sector, any downtime is costly.*?</div>',
    r'\g<1>Developed on sustainable values and creating empowerment opportunities in South Africa, whilst striving to promote sustainable energy.</div>',
    text, flags=re.DOTALL
)
# Fix Slide 3 text
text = re.sub(
    r'(<div class="testimonial-one-desc">)“We rely heavily on consistent diesel supply.*?</div>',
    r'\g<1>Sustainable Values. Empowerment. Excellence.</div>',
    text, flags=re.DOTALL
)

# 4. Move Testimonials right after Tabs section
# Extract Testimonials
testi_match = re.search(r'(<section class="testimonial-section section-margin bg-white">.*?</section>)', text, re.DOTALL)
if testi_match:
    testi_html = testi_match.group(1)
    text = text.replace(testi_html, '')
    
    # Inject after tab-image-section
    # tab-image-section ends with </div></div></div></div></div></section>
    # Find the FIRST </section> after tab-image-section
    
    def inject_after_tabs(match):
        return match.group(0) + "\n\n" + testi_html + "\n\n"

    text = re.sub(r'<section class="tab-image-section section-margin">.*?</section>', inject_after_tabs, text, flags=re.DOTALL)

with open(about_us_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Update complete!")
