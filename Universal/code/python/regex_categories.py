import os
import re

index_path = r"C:\Users\angam\Downloads\Leano Website V1\Index\website\Index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# We will find all instances of `<div class="service-one-title">Title</div>`
# and the preceding `<div class="service-one-category-list">...</div>`
# Wait, the category list comes BEFORE the title!
# Here is the structure:
# <div class="service-one-category-list">
#   <div class="service-one-category">Equipment</div>
#   <div class="service-one-category">Supply</div>
# </div>
# ... image grids ...
# <div class="service-one-title">Fuel Distribution</div>

# A simpler way: just regex replace the categories sequentially.
# The template has 8 category lists (2 sets of 4).
# We can just extract all of them using regex, and replace them in order.

pattern = re.compile(r'(<div class="service-one-category-list">\s*<div class="service-one-category">)(.*?)(</div>\s*<div class="service-one-category">)(.*?)(</div>\s*</div>)')

matches = pattern.findall(content)
# matches will be list of tuples: (prefix, cat1, mid, cat2, suffix)

tags = [
    ("Distribution", "Supply"),
    ("Management", "Monitoring"),
    ("Lubricants", "Industrial"),
    ("Biofuel", "Sustainable")
]

def repl(match):
    global idx
    tag = tags[idx % 4]
    idx += 1
    return match.group(1) + tag[0] + match.group(3) + tag[1] + match.group(5)

idx = 0
new_content = pattern.sub(repl, content)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"Replaced {idx} category lists.")
