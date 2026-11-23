document.addEventListener("DOMContentLoaded", () => {
    // 1. Determine default language (English if nothing in localStorage)
    const defaultLang = "en";
    const savedLang = localStorage.getItem("preferredLanguage");
    const currentLang = savedLang || defaultLang;

    // 2. Initialize language on load
    setLanguage(currentLang);

    // 3. Add event listeners to language selector
    const langSelect = document.getElementById("lang-select");
    if (langSelect) {
        // Update the <select> value to match the language
        langSelect.value = currentLang;

        langSelect.addEventListener("change", (e) => {
            const selectedLang = e.target.value;
            setLanguage(selectedLang);
        });
    }
});

/**
 * Change la langue du site
 * @param {string} lang - Le code de la langue ('en', 'ar', 'fr', 'es')
 */
function setLanguage(lang) {
    // 1. Sauvegarder la langue dans le localStorage
    localStorage.setItem("preferredLanguage", lang);

    // 2. Mettre à jour l'attribut lang sur <html>
    document.documentElement.setAttribute("lang", lang);

    // 3. Mettre à jour la direction (RTL pour l'arabe, LTR pour les autres)
    if (lang === "ar") {
        document.documentElement.setAttribute("dir", "rtl");
    } else {
        document.documentElement.setAttribute("dir", "ltr");
    }

    // 4. Mettre à jour tous les éléments textuels ayant l'attribut data-i18n
    const elementsToTranslate = document.querySelectorAll("[data-i18n]");
    
    elementsToTranslate.forEach((element) => {
        const key = element.getAttribute("data-i18n");
        // Vérifier si la traduction existe pour cette langue et cette clé
        if (translations[lang] && translations[lang][key]) {
            if (element.tagName.toLowerCase() === 'title') {
                document.title = translations[lang][key];
            } else if (element.tagName.toLowerCase() === 'meta') {
                element.setAttribute("content", translations[lang][key]);
            } else {
                element.innerHTML = translations[lang][key];
            }
        }
    });

    // 5. Mettre à jour les placeholders
    const placeholdersToTranslate = document.querySelectorAll("[data-i18n-placeholder]");
    placeholdersToTranslate.forEach((element) => {
        const key = element.getAttribute("data-i18n-placeholder");
        if (translations[lang] && translations[lang][key]) {
            element.setAttribute("placeholder", translations[lang][key]);
        }
    });
}
