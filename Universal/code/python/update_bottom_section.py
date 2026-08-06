import os
import glob
import re

base_dir = r'C:\Users\angam\Downloads\Leano Website V1\Industries'
html_files = glob.glob(os.path.join(base_dir, 'Industries Sub Page *', 'website', '*.html'), recursive=True)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # "Our Projects" -> "Industries We Serve"
    text = text.replace('Our Projects', 'Industries We Serve')
    
    # "Innovating for a Better Future" -> "Powering South Africa's Key Sectors"
    text = text.replace('Innovating for a Better Future', "Powering South Africa's Key Sectors")
    
    # "More Project" -> "More Industries"
    text = text.replace('More Project', 'More Industries')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(text)

print('Updated the bottom section across all 6 Sub Pages!')
