import os

files = [
    r'Policies\Environmental Policy\website\Environmental Policy.html',
    r'Policies\Privacy Policy\website\Privacy Policy.html',
    r'Policies\Quality Policy\website\Quality Policy.html',
    r'Policies\Safety Policy\website\Safety Policy.html',
    r'Policies\Terms and Conditions\website\Terms and Conditions.html',
    r'News\News Main Page\website\News Main Page.html',
    r'News\News Sub Page 1\website\News Sub Page 1.html',
    r'News\News Sub Page 2\website\News Sub Page 2.html',
    r'News\News Sub Page 3\website\News Sub Page 3.html',
    r'News\News Sub Page 4\website\News Sub Page 4.html',
    r'News\News Sub Page 5\website\News Sub Page 5.html',
    r'News\News Sub Page 6\website\News Sub Page 6.html'
]

css_fix = '''<style id="breadcrumb-bg-fix-css">
    .breadcrumb-bg-wrap {
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        width: 100% !important;
        height: 100% !important;
        overflow: hidden !important;
        z-index: 0 !important;
    }
    .breadcrumb-bg-wrap img.breadcrumb-bg,
    img.breadcrumb-bg {
        width: 100% !important;
        height: 100% !important;
        object-fit: cover !important;
        object-position: center !important;
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        right: 0 !important;
        bottom: 0 !important;
        opacity: 0.35 !important;
    }
</style>
'''

for file_path in files:
    full_path = os.path.join(r'C:\Users\angam\Downloads\Leano Website V1', file_path)
    if os.path.exists(full_path):
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'breadcrumb-bg-fix-css' not in content:
            content = content.replace('</head>', css_fix + '</head>')
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {file_path}")
        else:
            print(f"Already fixed {file_path}")
    else:
        print(f"Not found {file_path}")
