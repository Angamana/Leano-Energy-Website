import os
import re

base_dir = r"C:\Users\angam\Downloads\Leano Website V1"

favicon_path = os.path.join(base_dir, "Universal", "images", "Leano Energy Logo.png")

for root, _, files in os.walk(base_dir):
    if "Donor" in root: continue
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                    
                # 1. Update Title
                # Extract page name from filename
                page_name = os.path.splitext(file)[0]
                if page_name.lower() == "index":
                    page_name = "Home"
                    
                new_title = f"Leano Energy | {page_name}"
                
                # Replace <title> tag
                content = re.sub(r"<title>.*?</title>", f"<title>{new_title}</title>", content, flags=re.IGNORECASE)
                
                # 2. Update Favicon
                rel_favicon_path = os.path.relpath(favicon_path, root).replace("\\", "/")
                
                # Replace shortcut icon
                content = re.sub(
                    r'<link[^>]*rel="shortcut icon"[^>]*>', 
                    f'<link href="{rel_favicon_path}" rel="shortcut icon" type="image/x-icon" />', 
                    content, 
                    flags=re.IGNORECASE
                )
                
                # Replace apple-touch-icon
                content = re.sub(
                    r'<link[^>]*rel="apple-touch-icon"[^>]*>', 
                    f'<link href="{rel_favicon_path}" rel="apple-touch-icon" />', 
                    content, 
                    flags=re.IGNORECASE
                )
                
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)
                    
                print(f"Updated title and favicon in {file}")
            except Exception as e:
                print(f"Failed on {file}: {e}")
