from html.parser import HTMLParser
import re

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_i18n = 0
        self.untagged = []
        
    def handle_starttag(self, tag, attrs):
        # check if it has data-i18n or data-i18n-placeholder
        is_i18n = False
        for k, v in attrs:
            if k in ['data-i18n', 'data-i18n-placeholder']:
                is_i18n = True
                break
        
        if is_i18n or self.in_i18n > 0:
            self.in_i18n += 1

        # Also check placeholders of inputs if not i18n
        if tag == 'input' or tag == 'textarea':
            if not is_i18n:
                for k, v in attrs:
                    if k == 'placeholder' and re.search(r'[\u0600-\u06FF]', v):
                        self.untagged.append(f"Line {self.getpos()[0]}: Untagged placeholder: {v}")

    def handle_endtag(self, tag):
        if self.in_i18n > 0:
            self.in_i18n -= 1

    def handle_data(self, data):
        if self.in_i18n == 0:
            if re.search(r'[\u0600-\u06FF]', data):
                text = data.strip()
                if text:
                    self.untagged.append(f"Line {self.getpos()[0]}: {text}")

parser = MyHTMLParser()
with open('index.html', 'r', encoding='utf-8') as f:
    parser.feed(f.read())

with open('real_untagged.txt', 'w', encoding='utf-8') as f:
    for item in parser.untagged:
        f.write(item + '\n')
    if not parser.untagged:
        f.write("All clear!\n")
