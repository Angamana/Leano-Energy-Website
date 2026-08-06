import os

index_path = r"C:\Users\angam\Downloads\Leano Website V1\Index\website\Index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Fix the About Us headline
content = content.replace(
    '<h3 class="small-heading-title">Welcome to Leano Energy, a leading industry innovator with a rich history of excellence.</h3>',
    '<h3 class="small-heading-title">Youth-Owned. Level 1 BBBEE. Driven by Innovation.</h3>'
)

# 2. Fix the Services subtitle
content = content.replace('<div class="subtitle-head">our Services</div>', '<div class="subtitle-head">Our Solutions</div>')

# 3. Fix the Services headline (which was accidentally set to the About Us text)
content = content.replace(
    '<h2 class="heading-title service-heading">Youth-Owned. Level 1 BBBEE. Driven by Innovation.</h2>',
    '<h2 class="heading-title service-heading">Complete Fuel and Energy Solutions for South African Industry</h2>'
)

# 4. Fix the Services description
content = content.replace(
    '<div class="heading-subheading-desc">We support the gas and oil sector with high-precision engineered solutions \ndesigned to perform under extreme pressure, and load condition.</div>',
    '<div class="heading-subheading-desc">From fuel supply to fuel management and renewable energy solutions, we provide everything you need to keep your operations running efficiently.</div>'
)
# (Also try without the newline in case it's formatted differently)
content = content.replace(
    'We support the gas and oil sector with high-precision engineered solutions designed to perform under extreme pressure, and load condition.',
    'From fuel supply to fuel management and renewable energy solutions, we provide everything you need to keep your operations running efficiently.'
)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Services and About Us headers fixed successfully!")
