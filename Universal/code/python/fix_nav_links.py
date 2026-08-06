import re

services_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html"

with open(services_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find the navbar block
match = re.search(r'<div[^>]*class="[^"]*navbar w-nav[^"]*"[^>]*>', content)
if match:
    start_index = match.start()
    
    # Find matching closing div
    open_divs = 0
    i = start_index
    end_index = -1
    while i < len(content):
        if content[i:i+4] == '<div':
            open_divs += 1
            i += 4
        elif content[i:i+6] == '</div>':
            open_divs -= 1
            if open_divs == 0:
                end_index = i + 6
                break
            i += 6
        else:
            i += 1
            
    if end_index != -1:
        navbar = content[start_index:end_index]
        
        # Replace href="Index.html" with href="../../Index/website/Index.html"
        navbar = navbar.replace('href="Index.html"', 'href="../../Index/website/Index.html"')
        
        # Replace href="/pricing-plan" with "#" or Pricing page if exists
        navbar = navbar.replace('href="/pricing-plan"', 'href="#"')
        
        # The other links were already absolute relative paths starting with ../../
        # so they should correctly resolve from Services/website/ as well.
        
        # Now place it back
        content = content[:start_index] + navbar + content[end_index:]
        
        with open(services_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated navbar links.")
    else:
        print("Could not find end of navbar.")
else:
    print("Could not find navbar.")
