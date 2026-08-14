from bs4 import BeautifulSoup
import glob
import re
import os

main_page_path = r'News/News Main Page/website/News Main Page.html'
with open(main_page_path, 'r', encoding='utf-8') as f:
    main_soup = BeautifulSoup(f.read(), 'html.parser')

blog_list_to_copy = main_soup.find('div', class_='blog-two-list')
if not blog_list_to_copy:
    print("Could not find blog list in main page!")
    exit(1)

all_items = blog_list_to_copy.find_all('div', class_='blog-two-item', recursive=False)
print(f"Found {len(all_items)} articles in main page.")

sub_pages = glob.glob(r'News/News Sub Page */website/News Sub Page *.html')
for sub_page in sub_pages:
    # determine the sub page number from filename
    match = re.search(r'News Sub Page (\d+)', os.path.basename(sub_page))
    if not match:
        continue
    page_num = match.group(1)
    
    # filter out the item that points to this sub page
    items_to_keep = []
    for item in all_items:
        # check the link href
        link = item.find('a', class_='blog-two-link')
        if link and f'News Sub Page {page_num}' in link.get('href', ''):
            continue # skip the current page's article
        items_to_keep.append(item)
    
    # keep only 3
    items_to_keep = items_to_keep[:3]
    
    with open(sub_page, 'r', encoding='utf-8') as f:
        sub_soup = BeautifulSoup(f.read(), 'html.parser')
    
    target_blog_list = sub_soup.find('div', class_='blog-two-list')
    if target_blog_list:
        target_blog_list.clear()
        for item in items_to_keep:
            # We must copy the item so it's not removed from original list
            import copy
            target_blog_list.append(copy.copy(item))
            # Also add a newline for formatting if we want
            target_blog_list.append('\n')
            
        # Write back
        with open(sub_page, 'w', encoding='utf-8') as f:
            f.write(str(sub_soup))
        print(f"Updated {sub_page} with {len(items_to_keep)} articles.")
    else:
        print(f"Could not find blog list in {sub_page}")
