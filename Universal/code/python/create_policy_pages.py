import os
import shutil
import re

base_dir = r'C:\Users\angam\Downloads\Leano Website V1'
source_dir = os.path.join(base_dir, 'News', 'News Sub Page 1')
policies_dir = os.path.join(base_dir, 'Policies')

if not os.path.exists(policies_dir):
    os.makedirs(policies_dir)

policies = [
    'Quality Policy',
    'Environmental Policy',
    'Safety Policy',
    'Privacy Policy',
    'Terms and Conditions'
]

content_template = """
<h3>1. Introduction</h3>
<p class="paragraph">This is a placeholder for the {policy_name} of Leano Energy. Please replace this text with your official legal documentation.</p>
<h3>2. Scope</h3>
<p class="paragraph">This policy applies to all operations, employees, and contractors working on behalf of Leano Energy across all sites and facilities.</p>
<h3>3. Commitment</h3>
<p class="paragraph">Leano Energy is committed to maintaining the highest standards of integrity and compliance in all our operations. We continuously monitor and improve our processes to ensure we meet or exceed all regulatory requirements.</p>
"""

for policy in policies:
    target_dir = os.path.join(policies_dir, policy)
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    
    # Copy the entire directory structure from News Sub Page 1
    shutil.copytree(source_dir, target_dir)
    
    # Rename the website HTML file
    old_html_path = os.path.join(target_dir, 'website', 'News Sub Page 1.html')
    new_html_path = os.path.join(target_dir, 'website', f'{policy}.html')
    os.rename(old_html_path, new_html_path)
    
    # Rename the CSS file
    old_css_path = os.path.join(target_dir, 'code', 'css', 'News Sub Page 1 CSS Code.css')
    new_css_path = os.path.join(target_dir, 'code', 'css', f'{policy} CSS Code.css')
    if os.path.exists(old_css_path):
        os.rename(old_css_path, new_css_path)
    
    # Update the HTML content
    with open(new_html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Replace Title
    html = re.sub(r'<title>.*?</title>', f'<title>{policy} | Leano Energy</title>', html)
    
    # Replace Breadcrumb Head
    html = re.sub(r'<div class=\x22breadcrumb-subtitle-head\x22>.*?</div>', f'<div class="breadcrumb-subtitle-head">Policies</div>', html)
    
    # Replace Breadcrumb Sub
    html = re.sub(r'<div class=\x22bradcrumb-subtitle\x22>.*?</div>', f'<div class="bradcrumb-subtitle">{policy}</div>', html)
    
    # Replace Main Heading
    html = re.sub(r'<h2 class=\x22blog-detail-title\x22>.*?</h2>', f'<h2 class="blog-detail-title">{policy}</h2>', html, flags=re.DOTALL)
    
    # Replace the Content Area (We'll just strip out the rich-text block and replace it)
    html = re.sub(r'<div class=\x22w-richtext\x22>.*?</div>', f'<div class="w-richtext">{content_template.format(policy_name=policy)}</div>', html, flags=re.DOTALL)
    
    # Replace CSS Link
    html = html.replace('News%20Sub%20Page%201%20CSS%20Code.css', f'{policy.replace(" ", "%20")}%20CSS%20Code.css')
    
    with open(new_html_path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Created 5 Policy pages with placeholder content!")
