from html.parser import HTMLParser
import json
import re

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = {}
        self.current_key = None
        self.current_text = ""
        
    def handle_starttag(self, tag, attrs):
        for k, v in attrs:
            if k == 'data-i18n':
                self.current_key = v
                self.current_text = ""
                break
            
    def handle_endtag(self, tag):
        if self.current_key:
            self.tags[self.current_key] = self.current_text.strip()
            self.current_key = None

    def handle_data(self, data):
        if self.current_key:
            self.current_text += data

parser = MyHTMLParser()
with open('index.html', 'r', encoding='utf-8') as f:
    parser.feed(f.read())

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

missing = {}
for k, v in parser.tags.items():
    if k not in en_dict:
        missing[k] = v

with open('missing_tags.json', 'w', encoding='utf-8') as f:
    json.dump(missing, f, ensure_ascii=False, indent=2)

print(f"Found {len(parser.tags)} total tags in HTML.")
print(f"Found {len(missing)} tags missing from translations.js.")
