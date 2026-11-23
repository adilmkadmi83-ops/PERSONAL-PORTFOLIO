import json
import re

translations = {
  "serv_t1": "Campaign Management",
  "serv_d1": "Building and launching comprehensive ad campaigns across multiple platforms, monitoring daily performance to ensure the highest ROI.",
  "serv_p1": "Comprehensive audience and competitor research",
  "serv_p2": "Campaign Setup & Structure",
  "serv_p3": "Budget Allocation",
  "serv_t2": "Performance Marketing",
  "serv_d2": "Focusing on measurable results (sales, leads) and paying for actual outcomes through continuous optimization strategies.",
  "serv_p4": "CPA Optimization",
  "serv_p5": "Increase Return on Ad Spend (ROAS)",
  "serv_p6": "Retargeting Strategies",
  "serv_t3": "Tracking & Analytics",
  "serv_d3": "Installing advanced tracking tools to accurately measure customer journeys, helping in data-driven decisions.",
  "serv_p7": "Google Tag Manager (GTM) Setup",
  "serv_p8": "Meta Pixel & Conversions API (CAPI)",
  "serv_p9": "Event Tracking Setup",
  "serv_t4": "Data Analysis & Optimization",
  "serv_d4": "Reading numbers to extract marketing insights, finding funnel bottlenecks, and applying instant solutions.",
  "serv_p10": "Campaign Performance Analysis & Reporting",
  "serv_p11": "A/B Testing for Offers and Ads",
  "serv_p12": "Landing Page Analysis for CRO",
  
  "platforms_title": "Where I Work?",
  "platforms_subtitle": "I manage campaigns across top digital platforms to reach your audience anywhere.",
  "plat_d1": "Facebook & Instagram Ads",
  "plat_s1": "Brand Awareness Campaigns",
  "plat_s2": "Lead Generation Campaigns",
  "plat_s3": "Sales & Catalog Campaigns",
  "plat_s4": "Advanced Tracking (CAPI & Pixel)",
  "plat_s5": "Dynamic Retargeting",
  
  "plat_d2": "TikTok Ads",
  "plat_s6": "Targeting Young & Interactive Audiences",
  "plat_s7": "Store Conversions Campaigns",
  "plat_s8": "Spark Ads",
  "plat_s9": "TikTok Pixel Integration",
  
  "plat_d3": "Snapchat Ads",
  "plat_s10": "Precise Local Targeting (GCC)",
  "plat_s11": "Collection & Story Ads",
  "plat_s12": "Dynamic Ads",
  "plat_s13": "Snapchat Pixel Integration",
  "plat_s14": "Mobile Shopping Optimization",
  
  "plat_d4": "Google Ads",
  "plat_s15": "Search Ads",
  "plat_s16": "Performance Max",
  "plat_s17": "Display Ads",
  "plat_s18": "YouTube Video Ads",
  "plat_s19": "Google Analytics 4 Integration",
  
  "journey_label": "Customer Journey",
  "journey_title": "How I Build a Sales Funnel?",
  "journey_subtitle": "Designing a complete customer journey from the first ad view to checkout.",
  
  "fun_t1": "Awareness & Impression",
  "fun_d1": "Attracting the target audience and building brand awareness.",
  "fun_t2": "Interest & Engagement",
  "fun_d2": "Educating the customer about the product and highlighting value.",
  "fun_t3": "Decision & Click",
  "fun_d3": "Motivating the customer to take action (Visit site / Add to cart).",
  "fun_t4": "Conversion & Purchase",
  "fun_d4": "Facilitating the payment process and completing the purchase.",
  "fun_t5": "Retargeting",
  "fun_d5": "Reaching out to abandoned carts and increasing customer lifetime value.",
  
  "jour_prin_title": "Key Principles in the Customer Journey:",
  "jour_p1": "Customized message for each stage.",
  "jour_p2": "Precise tracking of exit points.",
  "jour_p3": "Continuous landing page optimization.",
  
  "metrics_label": "Performance Analysis",
  "metrics_title": "What We Measure? How We Improve?",
  "metrics_subtitle": "Data is the compass. I rely on analyzing precise metrics to direct the budget towards winning ads.",
  "track_title": "Tracking Tools I Rely On:",
  
  "m1_t": "Return on Ad Spend (ROAS)",
  "m1_d": "Revenue generated for every dollar spent on ads.",
  "m2_t": "Cost Per Acquisition (CPA)",
  "m2_d": "Cost of acquiring a new customer or purchase.",
  "m3_t": "Click-Through Rate (CTR)",
  "m3_d": "Ad attractiveness and creative content effectiveness.",
  "m4_t": "Conversion Rate (CR)",
  "m4_d": "Percentage of visitors who completed the desired goal.",
  "m5_t": "Cost Per Mille (CPM)",
  "m5_d": "Cost of reaching 1000 users, an indicator of competition.",
  "m6_t": "Cost Per Click (CPC)",
  "m6_d": "Amount paid for each click on the ad.",
  "m7_t": "Add To Cart Rate",
  "m7_d": "Percentage of visitors who added products to the cart.",
  "m8_t": "Cart Abandonment Rate",
  "m8_d": "Analyzing and addressing reasons for incomplete checkouts.",
  
  "meth_label": "Methodology",
  "meth_title": "How We Manage Your Campaigns?",
  "meth_subtitle": "Clear practical steps to ensure launching successful campaigns and achieving the best results.",
  
  "meth_s1_t": "Business Analysis",
  "meth_s1_d": "Analyzing the product, audience, offers, and competitors.",
  "meth_s2_t": "Tracking & Integration",
  "meth_s2_d": "Setting up Pixel & API for accurate measurement.",
  "meth_s3_t": "Strategy Building",
  "meth_s3_d": "Defining structure, budget, and sales funnel.",
  "meth_s4_t": "Creative Preparation",
  "meth_s4_d": "Drafting headlines and preparing ad copy for testing.",
  "meth_s5_t": "Testing Phase",
  "meth_s5_d": "Testing audiences, ads, and offers.",
  "meth_s6_t": "Initial Analysis",
  "meth_s6_d": "Reading data and excluding unprofitable ads.",
  "meth_s7_t": "Scaling",
  "meth_s7_d": "Increasing budget on winning campaigns strategically.",
  "meth_s8_t": "Reporting & Transparency",
  "meth_s8_d": "Sharing results and discussing next steps.",
  
  "skills_label": "Technical Skills",
  "skills_title": "Marketing Tools & Expertise",
  
  "cat1_title": "Strategy & Planning",
  "cat1_s1": "Sales Funnel Building",
  "cat1_s2": "Competitor Analysis",
  "cat1_s3": "Target Audience Research",
  "cat1_s4": "Ad Budget Management",
  "cat1_s5": "Offer Creation",
  
  "cat2_title": "Media Buying",
  "cat2_s5": "Campaign Scaling",
  "cat2_s6": "Retargeting",
  
  "cat3_title": "CRO & Creative",
  "cat3_s1": "A/B Testing",
  "cat3_s2": "Landing Page Optimization",
  "cat3_s3": "User Journey Analysis",
  "cat3_s4": "Copywriting",
  "cat3_s5": "Testing Angles",
  "cat3_s6": "Testing Headlines & Creatives",
  
  "cat4_title": "Analytics & Tracking",
  "cat4_s1": "Conversion Tracking Setup",
  "cat4_s2": "Meta Pixel Setup",
  "cat4_s3": "Conversions API Setup",
  "cat4_s6": "UTM Tracking",
  "cat4_s7": "KPI Analysis",
  
  "case_label": "Case Study",
  "case_title": "Campaign Management Simulation",
  "case_subtitle": "This hypothetical model explains how I handle marketing challenges to drive sales.",
  "case_badge": "Demo Case Study",
  "case_store_title": "E-commerce Store in Saudi Arabia",
  "case_m1_l": "Industry",
  "case_m1_v": "E-commerce",
  "case_m2_l": "Target Market",
  "case_m2_v": "Saudi Arabia",
  "case_m3_l": "Primary Goal",
  "case_m3_v": "Increase Sales & Conversions",
  "case_disc": "This is a demo model explaining the thought process and strategy, not a real client project.",
  
  "case_chal_t": "The Challenge",
  "case_chal_d": "An e-commerce store struggling to reach new customers and achieve stable sales, wanting to use digital ads to build an organized, scalable sales channel and increase conversion rates.",
  "case_obj_t": "The Objectives",
  "case_obj_1": "Setup and activate a 100% complete tracking and analytics infrastructure.",
  "case_obj_2": "Lower Cost Per Acquisition (CPA) while increasing sales volume.",
  "case_obj_3": "Optimize and improve landing page Conversion Rate.",
  "case_funnel_t": "Sales Funnel Model",
  "case_f1_l": "Impressions",
  "case_f2_l": "Clicks",
  "case_f3_l": "Store Visits",
  "case_f3_p": "80% of Clicks",
  "case_f4_l": "Add to Cart",
  "case_f5_l": "Checkout",
  "case_f6_l": "Purchase",
  "case_f6_p": "3% of Visits",
  "case_sol_t": "The Solution & Strategy",
  "case_phase1": "Phase 1: Deep Setup",
  "case_p1_d": "Integrating Meta Pixel, CAPI, and Google Analytics. Defining the target audience based on purchasing power.",
  "case_phase2": "Phase 2: Creative Testing",
  "case_p2_d": "Testing 5 different ad angles (e.g., Quality, Fast Shipping, Discounts) using Video and Carousel ads.",
  "case_phase3": "Phase 3: Data Analysis",
  "case_p3_d": "Identifying winning ads with CTR > 2% and CPA below the target threshold.",
  "case_phase4": "Phase 4: Scaling & Retargeting",
  "case_p4_d": "Increasing budgets on winning ads by 20% every 48 hours, and retargeting cart abandoners with a special offer.",
  
  "ind_label": "Target Audience",
  "ind_title": "Industries I Work With",
  "ind_subtitle": "Specialized in performance marketing for businesses focusing on direct sales and lead generation.",
  "ind_1_t": "E-commerce Stores",
  "ind_1_d": "Focusing on increasing sales (Purchases), lowering CPA, and improving ROAS.",
  "ind_2_t": "Services & Agencies",
  "ind_2_d": "Lead generation for B2B and B2C service providers with high intent targeting.",
  "ind_3_t": "Digital Products",
  "ind_3_d": "Marketing courses, software, and subscriptions with high conversion strategies.",
  
  "markets_label": "Target Markets",
  "markets_title": "Markets I Serve",
  "markets_subtitle": "Strong expertise in targeting and understanding consumer behavior in the GCC region.",
  "market_sa": "Saudi Arabia",
  "market_ae": "United Arab Emirates",
  "market_kw": "Kuwait",
  "market_qa": "Qatar",
  "market_bh": "Bahrain",
  "market_om": "Oman",
  "markets_notice": "« Available for remote work with companies in the GCC and international markets. »",
  
  "princ_label": "What I Believe In",
  "princ_title": "My Marketing Philosophy",
  "princ_subtitle": "The core principles I adhere to for delivering professional work focused on business goals.",
  "princ_conclusion": "Marketing Thinking + Audience Understanding + Data Analysis + Continuous Improvement",
  
  "why_label": "Why Me?",
  "obj_label": "Career Objective",
  "obj_text": "Building long-term partnerships with companies looking to scale their digital ads in an organized, measurable way.",
  "obj_subtext": "« The goal is not just running an ad, but building an advertising process that can be tested, analyzed, and continuously improved. »",
  
  "contact_label": "Contact Me",
  "contact_title": "Have a campaign that needs scaling?",
  "contact_subtitle": "If you're looking for a specialist to manage your campaigns, understand your audience, analyze performance, and improve results, I'd be happy to discuss your project.",
  
  "c_info_t": "Contact Information",
  "c_loc_l": "Location:",
  "c_loc_v": "Algeria (Available for Remote Work)",
  "c_email_l": "Email:",
  "c_phone_l": "WhatsApp:",
  "c_social_t": "Social Media:",
  
  "c_form_t": "Send a Message",
  "c_name": "Full Name",
  "c_name_p": "Enter your full name",
  "c_email": "Email Address",
  "c_email_p": "example@domain.com",
  "c_proj": "Project Details",
  "c_proj_p": "Tell me about your business, website link, and current ad budget...",
  "c_submit": "Send Message",
  
  "faq_label": "FAQ",
  "faq_title": "Frequently Asked Questions",
  "faq_subtitle": "Clear answers to the most common questions about the workflow.",
  
  "faq1_q": "Do you offer ad design services?",
  "faq1_a": "I specialize entirely in ad management, strategy, and data analysis. The client must provide the creative assets, though I can provide directives for the best angles.",
  
  "faq2_q": "What is the minimum ad budget you work with?",
  "faq2_a": "To ensure enough data for optimization, I recommend a minimum ad budget of $1500 to $2000 per month.",
  
  "faq3_q": "Do you guarantee specific sales or results?",
  "faq3_a": "No professional marketer can guarantee exact numbers. I guarantee proper setup, rigorous testing, and continuous optimization to achieve the best possible CPA and ROAS.",
  
  "faq4_q": "How do we communicate?",
  "faq4_a": "We communicate via WhatsApp or Email, with regular performance reports shared periodically.",
  
  "footer_brand": "Adil ads",
  "footer_desc": "Digital Advertising & Performance Marketing Specialist.",
  "footer_links_t": "Quick Links",
  "footer_contact_t": "Contact",
  "footer_copy": "© 2026 Adel Mokaddemi — All Rights Reserved.",

  "logo_subtitle": "Adil Ads"
}

with open('js/translations.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

en_block_match = re.search(r'en:\s*\{([\s\S]*?)\},\s*ar:', js_content)
if en_block_match:
    en_block = en_block_match.group(1)
    
    # Replace the matches in the en block
    # Note: we need to replace based on keys, not values, because the current values in 'en' might be arabic text or mixed.
    for k, v in translations.items():
        # find the key in en_block: "k": "anything"
        # and replace it with "k": "v"
        safe_v = v.replace('"', '\\"')
        pattern = r'"{0}"\s*:\s*"[^"]*"'.format(k)
        replacement = '"{0}": "{1}"'.format(k, safe_v)
        en_block = re.sub(pattern, replacement, en_block)

    # Reconstruct file
    js_content = js_content[:en_block_match.start(1)] + en_block + js_content[en_block_match.end(1):]

with open('js/translations.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Full translations applied to EN block.")
