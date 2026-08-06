import re
import os

filepath = r"C:\Users\angam\Downloads\Leano Website V1\Index\website\Index.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

home_pattern = re.compile(
    r'<li class="nav-list">\s*<div[^>]*class="dropdown-nav w-dropdown"[^>]*>.*?<div href="#" class="nav-text">Home</div>.*?<nav class="dropdown-list _12 w-dropdown-list">\s*<a href="([^"]+)".*?</nav>\s*</div>\s*</li>', 
    re.DOTALL
)

match = home_pattern.search(content)
if match:
    print("MATCHED HOME!")
    print("Target link:", match.group(1))
    
    # We want to replace it with:
    # <li class="nav-list">
    #     <a href="{match.group(1)}" class="nav-link small w-inline-block">
    #         <div class="nav-text-wrap">
    #             <div class="nav-text">Home</div>
    #         </div>
    #     </a>
    # </li>
else:
    print("NO MATCH FOR HOME")

pages_pattern = re.compile(
    r'(<nav class="dropdown-list _w-auto w-dropdown-list">\s*<div class="mega-menu-column-wrap">\s*<div class="mega-menu-column">).*?(<a href="([^"]+)" class="dropdown-link w-dropdown-link">About Us</a>).*?(<a href="([^"]+)" class="dropdown-link w-dropdown-link">Pricing Plan</a>).*?(<a[^>]*href="([^"]+)" class="dropdown-link w-dropdown-link">Projects</a>).*?</div>\s*<div class="mega-menu-column">.*?</div>\s*</div>\s*</nav>)',
    re.DOTALL
)

pmatch = pages_pattern.search(content)
if pmatch:
    print("MATCHED PAGES!")
else:
    print("NO MATCH FOR PAGES")
