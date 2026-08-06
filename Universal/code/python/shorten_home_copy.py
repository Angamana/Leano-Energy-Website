import os

index_path = r"C:\Users\angam\Downloads\Leano Website V1\Index\website\Index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace Slide 1 text
content = content.replace("Leano Energy is a Level 1 BBBEE fuel distributor providing diesel, petrol, paraffin, oils, and lubricants to industries across Gauteng, Mpumalanga, Limpopo, and the North West.", 
                          "Level 1 BBBEE fuel distributor providing diesel, petrol, paraffin, and lubricants across Gauteng, Mpumalanga, Limpopo, and the North West.")

# Replace Slide 2 text
content = content.replace("Our fuel management systems monitor your monthly usage, prevent theft, and ensure you're always refueled on time. We install on-site storage tanks and provide real-time monitoring.", 
                          "Monitor monthly usage, prevent theft, and ensure timely refueling. We provide on-site tanks and real-time monitoring.")

# Replace Slide 3 text
content = content.replace("We're committed to sustainable energy. From biofuel solutions to promoting renewable energy, we're building a cleaner, greener future for South Africa.", 
                          "Committed to sustainable energy. From biofuel to renewable solutions, we're building a greener future for South Africa.")

# Replace About Us text
content = content.replace("Leano Energy is a Level 1 BBBEE fuel distributor founded on the belief that South Africa's future lies in the hands of its youth. As a 100% black youth-owned company, we bring fresh thinking, innovative ideas, and a commitment to sustainable growth to the fuel industry.<br><br>We are licensed wholesalers and distributors of bulk fuels, diesel, paraffin, oils, and various lubricants. Our products serve clients across Gauteng, Mpumalanga, Limpopo, and the North West, including mining, agriculture, logistics, airports, factories, and municipalities.", 
                          "As a 100% black youth-owned, Level 1 BBBEE distributor, we bring fresh, innovative thinking to the fuel industry.<br><br>We supply bulk fuels and lubricants to mining, agriculture, logistics, and more across Gauteng, Mpumalanga, Limpopo, and the North West.")

# Replace Service 1 text
content = content.replace("We supply high-quality fuels to industries across Gauteng, Mpumalanga, Limpopo, and the North West. Our products include Petrol Unleaded, Diesel, Illuminating Paraffin, Oils & Lubricants, and Biofuel.", 
                          "Supplying high-quality fuels—including Petrol, Diesel, Paraffin, Oils, and Biofuel—across Gauteng, Mpumalanga, Limpopo, and the North West.")

# Replace Service 2 text
content = content.replace("Protect your business from fuel theft and reduce costs with our comprehensive fuel management system. On-site storage tank installation, monthly usage monitoring, and real-time reporting.", 
                          "Protect your business from fuel theft and cut costs with on-site storage, monthly monitoring, and real-time reporting.")

# Replace Service 3 text
content = content.replace("We supply a full range of oils and lubricants for all industrial applications: Engine oils, Gear oils, Drive train oils, Hydraulic oils, Compressor oils, and Industrial oils.", 
                          "A full range of oils and lubricants for industrial applications, including engine, gear, hydraulic, and compressor oils.")

# Replace Service 4 text
content = content.replace("We're committed to promoting sustainable energy through innovative solutions. Blended biofuel, cleaner and safer for engines, and eco-friendly practices.", 
                          "Promoting sustainable energy with innovative solutions like blended biofuel—cleaner, safer, and eco-friendly.")

# Replace Testimonials text
content = content.replace("We've built long-term relationships with clients in mining, agriculture, logistics, airports, factories, and municipalities. Here's what they say about working with us.<br><br><i>These testimonials reflect real client experiences. Every client's needs are unique, and we tailor our solutions accordingly.</i>", 
                          "We've built long-term relationships across multiple industries. Here's what clients say about working with us.<br><br><i>Every client's needs are unique, and we tailor our solutions accordingly.</i>")


with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Home page content shortened successfully!")
