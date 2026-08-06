import re
import os
from glob import glob

root_dir = r"C:\Users\angam\Downloads\Leano Website V1"
html_files = glob(os.path.join(root_dir, "**", "*.html"), recursive=True)

home_pattern = re.compile(
    r'(<li class="nav-list">\s*<div[^>]*class="dropdown-nav w-dropdown"[^>]*>.*?<div (?:href="#")?\s*class="nav-text">Home</div>.*?<nav class="dropdown-list _12 w-dropdown-list">\s*<a href="([^"]+)".*?</nav>\s*</div>\s*</li>)', 
    re.DOTALL
)

def home_replacer(match):
    target_link = match.group(2)
    return f'''<li class="nav-list">
                                        <a href="{target_link}" class="nav-link small w-inline-block">
                                            <div class="nav-text-wrap">
                                                <div class="nav-text">Home</div>
                                            </div>
                                        </a>
                                    </li>'''

pages_pattern = re.compile(
    r'(<nav class="dropdown-list _w-auto w-dropdown-list">\s*<div class="mega-menu-column-wrap">\s*<div class="mega-menu-column">).*?(<a href="[^"]+" class="dropdown-link w-dropdown-link">About Us</a>).*?(<a href="[^"]+" class="dropdown-link w-dropdown-link">Pricing Plan</a>).*?(<a[^>]*href="[^"]+" class="dropdown-link w-dropdown-link">)Projects(</a>).*?</div>\s*<div class="mega-menu-column">.*?</div>\s*</div>\s*</nav>',
    re.DOTALL
)

def pages_replacer(match):
    return f'{match.group(1)}\n                                                        {match.group(2)}\n                                                        {match.group(3)}\n                                                        {match.group(4)}Industries{match.group(5)}\n                                                    </div>\n                                                </div>\n                                            </nav>'

modified_count = 0

for filepath in html_files:
    if "Old Leano Website" in filepath or "Backup" in filepath:
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    original = content
    content = home_pattern.sub(home_replacer, content)
    content = pages_pattern.sub(pages_replacer, content)
    
    if original != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        modified_count += 1
        print(f"Modified {filepath}")

print(f"Modified {modified_count} files total.")
