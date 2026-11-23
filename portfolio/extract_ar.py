import re
import json

with open('js/translations.js', 'r', encoding='utf-8') as f:
    content = f.read()

en_block_match = re.search(r'en:\s*\{([\s\S]*?)\},\s*ar:', content)
if en_block_match:
    en_block = en_block_match.group(1)
    
    # Extract keys and values
    pattern = r'"([^"]+)":\s*"([^"]+)"'
    matches = re.findall(pattern, en_block)
    
    arabic_keys = []
    for key, val in matches:
        # check for arabic characters
        if re.search(r'[\u0600-\u06FF]', val):
            arabic_keys.append((key, val))
            
    with open('arabic_keys.json', 'w', encoding='utf-8') as out:
        json.dump(arabic_keys, out, ensure_ascii=False, indent=2)

    print(f"Found {len(arabic_keys)} keys to translate.")
