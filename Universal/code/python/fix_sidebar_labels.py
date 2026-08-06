import os
import glob
import re

base_dir = r'C:\Users\angam\Downloads\Leano Website V1\Industries'
html_files = glob.glob(os.path.join(base_dir, 'Industries Sub Page *', 'website', '*.html'), recursive=True)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Do replacements using re.sub for exact string match without worrying about casing if we just match the known casing
    # "Project Information" -> "Industry Information"
    text = text.replace('Project Information', 'Industry Information')
    
    # "Client :" -> "Clients :"
    text = text.replace('Client :', 'Clients :')
    
    # "Category :" -> "Sector :"
    text = text.replace('Category :', 'Sector :')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(text)

print('Updated Sidebar Information in all 6 Sub Pages!')
