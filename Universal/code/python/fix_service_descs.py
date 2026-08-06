import os

index_path = r"C:\Users\angam\Downloads\Leano Website V1\Index\website\Index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace descriptions
content = content.replace(
    "CNC turning is an advanced machining method used to produce precise cylindrical \ncomponents by rotating raw material against computer-controlled cutting tools.",
    "Supplying high-quality fuels—including Petrol, Diesel, Paraffin, Oils, and Biofuel—across Gauteng, Mpumalanga, Limpopo, and the North West."
)
# Also without the newline just in case
content = content.replace(
    "CNC turning is an advanced machining method used to produce precise cylindrical components by rotating raw material against computer-controlled cutting tools.",
    "Supplying high-quality fuels—including Petrol, Diesel, Paraffin, Oils, and Biofuel—across Gauteng, Mpumalanga, Limpopo, and the North West."
)

content = content.replace(
    "Robot installation is the process of deploying industrial robots into manufacturing \nenvironments, including setup, programming, calibration, and safety integration.",
    "Protect your business from fuel theft and cut costs with on-site storage, monthly monitoring, and real-time reporting."
)
content = content.replace(
    "Robot installation is the process of deploying industrial robots into manufacturing environments, including setup, programming, calibration, and safety integration.",
    "Protect your business from fuel theft and cut costs with on-site storage, monthly monitoring, and real-time reporting."
)

content = content.replace(
    "Complete Oil and Lubricant Solutions involves generating power from natural sources like \nsolar, wind, and hydro. It reduces environmental impact while delivering solutions.",
    "A full range of oils and lubricants for industrial applications, including engine, gear, hydraulic, and compressor oils."
)
content = content.replace(
    "Complete Oil and Lubricant Solutions involves generating power from natural sources like solar, wind, and hydro. It reduces environmental impact while delivering solutions.",
    "A full range of oils and lubricants for industrial applications, including engine, gear, hydraulic, and compressor oils."
)

content = content.replace(
    "The gas and oil industry focuses on the exploration, extraction, processing, and \ndistribution of energy resources essential for powering global industries.",
    "Promoting sustainable energy with innovative solutions like blended biofuel—cleaner, safer, and eco-friendly."
)
content = content.replace(
    "The gas and oil industry focuses on the exploration, extraction, processing, and distribution of energy resources essential for powering global industries.",
    "Promoting sustainable energy with innovative solutions like blended biofuel—cleaner, safer, and eco-friendly."
)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Service card descriptions updated successfully!")
