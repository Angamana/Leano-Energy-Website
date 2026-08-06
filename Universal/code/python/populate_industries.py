import os
import re

base_path = r'C:\Users\angam\Downloads\Leano Website V1\Industries'
template_path = os.path.join(base_path, 'Industries Sub Page 1', 'website', 'Industries Sub Page 1.html')

with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

# Pages configuration
pages = {
    '2': {
        'folder': 'Industries Sub Page 2',
        'title': 'Timely fuel and lubricant solutions for farms and agricultural operations.',
        'heading': 'Agriculture Solutions',
        'desc': 'Leano Energy provides uninterrupted fuel supply for seasonal harvesting and daily agricultural operations. We deliver high-quality diesel and lubricants directly to farms, ensuring tractors, harvesters, and irrigation systems run optimally all year round.',
        'client': 'Farms',
        'sector': 'Agriculture',
        'bullet1': 'Seasonal Reliability :  Guaranteed supply during peak harvest times',
        'bullet2': 'On-site Delivery :  Direct-to-farm bulk fuel drops',
        'bullet3': 'Equipment Protection :  Premium lubricants for heavy farm machinery'
    },
    '3': {
        'folder': 'Industries Sub Page 3',
        'title': 'Consistent energy supply for uninterrupted manufacturing processes.',
        'heading': 'Manufacturing & Production Solutions',
        'desc': 'Unplanned downtime in manufacturing can be costly. We supply factories and production plants with consistent, high-grade fuels and industrial lubricants to keep assembly lines and generators running at peak efficiency, minimizing operational disruptions.',
        'client': 'Factories',
        'sector': 'Manufacturing',
        'bullet1': 'Uninterrupted Supply :  Continuous fuel for generators and boilers',
        'bullet2': 'Industrial Grade :  High-performance oils and lubricants',
        'bullet3': 'Cost Management :  Predictable and competitive bulk pricing'
    },
    '4': {
        'folder': 'Industries Sub Page 4',
        'title': 'Powering commercial fleets and logistics networks across the country.',
        'heading': 'Transport & Logistics Solutions',
        'desc': 'For logistics companies, fuel is the largest operational expense. Leano Energy offers strategic fuel supply and advanced consumption monitoring systems to help fleet managers track usage, prevent theft, and optimize routes for long-haul transport networks.',
        'client': 'Fleet Operators',
        'sector': 'Transport & Logistics',
        'bullet1': 'Fleet Monitoring :  IoT-driven fuel tracking and reporting',
        'bullet2': 'National Network :  Reliable supply across major transport routes',
        'bullet3': 'Fuel Quality :  Clean diesel for optimal engine lifespan'
    },
    '5': {
        'folder': 'Industries Sub Page 5',
        'title': 'High-quality aviation fuels for safe and efficient flight operations.',
        'heading': 'Aviation Solutions',
        'desc': 'Safety and precision are paramount in aviation. Leano Energy strictly adheres to international quality standards in supplying aviation fuels, ensuring commercial airlines, private charters, and cargo flights have access to uncontaminated, top-tier products.',
        'client': 'Airports & Airlines',
        'sector': 'Aviation',
        'bullet1': 'Quality Assurance :  Strict adherence to international aviation standards',
        'bullet2': 'Timely Refueling :  Efficient operations to prevent flight delays',
        'bullet3': 'Safety First :  Impeccable handling and contaminant-free delivery'
    },
    '6': {
        'folder': 'Industries Sub Page 6',
        'title': 'Reliable energy partnership for government and public sector projects.',
        'heading': 'Government & Parastatals Solutions',
        'desc': 'Leano Energy is a trusted partner for state-owned enterprises and government municipalities. We supply bulk fuels for public transport networks, infrastructure projects, and emergency backup generators, strictly complying with all procurement and safety regulations.',
        'client': 'Municipalities',
        'sector': 'Public Sector',
        'bullet1': 'Compliance :  Strict adherence to government procurement regulations',
        'bullet2': 'Scale & Reliability :  Capable of supplying large-scale state projects',
        'bullet3': 'Infrastructure Support :  Fueling public transport and civic works'
    }
}

old_title = 'Reliable fuel supply and management solutions to keep heavy mining machinery running.'
old_heading = 'Mining &amp; Civil Engineering Solutions'
old_desc = 'Efficient fuel management is critical in mining and civil engineering operations. Leano Energy reduces fuel wastage through IoT-driven monitoring systems and strategic bulk supply, lowering operational costs for heavy plant machinery and large-scale construction projects.'
old_client = 'Mines'
old_sector = 'Mining'
old_bullet1 = 'Precision Fuel Management : </span> accurate tracking and automated reporting'
old_bullet2 = 'Bulk Diesel Supply : </span> high-volume, cost-effective deliveries'
old_bullet3 = 'Operational Efficiency : </span> minimising downtime and maximising productivity'
old_css = 'Industries%20Sub%20Page%201%20CSS%20Code.css'

for p_num, p_data in pages.items():
    new_html = template
    
    # Replace content
    new_html = new_html.replace(old_title, p_data['title'])
    new_html = new_html.replace('Mining & Civil Engineering Solutions', p_data['heading'])
    new_html = new_html.replace(old_desc, p_data['desc'])
    new_html = new_html.replace(f'>{old_client}<', f'>{p_data["client"]}<')
    new_html = new_html.replace(f'>{old_sector}<', f'>{p_data["sector"]}<')
    new_html = new_html.replace(old_bullet1, f"{p_data['bullet1'].split(':')[0]} : </span>{p_data['bullet1'].split(':')[1]}")
    new_html = new_html.replace(old_bullet2, f"{p_data['bullet2'].split(':')[0]} : </span>{p_data['bullet2'].split(':')[1]}")
    new_html = new_html.replace(old_bullet3, f"{p_data['bullet3'].split(':')[0]} : </span>{p_data['bullet3'].split(':')[1]}")
    
    # Fix the CSS link to point to the correct sub-page CSS!
    new_html = new_html.replace(old_css, f'Industries%20Sub%20Page%20{p_num}%20CSS%20Code.css')
    
    # Write the new HTML
    target_file = os.path.join(base_path, p_data['folder'], 'website', f'{p_data["folder"]}.html')
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(new_html)

print('Successfully populated all 5 remaining Industry sub-pages!')
