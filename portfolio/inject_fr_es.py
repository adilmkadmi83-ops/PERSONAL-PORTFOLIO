import json
import re

# Read translation blocks
with open('fr.json', 'r', encoding='utf-8') as f:
    fr_dict = json.load(f)
    
with open('es.json', 'r', encoding='utf-8') as f:
    es_dict = json.load(f)

# Read the translations.js
with open('js/translations.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

def update_lang_block(js, lang, new_dict):
    pattern = r"(" + lang + r":\s*\{)([\s\S]*?)(\},\s*(?:ar|fr|es):|\}\s*;)"
    
    def replacer(match):
        prefix = match.group(1)
        suffix = match.group(3)
        
        lines = []
        for k, v in new_dict.items():
            safe_v = v.replace('"', '\\"').replace('\n', ' ')
            lines.append(f'        "{k}": "{safe_v}"')
            
        new_content = ",\n".join(lines)
        return prefix + "\n" + new_content + "\n    " + suffix
             
    return re.sub(pattern, replacer, js, count=1)

js_content = update_lang_block(js_content, "fr", fr_dict)
js_content = update_lang_block(js_content, "es", es_dict)

with open('js/translations.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Injected French and Spanish translations completely.")
