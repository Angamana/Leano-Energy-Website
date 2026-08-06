import os

base_dir = r"C:\Users\angam\Downloads\Leano Website V1"

badge_css = """
<style>
/* Forcefully hide the dynamically injected Webflow badge */
.w-webflow-badge {
    display: none !important;
    opacity: 0 !important;
    visibility: hidden !important;
}
</style>
"""

count = 0
for root, _, files in os.walk(base_dir):
    # skip Donor folder
    if "Donor" in root:
        continue
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    text = f.read()
                
                if "Forcefully hide the dynamically injected Webflow badge" not in text:
                    text = text.replace("</head>", badge_css + "</head>")
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(text)
                    count += 1
            except Exception as e:
                print(f"Error on {file_path}: {e}")

print(f"Removed Webflow badge from {count} HTML files globally!")
