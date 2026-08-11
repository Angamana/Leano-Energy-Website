import os

repo_dir = r"c:\Users\angam\Downloads\Leano Website V1"

old_script = '''<script id="disable-right-click">
        document.addEventListener('contextmenu', event => event.preventDefault());
    </script>'''

new_script = '''<script id="disable-right-click">
document.addEventListener("contextmenu", function(e) {
  e.preventDefault();
}, false);

document.addEventListener("keydown", function(e) {
  // "I" key
  if (e.ctrlKey && e.shiftKey && e.keyCode == 73) {
    e.preventDefault();
  }
  // "J" key
  if (e.ctrlKey && e.shiftKey && e.keyCode == 74) {
    e.preventDefault();
  }
  // "S" key + macOS
  if (e.keyCode == 83 && (navigator.platform.match("Mac") ? e.metaKey : e.ctrlKey)) {
    e.preventDefault();
  }
  // "U" key
  if (e.ctrlKey && e.keyCode == 85) {
    e.preventDefault();
  }
  // "F12" key
  if (e.keyCode == 123) {
    e.preventDefault();
  }
}, false);
</script>'''

html_files = []
for root, _, files in os.walk(repo_dir):
    for f in files:
        if f.lower().endswith('.html'):
            html_files.append(os.path.join(root, f))

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_script in content:
        content = content.replace(old_script, new_script)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file_path}")
    elif '<script id="disable-right-click">' not in content:
        content = content.replace('</body>', f'{new_script}\n</body>')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added to {file_path}")
