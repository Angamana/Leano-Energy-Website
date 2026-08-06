import os
import re

about_us_path = r"C:\Users\angam\Downloads\Leano Website V1\About Us\website\About Us.html"

with open(about_us_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Transform Testimonials into Mission, Vision, Values
content = content.replace('<div class="subtitle-head">our Testimonials</div>', '<div class="subtitle-head">Our Future</div>')
content = content.replace('<h2 class="heading-title">What Our Clients Say?</h2>', '<h2 class="heading-title">Mission, Vision and values</h2>')

# Remove Quotation Images
content = re.sub(r'<div class="testimonial-quote-wrap">.*?</div>', '', content, flags=re.DOTALL)
# Remove Author Images
content = re.sub(r'<div class="testimonial-one-image-wrap">.*?</div>', '', content, flags=re.DOTALL)
# Remove Designations
content = re.sub(r'<div class="testimonial-one-designation">.*?</div>', '', content, flags=re.DOTALL)

# Slide 1: Mission
content = re.sub(
    r'(<div class="testimonial-one-desc">)“Leano Energy has completely transformed our supply chain.*?</div>',
    r'\g<1>Leano Energy aims to enter the green energy market by promoting renewable energy together with high quality and affordable services.</div>',
    content, flags=re.DOTALL
)
content = content.replace('<div class="text-style-h5">Thabo Mokoena</div>', '<div class="text-style-h5">Mission</div>')

# Slide 2: Vision
content = re.sub(
    r'(<div class="testimonial-one-desc">)“In the mining sector, any downtime is costly.*?</div>',
    r'\g<1>Developed on sustainable values and creating empowerment opportunities in South Africa, whilst striving to promote sustainable energy.</div>',
    content, flags=re.DOTALL
)
content = content.replace('<div class="text-style-h5">Sibusiso Ndlovu</div>', '<div class="text-style-h5">Vision</div>')

# Slide 3: Values
content = re.sub(
    r'(<div class="testimonial-one-desc">)“We rely heavily on consistent diesel supply.*?</div>',
    r'\g<1>Sustainable Values. Empowerment. Excellence.</div>',
    content, flags=re.DOTALL
)
content = content.replace('<div class="text-style-h5">Anika van der Merwe</div>', '<div class="text-style-h5">Values</div>')

# 2. Reorder Sections
# Currently it is: Hero -> Company Overview (Mission/Vision from my prev edit) -> Working Process -> Testimonials(now Mission/Vision) -> Footer
# We want: Hero -> Testimonials(now Mission/Vision) -> Working Process -> Footer

# Let's extract the Testimonials section
match_testi = re.search(r'(<section class="testimonial-section section-margin bg-white">.*?</section>)', content, re.DOTALL)
if match_testi:
    testi_html = match_testi.group(1)
    # Remove it from current position
    content = content.replace(testi_html, '')
    
    # Let's extract the Working Process section
    match_wp = re.search(r'(<section class="tab-image-section section-margin">.*?<div class="subtitle-head">About Us</div>.*?</section>)', content, re.DOTALL)
    if match_wp:
        wp_html = match_wp.group(1)
        # Remove it
        content = content.replace(wp_html, '')
        
        # Now remove the old Company Overview section (the one I modified to Our Purpose)
        match_co = re.search(r'(<section class="tab-image-section section-margin">.*?<div class="subtitle-head">Our Purpose</div>.*?</section>)', content, re.DOTALL)
        if match_co:
            content = content.replace(match_co.group(1), '')
            
        # Re-inject Testimonials then Working Process right after the Hero section.
        # The hero section ends with </div></div></div></div></div></section>
        # Let's find </section> after the hero.
        parts = content.split('</section>')
        if len(parts) >= 2:
            # First section is hero, we reassemble
            content = parts[0] + '</section>\n\n' + testi_html + '\n\n' + wp_html + '\n\n' + '</section>'.join(parts[1:])

with open(about_us_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Update complete!")
