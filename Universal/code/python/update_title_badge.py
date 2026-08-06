import os
import re

html_files = [
    "Index/website/index.html",
    "About Us/website/about-us.html",
    "Services/website/services.html",
    "Blog/website/blog.html",
    "Contact Us/website/contact.html"
]

style_injection = "\n    <style>.w-webflow-badge { display: none !important; }</style>\n"

for html_file in html_files:
    if not os.path.exists(html_file):
        print(f"Not found: {html_file}")
        continue
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Update Title
    content = re.sub(r'<title>.*?</title>', '<title>Leano Energy</title>', content, flags=re.IGNORECASE)

    # Inject CSS to hide badge if not already there
    if ".w-webflow-badge { display: none !important; }" not in content:
        content = content.replace("</head>", f"{style_injection}</head>")

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(content)

print("Title and Badge updates complete.")
