import os
import re

index_path = r"C:\Users\angam\Downloads\Leano Website V1\Index\website\Index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Subtitle
content = content.replace(">Process<", ">Key Differentiators<")
content = content.replace(">PROCESS<", ">KEY DIFFERENTIATORS<")

# 2. Titles
content = content.replace("Diverse Building Applications", "Turnkey Fuel Supply Chain")
content = content.replace("Proven Durability Over Time", "Advanced Fuel Management")
content = content.replace("Guarantees to Count On", "Rapid Deployment & Scalability")
content = content.replace("Eco-Friendly Material", "Sustainability Focus")

# 3. Descriptions using regex since I don't know the exact text of #3 and #4
pattern = re.compile(r'(<div class="accordian-style-one-desc">)(.*?)(</div>)')
matches = pattern.findall(content)

descs = [
    "End-to-end solutions, from source to site.",
    "Cutting-edge technology to prevent fuel loss and optimize consumption.",
    "Capability to set up temporary sites quickly and scale operations based on demand.",
    "Offering alternative fuels and lubricants that help clients meet their environmental targets."
]

def repl(match):
    global idx
    desc = descs[idx % 4]
    idx += 1
    return match.group(1) + desc + match.group(3)

idx = 0
content = pattern.sub(repl, content)

# 4. Swap images
# Let's replace the process images with service-img-04-01.jpg
# Wait, I don't want to replace ALL images, just the ones in process section.
# The process section images have filenames like process-img-01.jpg, process-img-02.jpg, process-img-03.jpg, process-img-04.jpg
content = re.sub(r'src="../../Universal/images/[a-zA-Z0-9_]+_process-img-\d\d\.jpg"', 'src="../../Universal/images/693b98cf84dea43415aaf60d_service-img-04-01.jpg"', content)
content = re.sub(r'srcset="../../Universal/images/[a-zA-Z0-9_]+_process-img-\d\d-p-500\.jpg 500w, ../../Universal/images/[a-zA-Z0-9_]+_process-img-\d\d\.jpg 720w"', 'srcset="../../Universal/images/693b98cf84dea43415aaf60d_service-img-04-01-p-500.jpg 500w, ../../Universal/images/693b98cf84dea43415aaf60d_service-img-04-01.jpg 700w"', content)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Process section updated successfully. Replaced {idx} descriptions.")
