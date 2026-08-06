import os
import glob

base_dir = r'C:\Users\angam\Downloads\Leano Website V1'
html_files = glob.glob(os.path.join(base_dir, '**', '*.html'), recursive=True)

count = 0
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # We need to replace Blog%20 with News%20
    new_text = text.replace('Blog%20Main%20Page', 'News%20Main%20Page')
    new_text = new_text.replace('Blog%20Sub%20Page', 'News%20Sub%20Page')
    
    # Also if there are any other missed Blog words in paths, like href="...Blog..."
    
    if new_text != text:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_text)
        count += 1

print(f"Updated {count} HTML files to fix the broken CSS styling links!")
