import json
import re

with open('js/translations.js', 'r', encoding='utf-8') as f:
    js = f.read()

en_match = re.search(r'en:\s*\{([\s\S]*?)\},\s*(?:ar|fr|es):', js)
if en_match:
    en_block = en_match.group(1)
    # Convert JS object to JSON
    en_str = '{' + re.sub(r'(\w+):', r'"\1":', en_block) + '}'
    en_str = re.sub(r',\s*\}', '}', en_str)
    try:
        en_dict = json.loads(en_str)
    except Exception as e:
        print(f"JSON loads failed: {e}")
        # fallback regex
        en_dict = {}
        pattern = r'"([^"]+)":\s*"([^"]*)"'
        for k, v in re.findall(pattern, en_block):
            en_dict[k] = v
            
    with open('en_keys.json', 'w', encoding='utf-8') as f:
        json.dump(en_dict, f, ensure_ascii=False, indent=2)
    print(f"Extracted {len(en_dict)} keys.")
else:
    print("Failed to find EN block.")
