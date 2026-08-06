import os

path = r"C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Put back the generator tag in the head
if '<meta content="Webflow" name="generator" />' not in content:
    content = content.replace('<head>', '<head>\n    <meta content="Webflow" name="generator" />')

# Put back the data-wf-domain attribute on the html tag
if 'data-wf-domain=' not in content:
    content = content.replace('<html ', '<html data-wf-domain="induyst.webflow.io" ')

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Restored critical Webflow JS initialization markers.")
