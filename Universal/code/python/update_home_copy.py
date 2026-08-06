import os

index_path = r"C:\Users\angam\Downloads\Leano Website V1\Index\website\Index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# --- HERO SECTION SLIDER ---
# Slide 1 (Currently "Industrial machine", "Strength in Every Detail")
content = content.replace("Industrial machine", "Bulk Fuel Distributors", 1)
content = content.replace("Strength in Every Detail", "Fueling Successful Journeys, Delivering Energy That Powers South Africa", 1)
content = content.replace("We provide precision-driven solutions across robotics setup, renewable energy, oil and gas, and CNC machining, delivering reliable performance and lasting impact for every industrial project.", "Leano Energy is a Level 1 BBBEE fuel distributor providing diesel, petrol, paraffin, oils, and lubricants to industries across Gauteng, Mpumalanga, Limpopo, and the North West.", 1)
content = content.replace(">Discover more<", ">Request a Quote Today<", 1)
content = content.replace(">Our Projects<", ">View Our Products<", 1)

# Slide 2 (Currently "Industrial machine" - Wait, let me check the second one. Usually they are the same subtitle)
content = content.replace("Industrial machine", "Fuel Management Solutions", 1)
content = content.replace("Precision in Every Detail", "Stop Fuel Theft. Cut Costs. Take Control.", 1)
content = content.replace("We provide precision-driven solutions across robotics setup, renewable energy, oil and gas, and CNC machining, delivering reliable performance and lasting impact for every industrial project.", "Our fuel management systems monitor your monthly usage, prevent theft, and ensure you're always refueled on time. We install on-site storage tanks and provide real-time monitoring.", 1)
content = content.replace(">Discover more<", ">Learn About Fuel Management<", 1)
content = content.replace(">Our Projects<", ">Explore Our Services<", 1)

# Slide 3
content = content.replace("Industrial machine", "Sustainable Energy Solutions", 1)
content = content.replace("Efficiency in Every Design", "Powering Growth, Responsibly", 1)
content = content.replace("We provide precision-driven solutions across robotics setup, renewable energy, oil and gas, and CNC machining, delivering reliable performance and lasting impact for every industrial project.", "We're committed to sustainable energy. From biofuel solutions to promoting renewable energy, we're building a cleaner, greener future for South Africa.", 1)
content = content.replace(">Discover more<", ">Contact Our Team<", 1)
content = content.replace(">Our Projects<", ">Read Our Story<", 1)

# --- TRUST BAR (Marquee) ---
content = content.replace("Powering your success through precision engineering and advanced industrial solutions.", "Level 1 BBBEE Contributor: 100% Black Youth Owned • Authorized Distributors for Sasol, Shell, BP, Engen & Chevron • Serving Gauteng, Mpumalanga, Limpopo & North West.", 2) # There might be two marquees in the HTML for seamless scrolling

# --- ABOUT US SECTION ---
content = content.replace("Who We Are", "Who We Are", 1) # Already correct subtitle? Let's check.
content = content.replace("quality industy is the better future", "Youth-Owned. Level 1 BBBEE. Driven by Innovation.", 1)
# The text for About Us in Index.html is currently: "We provide precision-driven solutions across robotics setup, renewable energy, oil and gas, and CNC machining, delivering reliable performance and lasting impact for every industrial project." Wait, I replaced this three times already. Is there a 4th time for the About section? Let's replace the one under the about image.
content = content.replace("We provide precision-driven solutions across robotics setup, renewable energy, oil and gas, and CNC machining, delivering reliable performance and lasting impact for every industrial project.", "Leano Energy is a Level 1 BBBEE fuel distributor founded on the belief that South Africa's future lies in the hands of its youth. As a 100% black youth-owned company, we bring fresh thinking, innovative ideas, and a commitment to sustainable growth to the fuel industry.<br><br>We are licensed wholesalers and distributors of bulk fuels, diesel, paraffin, oils, and various lubricants. Our products serve clients across Gauteng, Mpumalanga, Limpopo, and the North West, including mining, agriculture, logistics, airports, factories, and municipalities.", 1)
content = content.replace(">Discover more<", ">Learn More About Us<", 1) # Note: this will replace the first "Discover more" it finds, which might be in About Us.

