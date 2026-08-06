import os
import re

index_path = r"C:\Users\angam\Downloads\Leano Website V1\Index\website\Index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace "1995" with "2016" in the "WE ARE SINCE" section
content = content.replace("1995", "2016")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Year updated successfully!")
