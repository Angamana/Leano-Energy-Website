import re

path = r'C:\Users\angam\Downloads\Leano Website V1\Industries\Industries Sub Page 1\website\Industries Sub Page 1.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the left and right columns
# We will find `<div class="w-layout-grid project-detail-grid">` and replace its inner HTML 
# but it's not a grid, it's `w-row`. Let's just find the columns.

# Left column: <div class="project-details-left-column ..."> ... </div></div></div>
# Right column: <div class="project-details-right-column ..."> ... </div>

# Let's just replace the whole row content.
# The row usually has `<div class="project-details-row w-row">` or similar. Let's find it.
m = re.search(r'<div class="w-row">.*?<div class="project-details-left-column', text, flags=re.DOTALL)
if not m:
    # Just look for the left column
    pass

# We can replace the left column with empty string
text = re.sub(r'<div class="project-details-left-column[^>]*>.*?<!-- end of left column if we could match it -->', '', text, flags=re.DOTALL) 
# Too risky with regex DOTALL. 

# Safer: parse the HTML structure or use a precise regex boundary.
