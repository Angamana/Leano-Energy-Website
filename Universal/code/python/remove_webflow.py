import os
import re

services_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html"

with open(services_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Strip the HTML comment
content = re.sub(r'<!-- This site was created in Webflow\. https://webflow\.com -->\n?', '', content)

# 2. Strip generator meta tag
content = re.sub(r'<meta content="Webflow" name="generator" />\n?', '', content)

# 3. Strip data-wf-domain
content = re.sub(r'\s*data-wf-domain="[^"]+"', '', content)

# 4. Change Titles and metadata
content = content.replace('Induyst - Webflow HTML website template', 'Leano')

# 5. Change "Powered by Webflow" in footer
content = re.sub(r'Powered by <a href="https://webflow\.com/"\s*class="footer-small-link-text-link">Webflow</a>', 'Powered by Leano', content)

# 6. Change induyst.webflow.io links to '#'
content = content.replace('https://induyst.webflow.io/404', '#')

# 7. Update JS script references from 'webflow.*.js' to 'leano.*.js'
content = content.replace('/js/webflow.schunk.', '/js/leano.schunk.')
content = content.replace('/js/webflow.d050', '/js/leano.d050')

with open(services_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Removed webflow traces from Services.html")
