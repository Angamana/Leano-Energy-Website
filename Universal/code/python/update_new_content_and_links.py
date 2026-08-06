import os
import re

base_path = r'C:\Users\angam\Downloads\Leano Website V1\Industries'

# 1. Update text for Pages 3, 4, 5, 6
pages = {
    '3': {
        'old_heading': 'Manufacturing & Production Solutions',
        'old_desc': 'Unplanned downtime in manufacturing can be costly. We supply factories and production plants with consistent, high-grade fuels and industrial lubricants to keep assembly lines and generators running at peak efficiency, minimizing operational disruptions.',
        'old_b1': 'Uninterrupted Supply : </span> Continuous fuel for generators and boilers',
        'old_b2': 'Industrial Grade : </span> High-performance oils and lubricants',
        'old_b3': 'Cost Management : </span> Predictable and competitive bulk pricing',
        
        'heading': 'Healthcare & Manufacturing',
        'desc': 'Hospitals, factories, and industrial plants rely on consistent thermal energy for boilers, machinery, and process operations. Leano Energy delivers specialised Heavy Fuel Oil (HFO) and industrial fuels that ensure an uninterrupted energy supply.',
        'b1': 'Industrial-Grade HFO : </span> high-performance fuel for boilers and large-scale heating',
        'b2': 'Continuous Supply Assurance : </span> avoid downtime in critical operations',
        'b3': 'Custom Delivery Schedules : </span> aligning fuel deliveries with operational needs'
    },
    '4': {
        'old_heading': 'Transport & Logistics Solutions',
        'old_desc': 'For logistics companies, fuel is the largest operational expense. Leano Energy offers strategic fuel supply and advanced consumption monitoring systems to help fleet managers track usage, prevent theft, and optimize routes for long-haul transport networks.',
        'old_b1': 'Fleet Monitoring : </span> IoT-driven fuel tracking and reporting',
        'old_b2': 'National Network : </span> Reliable supply across major transport routes',
        'old_b3': 'Fuel Quality : </span> Clean diesel for optimal engine lifespan',
        
        'heading': 'Transporters & Logistics',
        'desc': 'Fleet operators require high-capacity, cost-effective diesel supply to maintain national and regional transport networks. Leano Energy combines competitive bulk pricing with a reliable delivery network, keeping logistics operations moving efficiently.',
        'b1': 'Bulk Diesel Solutions : </span> tailored to fleet size and route requirements',
        'b2': 'Technology-Enabled Routing : </span> BI-optimised delivery for speed and safety',
        'b3': 'Fleet Efficiency Tracking : </span> data-driven insights to reduce fuel costs'
    },
    '5': {
        'old_heading': 'Aviation Solutions',
        'old_desc': 'Safety and precision are paramount in aviation. Leano Energy strictly adheres to international quality standards in supplying aviation fuels, ensuring commercial airlines, private charters, and cargo flights have access to uncontaminated, top-tier products.',
        'old_b1': 'Quality Assurance : </span> Strict adherence to international aviation standards',
        'old_b2': 'Timely Refueling : </span> Efficient operations to prevent flight delays',
        'old_b3': 'Safety First : </span> Impeccable handling and contaminant-free delivery',
        
        'heading': 'Aviation & Airports',
        'desc': 'Flight operations depend on on-time, reliable Jet Fuel supply. Leano Energy ensures that airports, private charters, and aviation service providers receive consistent fuel deliveries with industry-leading reliability.',
        'b1': 'Timely Jet Fuel Delivery : </span> maintaining strict schedules',
        'b2': 'Premium Fuel Quality : </span> meeting aviation-grade standards',
        'b3': 'Strategic Refined Sourcing : </span> safeguarding clients against price fluctuations'
    },
    '6': {
        'old_heading': 'Government & Parastatals Solutions',
        'old_desc': 'Leano Energy is a trusted partner for state-owned enterprises and government municipalities. We supply bulk fuels for public transport networks, infrastructure projects, and emergency backup generators, strictly complying with all procurement and safety regulations.',
        'old_b1': 'Compliance : </span> Strict adherence to government procurement regulations',
        'old_b2': 'Scale & Reliability : </span> Capable of supplying large-scale state projects',
        'old_b3': 'Infrastructure Support : </span> Fueling public transport and civic works',
        
        'heading': 'Municipalities & Public Infrastructure',
        'desc': 'Public service vehicles, utilities, and municipal operations require a dependable energy supply to serve communities effectively. Leano Energy provides bulk fuel and paraffin solutions that support municipal fleets and essential infrastructure.',
        'b1': 'Reliable Fuel for Public Services : </span> buses, emergency vehicles, and maintenance fleets',
        'b2': 'Infrastructure Support : </span> fueling public utilities and city projects',
        'b3': 'Transparent, Cost-Efficient Contracts : </span> protecting taxpayer resources'
    }
}

for i in ['3', '4', '5', '6']:
    path = os.path.join(base_path, f'Industries Sub Page {i}', 'website', f'Industries Sub Page {i}.html')
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    text = text.replace(pages[i]['old_heading'], pages[i]['heading'])
    text = text.replace(pages[i]['old_desc'], pages[i]['desc'])
    text = text.replace(pages[i]['old_b1'], pages[i]['b1'])
    text = text.replace(pages[i]['old_b2'], pages[i]['b2'])
    text = text.replace(pages[i]['old_b3'], pages[i]['b3'])
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

# 2. Update navigation links at the bottom of ALL 6 pages
for i in range(1, 7):
    path = os.path.join(base_path, f'Industries Sub Page {i}', 'website', f'Industries Sub Page {i}.html')
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Let's fix the links manually using regex.
    # The bottom section has links to page 1, 2, 3 originally. Let's make them link to pages 4, 5, 6 as an example,
    # or better, just link to 1, 2, 3 generically.
    # We will replace `../../Industries Sub Page 1/website/Industries Sub Page 1.html`
    text = text.replace('../../Industries Sub Page 1/website/Industries Sub Page 1.html', '../../Industries Sub Page 4/website/Industries Sub Page 4.html')
    text = text.replace('Industries Sub Page 2.html', '../../Industries Sub Page 5/website/Industries Sub Page 5.html')
    text = text.replace('../../Industries Sub Page 3/website/Industries Sub Page 3.html', '../../Industries Sub Page 6/website/Industries Sub Page 6.html')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

print('Updated texts and links in industry sub pages!')
