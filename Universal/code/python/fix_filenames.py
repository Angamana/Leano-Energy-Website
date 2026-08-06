import os
import re
from glob import glob

root_dir = r"C:\Users\angam\Downloads\Leano Website V1"
html_files = glob(os.path.join(root_dir, "**", "*.html"), recursive=True)

for html_file in html_files:
    if "Old Leano Website" in html_file or "Backup" in html_file:
        continue
        
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Replace the incorrect paths with the correct ones
    # automated-robot-setup-integration.html -> automated-robot-setup-integration-project.html
    # renewable-energy-improvement-models.html -> renewable-energy-improvement-model.html
    
    content = content.replace("automated-robot-setup-integration.html", "automated-robot-setup-integration-project.html")
    content = content.replace("renewable-energy-improvement-models.html", "renewable-energy-improvement-model.html")
    
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(content)

print("Fixed links.")
