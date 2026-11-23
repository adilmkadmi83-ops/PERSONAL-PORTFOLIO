import json
import re

with open('final_translations.json', 'r', encoding='utf-8') as f:
    new_translations = json.load(f)

with open('js/translations.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

def update_lang_block(js, lang, new_dict):
    pattern = r"(" + lang + r":\s*\{)([\s\S]*?)(\},\s*(?:ar|fr|es):|\}\s*;)"
    
    def replacer(match):
        prefix = match.group(1)
        block = match.group(2)
        suffix = match.group(3)
        
        # inject new dict entries
        lines = []
        for k, v in new_dict.items():
            safe_v = v.replace('"', '\\"').replace('\n', ' ')
            # if the key is already there, we should replace it, but these were missing, so just append
            lines.append(f'        "{k}": "{safe_v}"')
            
        new_content = ",\n".join(lines)
        if block.strip().endswith(','):
             return prefix + block + "\n" + new_content + "\n    " + suffix
        else:
             return prefix + block + ",\n" + new_content + "\n    " + suffix
             
    return re.sub(pattern, replacer, js, count=1)

# We update EN, FR, ES with the english translations to guarantee no Arabic
js_content = update_lang_block(js_content, "en", new_translations)
js_content = update_lang_block(js_content, "fr", new_translations)
js_content = update_lang_block(js_content, "es", new_translations)

with open('js/translations.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Injected final translations into EN, FR, ES blocks.")
