import os
import re

html_path = r"C:\Users\angam\Downloads\Leano Website V1\Services\website\Services.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# The Team section starts with <section ... and ends with </section>. 
# Inside it, we know there's text like "Become Part Of Our Team" or "team-one w-dyn-list"
team_pattern = re.compile(r'<section [^>]*>.*?Become Part Of Our Team.*?</section>', re.DOTALL | re.IGNORECASE)
content = team_pattern.sub('', content)

# The Process section ends right before <footer class="footer">, let's see. 
# Inside it, there's text "Diverse Building Applications" and "Process" 
process_pattern = re.compile(r'<section [^>]*>.*?Diverse Building Applications.*?</section>', re.DOTALL | re.IGNORECASE)
content = process_pattern.sub('', content)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Irrelevant sections (Team and Process) removed successfully from Services page.")
