import os
import glob
import shutil
import re

base_dir = r'C:\Users\angam\Downloads\Leano Website V1'

# 1. Rename files and folders
blog_dir = os.path.join(base_dir, 'Blog')
news_dir = os.path.join(base_dir, 'News')

if os.path.exists(blog_dir):
    os.rename(blog_dir, news_dir)

# Recursively rename folders containing "Blog"
for root, dirs, files in os.walk(news_dir, topdown=False):
    for dir_name in dirs:
        if 'Blog' in dir_name:
            new_dir_name = dir_name.replace('Blog', 'News')
            os.rename(os.path.join(root, dir_name), os.path.join(root, new_dir_name))
            
for root, dirs, files in os.walk(news_dir, topdown=False):
    for file_name in files:
        if 'Blog' in file_name:
            new_file_name = file_name.replace('Blog', 'News')
            os.rename(os.path.join(root, file_name), os.path.join(root, new_file_name))

print("Renamed files and folders in News directory.")

# 2. Update HTML content in ALL HTML files
html_files = glob.glob(os.path.join(base_dir, '**', '*.html'), recursive=True)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Update paths inside hrefs and other attributes
    # The paths look like ../../../Blog/Blog Main Page/website/Blog Main Page.html
    # We will replace any string 'Blog' if it's part of a path or visible text we want to target.
    
    # Safe replacements for paths
    text = text.replace('/Blog/', '/News/')
    text = text.replace('Blog Main Page', 'News Main Page')
    text = text.replace('Blog Sub Page', 'News Sub Page')
    
    # Update navigation text
    # Usually it's <div class="nav-text">Our Blog</div> or similar
    text = text.replace('>Our Blog<', '>News<')
    
    # Wait, the breadcrumb or title might have "Blog".
    text = text.replace('<title>Blog', '<title>News')
    text = text.replace('Blog | Leano Energy', 'News | Leano Energy')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(text)

print("Updated links and text across all HTML files.")
