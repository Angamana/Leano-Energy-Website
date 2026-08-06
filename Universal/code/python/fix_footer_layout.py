import os
import glob
import re

base_dir = r'C:\Users\angam\Downloads\Leano Website V1'
html_files = glob.glob(os.path.join(base_dir, '**', '*.html'), recursive=True)

count_contact_now = 0
count_safety_policy = 0
count_newsletter_move = 0

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    modified = False
    
    # 1. Change "Call Us: 010 442 4895" to "CONTACT NOW"
    if 'Call Us: 010 442 4895' in text:
        text = text.replace('Call Us: 010 442 4895', 'CONTACT NOW')
        count_contact_now += 1
        modified = True
        
    # 2. Change "Health &amp; Safety Policy" to "Safety Policy"
    if 'Health &amp; Safety Policy' in text:
        text = text.replace('Health &amp; Safety Policy', 'Safety Policy')
        count_safety_policy += 1
        modified = True
    elif 'Health & Safety Policy' in text:
        text = text.replace('Health & Safety Policy', 'Safety Policy')
        count_safety_policy += 1
        modified = True

    # 3. Move Newsletter Subscription into footer-block-wrap
    # The current pattern is `</div>\s*<div class="footer-column last"` 
    # which implies `footer-block-wrap` was closed right before `footer-column last`.
    # We want to remove that closing `</div>` and place it AFTER the `footer-column last` div.
    
    # Let's search for:
    # </div>
    # <div class="footer-column last" id="w-node-c5b0ccc7-036a-436e-de2b-724dbf0b4440-8ec1389c">
    pattern = r'</div>(\s*<div class="footer-column last".*?</div>\s*</div>)'
    # Wait, the structure of footer-column last is:
    # <div class="footer-column last" ...>
    #   <div class="footer-title-wrap">...</div>
    #   <div class="footer-line contact-info">...</div>
    # </div>
    # So it has 2 nested divs (footer-title-wrap and footer-line), and then closes itself.
    # We can match `</div>\s*<div class="footer-column last"` exactly.
    # And we know `footer-column last` has its own closing `</div>`.
    
    # A safer regex replacement:
    # Find `</div>` followed by `<div class="footer-column last"`
    move_pattern = r'</div>\s*(<div class="footer-column last" [^>]*>.*?(?:</div>\s*){3})'
    # Wait, `.*?` might consume too much.
    
    # Let's be very explicit:
    # We know the HTML snippet exactly from our dump:
    # </div>
    # <div class="footer-column last" id="w-node-c5b0ccc7-036a-436e-de2b-724dbf0b4440-8ec1389c">
    # ...
    # </div>
    # </div>
    # </div>
    
    # Let's just find the string:
    # `</div>\n<div class="footer-column last"`
    # or `</div>\r\n<div class="footer-column last"`
    
    if re.search(r'</div>\s*<div class="footer-column last"', text):
        # We replace `</div>\s*<div class="footer-column last"` with `\n<div class="footer-column last"`
        # Then we must insert `</div>` at the end of the `footer-column last` div.
        # But where is the end? 
        # The `footer-column last` div is closed by the first `</div>` that brings the div depth to 0, or roughly:
        # <div class="footer-column last" ...>
        #   <div class="footer-title-wrap"> ... </div>
        #   <div class="footer-line contact-info"> ... </div>
        # </div>
        
        # Actually, let's use a simpler approach. We know the `footer-main` div ends right after it.
        # Original:
        # </div> <!-- closes footer-block-wrap -->
        # <div class="footer-column last" ...>
        #    ...
        # </div> <!-- closes footer-column last -->
        # </div> <!-- closes footer-main -->
        
        # We want:
        # <div class="footer-column last" ...>
        #    ...
        # </div> <!-- closes footer-column last -->
        # </div> <!-- closes footer-block-wrap -->
        # </div> <!-- closes footer-main -->
        
        # Notice that in both cases, the number of closing `</div>`s at the end is the same!
        # It's literally just deleting the `</div>` before `<div class="footer-column last"` 
        # and inserting an extra `</div>` after the `footer-column last` block.
        # Which effectively means we are just moving the `</div>` from BEFORE the block to AFTER the block.
        
        # Regex to capture the block:
        # `</div>\s*(<div class="footer-column last".*?</div>\s*</div>)`
        # No, wait. 
        # `<div class="footer-column last"` contains `</div>` for title wrap, `</div>` for contact info, and then `</div>` to close itself.
        
        # Let's do string replacement for the start:
        text = re.sub(r'</div>(\s*<div class="footer-column last")', r'\1', text, count=1)
        # Now we need to add `</div>` after the footer-column last.
        # The footer-column last block looks like:
        # <div class="footer-line contact-info"><a ...>...</a></div>
        # </div> <!-- closes footer-column last -->
        # </div> <!-- closes footer-main -->
        # We want to change the end to:
        # </div> <!-- closes footer-column last -->
        # </div> <!-- closes footer-block-wrap -->
        # </div> <!-- closes footer-main -->
        
        # Let's find `</footer>` and add a `</div>` before it? No, there are other wrappers like `footer-main-wrap`.
        
        # Let's find:
        # <div class="footer-title">Newsletter Subscription</div>
        # </div>
        # <div class="footer-line contact-info">.*?</div>
        # </div>
        # We will append `\n</div>` right after that last `</div>`.
        
        pattern_end = r'(<div class="footer-title">Newsletter Subscription</div>\s*</div>\s*<div class="footer-line[^>]*>.*?</div>\s*</div>)'
        text = re.sub(pattern_end, r'\1\n</div>', text, flags=re.DOTALL)
        
        count_newsletter_move += 1
        modified = True
        
    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(text)

print(f"Updated 'CONTACT NOW' in {count_contact_now} files.")
print(f"Updated 'Safety Policy' in {count_safety_policy} files.")
print(f"Moved Newsletter Subscription in {count_newsletter_move} files.")
