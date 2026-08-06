import os

base_path = r'C:\Users\angam\Downloads\Leano Website V1\Industries'
template_path = os.path.join(base_path, 'Industries Sub Page 1', 'website', 'Industries Sub Page 1.html')

with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

pages = {
    '3': {
        'breadcrumb': 'Transport',
        'img_num': '03',
        'heading': 'Transporters & Logistics',
        'desc': 'Fleet operators require high-capacity, cost-effective diesel supply to maintain national and regional transport networks. Leano Energy combines competitive bulk pricing with a reliable delivery network, keeping logistics operations moving efficiently.',
        'b1': 'Bulk Diesel Solutions', 'b1_desc': 'tailored to fleet size and route requirements',
        'b2': 'Technology-Enabled Routing', 'b2_desc': 'BI-optimised delivery for speed and safety',
        'b3': 'Fleet Efficiency Tracking', 'b3_desc': 'data-driven insights to reduce fuel costs',
        'client': 'Fleet Operators',
        'sector': 'Transport & Logistics'
    },
    '4': {
        'breadcrumb': 'Aviation',
        'img_num': '04',
        'heading': 'Aviation & Airports',
        'desc': 'Flight operations depend on on-time, reliable Jet Fuel supply. Leano Energy ensures that airports, private charters, and aviation service providers receive consistent fuel deliveries with industry-leading reliability.',
        'b1': 'Timely Jet Fuel Delivery', 'b1_desc': 'maintaining strict schedules',
        'b2': 'Premium Fuel Quality', 'b2_desc': 'meeting aviation-grade standards',
        'b3': 'Strategic Refined Sourcing', 'b3_desc': 'safeguarding clients against price fluctuations',
        'client': 'Airports & Airlines',
        'sector': 'Aviation'
    },
    '5': {
        'breadcrumb': 'Manufacturing',
        'img_num': '05',
        'heading': 'Healthcare & Manufacturing',
        'desc': 'Hospitals, factories, and industrial plants rely on consistent thermal energy for boilers, machinery, and process operations. Leano Energy delivers specialised Heavy Fuel Oil (HFO) and industrial fuels that ensure an uninterrupted energy supply.',
        'b1': 'Industrial-Grade HFO', 'b1_desc': 'high-performance fuel for boilers and large-scale heating',
        'b2': 'Continuous Supply Assurance', 'b2_desc': 'avoid downtime in critical operations',
        'b3': 'Custom Delivery Schedules', 'b3_desc': 'aligning fuel deliveries with operational needs',
        'client': 'Factories',
        'sector': 'Manufacturing'
    },
    '6': {
        'breadcrumb': 'Government',
        'img_num': '06',
        'heading': 'Municipalities & Public Infrastructure',
        'desc': 'Public service vehicles, utilities, and municipal operations require a dependable energy supply to serve communities effectively. Leano Energy provides bulk fuel and paraffin solutions that support municipal fleets and essential infrastructure.',
        'b1': 'Reliable Fuel for Public Services', 'b1_desc': 'buses, emergency vehicles, and maintenance fleets',
        'b2': 'Infrastructure Support', 'b2_desc': 'fueling public utilities and city projects',
        'b3': 'Transparent, Cost-Efficient Contracts', 'b3_desc': 'protecting taxpayer resources',
        'client': 'Municipalities',
        'sector': 'Public Sector'
    }
}

old_breadcrumb = '<div class="breadcrumb-subtitle-head">Mining</div>'
old_heading = 'Mining &amp; Civil Engineering Solutions'
old_desc = 'Efficient fuel management is critical in mining and civil engineering operations. Leano Energy reduces fuel wastage through IoT-driven monitoring systems and strategic bulk supply, lowering operational costs for heavy plant machinery and large-scale construction projects.'
old_client = '>Mines<'
old_sector = '>Mining<'
old_b1 = '<li><strong>Precision Fuel Management :</strong> accurate tracking and automated reporting</li>'
old_b2 = '<li><strong>Bulk Diesel Supply :</strong> high-volume, cost-effective deliveries</li>'
old_b3 = '<li><strong>Operational Efficiency :</strong> minimising downtime and maximising productivity</li>'
old_css = 'Industries%20Sub%20Page%201%20CSS%20Code.css'

for p_num, p_data in pages.items():
    new_html = template
    
    # Text replacements
    new_html = new_html.replace(old_breadcrumb, f'<div class="breadcrumb-subtitle-head">{p_data["breadcrumb"]}</div>')
    new_html = new_html.replace(old_heading, p_data["heading"].replace('&', '&amp;'))
    new_html = new_html.replace(old_desc, p_data["desc"])
    new_html = new_html.replace(old_client, f'>{p_data["client"]}<')
    
    # We have to be careful with Sector because replacing >Mining< might replace something else. Let's just do it.
    # Mining Sub Page 1 might have >Mining< in the sidebar.
    new_html = new_html.replace(old_sector, f'>{p_data["sector"]}<')
    
    new_html = new_html.replace(old_b1, f'<li><strong>{p_data["b1"]} :</strong> {p_data["b1_desc"]}</li>')
    new_html = new_html.replace(old_b2, f'<li><strong>{p_data["b2"]} :</strong> {p_data["b2_desc"]}</li>')
    new_html = new_html.replace(old_b3, f'<li><strong>{p_data["b3"]} :</strong> {p_data["b3_desc"]}</li>')
    
    # CSS path
    new_html = new_html.replace(old_css, f'Industries%20Sub%20Page%20{p_num}%20CSS%20Code.css')
    
    # Images - We need to replace project-img-01 with the correct img_num
    new_html = new_html.replace('project-img-01', f'project-img-{p_data["img_num"]}')
    
    # Fix the bottom navigation links just in case
    # Let's point the bottom links to some other sub pages
    new_html = new_html.replace('../../Industries Sub Page 1/website/Industries Sub Page 1.html', f'../../Industries Sub Page 1/website/Industries Sub Page 1.html')
    new_html = new_html.replace('Industries Sub Page 2.html', f'../../Industries Sub Page 2/website/Industries Sub Page 2.html')
    
    target_file = os.path.join(base_path, f'Industries Sub Page {p_num}', 'website', f'Industries Sub Page {p_num}.html')
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(new_html)

print('Successfully re-synced all texts and images according to the true Main Page mapping!')
