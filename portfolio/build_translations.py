import json
import re
import os

with open('js/translations.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Extract AR block
ar_match = re.search(r'ar:\s*\{([\s\S]*?)\}(?=\s*,\s*fr:|\s*,\s*es:|\s*;)', js_content)
if ar_match:
    ar_block = ar_match.group(1)
    ar_str = '{' + re.sub(r'(\w+):', r'"\1":', ar_block) + '}'
    # Remove trailing commas inside the block
    ar_str = re.sub(r',\s*\}', '}', ar_str)
    
    try:
        ar_dict = json.loads(ar_str)
    except Exception as e:
        print("Failed to parse AR block using json.loads, using regex fallback")
        ar_dict = {}
        pattern = r'"([^"]+)":\s*"([^"]*)"'
        for k, v in re.findall(pattern, ar_block):
            ar_dict[k] = v
else:
    print("Could not find AR block!")
    exit(1)

# Load others
with open('en_keys.json', 'r', encoding='utf-8') as f:
    en_dict = json.load(f)
with open('fr.json', 'r', encoding='utf-8') as f:
    fr_dict = json.load(f)
with open('es.json', 'r', encoding='utf-8') as f:
    es_dict = json.load(f)

# Combine
final_js = "const translations = {\n"

def format_block(lang, d):
    res = f"    {lang}: {{\n"
    items = list(d.items())
    for i, (k, v) in enumerate(items):
        safe_v = str(v).replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ')
        res += f'        "{k}": "{safe_v}"'
        if i < len(items) - 1:
            res += ",\n"
        else:
            res += "\n"
    res += "    }"
    return res

final_js += format_block("en", en_dict) + ",\n"
final_js += format_block("ar", ar_dict) + ",\n"
final_js += format_block("fr", fr_dict) + ",\n"
final_js += format_block("es", es_dict) + "\n"
final_js += "};\n"

with open('js/translations.js', 'w', encoding='utf-8') as f:
    f.write(final_js)

print("Successfully rebuilt translations.js")
