import os
from glob import glob
from bs4 import BeautifulSoup

root_dir = r"C:\Users\angam\Downloads\Leano Website V1"
html_files = glob(os.path.join(root_dir, "**", "*.html"), recursive=True)

targets = {
    "Home": r"Index\website\Index.html",
    "About Us": r"About Us\website\About Us.html",
    "Pricing Plan": "/pricing-plan",
    "Industries": r"Industries\Industries Main Page\website\Industries Main Page.html",
    "Services": r"Services\website\Services.html",
    "Our Blog": r"Blog\Blog Main Page\website\Blog Main Page.html",
    "Contact": r"Contact Us\website\Contact Us.html"
}

modified_count = 0

for filepath in html_files:
    if "Old Leano Website" in filepath or "Backup" in filepath:
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
        
    # We want to replace the entire <ul role="list" class="nav-menu w-list-unstyled">
    soup = BeautifulSoup(html, 'html.parser')
    nav_ul = soup.find('ul', class_='nav-menu w-list-unstyled')
    if not nav_ul:
        continue
        
    def get_rel(target_key):
        if targets[target_key].startswith("/"):
            return targets[target_key]
        abs_target = os.path.join(root_dir, targets[target_key])
        return os.path.relpath(abs_target, os.path.dirname(filepath)).replace("\\", "/")
        
    def is_curr(target_key):
        if targets[target_key].startswith("/"): return False
        return os.path.abspath(filepath) == os.path.abspath(os.path.join(root_dir, targets[target_key]))

    # Construct the new HTML
    new_nav_html = f'''
<ul role="list" class="nav-menu w-list-unstyled">
    <li class="nav-list">
        <a href="{get_rel("Home")}" class="nav-link small w-inline-block{' w--current' if is_curr('Home') else ''}"{' aria-current="page"' if is_curr('Home') else ''}>
            <div class="nav-text-wrap">
                <div class="nav-text">Home</div>
            </div>
        </a>
    </li>
    <li class="nav-list">
        <div data-delay="0" data-hover="false" class="dropdown-nav w-dropdown">
            <div class="dropdown-toggle w-dropdown-toggle">
                <div class="nav-link small">
                    <div class="nav-text-wrap">
                        <div class="nav-text">Pages</div>
                    </div>
                </div>
                <div class="down-icon w-icon-dropdown-toggle"></div>
            </div>
            <nav class="dropdown-list _w-auto w-dropdown-list">
                <div class="mega-menu-column-wrap">
                    <div class="mega-menu-column">
                        <a href="{get_rel("About Us")}" class="dropdown-link w-dropdown-link{' w--current' if is_curr('About Us') else ''}"{' aria-current="page"' if is_curr('About Us') else ''}>About Us</a>
                        <a href="{get_rel("Pricing Plan")}" class="dropdown-link w-dropdown-link">Pricing Plan</a>
                        <a href="{get_rel("Industries")}" class="dropdown-link w-dropdown-link{' w--current' if is_curr('Industries') else ''}"{' aria-current="page"' if is_curr('Industries') else ''}>Industries</a>
                    </div>
                </div>
            </nav>
        </div>
    </li>
    <li class="nav-list">
        <a href="{get_rel("Services")}" class="nav-link small w-inline-block{' w--current' if is_curr('Services') else ''}"{' aria-current="page"' if is_curr('Services') else ''}>
            <div class="nav-text-wrap">
                <div class="nav-text">Services</div>
            </div>
        </a>
    </li>
    <li class="nav-list">
        <a href="{get_rel("Our Blog")}" class="nav-link small w-inline-block{' w--current' if is_curr('Our Blog') else ''}"{' aria-current="page"' if is_curr('Our Blog') else ''}>
            <div class="nav-text-wrap">
                <div class="nav-text">Our Blog</div>
            </div>
        </a>
    </li>
    <li class="nav-list">
        <a href="{get_rel("Contact")}" class="nav-link small w-inline-block{' w--current' if is_curr('Contact') else ''}"{' aria-current="page"' if is_curr('Contact') else ''}>
            <div class="nav-text-wrap">
                <div class="nav-text">Contact</div>
            </div>
        </a>
    </li>
</ul>
    '''
    
    new_ul_soup = BeautifulSoup(new_nav_html, 'html.parser')
    nav_ul.replace_with(new_ul_soup.ul)
    
    # BeautifulSoup modifies some formatting. We will convert it back to string.
    # Note: Using soup.encode/decode might break Webflow's script tags or entities if not careful.
    # Let's see if we can just string replace the block so we don't rewrite the whole document.
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(str(soup))
        
    modified_count += 1
    print(f"Fixed {filepath}")

print(f"Modified {modified_count} files total.")