# --- SERVICES SECTION ---
content = content.replace(">Our Services<", ">Our Solutions<", 1)
content = content.replace("Powering progress with proven", "Complete Fuel and Energy Solutions", 1)
content = content.replace("industrial experience", "for South African Industry", 1)
content = content.replace("Our industrial experience drives innovative, efficient solutions designed to meet the toughest challenges and power sustainable progress.", "From bulk fuel supply to fuel management and renewable energy solutions, we provide everything you need to keep your operations running efficiently.", 1)

# Service Cards (4 cards)
# Card 1: Currently "CNC Turning", desc: "Delivering high-precision CNC turning..."
content = content.replace(">CNC Turning<", ">Bulk Fuel Distribution<", 1)
content = content.replace("Delivering high-precision CNC turning solutions tailored to your complex specifications, ensuring accuracy and efficiency.", "We supply high-quality fuels to industries across Gauteng, Mpumalanga, Limpopo, and the North West. Our products include Petrol Unleaded, Diesel, Illuminating Paraffin, Oils & Lubricants, and Biofuel.", 1)
content = content.replace(">Learn More<", ">Request a Quote<", 1)

# Card 2: Currently "Robot Installation", desc: "Expert robot installation services..."
content = content.replace(">Robot Installation<", ">Fuel Management Solutions<", 1)
content = content.replace("Expert robot installation services to automate and streamline your operations, enhancing both productivity and safety.", "Protect your business from fuel theft and reduce costs with our comprehensive fuel management system. On-site storage tank installation, monthly usage monitoring, and real-time reporting.", 1)
content = content.replace(">Learn More<", ">Learn More<", 1) # Keep Learn More or Request a Quote? Will just keep the existing text if it works.

# Card 3: Currently "Renewable energy", desc: "Implementing renewable energy systems..."
content = content.replace(">Renewable energy<", ">Complete Oil and Lubricant Solutions<", 1)
content = content.replace("Implementing renewable energy systems that reduce costs and environmental impact, driving sustainable industrial growth.", "We supply a full range of oils and lubricants for all industrial applications: Engine oils, Gear oils, Drive train oils, Hydraulic oils, Compressor oils, and Industrial oils.", 1)
content = content.replace(">Learn More<", ">Contact Our Team<", 1)

# Card 4: Currently "Gas & oil industry", desc: "Providing robust and reliable solutions..."
content = content.replace(">Gas &amp; oil industry<", ">Biofuel & Sustainable Energy<", 1)
content = content.replace("Providing robust and reliable solutions for the gas and oil industry, focused on optimizing performance and safety.", "We're committed to promoting sustainable energy through innovative solutions. Blended biofuel, cleaner and safer for engines, and eco-friendly practices.", 1)
content = content.replace(">Learn More<", ">Learn About Biofuel<", 1)


# --- TESTIMONIAL SECTION ---
content = content.replace("Client Feedback", "Client Feedback", 1)
content = content.replace("Happy clients share their stories", "Trusted by Industries Across South Africa", 1)
content = content.replace("Read what our clients have to say about their experiences and the value we’ve delivered.", "We've built long-term relationships with clients in mining, agriculture, logistics, airports, factories, and municipalities. Here's what they say about working with us.<br><br><i>These testimonials reflect real client experiences. Every client's needs are unique, and we tailor our solutions accordingly.</i>", 1)

# --- BLOG SECTION ---
content = content.replace("News &amp; Article", "Industry Insights", 1)
content = content.replace("Industry Insights and news", "Fuel Industry Knowledge, Practical Guidance", 1)
content = content.replace("Stay updated with the latest trends, insights, and innovations in the industrial sector through our articles.", "Expert insights on fuel management, energy solutions, and sustainable growth from the Leano Energy team.", 1)


# --- FOOTER SECTION ---
content = content.replace("Let’s Talk", "Ready to Power Your Journey?", 1)
content = content.replace("Contact now", "Call Us: 010 442 4895", 1)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Index.html copy updated!")
