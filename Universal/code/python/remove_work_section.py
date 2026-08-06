import os

index_path = r"C:\Users\angam\Downloads\Leano Website V1\Index\website\Index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find the index of "project-title"
start_idx = content.find("project-title")

if start_idx != -1:
    # Find the preceding "<section"
    section_start = content.rfind("<section", 0, start_idx)
    
    # We need to find the matching closing "</section>". 
    # Since we don't have a full HTML parser, we will count nested sections, though typically sections aren't nested in this layout.
    # We'll just find the next "</section>" after start_idx
    # Wait, the section could contain other sections? Usually not. Let's just find the next "</section>".
    
    section_end = content.find("</section>", start_idx)
    
    if section_start != -1 and section_end != -1:
        # Include the closing tag length
        section_end += len("</section>")
        
        # Remove the section
        new_content = content[:section_start] + content[section_end:]
        
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Section removed successfully!")
    else:
        print("Could not find section boundaries.")
else:
    print("Could not find project-title.")
