import os
import re

index_path = r"C:\Users\angam\Downloads\Leano Website V1\Index\website\Index.html"
about_path = r"C:\Users\angam\Downloads\Leano Website V1\About Us\website\About Us.html"

# Read Index
with open(index_path, "r", encoding="utf-8") as f:
    index_text = f.read()

# Read About Us
with open(about_path, "r", encoding="utf-8") as f:
    about_text = f.read()

# Extract header and footer from Index
header_match = re.search(r'<header.*?</header>', index_text, flags=re.DOTALL)
footer_match = re.search(r'<footer.*?</footer>', index_text, flags=re.DOTALL)

if header_match and footer_match:
    index_header = header_match.group(0)
    index_footer = footer_match.group(0)
    
    # Replace in About Us
    about_text = re.sub(r'<header.*?</header>', index_header, about_text, flags=re.DOTALL)
    about_text = re.sub(r'<footer.*?</footer>', index_footer, about_text, flags=re.DOTALL)
    
    with open(about_path, "w", encoding="utf-8") as f:
        f.write(about_text)
        
    print("Nav and Footer injected successfully!")
else:
    print("Failed to find header or footer in Index.html")
