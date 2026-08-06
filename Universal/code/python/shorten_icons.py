import os

index_path = r"C:\Users\angam\Downloads\Leano Website V1\Index\website\Index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("Level 1 BBBEE Contributor: 100% Black Youth Owned", "Level 1 BBBEE Contributor")
content = content.replace("Authorized Distributor: Sasol, Shell, BP, Engen & Chevron", "Authorized Premium Distributor")
content = content.replace("Serving Gauteng, Mpumalanga, Limpopo & North West", "Serving 4 Major Provinces")
content = content.replace("Fuel Management: 99% Accuracy or Better", "99% Management Accuracy")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Icons text shortened successfully!")
