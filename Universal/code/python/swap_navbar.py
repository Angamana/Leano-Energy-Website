import os
import re

def get_navbar_block(content):
    # Find start index of the div containing "navbar w-nav"
    match = re.search(r'<div[^>]*class="[^"]*navbar w-nav[^"]*"[^>]*>', content)
    if not match:
        return -1, -1
        
    start_index = match.start()
        
    # Find matching closing div
    open_divs = 0
    i = start_index
    while i < len(content):
        if content[i:i+4] == '<div':
            open_divs += 1
            i += 4
        elif content[i:i+6] == '</div>':
            open_divs -= 1
            if open_divs == 0:
                return start_index, i + 6
            i += 6
        else:
            i += 1
    return -1, -1

index_path = r"C:\Users\angam\Downloads\Leano Website V1\Index\website\Index.html"
services_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html"

with open(index_path, "r", encoding="utf-8") as f:
    index_content = f.read()

with open(services_path, "r", encoding="utf-8") as f:
    services_content = f.read()

idx_start, idx_end = get_navbar_block(index_content)
if idx_start != -1:
    index_navbar = index_content[idx_start:idx_end]
    print("Found navbar in Index.html")
    
    srv_start, srv_end = get_navbar_block(services_content)
    if srv_start != -1:
        print("Found navbar in Services.html, replacing...")
        new_services_content = services_content[:srv_start] + index_navbar + services_content[srv_end:]
        with open(services_path, "w", encoding="utf-8") as f:
            f.write(new_services_content)
        print("Success! Navbar replaced.")
    else:
        print("Could not find navbar in Services.html")
else:
    print("Could not find navbar in Index.html")
