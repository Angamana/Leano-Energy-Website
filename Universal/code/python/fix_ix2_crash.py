import os
import re

services_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html"

with open(services_path, "r", encoding="utf-8") as f:
    text = f.read()

css_inject = """
<style>
/* Override for Webflow IX2 crash caused by adding a 5th tab */
.staticbox-open-content {
    transition: opacity 0.4s ease !important;
}
.w-tab-link.w--current .staticbox-open-content {
    opacity: 1 !important;
    display: flex !important; /* or block depending on layout */
}
.w-tab-link:not(.w--current) .staticbox-open-content {
    opacity: 0 !important;
}
</style>
"""

if "Override for Webflow IX2 crash" not in text:
    text = text.replace("</head>", css_inject + "</head>")

with open(services_path, "w", encoding="utf-8") as f:
    f.write(text)

print("CSS override injected successfully!")
