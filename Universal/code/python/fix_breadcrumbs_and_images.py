import os
import re

base_path = r'C:\Users\angam\Downloads\Leano Website V1\Industries'

pages = {
    '1': {
        'breadcrumb': 'Mining',
        'img_num': '01'
    },
    '2': {
        'breadcrumb': 'Agriculture',
        'img_num': '02'
    },
    '3': {
        'breadcrumb': 'Manufacturing',
        'img_num': '05' # Wait, on the main page, Manufacturing HTML points to 05. The file on disk was swapped. So HTML should point to 05.
    },
    '4': {
        'breadcrumb': 'Transport',
        'img_num': '04'
    },
    '5': {
        'breadcrumb': 'Aviation',
        'img_num': '03' # On main page Aviation was 03? Wait, let's check.
    },
    '6': {
        'breadcrumb': 'Government',
        'img_num': '06'
    }
}

# Actually, let's make sure we know which image goes to which page.
# I'll just pull the img name from the main page for each.
with open(os.path.join(base_path, 'Industries Main Page', 'website', 'Industries Main Page.html'), 'r', encoding='utf-8') as f:
    main_text = f.read()

# I can parse the project-item-wrap links to see which HTML file gets which image!
links = re.findall(r'<a[^>]+href=\x22\.\./\.\./Industries Sub Page (\d)/website/[^\x22]+\x22[^>]*>.*?<img[^>]+src=\x22[^\x22]+(project-img-0[1-6])\.jpg\x22', main_text, flags=re.DOTALL)
# links is a list of tuples: [('1', 'project-img-01'), ('2', 'project-img-02'), ...]
img_mapping = {l[0]: l[1][-2:] for l in links}
# Just in case, let's manually verify mapping.
# I'll use the mapping dynamically from the main page to ensure absolute consistency!

for p_num, p_data in pages.items():
    path = os.path.join(base_path, f'Industries Sub Page {p_num}', 'website', f'Industries Sub Page {p_num}.html')
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # 1. Update Breadcrumb Head
    text = re.sub(r'<div class=\x22breadcrumb-subtitle-head\x22>Agriculture</div>', f'<div class="breadcrumb-subtitle-head">{p_data["breadcrumb"]}</div>', text, count=1)
    
    # 2. Update Breadcrumb Sub
    text = text.replace('Project Detail', 'Industry Detail')
    
    # 3. Update Main Hero Image
    # We only want to replace the first occurrence of the project-img-02 in the project-detail section!
    # Let's find the project-detail-image-wrap section
    target_img_num = img_mapping.get(p_num, p_data['img_num'])
    
    # The image HTML looks like:
    # <div class="project-detail-image-wrap"><img src="../images/..._project-img-02.jpg" srcset="..._project-img-02-p-500.jpg 500w, ..." />
    # We can use regex to replace it inside that specific div.
    def img_repl(match):
        return match.group(0).replace('project-img-02', f'project-img-{target_img_num}')
    
    text = re.sub(r'<div class=\x22project-detail-image-wrap\x22>.*?</div>', img_repl, text, flags=re.DOTALL)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

print('Updated breadcrumbs and hero images for all 6 sub pages!')
