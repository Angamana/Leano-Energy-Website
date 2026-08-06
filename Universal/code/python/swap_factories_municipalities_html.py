import os
import re

base_path = r'C:\Users\angam\Downloads\Leano Website V1\Industries'

path_5 = os.path.join(base_path, 'Industries Sub Page 5', 'website', 'Industries Sub Page 5.html')
path_6 = os.path.join(base_path, 'Industries Sub Page 6', 'website', 'Industries Sub Page 6.html')

prefix_5 = '693bab7565a80b9096836890_project-img-05'
prefix_6 = '693bab8cbe5a8458b5e10948_project-img-06'

# Swap 5 with 6
with open(path_5, 'r', encoding='utf-8') as f:
    text_5 = f.read()

def replacer_5(match):
    return match.group(0).replace(prefix_5, prefix_6)

text_5 = re.sub(r'<img[^>]+class=\x22service-details-image\x22[^>]*>', replacer_5, text_5)

with open(path_5, 'w', encoding='utf-8') as f:
    f.write(text_5)

# Swap 6 with 5
with open(path_6, 'r', encoding='utf-8') as f:
    text_6 = f.read()

def replacer_6(match):
    return match.group(0).replace(prefix_6, prefix_5)

text_6 = re.sub(r'<img[^>]+class=\x22service-details-image\x22[^>]*>', replacer_6, text_6)

with open(path_6, 'w', encoding='utf-8') as f:
    f.write(text_6)

print("Swapped the images between Sub Page 5 and Sub Page 6 in the HTML.")
