import os

services_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html"

with open(services_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the Index script with the Services script
content = content.replace("webflow.f73038d4.86e8628c28dd3a64.js", "webflow.d0509937.b285daf4e1885937.js")

# Revert "Ready to Power Your Journey?" to "Let’s Talk" in the footer title
content = content.replace("Ready to Power Your Journey?", "Let’s Talk")

with open(services_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed scripts and footer text!")
