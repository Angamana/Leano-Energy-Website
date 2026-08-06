import os
import re

services_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html"

with open(services_path, "r", encoding="utf-8") as f:
    content = f.read()

# Remove integrity="..." and crossorigin="anonymous"
content = re.sub(r'\s+integrity="[^"]+"', '', content)
content = re.sub(r'\s+crossorigin="anonymous"', '', content)

with open(services_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Stripped integrity and crossorigin attributes!")
