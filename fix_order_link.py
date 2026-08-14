import glob

files = glob.glob(r'News/**/website/*.html', recursive=True)
count = 0
for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix order tab link
    if 'href="../../Order/website/Order.html"' in content:
        content = content.replace('href="../../Order/website/Order.html"', 'href="../../../Order/website/Order.html"')
        
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f"Fixed link in {fpath}")

print(f"Fixed links in {count} files")
