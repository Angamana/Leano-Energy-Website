import os

services_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html"

with open(services_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Hero text
content = content.replace('Forging the Future', 'Our Services')
content = content.replace('Service detail', 'Comprehensive Fuel Solutions')

# Intro paragraph injection
intro_html = '''</div>
                        <p class="white-text" style="margin-top: 20px; margin-bottom: 30px; font-size: 18px; max-width: 800px; line-height: 1.6;">At Leano Energy, we go beyond mere delivery. We offer a full suite of services designed to optimize your operations, reduce costs, and ensure a steady supply of energy whenever and wherever you need it.</p>
                        <div data-w-id="763f2668-16da-1dc5-5e82-724fa3bd9a02"'''
                        
content = content.replace('</div>\n                        <div data-w-id="763f2668-16da-1dc5-5e82-724fa3bd9a02"', intro_html)


# 2. Service 1
content = content.replace('>CNC Turning<', '>Bulk Fuel Supply &amp; Distribution<')
content = content.replace(
    'CNC turning is an advanced machining method used to produce precise cylindrical components by rotating raw material against computer-controlled cutting tools.',
    'Supplying high-quality fuels—including Petrol, Diesel, Paraffin, Oils, and Biofuel—across Gauteng, Mpumalanga, Limpopo, and the North West. We cater to wholesale, retail, and commercial sectors.<br><br><strong>Features:</strong> Reliable delivery schedules, certified fuel quality, competitive pricing.'
)

# 3. Service 2
content = content.replace('>Robot Installation<', '>Fuel Management Solutions<')
content = content.replace(
    'Robot installation is the process of deploying industrial robots into manufacturing environments, including setup, programming, calibration, and safety integration.',
    'Protect your business from fuel theft and mismanagement. Our advanced systems include on-site storage solutions, monthly consumption monitoring, and real-time reporting.<br><br><strong>Features:</strong> Smart meters, secure storage tanks, detailed analytics.'
)

# 4. Service 3
content = content.replace('>Renewable energy<', '>Lubricants &amp; Oils<')
content = content.replace(
    'Renewable energy involves generating power from natural sources like solar, wind, and hydro. It reduces environmental impact while delivering solutions.',
    'A comprehensive range of industrial lubricants to keep your machinery running smoothly, reducing wear and extending equipment lifespan.<br><br><strong>Features:</strong> High-performance formulas, diverse applications, technical support.'
)

# 5. Service 4
content = content.replace('>Gas &amp; oil industry<', '>Logistics &amp; Temporary Sites<')
content = content.replace(
    'The gas and oil industry focuses on the exploration, extraction, processing, and distribution of energy resources essential for powering global industries.',
    'Need fuel at a remote mining site or a temporary construction project? We specialize in setting up rapid-deployment fuel stations tailored to your project’s duration.<br><br><strong>Features:</strong> Mobile tanks, rapid setup, strict compliance.'
)


with open(services_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Content replaced successfully.")
