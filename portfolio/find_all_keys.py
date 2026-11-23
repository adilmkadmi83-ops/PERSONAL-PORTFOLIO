import re
import json

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all data-i18n="key"
keys = re.findall(r'data-i18n="([^"]+)"', html)
keys = list(set(keys))

# Check what we have in translations.js
with open('js/translations.js', 'r', encoding='utf-8') as f:
    js = f.read()
    
en_match = re.search(r'en:\s*\{([\s\S]*?)\},\s*ar:', js)
if en_match:
    en_str = '{' + en_match.group(1) + '}'
    en_str = re.sub(r'(\w+):', r'"\1":', en_str)
    en_str = re.sub(r',\s*\}', r'}', en_str)
    try:
        en_dict = json.loads(en_str)
    except:
        en_dict = {}
        pattern = r'"([^"]+)":\s*"([^"]*)"'
        for k, v in re.findall(pattern, en_match.group(1)):
            en_dict[k] = v
else:
    en_dict = {}

missing_keys = [k for k in keys if k not in en_dict]
print(f"Total data-i18n tags in HTML: {len(keys)}")
print(f"Missing in translations.js: {len(missing_keys)}")

with open('all_missing_keys.json', 'w', encoding='utf-8') as f:
    json.dump(missing_keys, f, ensure_ascii=False, indent=2)
