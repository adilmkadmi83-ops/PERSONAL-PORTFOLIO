import re

with open('js/translations.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Specifically for the 'en' block, remove all " (EN)" 
# We can just do a global replace of " (EN)" with "" since it was only added there
content = content.replace(" (EN)", "")

# Now we apply the specific English translations the user asked for:
replacements = {
    '"princ1_t": "العميل أولًا"': '"princ1_t": "Client First"',
    '"princ2_t": "العرض والرسالة"': '"princ2_t": "Offer & Message"',
    '"princ3_t": "البيانات"': '"princ3_t": "Data & Analytics"',
    '"princ4_t": "التحسين المستمر"': '"princ4_t": "Continuous Improvement"',
    '"why_title": "لماذا تتعامل مع عادل مقدمي؟"': '"why_title": "Why Work with Adel Mokaddemi?"',
    '"why1_t": "التفكير المبني على البيانات"': '"why1_t": "Data-Driven Thinking"',
    '"why2_t": "التركيز على الاختبار"': '"why2_t": "Focus on Testing"',
    '"why3_t": "فهم النشاط التجاري"': '"why3_t": "Understanding the Business"',
    '"why4_t": "العمل عبر عدة منصات"': '"why4_t": "Multi-Platform Approach"',
    '"why5_t": "التحسين المستمر"': '"why5_t": "Continuous Improvement"',
    '"why6_t": "الشفافية والوضوح"': '"why6_t": "Transparency & Clarity"'
}

# The block 'en' might currently have the arabic text without (EN) now since we stripped it.
# Let's replace the Arabic text inside the 'en' object.
# We will isolate the 'en' block to do replacements safely.

en_block_match = re.search(r'en:\s*\{([\s\S]*?)\},\s*ar:', content)
if en_block_match:
    en_block = en_block_match.group(1)
    
    for ar_str, en_str in replacements.items():
        # ar_str currently looks like '"princ1_t": "العميل أولًا"'
        # we want to replace it with '"princ1_t": "Client First"'
        en_block = en_block.replace(ar_str, en_str)
        
    content = content[:en_block_match.start(1)] + en_block + content[en_block_match.end(1):]

with open('js/translations.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("translations updated")
