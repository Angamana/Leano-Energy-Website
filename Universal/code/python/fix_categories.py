import os
import re

index_path = r"C:\Users\angam\Downloads\Leano Website V1\Index\website\Index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# I will split the content by "service-one-content-wrapper" to isolate each card.
# The template might repeat the 4 cards multiple times, so there might be 8 or 12 blocks.
# A safer way: find the category list right before the image grid, and since the cards follow a specific order (Card 1, Card 2, Card 3, Card 4), I can keep track of a counter modulo 4.

blocks = content.split('<div class="service-one-category-list">')
new_content = blocks[0]

# The order of cards in the HTML: 
# 1. Fuel Distribution
# 2. Fuel Management Solutions
# 3. Complete Oil and Lubricant Solutions
# 4. Biofuel & Sustainable Energy

tags = [
    ["Distribution", "Supply"],
    ["Management", "Monitoring"],
    ["Lubricants", "Industrial"],
    ["Biofuel", "Sustainable"]
]

tag_index = 0
for i in range(1, len(blocks)):
    block = blocks[i]
    # Find the end of the category list
    end_idx = block.find('</div>\n  </div>\n  <div class="w-layout-grid service-one-image-grid">')
    if end_idx == -1:
        end_idx = block.find('</div>\n  </div>\n  <div class="w-layout-grid') # Try a more generic match
    
    if end_idx != -1:
        # We found a category list to replace
        current_tags = tags[tag_index % 4]
        
        replacement = f'\n  <div class="service-one-category">{current_tags[0]}</div>\n  <div class="service-one-category">{current_tags[1]}</div>\n  '
        
        # Replace the contents
        block = replacement + block[end_idx:]
        
        tag_index += 1
    
    new_content += '<div class="service-one-category-list">' + block

with open(index_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Categories updated successfully!")
