import re
import json

with open('js/translations.js', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    '"platform_title": "المنصات التي أعمل عليها"': '"platform_title": "Platforms I Work With"',
    '"platforms_label": "المنصات الإعلانية"': '"platforms_label": "Ad Platforms"',
    '"platform_subtitle": "لا أختار المنصة لمجرد شهرتها، بل وفقًا لطبيعة النشاط والجمهور والهدف الإعلاني."': '"platform_subtitle": "I don\'t choose a platform just for its popularity, but based on business nature, audience, and ad goals."',
    '"plat_msg": "« لا أختار المنصة لمجرد شهرتها، بل وفقًا لطبيعة النشاط والجمهور والهدف الإعلاني. »"': '"plat_msg": "« I don\'t choose a platform just for its popularity, but based on business nature, audience, and ad goals. »"',
    '"plat_meta": "فيسبوك وانستغرام"': '"plat_meta": "Facebook & Instagram"',
    '"plat_google": "جوجل ويوتيوب"': '"plat_google": "Google & YouTube"',
    '"plat_tiktok": "تيك توك"': '"plat_tiktok": "TikTok"',
    '"plat_snap": "سناب شات"': '"plat_snap": "Snapchat"',
    
    '"plat_meta_1": "إنشاء وإعداد الحملات الإعلانية المتقدمة"': '"plat_meta_1": "Advanced Ad Campaign Setup"',
    '"plat_meta_2": "استهداف شرائح دقيقة من الجماهير (Audience Targeting)"': '"plat_meta_2": "Precise Audience Targeting"',
    '"plat_meta_3": "إعادة استهداف المهتمين (Retargeting)"': '"plat_meta_3": "Audience Retargeting"',
    '"plat_meta_4": "اختبار الأفكار والمحتوى الإعلاني (Creative Testing)"': '"plat_meta_4": "Creative & Ad Content Testing"',
    '"plat_meta_5": "اختبار شرائح الجماهير ومجموعات الإعلانات (Audience Testing)"': '"plat_meta_5": "Audience & Ad Set Testing"',
    '"plat_meta_6": "تحسين الأداء بشكل دوري لخفض تكلفة التحويل"': '"plat_meta_6": "Continuous Optimization to Lower CPA"',
    '"plat_meta_7": "تحليل سلوك العملاء وقمع المبيعات (Conversion Analysis)"': '"plat_meta_7": "Customer Journey & Funnel Analysis"'
}

en_block_match = re.search(r'en:\s*\{([\s\S]*?)\},\s*ar:', content)
if en_block_match:
    en_block = en_block_match.group(1)
    
    for ar_str, en_str in replacements.items():
        en_block = en_block.replace(ar_str, en_str)
        
    content = content[:en_block_match.start(1)] + en_block + content[en_block_match.end(1):]

with open('js/translations.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Platforms EN translations applied successfully.")
