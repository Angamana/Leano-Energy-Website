import os
import re

about_us_path = r"C:\Users\angam\Downloads\Leano Website V1\About Us\website\About Us.html"

with open(about_us_path, "r", encoding="utf-8") as f:
    text = f.read()

# Remove integrity and crossorigin attributes
text = re.sub(r'\s*integrity="[^"]+"', '', text)
text = re.sub(r'\s*crossorigin="[^"]+"', '', text)

with open(about_us_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Integrity and crossorigin removed!")
