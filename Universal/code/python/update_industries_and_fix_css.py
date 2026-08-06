import re

# 1. Update text in Industries Main Page.html
main_path = r'C:\Users\angam\Downloads\Leano Website V1\Industries\Industries Main Page\website\Industries Main Page.html'
with open(main_path, 'r', encoding='utf-8') as f:
    main_text = f.read()

replacements = {
    '<div class="breadcrumb-subtitle-head">Our Work</div>': '<div class="breadcrumb-subtitle-head">Industries We Serve</div>',
    '<h2 class="breadcrumb-heading-title">Project Scope &amp; Objectives</h2>': '<h2 class="breadcrumb-heading-title">Energy Solutions for South African Industries</h2>',
    'data-w-id="0374a76a-361f-962d-7def-1aaa8dde4c78">Projects</div>': 'data-w-id="0374a76a-361f-962d-7def-1aaa8dde4c78">Industries</div>'
}

for old, new in replacements.items():
    main_text = main_text.replace(old, new)

with open(main_path, 'w', encoding='utf-8') as f:
    f.write(main_text)

print("Updated Industries Main Page text.")

# 2. Fix CSS link in Industries Sub Page 1.html
sub_path = r'C:\Users\angam\Downloads\Leano Website V1\Industries\Industries Sub Page 1\website\Industries Sub Page 1.html'
with open(sub_path, 'r', encoding='utf-8') as f:
    sub_text = f.read()

# I had accidentally copied the href for Sub Page 2, so let's change it back
sub_text = sub_text.replace('Industries%20Sub%20Page%202%20CSS%20Code.css', 'Industries%20Sub%20Page%201%20CSS%20Code.css')

with open(sub_path, 'w', encoding='utf-8') as f:
    f.write(sub_text)

print("Fixed CSS link in Mining sub page.")
