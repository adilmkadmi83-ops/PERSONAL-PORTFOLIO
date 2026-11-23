import json
import re

missing_translations = {
    # Strategy Section
    "case_strat_t": "The Strategy Applied",
    "case_p1_n": "Phase One",
    "case_p1_t": "Reaching New Customers",
    "case_p1_d": "Testing different audience segments and drafting multiple marketing messages tailored to each segment.",
    "case_p2_n": "Phase Two",
    "case_p2_t": "Ad Testing",
    "case_p2_d": "Testing various ad angles (images, videos, headlines) and identifying the most engaging and impactful concepts.",
    "case_p3_n": "Phase Three",
    "case_p3_t": "Retargeting",
    "case_p3_d": "Retargeting store visitors and interested users who did not complete the purchase with special offers.",
    "case_p4_n": "Phase Four",
    "case_p4_t": "Continuous Optimization",
    "case_p4_d": "Monitoring the customer journey in detail and analyzing data to address weaknesses in landing pages and checkout.",

    # Philosophy Section
    "princ1_t": "Client First",
    "princ1_d": "Who is the customer? What real problem are we solving for them? We always start by understanding their behavior.",
    "princ2_t": "Offer & Message",
    "princ2_d": "Why would the customer care about the product? Why choose this offer over competitors?",
    "princ3_t": "Data",
    "princ3_d": "What do the numbers and statistics tell us after launching campaigns? We read the data to determine the next step.",
    "princ4_t": "Continuous Improvement",
    "princ4_d": "Advertising is a continuous, never-ending cycle of testing, analysis, and daily optimization to increase efficiency.",
    "princ_conclusion": "Marketing Thinking + Audience Understanding + Data Analysis + Continuous Optimization",

    # Why Adel Section
    "why_label": "Why Me?",
    "why_title": "Why Work with Adel Mokaddemi?",
    "why1_t": "Data-Driven Thinking",
    "why1_d": "Making decisions and adjusting ad campaigns based on clear, actual numbers and results, not guesswork.",
    "why2_t": "Focus on Testing",
    "why2_d": "Testing multiple ad concepts, visuals, and audiences to find the most profitable elements.",
    "why3_t": "Understanding the Business",
    "why3_d": "Aligning ads with the actual business goal and sales, rather than getting empty, valueless traffic.",
    "why4_t": "Multi-Platform Expertise",
    "why4_d": "Identifying and choosing the right ad platforms and channels according to the client's nature, budget, and audience.",
    "why5_t": "Continuous Optimization",
    "why5_d": "Monitoring daily performance and making constant adjustments to improve CPA and scale ad results.",
    "why6_t": "Transparency & Clarity",
    "why6_d": "Full clarity in strategies, workflow, data, and sharing periodic reports with partners.",

    # Footer
    "footer_rights": "All Rights Reserved",
    "footer_about": "Digital marketing and performance advertising specialist, helping brands achieve measurable and scalable results.",
    "footer_links_title": "Main Links",
    "footer_services_title": "Main Services",
    "foot_l1": "Home",
    "foot_l2": "About Me",
    "foot_l3": "My Services",
    "foot_l4": "Portfolio & Results",
    "foot_l5": "Contact Me",
    "foot_s1": "Campaign Management",
    "foot_s2": "Performance Marketing",
    "foot_s3": "Tracking & Conversions",
    "foot_s4": "Data Analysis",
    "foot_m_t": "Target Markets",
    "foot_m1": "USA",
    "foot_m2": "Europe",
    "foot_m3": "GCC Countries",

    # Contact Form
    "contact_form_name": "Full Name",
    "contact_form_name_p": "Enter your full name",
    "contact_form_email": "Email Address",
    "contact_form_email_p": "Enter your email address",
    "contact_form_company": "Company / Business Name",
    "contact_form_company_p": "Enter your business name",
    "contact_form_msg": "Project Details or Inquiry",
    "contact_form_msg_p": "How can I help you improve your ad campaigns?",
    "contact_form_btn": "Send Message",
    "contact_remote_badge": "Remote Work | USA & Europe | GCC Markets"
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

# Apply these translations to en, fr, es
js_content = update_lang_block(js_content, "en", missing_translations)
js_content = update_lang_block(js_content, "fr", missing_translations)
js_content = update_lang_block(js_content, "es", missing_translations)

with open('js/translations.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Injected final missing sections into EN, FR, ES blocks.")
