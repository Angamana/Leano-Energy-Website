import os
import re

base_dir = r"C:\Users\angam\Downloads\Leano Website V1\Industries"

data = {
    1: {
        "old_cat": "Automation",
        "old_title": "Technological solutions for factories",
        "new_cat": "Mining",
        "new_title": "Reliable fuel supply and management solutions to keep heavy mining machinery running."
    },
    2: {
        "old_cat": "Engineering",
        "old_title": "Clean energy efficiency development",
        "new_cat": "Agriculture",
        "new_title": "Timely fuel and lubricant solutions for farms and agricultural operations."
    },
    3: {
        "old_cat": "Industrial",
        "old_title": "Industrial technology research",
        "new_cat": "Logistics & Transport",
        "new_title": "Bulk diesel and fuel management to keep logistics fleets moving reliably."
    },
    4: {
        "old_cat": "Technology",
        "old_title": "Sustainable process design concept",
        "new_cat": "Airports",
        "new_title": "Specialized aviation fuel solutions for airports and aviation operations."
    },
    5: {
        "old_cat": "Engineering",
        "old_title": "Automated robot setup integration project",
        "new_cat": "Factories & Manufacturing",
        "new_title": "Industrial diesel, oils, and lubricants for factories and manufacturing plants."
    },
    6: {
        "old_cat": "Industrial",
        "old_title": "Renewable energy improvement model",
        "new_cat": "Municipalities",
        "new_title": "Reliable fuel supply and management for municipal fleets and operations."
    }
}

# 1. Update Industries Main Page.html
main_page_path = os.path.join(base_dir, "Industries Main Page", "website", "Industries Main Page.html")
with open(main_page_path, "r", encoding="utf-8") as f:
    main_content = f.read()

# Since some old categories repeat (Engineering, Industrial), we can't do a blind global replace.
# We must replace within the specific cards. The cards link to sub page X.
for i in range(1, 7):
    # Find the link block for this sub page
    pattern = r'(<a[^>]*href="\.\./\.\./Industries Sub Page ' + str(i) + r'/website/Industries Sub Page ' + str(i) + r'\.html".*?</a>)'
    def repl(m):
        block = m.group(1)
        # Replace category
        block = re.sub(r'(class="category[^"]*"[^>]*>)[^<]+(</div>)', r'\g<1>' + data[i]["new_cat"] + r'\g<2>', block, flags=re.IGNORECASE)
        # Replace title
        block = re.sub(r'(class="project-one-title[^"]*"[^>]*>)[^<]+(</h3>)', r'\g<1>' + data[i]["new_title"] + r'\g<2>', block, flags=re.IGNORECASE)
        return block
    
    main_content = re.sub(pattern, repl, main_content, flags=re.DOTALL | re.IGNORECASE)

with open(main_page_path, "w", encoding="utf-8") as f:
    f.write(main_content)
print("Updated Industries Main Page.html")

# 2. Update the Sub Pages
for i in range(1, 7):
    sub_page_path = os.path.join(base_dir, f"Industries Sub Page {i}", "website", f"Industries Sub Page {i}.html")
    if os.path.exists(sub_page_path):
        with open(sub_page_path, "r", encoding="utf-8") as f:
            sub_content = f.read()
            
        # Update <title>
        # The previous script made it <title>Leano Energy | Industries Sub Page X</title>
        sub_content = re.sub(r'<title>.*?</title>', f'<title>Leano Energy | {data[i]["new_cat"]}</title>', sub_content, flags=re.IGNORECASE)
        
        # Replace old category globally in this file (e.g., breadcrumbs, headings)
        # We must be careful if old_cat is a common word, but in this context it's fine.
        # Actually, let's just replace exact string occurrences
        sub_content = sub_content.replace("Automation", "Mining")
        # For others, we only replace exactly the old_cat
        # Wait, if we globally replace "Engineering" it might break things.
        # Let's replace only inside HTML tags that contain the exact text.
        sub_content = re.sub(r'(>)\s*' + re.escape(data[i]["old_cat"]) + r'\s*(</)', r'\1' + data[i]["new_cat"] + r'\2', sub_content, flags=re.IGNORECASE)
        
        # Replace old title globally
        sub_content = sub_content.replace(data[i]["old_title"], data[i]["new_title"])
        sub_content = sub_content.replace(data[i]["old_title"].strip(), data[i]["new_title"])
        
        # In case there are stray spaces
        old_title_clean = re.sub(r'\s+', ' ', data[i]["old_title"]).strip()
        sub_content = re.sub(r'(>)\s*' + re.escape(old_title_clean) + r'\s*(</)', r'\1' + data[i]["new_title"] + r'\2', sub_content, flags=re.IGNORECASE)

        with open(sub_page_path, "w", encoding="utf-8") as f:
            f.write(sub_content)
        print(f"Updated Industries Sub Page {i}.html")
