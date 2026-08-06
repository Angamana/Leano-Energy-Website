import os

index_path = r"C:\Users\angam\Downloads\Leano Website V1\Index\website\Index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Card 1 (already partially replaced Fuel Distribution, but let's replace remaining CNC Turning)
content = content.replace("CNC Turning", "Fuel Distribution")
content = content.replace("Delivering high-precision CNC turning solutions tailored to your complex specifications, ensuring accuracy and efficiency.", "Supplying high-quality fuels—including Petrol, Diesel, Paraffin, Oils, and Biofuel—across Gauteng, Mpumalanga, Limpopo, and the North West.")

# Card 2
content = content.replace("Robot Installation", "Fuel Management Solutions")
content = content.replace("Expert robot installation services to automate and streamline your operations, enhancing both productivity and safety.", "Protect your business from fuel theft and cut costs with on-site storage, monthly monitoring, and real-time reporting.")

# Card 3
content = content.replace("Renewable energy", "Complete Oil and Lubricant Solutions")
content = content.replace("Implementing renewable energy systems that reduce costs and environmental impact, driving sustainable industrial growth.", "A full range of oils and lubricants for industrial applications, including engine, gear, hydraulic, and compressor oils.")

# Card 4
content = content.replace("Gas &amp; oil industry", "Biofuel & Sustainable Energy")
content = content.replace("Gas & oil industry", "Biofuel & Sustainable Energy")
content = content.replace("Providing robust and reliable solutions for the gas and oil industry, focused on optimizing performance and safety.", "Promoting sustainable energy with innovative solutions like blended biofuel—cleaner, safer, and eco-friendly.")

# Update categories inside the cards just in case
content = content.replace(">Fabricators<", ">Supply<", 2)
content = content.replace(">Automation<", ">Monitoring<", 2)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Service cards globally updated!")
