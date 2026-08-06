import os
import re

base_path = r'C:\Users\angam\Downloads\Leano Website V1\Industries'

# Mapping of page number to the correct image prefix
correct_prefixes = {
    '1': '693bab1c2ae8a050a77fcc51_project-img-01',
    '2': '693bab36a9e5ca35d59ea50e_project-img-02',
    '3': '693bab488962cf0586d210a5_project-img-03',
    '4': '693bab636a5949a358a180e3_project-img-04',
    '5': '693bab7565a80b9096836890_project-img-05',
    '6': '693bab8cbe5a8458b5e10948_project-img-06'
}

# The incorrect prefix currently hardcoded in the template as the main image
template_prefix = '693bab36a9e5ca35d59ea50e_project-img-02'

for p_num, correct_prefix in correct_prefixes.items():
    if p_num == '2':
        continue # Page 2 is already correct
        
    path = os.path.join(base_path, f'Industries Sub Page {p_num}', 'website', f'Industries Sub Page {p_num}.html')
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # We only want to replace the FIRST occurrence which is the main hero image.
    # The first image tag has class="service-details-image".
    # Let's target it specifically using regex.
    def replacer(match):
        return match.group(0).replace(template_prefix, correct_prefix)
    
    # Replace ONLY inside the service-details-image img tag!
    text = re.sub(r'<img[^>]+class=\x22service-details-image\x22[^>]*>', replacer, text)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

print('Successfully replaced the hero images with their exact hashes on all sub pages!')
