import glob
import os

files_to_modify = [
    'News/News Main Page/website/News Main Page.html',
    'News/News Sub Page 1/website/News Sub Page 1.html',
    'News/News Sub Page 2/website/News Sub Page 2.html',
    'News/News Sub Page 3/website/News Sub Page 3.html',
    'News/News Sub Page 4/website/News Sub Page 4.html',
    'News/News Sub Page 5/website/News Sub Page 5.html',
    'News/News Sub Page 6/website/News Sub Page 6.html'
]

CSS_SNIPPET = '''
<style id="footer-sticky-fix">
  /* Force footer to the bottom of the screen to remove black space */
  html, body {
    height: 100%;
    margin: 0;
  }
  body {
    display: flex;
    flex-direction: column;
  }
  .footer-section, footer {
    margin-top: auto;
  }
</style>
'''

count = 0
for filepath in files_to_modify:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'id="footer-sticky-fix"' not in content:
            # Insert just before </head>
            if '</head>' in content:
                content = content.replace('</head>', CSS_SNIPPET + '</head>')
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
                
print(f"Added sticky footer CSS to {count} files.")
