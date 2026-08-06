from PIL import Image
from collections import Counter

img = Image.open(r"C:\Users\angam\Downloads\Leano Website V1\Universal\images\leano energy logo + Tagline.png")
img = img.convert("RGBA")
data = img.getdata()

# Filter out white, black, transparent, grayscale
colors = []
for r, g, b, a in data:
    if a > 200: # mostly opaque
        if max(r,g,b) - min(r,g,b) > 30: # not grayscale
            colors.append(f"#{r:02x}{g:02x}{b:02x}")
            
counts = Counter(colors)
print("Most common colored pixels in the logo:")
for c, count in counts.most_common(5):
    print(f"  {c} (used {count} times)")
