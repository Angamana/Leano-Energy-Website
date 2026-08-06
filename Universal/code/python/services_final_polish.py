import os
import re

services_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html"

with open(services_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Hide the Webflow badge
badge_css = """
<style>
/* Forcefully hide the dynamically injected Webflow badge */
.w-webflow-badge {
    display: none !important;
    opacity: 0 !important;
    visibility: hidden !important;
}
</style>
"""
if "Forcefully hide the dynamically injected Webflow badge" not in text:
    text = text.replace("</head>", badge_css + "</head>")

# 2. Add padding/margin to the bottom of the CTA spans
# In my previous script, I used:
# style='color: var(--theme-color); text-decoration: underline; font-weight: bold; cursor: pointer;'
# I will replace this to include display: inline-block; margin-bottom: 30px;
old_style = "style='color: var(--theme-color); text-decoration: underline; font-weight: bold; cursor: pointer;'"
new_style = "style='color: var(--theme-color); text-decoration: underline; font-weight: bold; cursor: pointer; display: inline-block; margin-bottom: 30px;'"

text = text.replace(old_style, new_style)

with open(services_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Updates applied successfully!")
