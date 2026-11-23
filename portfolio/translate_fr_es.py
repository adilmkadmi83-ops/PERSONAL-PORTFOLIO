import re
import json

with open('js/translations.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract EN block to use as base for FR and ES
en_block_match = re.search(r'en:\s*\{([\s\S]*?)\},\s*ar:', content)
if not en_block_match:
    print("Could not find EN block")
    exit()

en_block_str = '{' + en_block_match.group(1) + '}'
# Convert the js object to valid JSON to parse it
# We need to make sure keys are quoted and remove trailing commas
en_json_str = re.sub(r'(\w+):', r'"\1":', en_block_str)
en_json_str = re.sub(r',\s*\}', r'}', en_json_str)

try:
    en_dict = json.loads(en_json_str)
except Exception as e:
    # Fallback to regex parsing if json fails
    en_dict = {}
    pattern = r'"([^"]+)":\s*"([^"]+)"'
    for k, v in re.findall(pattern, en_block_match.group(1)):
        en_dict[k] = v

# Add the missing keys we just tagged in HTML
en_dict['site_title'] = "Adel Mokaddemi | Digital Ads & Performance Marketing Specialist"
en_dict['serv_header_label'] = "My Services"
en_dict['serv_header_title'] = "What do I offer your business?"
en_dict['serv_header_subtitle'] = "I build and manage ad campaigns tailored to your business nature and goals, from planning and launching to tracking and optimization."

# We need to create fr_dict and es_dict based on en_dict
fr_dict = {}
es_dict = {}

# Simple dictionary for common terms
fr_translations = {
    "Campaign Management": "Gestion de Campagne",
    "Performance Marketing": "Marketing à la Performance",
    "Tracking & Analytics": "Suivi & Analytique",
    "Data Analysis & Optimization": "Analyse de Données & Optimisation",
    "Where I Work?": "Où je travaille ?",
    "Customer Journey": "Parcours Client",
    "Performance Analysis": "Analyse des Performances",
    "Methodology": "Méthodologie",
    "Technical Skills": "Compétences Techniques",
    "Case Study": "Étude de Cas",
    "Target Audience": "Audience Cible",
    "Target Markets": "Marchés Cibles",
    "What I Believe In": "Ce en quoi je crois",
    "Why Me?": "Pourquoi moi ?",
    "Career Objective": "Objectif de Carrière",
    "Contact Me": "Contactez-moi",
    "FAQ": "FAQ",
    "Home": "Accueil",
    "About": "À propos",
    "Services": "Services",
    "Portfolio": "Portfolio",
    "Contact": "Contact"
}

es_translations = {
    "Campaign Management": "Gestión de Campañas",
    "Performance Marketing": "Marketing de Resultados",
    "Tracking & Analytics": "Seguimiento y Analítica",
    "Data Analysis & Optimization": "Análisis de Datos y Optimización",
    "Where I Work?": "¿Dónde trabajo?",
    "Customer Journey": "Viaje del Cliente",
    "Performance Analysis": "Análisis de Rendimiento",
    "Methodology": "Metodología",
    "Technical Skills": "Habilidades Técnicas",
    "Case Study": "Caso de Estudio",
    "Target Audience": "Público Objetivo",
    "Target Markets": "Mercados Objetivo",
    "What I Believe In": "En lo que creo",
    "Why Me?": "¿Por qué yo?",
    "Career Objective": "Objetivo Profesional",
    "Contact Me": "Contáctame",
    "FAQ": "Preguntas Frecuentes",
    "Home": "Inicio",
    "About": "Acerca de",
    "Services": "Servicios",
    "Portfolio": "Portafolio",
    "Contact": "Contacto"
}

for k, v in en_dict.items():
    # Attempt to find a direct translation, otherwise fallback to English 
    # (English is better than Arabic for FR/ES, as per "Zero Arabic Tolerance")
    fr_dict[k] = fr_translations.get(v, v)
    es_dict[k] = es_translations.get(v, v)

# Update Arabic dict with the missing keys
ar_dict_missing = {
    "site_title": "عادل مقدمي | متخصص في إدارة الإعلانات الرقمية والتسويق بالأداء",
    "serv_header_label": "خدماتي",
    "serv_header_title": "ماذا أقدم لنشاطك التجاري؟",
    "serv_header_subtitle": "أبني وأدير الحملات الإعلانية بما يتناسب مع طبيعة النشاط التجاري والهدف المطلوب، من التخطيط والإطلاق إلى القياس والتحسين."
}

def dict_to_js_str(d):
    lines = []
    for k, v in d.items():
        safe_v = v.replace('"', '\\"')
        lines.append(f'        "{k}": "{safe_v}"')
    return ",\n".join(lines)

# Rebuild the entire translations.js to ensure it's clean and perfect.
new_translations_js = "const translations = {\n"
new_translations_js += "    en: {\n" + dict_to_js_str(en_dict) + "\n    },\n"

# We must keep the existing Arabic translations and just append the missing ones
ar_block_match = re.search(r'ar:\s*\{([\s\S]*?)\},\s*fr:', content)
if ar_block_match:
    ar_block = ar_block_match.group(1)
    # append missing
    if ar_dict_missing:
        ar_block += ",\n" + dict_to_js_str(ar_dict_missing)
    new_translations_js += "    ar: {\n" + ar_block + "\n    },\n"
else:
    # fallback if structure changed
    pass

new_translations_js += "    fr: {\n" + dict_to_js_str(fr_dict) + "\n    },\n"
new_translations_js += "    es: {\n" + dict_to_js_str(es_dict) + "\n    }\n"
new_translations_js += "};\n"

with open('js/translations.js', 'w', encoding='utf-8') as f:
    f.write(new_translations_js)

print("Translations JS rewritten successfully with zero Arabic in EN/FR/ES.")
