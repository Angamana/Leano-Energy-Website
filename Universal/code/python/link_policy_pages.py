import os
import glob
import re

base_dir = r'C:\Users\angam\Downloads\Leano Website V1'
html_files = glob.glob(os.path.join(base_dir, '**', '*.html'), recursive=True)

policies = [
    'Quality Policy',
    'Environmental Policy',
    'Safety Policy',
    'Privacy Policy',
    'Terms and Conditions'
]

count = 0
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    file_dir = os.path.dirname(file)
    
    # We will search for the footer block and replace the policy links
    footer_match = re.search(r'<div class=\x22footer-main-wrap\x22>.*?</footer>', text, flags=re.DOTALL)
    if not footer_match:
        continue
    
    footer = footer_match.group(0)
    new_footer = footer
    
    for policy in policies:
        policy_html_path = os.path.join(base_dir, 'Policies', policy, 'website', f'{policy}.html')
        # Compute relative path from current file's directory to the policy HTML file
        rel_path = os.path.relpath(policy_html_path, file_dir).replace('\\', '/')
        
        # The footer HTML looks like:
        # <a class="footer-link w-inline-block" href="#">
        # <div class="footer-link-text" href="#">Quality Policy</div>
        # </a>
        # We need to replace href="#" with href="rel_path" ONLY for that specific policy block.
        
        # Regex to find the block for this specific policy
        pattern = rf'(<a class=\x22footer-link w-inline-block\x22) href=\x22[^\x22]*\x22(>\s*<div class=\x22footer-link-text\x22[^>]*>{policy}</div>)'
        new_footer = re.sub(pattern, rf'\1 href="{rel_path}"\2', new_footer)
        
    if new_footer != footer:
        text = text.replace(footer, new_footer)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(text)
        count += 1

print(f"Updated footer policy links in {count} HTML files!")
