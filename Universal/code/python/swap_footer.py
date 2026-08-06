import os
import re

def get_footer_block(content):
    # Find start index of the footer tag
    match = re.search(r'<footer[^>]*>', content)
    if not match:
        return -1, -1
        
    start_index = match.start()
        
    # Find matching closing footer
    # Since footer is a distinct tag, we can just look for </footer>
    # Wait, the footer could contain nested elements, but </footer> is unique unless there are multiple footers
    end_index = content.find('</footer>', start_index)
    if end_index != -1:
        return start_index, end_index + 9 # len('</footer>')
        
    return -1, -1

index_path = r"C:\Users\angam\Downloads\Leano Website V1\Index\website\Index.html"
services_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html"

with open(index_path, "r", encoding="utf-8") as f:
    index_content = f.read()

with open(services_path, "r", encoding="utf-8") as f:
    services_content = f.read()

idx_start, idx_end = get_footer_block(index_content)
if idx_start != -1:
    index_footer = index_content[idx_start:idx_end]
    print("Found footer in Index.html")
    
    srv_start, srv_end = get_footer_block(services_content)
    if srv_start != -1:
        print("Found footer in Services.html, replacing...")
        new_services_content = services_content[:srv_start] + index_footer + services_content[srv_end:]
        with open(services_path, "w", encoding="utf-8") as f:
            f.write(new_services_content)
        print("Success! Footer replaced.")
    else:
        print("Could not find footer in Services.html")
else:
    print("Could not find footer in Index.html")
