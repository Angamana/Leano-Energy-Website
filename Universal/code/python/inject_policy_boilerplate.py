import os
import re

root_dir = r"C:\Users\angam\Downloads\Leano Website V1"
policies_dir = os.path.join(root_dir, "Policies")

policies = [
    "Quality Policy",
    "Environmental Policy",
    "Health & Safety Policy",
    "Privacy Policy",
    "Terms and Conditions"
]

boilerplate = {
    "Quality Policy": "<h2>Quality Policy (ISO 9001)</h2><br><p>Leano Energy is committed to customer satisfaction and continuous improvement...</p>",
    "Environmental Policy": "<h2>Environmental Policy (ISO 14001)</h2><br><p>Leano Energy is committed to sustainability and reducing environmental impact...</p>",
    "Health & Safety Policy": "<h2>Health & Safety Policy (ISO 45001)</h2><br><p>Leano Energy is committed to a safe working environment...</p>",
    "Privacy Policy": "<h2>Privacy Policy (POPIA Compliant)</h2><br><p>Leano Energy respects your privacy and is committed to protecting your personal data...</p>",
    "Terms and Conditions": "<h2>Terms and Conditions</h2><br><p>Welcome to Leano Energy. These terms and conditions outline the rules and regulations for the use of our website...</p>"
}

for policy in policies:
    policy_dir_name = policy
    policy_path = os.path.join(policies_dir, policy_dir_name)
    new_html = os.path.join(policy_path, "website", f"{policy}.html")
    
    with open(new_html, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We want to replace from </header> to <footer class="footer-section">
    # The replacement will be a single section with the boilerplate.
    
    replacement_block = f'</header>\n<section class="section-gap margin-top-100"><div class="w-layout-blockcontainer container w-container">{boilerplate[policy]}</div></section>\n<footer class="footer-section">'
    
    content = re.sub(r'</header>.*?<footer class="footer-section">', replacement_block, content, flags=re.DOTALL)
    
    with open(new_html, "w", encoding="utf-8") as f:
        f.write(content)

print("Content injected successfully.")
