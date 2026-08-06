import os

files = [
    r"C:\Users\angam\Downloads\Leano Website V1\Index\website\Index.html",
    r"C:\Users\angam\Downloads\Leano Website V1\About Us\website\About Us.html"
]

replacements = [
    # Testimonial 1
    ("“Working with this team transformed our entire production process. Their engineering expertise and innovative approach helped us achieve higher accuracy, faster output, and reduced downtime across all departments.”",
     "“Leano Energy has completely transformed our supply chain. Their reliable fuel delivery ensures our trucks are always on the road. We haven't had a single delay since partnering with them.”"),
    (">Ronald Benson<", ">Thabo Mokoena<"),
    (">Lead Supervisor<", ">Logistics Manager<"),
    
    # Testimonial 2
    ("“This team brought a new level of efficiency to our operations. Their engineering solutions boosted our accuracy, increased our production speed, and helped minimize downtime across every stage of our process.”",
     "“In the mining sector, any downtime is costly. Leano Energy's advanced fuel management and prompt on-site supply have been a game changer for our operations.”"),
    (">Heanri Dokanai<", ">Sibusiso Ndlovu<"),
    (">Marketing head<", ">Operations Director<"),
    
    # Testimonial 3
    ("“Partnering with them upgraded our entire engineering system. Their smart solutions delivered tighter precision, stronger performance, and smoother production flow with noticeably less downtime.”",
     "“We rely heavily on consistent diesel supply during the harvest season. The team at Leano Energy always goes above and beyond to ensure our farming equipment never runs dry.”"),
    (">Michele Clarke<", ">Anika van der Merwe<"),
    (">Manager<", ">Agricultural Lead<")
]

for file_path in files:
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        for old, new in replacements:
            content = content.replace(old, new)
            
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {os.path.basename(file_path)}")
    else:
        print(f"File not found: {file_path}")
