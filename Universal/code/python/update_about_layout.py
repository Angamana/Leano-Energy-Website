import os
import re

about_us_path = r"C:\Users\angam\Downloads\Leano Website V1\About Us\website\About Us.html"

with open(about_us_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Fix Tab spacing and wrapping
# Add flex-wrap and width to the tabs
content = content.replace('<div class="tabs-image-menu w-tab-menu">', '<div class="tabs-image-menu w-tab-menu" style="flex-wrap: wrap;">')
content = content.replace('<a data-w-tab="Tab 1" class="tab-image-link w-inline-block w-tab-link">', '<a data-w-tab="Tab 1" class="tab-image-link w-inline-block w-tab-link" style="width: 33.33%; min-width: 250px;">')
content = content.replace('<a data-w-tab="Tab 2" class="tab-image-link w-inline-block w-tab-link w--current">', '<a data-w-tab="Tab 2" class="tab-image-link w-inline-block w-tab-link w--current" style="width: 33.33%; min-width: 250px;">')
content = content.replace('<a data-w-tab="Tab 3" class="tab-image-link w-inline-block w-tab-link">', '<a data-w-tab="Tab 3" class="tab-image-link w-inline-block w-tab-link" style="width: 33.33%; min-width: 250px;">')
content = content.replace('<a data-w-tab="Tab 4" class="tab-image-link w-inline-block w-tab-link">', '<a data-w-tab="Tab 4" class="tab-image-link w-inline-block w-tab-link" style="width: 33.33%; min-width: 250px;">')
content = content.replace('<a data-w-tab="Tab 5" class="tab-image-link w-inline-block w-tab-link">', '<a data-w-tab="Tab 5" class="tab-image-link w-inline-block w-tab-link" style="width: 33.33%; min-width: 250px;">')

# Add spacing after the tabs section
content = content.replace('<div data-current="Tab 2" data-easing="ease" data-duration-in="300" data-duration-out="100" class="tab-image w-tabs">', '<div data-current="Tab 2" data-easing="ease" data-duration-in="300" data-duration-out="100" class="tab-image w-tabs" style="margin-bottom: 80px;">')

# 2. Rename Working Process to About Us
content = content.replace('<div class="subtitle-head">Working Process</div>', '<div class="subtitle-head">About Us</div>')
# Remove the old heading title "quality industy is the better future"
content = re.sub(r'<h2 class="heading-title">quality industy is the better future</h2>', '', content)

# 3. Transform Testimonials into Mission, Vision, Values
content = content.replace('WHAT OUR CLIENTS SAY?', 'Mission, Vision and values')
content = content.replace('OUR TESTIMONIALS', 'Our Future')

# Remove quotation marks
# Usually it's something like <div class="testimonial-one-quote">...</div> or similar. Let's just remove anything with "quote" class or similar if it's an image.
# We will use regex to remove the quote images and stars.
content = re.sub(r'<img[^>]*quote[^>]*>', '', content, flags=re.IGNORECASE)
content = re.sub(r'<div class="star-wrap[^>]*>.*?</div>\s*</div>', '', content, flags=re.IGNORECASE|re.DOTALL)
# Also remove star icons directly if they are there
content = re.sub(r'<img[^>]*star[^>]*>', '', content, flags=re.IGNORECASE)
# Sometimes the stars are a list of icons
content = re.sub(r'<div class="star-icon-wrap.*?</div>', '', content, flags=re.IGNORECASE|re.DOTALL)

# Slide 1: Mission
content = re.sub(r'(<div class="testimonial-one-slide w-slide">.*?<div class="testimonial-one-desc">).*?(</div>.*?<h5 class="author-title">).*?(</h5>.*?<p class="author-profession">).*?(</p>)',
    r'\g<1>Leano Energy aims to enter the green energy market by promoting renewable energy together with high quality and affordable services.\g<2>Mission\g<3>\g<4>', content, count=1, flags=re.DOTALL)
# Slide 2: Vision
content = re.sub(r'(<div class="testimonial-one-slide w-slide">.*?<div class="testimonial-one-desc">).*?(</div>.*?<h5 class="author-title">).*?(</h5>.*?<p class="author-profession">).*?(</p>)',
    r'\g<1>Developed on sustainable values and creating empowerment opportunities in South Africa, whilst striving to promote sustainable energy.\g<2>Vision\g<3>\g<4>', content, count=1, flags=re.DOTALL)
# Slide 3: Values
content = re.sub(r'(<div class="testimonial-one-slide w-slide">.*?<div class="testimonial-one-desc">).*?(</div>.*?<h5 class="author-title">).*?(</h5>.*?<p class="author-profession">).*?(</p>)',
    r'\g<1>Sustainable Values. Empowerment. Excellence.\g<2>Values\g<3>\g<4>', content, count=1, flags=re.DOTALL)

# Remove the author images
content = re.sub(r'<img[^>]*author-img[^>]*>', '', content, flags=re.IGNORECASE)
# Also remove the remaining author profession paragraphs that are empty now
content = re.sub(r'<p class="author-profession"></p>', '', content)

with open(about_us_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Update complete!")
