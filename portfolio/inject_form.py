import json
import re

exact_keys = {
    # Form
    "form_name_l": "Full Name",
    "form_name_p": "Enter your full name",
    "form_email_l": "Email Address",
    "form_email_p": "Enter your email address",
    "form_company_l": "Company / Business Name",
    "form_company_p": "Enter your business name",
    "form_msg_l": "Project Details or Inquiry",
    "form_msg_p": "How can I help you improve your ad campaigns?",
    "form_submit": "Send Message",
    
    # Contact badge
    "contact_badge": "Remote Work | USA & Europe | GCC Markets",
    
    # Target markets keys in HTML
    "market_usa": "USA",
    "market_eur": "Europe",
    "market_gcc": "GCC Countries",
    
    # Any other keys that might have been mismatched
    "contact_name": "Adel Mokaddemi",
    "contact_role": "Digital Advertising & Performance Marketing Specialist",
    "contact_email": "Email",
    "contact_whatsapp": "WhatsApp",
    "contact_facebook": "Facebook",
    "contact_instagram": "Instagram",
    "contact_label": "Contact Me",
    "contact_title": "Do you have an ad campaign that needs improvement?",
    "contact_subtitle": "If you are looking for a specialist to help you manage your campaigns, understand your audience, analyze performance, and optimize results, I'd be happy to discuss your project.",
    "obj_label": "Career Objective",
    "obj_text": "Building long-term partnerships with companies and brands that want to develop their digital ads in an organized, measurable, and optimizable way.",
    "obj_subtext": "\"The goal is not just to run an ad, but to build an advertising process that can be continuously tested, analyzed, and optimized.\""
}

with open('js/translations.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

def update_lang_block(js, lang, new_dict):
    pattern = r"(" + lang + r":\s*\{)([\s\S]*?)(\},\s*(?:ar|fr|es):|\}\s*;)"
    
    def replacer(match):
        prefix = match.group(1)
        block = match.group(2)
        suffix = match.group(3)
        
        lines = []
        for k, v in new_dict.items():
            safe_v = v.replace('"', '\\"').replace('\n', ' ')
            lines.append(f'        "{k}": "{safe_v}"')
            
        new_content = ",\n".join(lines)
        if block.strip().endswith(','):
             return prefix + block + "\n" + new_content + "\n    " + suffix
        else:
             return prefix + block + ",\n" + new_content + "\n    " + suffix
             
    return re.sub(pattern, replacer, js, count=1)

js_content = update_lang_block(js_content, "en", exact_keys)
js_content = update_lang_block(js_content, "fr", exact_keys)
js_content = update_lang_block(js_content, "es", exact_keys)

with open('js/translations.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Injected exact keys into EN, FR, ES blocks.")
