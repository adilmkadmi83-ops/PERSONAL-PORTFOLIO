import json
import re

with open('js/translations.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = re.sub(r'const\s+translations\s*=\s*', '', js)
js = re.sub(r';\s*$', '', js)
js = re.sub(r'\b(en|ar|fr|es)\s*:', r'"\1":', js)
js = re.sub(r',\s*\}', '}', js)

print(repr(js[-100:]))
