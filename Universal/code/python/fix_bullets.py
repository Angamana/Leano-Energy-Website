import os

base_path = r'C:\Users\angam\Downloads\Leano Website V1\Industries'

pages = {
    '2': [
        '<li><strong>Seasonal Reliability :</strong> Guaranteed supply during peak harvest times</li>',
        '<li><strong>On-site Delivery :</strong> Direct-to-farm bulk fuel drops</li>',
        '<li><strong>Equipment Protection :</strong> Premium lubricants for heavy farm machinery</li>'
    ],
    '3': [
        '<li><strong>Industrial-Grade HFO :</strong> high-performance fuel for boilers and large-scale heating</li>',
        '<li><strong>Continuous Supply Assurance :</strong> avoid downtime in critical operations</li>',
        '<li><strong>Custom Delivery Schedules :</strong> aligning fuel deliveries with operational needs</li>'
    ],
    '4': [
        '<li><strong>Bulk Diesel Solutions :</strong> tailored to fleet size and route requirements</li>',
        '<li><strong>Technology-Enabled Routing :</strong> BI-optimised delivery for speed and safety</li>',
        '<li><strong>Fleet Efficiency Tracking :</strong> data-driven insights to reduce fuel costs</li>'
    ],
    '5': [
        '<li><strong>Timely Jet Fuel Delivery :</strong> maintaining strict schedules</li>',
        '<li><strong>Premium Fuel Quality :</strong> meeting aviation-grade standards</li>',
        '<li><strong>Strategic Refined Sourcing :</strong> safeguarding clients against price fluctuations</li>'
    ],
    '6': [
        '<li><strong>Reliable Fuel for Public Services :</strong> buses, emergency vehicles, and maintenance fleets</li>',
        '<li><strong>Infrastructure Support :</strong> fueling public utilities and city projects</li>',
        '<li><strong>Transparent, Cost-Efficient Contracts :</strong> protecting taxpayer resources</li>'
    ]
}

old_bullets = [
    '<li><strong>Precision Fuel Management :</strong> accurate tracking and automated reporting</li>',
    '<li><strong>Bulk Diesel Supply :</strong> high-volume, cost-effective deliveries</li>',
    '<li><strong>Operational Efficiency :</strong> minimising downtime and maximising productivity</li>'
]

for p_num, new_bullets in pages.items():
    path = os.path.join(base_path, f'Industries Sub Page {p_num}', 'website', f'Industries Sub Page {p_num}.html')
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    text = text.replace(old_bullets[0], new_bullets[0])
    text = text.replace(old_bullets[1], new_bullets[1])
    text = text.replace(old_bullets[2], new_bullets[2])
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

print('Updated bullets for all sub-pages!')
