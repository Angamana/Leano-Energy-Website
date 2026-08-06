import os
import re

index_path = r"C:\Users\angam\Downloads\Leano Website V1\Index\website\Index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Shorten the long headline on Slide 1
content = content.replace("Fueling Successful Journeys, Delivering Energy That Powers South Africa", "Fueling Successful Journeys")

# Replace instances of "Bulk Fuel" with "Fuel" where appropriate to shorten
content = content.replace("Bulk Fuel Distributors", "Fuel Distributors")
content = content.replace("Bulk Fuel Distribution", "Fuel Distribution")
# Also the about us text: "We supply bulk fuels..."
content = content.replace("supply bulk fuels", "supply fuels")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Text shortened successfully!")
