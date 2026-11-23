import re
import json

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Very basic tag matcher. We look for any text containing Arabic characters.
tokens = re.split(r'(<[^>]+>)', html)
untagged_arabic = []
current_line = 1

# Note: this is a naive parse. If the text is wrapped in a tag that DOES have data-i18n,
# this simple loop won't know unless we keep track of the open tags.
# But since we just want to see ALL arabic text in the file, we can look at the HTML structure.

# Let's find all tags that contain data-i18n and replace their INNER text with empty string.
# That way whatever is left is untagged.
def remove_tagged_content(html_str):
    # This is hard to do with regex reliably.
    return html_str

for token in tokens:
    if token.startswith('<'):
        pass
    else:
        if re.search(r'[\u0600-\u06FF]', token):
            untagged_arabic.append(f"Line {current_line}: {token.strip()}")
            
    current_line += token.count('\n')

with open('untagged_ar_results.txt', 'w', encoding='utf-8') as f:
    if not untagged_arabic:
        f.write("No Arabic text found outside of tags (basic check).\n")
    else:
        for item in untagged_arabic:
            if item.split(': ')[1]: # ignore empty
                f.write(item + "\n")
