import re

path = r'C:\Users\angam\Downloads\Leano Website V1\Contact Us\website\Contact Us.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

replacements = {
    '>Selected Work<': '>Contact Us<',
    '>Innovation Starts With You<': ">Let's Power Your Journey<",
    'To contact our company, you can use the official contact details provided on our website, including our email, phone number, and inquiry form.': "Need reliable fuel supply, fuel management, or energy solutions? Contact Leano Energy today."
}

for old, new in replacements.items():
    text = text.replace(old, new)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated the left-hand text sections in Contact Us!')
