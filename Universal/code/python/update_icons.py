import os
import re

index_path = r"C:\Users\angam\Downloads\Leano Website V1\Index\website\Index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the 4 trust indicator icon texts
content = content.replace("We are certified company", "Level 1 BBBEE Contributor: 100% Black Youth Owned")
content = content.replace("We are bring quality services", "Authorized Distributor: Sasol, Shell, BP, Engen & Chevron")
content = content.replace("Engineering project study &amp; solution", "Serving Gauteng, Mpumalanga, Limpopo & North West")
content = content.replace("Engineering project study & solution", "Serving Gauteng, Mpumalanga, Limpopo & North West")
content = content.replace("Raw Materials Transportation", "Fuel Management: 99% Accuracy or Better")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Icon strip updated successfully!")
