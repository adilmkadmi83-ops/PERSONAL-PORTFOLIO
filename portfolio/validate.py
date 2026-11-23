import json
import re

with open('js/translations.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Remove const translations = 
js = re.sub(r'const\s+translations\s*=\s*', '', js)
# Remove trailing semicolon
js = re.sub(r';\s*$', '', js)
# Quote top level keys (en, ar, fr, es)
js = re.sub(r'\b(en|ar|fr|es)\s*:', r'"\1":', js)
# Remove trailing commas
js = re.sub(r',\s*\}', '}', js)
# Remove any other trailing commas in arrays/objects
js = re.sub(r',\s*\]', ']', js)

try:
    json.loads(js)
    print("Syntax OK")
except Exception as e:
    print("Error:", e)
