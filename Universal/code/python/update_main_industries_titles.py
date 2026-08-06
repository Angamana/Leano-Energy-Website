import re

main_page_path = r'C:\Users\angam\Downloads\Leano Website V1\Industries\Industries Main Page\website\Industries Main Page.html'
with open(main_page_path, 'r', encoding='utf-8') as f:
    text = f.read()

data = {
    1: 'Reliable fuel supply and management solutions to keep heavy mining machinery running.',
    2: 'Timely fuel and lubricant solutions for farms and agricultural operations.',
    3: 'Bulk diesel and fuel management to keep logistics fleets moving reliably.',
    4: 'Specialized aviation fuel solutions for airports and aviation operations.',
    5: 'Industrial diesel, oils, and lubricants for factories and manufacturing plants.',
    6: 'Reliable fuel supply and management for municipal fleets and operations.'
}

old_titles = {
    1: r'Technological solutions for factories\s*',
    2: r'Clean energy efficiency development\s*',
    3: r'Industrial technology research\s*',
    4: r'Sustainable process design concept\s*',
    5: r'Automated robot setup integration project\s*',
    6: r'Renewable energy improvement model\s*'
}

for i in range(1, 7):
    # Find the entire <a> block for this card
    pattern = r'(<a[^>]*href="\.\./\.\./Industries Sub Page ' + str(i) + r'/website/Industries Sub Page ' + str(i) + r'\.html".*?</a>)'
    def repl(m):
        block = m.group(1)
        block = re.sub(old_titles[i], data[i], block, flags=re.IGNORECASE)
        return block
    text = re.sub(pattern, repl, text, flags=re.DOTALL | re.IGNORECASE)

with open(main_page_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Titles in Industries Main Page updated!')
