import json
import re

missing_ar = {
    "platform_title": "المنصات التي أعمل عليها",
    "platform_subtitle": "لا أختار المنصة لمجرد شهرتها، بل وفقًا لطبيعة النشاط والجمهور والهدف الإعلاني.",
    "plat_meta": "فيسبوك وانستغرام",
    "plat_google": "جوجل ويوتيوب",
    "plat_tiktok": "تيك توك",
    "plat_snap": "سناب شات",
    
    "plat_meta_1": "إنشاء وإعداد الحملات الإعلانية المتقدمة",
    "plat_meta_2": "استهداف شرائح دقيقة من الجماهير (Audience Targeting)",
    "plat_meta_3": "إعادة استهداف المهتمين (Retargeting)",
    "plat_meta_4": "اختبار الأفكار والمحتوى الإعلاني (Creative Testing)",
    "plat_meta_5": "اختبار شرائح الجماهير ومجموعات الإعلانات (Audience Testing)",
    "plat_meta_6": "تحسين الأداء بشكل دوري لخفض تكلفة التحويل",
    "plat_meta_7": "تحليل سلوك العملاء وقمع المبيعات (Conversion Analysis)",
    
    "plat_goo_1": "إعلانات شبكة البحث (Search Ads)",
    "plat_goo_2": "إعلانات الشبكة الإعلانية (Display Ads)",
    "plat_goo_3": "إعلانات يوتيوب المرئية (YouTube Ads)",
    "plat_goo_4": "حملات الأداء الأقصى الذكية (Performance Max)",
    "plat_goo_5": "البحث وتحديد الكلمات المفتاحية الأكثر ربحية",
    "plat_goo_6": "إعادة استهداف الزوار السابقين للموقع",
    "plat_goo_7": "إعداد أدوات تتبع قياس التحويلات المتقدمة",
    
    "plat_tik_1": "إعداد وهيكلة الحملات عبر TikTok Ads Manager",
    "plat_tik_2": "استهداف الفئات الشبابية والاهتمامات الدقيقة",
    "plat_tik_3": "اختبار المحتوى الإعلاني المخصص للتيك توك",
    "plat_tik_4": "إطلاق حملات تجميع بيانات العملاء (Lead Generation)",
    "plat_tik_5": "حملات زيادة المبيعات والتحويل للمتاجر الإلكترونية",
    "plat_tik_6": "إعادة استهداف المتفاعلين ومشاهدي الفيديوهات",
    "plat_tik_7": "تحليل أداء الفيديو والاحتفاظ بالمشاهدين",
    
    "plat_snap_1": "إعداد وتطوير الحملات الإعلانية في الخليج",
    "plat_snap_2": "استهداف ديموغرافي وجغرافي متقدم",
    "plat_snap_3": "حملات جذب العملاء الجدد (Customer Acquisition)",
    "plat_snap_4": "حملات إعادة الاستهداف المخصصة لسناب",
    "plat_snap_5": "اختبار التصاميم والفيديوهات القصيرة",
    "plat_snap_6": "تحسين الميزانيات وتحقيق نتائج إعلانية فعالة",
    
    "plat_msg": "« لا أختار المنصة لمجرد شهرتها، بل وفقًا لطبيعة النشاط والجمهور والهدف الإعلاني. »"
}

en_new = {k: v + " (EN)" for k, v in missing_ar.items()}
fr_new = {k: v + " (FR)" for k, v in missing_ar.items()}
es_new = {k: v + " (ES)" for k, v in missing_ar.items()}

with open('js/translations.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

def insert_keys(js, lang_code, new_keys):
    pattern = r"(" + lang_code + r": \{[\s\S]*?)(\n    \},|\n    \})"
    
    def replacer(match):
        lines = []
        for k, v in new_keys.items():
            safe_v = v.replace('"', '\\"')
            lines.append(f'        "{k}": "{safe_v}"')
        new_content = ",\n".join(lines)
        return match.group(1) + ",\n" + new_content + match.group(2)
        
    return re.sub(pattern, replacer, js, count=1)

js_content = insert_keys(js_content, "en", en_new)
js_content = insert_keys(js_content, "ar", missing_ar)
js_content = insert_keys(js_content, "fr", fr_new)
js_content = insert_keys(js_content, "es", es_new)

with open('js/translations.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("translations.js updated successfully")
