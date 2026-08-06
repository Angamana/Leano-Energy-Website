import os

about_us_path = r"C:\Users\angam\Downloads\Leano Website V1\About Us\website\About Us.html"

with open(about_us_path, "r", encoding="utf-8") as f:
    text = f.read()

# Add a CSS rule to hide the Webflow badge
css_hide_badge = '<style>.w-webflow-badge { display: none !important; visibility: hidden !important; }</style>'

# Inject it right before </head>
text = text.replace('</head>', css_hide_badge + '\n</head>')

with open(about_us_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Badge hidden!")
