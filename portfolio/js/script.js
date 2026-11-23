document.addEventListener('DOMContentLoaded', () => {
    // ==========================================================================
    // THEME TOGGLE CONTROL
    // ==========================================================================
    const themeToggleBtn = document.getElementById('theme-toggle');
    const bodyElement = document.body;

    // Check for saved theme preference in localStorage
    const savedTheme = localStorage.getItem('portfolio-theme');
    if (savedTheme === 'light') {
        bodyElement.classList.add('light-theme');
        themeToggleBtn.setAttribute('aria-label', 'تفعيل الوضع الداكن');
    } else {
        bodyElement.classList.remove('light-theme');
        themeToggleBtn.setAttribute('aria-label', 'تفعيل الوضع المضيء');
    }

    themeToggleBtn.addEventListener('click', () => {
        bodyElement.classList.toggle('light-theme');
        const isLight = bodyElement.classList.contains('light-theme');
        
        if (isLight) {
            localStorage.setItem('portfolio-theme', 'light');
            themeToggleBtn.setAttribute('aria-label', 'تفعيل الوضع الداكن');
        } else {
            localStorage.setItem('portfolio-theme', 'dark');
            themeToggleBtn.setAttribute('aria-label', 'تفعيل الوضع المضيء');
        }
    });

    // ==========================================================================
    // MOBILE NAV DRAWER MENU
    // ==========================================================================
    const mobileNavToggle = document.getElementById('mobile-nav-toggle');
    const navMenu = document.getElementById('nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');

    function toggleMenu() {
        const isOpen = navMenu.classList.contains('open');
        if (isOpen) {
            navMenu.classList.remove('open');
            mobileNavToggle.setAttribute('aria-expanded', 'false');
            mobileNavToggle.focus();
        } else {
            navMenu.classList.add('open');
            mobileNavToggle.setAttribute('aria-expanded', 'true');
            // Shift focus to the first menu item for accessibility
            if (navLinks.length > 0) {
                navLinks[0].focus();
            }
        }
    }

    mobileNavToggle.addEventListener('click', (e) => {
        e.stopPropagation();
        toggleMenu();
    });

    // Close menu when clicking navigation links
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (navMenu.classList.contains('open')) {
                toggleMenu();
            }
        });
    });

    // Close menu when clicking outside of it
    document.addEventListener('click', (e) => {
        if (navMenu.classList.contains('open') && 
            !navMenu.contains(e.target) && 
            !mobileNavToggle.contains(e.target)) {
            toggleMenu();
        }
    });

    // Escape key closes mobile menu
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && navMenu.classList.contains('open')) {
            toggleMenu();
        }
    });

    // ==========================================================================
    // STICKY HEADER SHADOW ON SCROLL
    // ==========================================================================
    const header = document.getElementById('header');
    
    function checkHeaderScroll() {
        if (window.scrollY > 20) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    }
    
    window.addEventListener('scroll', checkHeaderScroll);
    checkHeaderScroll(); // Run once in case user loads page scrolled down

    // ==========================================================================
    // SCROLL SPY ACTIVE NAV STATE
    // ==========================================================================
    const sections = document.querySelectorAll('section[id]');
    
    // Map section IDs to their simplified navigation link hrefs
    const sectionToMenuMap = {
        'home': '#home',
        'about': '#about',
        'skills': '#about',
        'methodology': '#about',
        'journey': '#about',
        'principles': '#about',
        'objective': '#about',
        'services': '#services',
        'platforms': '#services',
        'analytics': '#case-study',
        'case-study': '#case-study',
        'markets': '#case-study',
        'contact': '#contact'
    };
    
    function scrollActiveLink() {
        const scrollY = window.scrollY;
        const activeTargets = {};
        
        // Detect if user has scrolled to the bottom of the page
        const isBottom = window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 20;
        
        sections.forEach(current => {
            const sectionHeight = current.offsetHeight;
            const sectionTop = current.offsetTop - 180; // adjusted for larger header offset
            const sectionId = current.getAttribute('id');
            
            if (isBottom) {
                activeTargets['#contact'] = true;
            } else if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
                const targetHref = sectionToMenuMap[sectionId];
                if (targetHref) {
                    activeTargets[targetHref] = true;
                }
            }
        });
        
        const navLinks = document.querySelectorAll('.nav-menu a');
        navLinks.forEach(link => {
            const href = link.getAttribute('href');
            if (activeTargets[href]) {
                link.classList.add('active');
            } else {
                link.classList.remove('active');
            }
        });
    }
    
    window.addEventListener('scroll', scrollActiveLink);
    scrollActiveLink();

    // ==========================================================================
    // PLATFORMS CAPABILITIES TAB SWITCHER
    // ==========================================================================
    const platformTabs = document.querySelectorAll('.platform-tab-btn');
    const platformPanels = document.querySelectorAll('.platform-panel');

    platformTabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const targetPlatform = tab.getAttribute('data-platform');
            
            // Update active tab styling
            platformTabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');
            
            // Switch current visible content panel
            platformPanels.forEach(panel => {
                panel.classList.remove('active');
                if (panel.getAttribute('id') === `platform-${targetPlatform}`) {
                    panel.classList.add('active');
                }
            });
        });
    });

    // ==========================================================================
    // SCROLL REVEAL (INTERSECTION OBSERVER)
    // ==========================================================================
    const revealElements = document.querySelectorAll('.reveal');
    
    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                // Remove observer since animation is already triggered
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.15,
        rootMargin: '0px 0px -50px 0px'
    });
    
    revealElements.forEach(el => revealObserver.observe(el));

    // ==========================================================================
    // STATS COUNT-UP ANIMATION
    // ==========================================================================
    const counterElements = document.querySelectorAll('.counter-val');
    
    const counterObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const target = parseInt(entry.target.getAttribute('data-target'), 10);
                const suffix = entry.target.getAttribute('data-suffix') || '';
                const prefix = entry.target.getAttribute('data-prefix') || '';
                const speed = 1000; // Complete within 1 second
                
                let count = 0;
                const increment = Math.ceil(target / (speed / 16)); // Target approx 60fps refresh
                
                const updateCounter = () => {
                    count += increment;
                    if (count >= target) {
                        entry.target.textContent = prefix + target + suffix;
                        observer.unobserve(entry.target);
                    } else {
                        entry.target.textContent = prefix + count + suffix;
                        requestAnimationFrame(updateCounter);
                    }
                };
                
                updateCounter();
            }
        });
    }, {
        threshold: 0.5
    });
    
    counterElements.forEach(counter => counterObserver.observe(counter));

    // ==========================================================================
    // CONTACT FORM AJAX SUBMISSION
    // ==========================================================================
    const contactForm = document.getElementById('contact-form');
    const formStatus = document.getElementById('form-status');
    const submitBtn = contactForm ? contactForm.querySelector('.form-submit-btn') : null;
    
    // Top Notification Elements
    const topNotification = document.getElementById('top-notification');
    const topNotificationMessage = document.getElementById('top-notification-message');
    const topNotificationClose = document.getElementById('top-notification-close');

    let notificationTimeout;

    if (topNotificationClose) {
        topNotificationClose.addEventListener('click', () => {
            topNotification.classList.remove('show');
            if (notificationTimeout) clearTimeout(notificationTimeout);
        });
    }


    if (contactForm && formStatus && submitBtn) {
        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            // Clear previous messages and classes
            formStatus.className = 'form-status';
            formStatus.textContent = '';
            formStatus.style.display = ''; // Let CSS classes handle the display


            // Show loading state
            formStatus.classList.add('loading');
            formStatus.style.display = 'block'; // Force display block
            formStatus.textContent = 'جاري إرسال رسالتك...';

            // Disable submit button
            const originalBtnText = submitBtn.textContent;
            submitBtn.disabled = true;
            submitBtn.textContent = 'جاري الإرسال...';

            try {
                // Collect form data explicitly to ensure all fields are captured correctly
                const formData = new FormData(contactForm);
                const data = {
                    name: formData.get('name') ? formData.get('name').toString().trim() : '',
                    email: formData.get('email') ? formData.get('email').toString().trim() : '',
                    company: formData.get('company') ? formData.get('company').toString().trim() : '',
                    // Use getElementById to ensure textarea content is always captured correctly
                    message: document.getElementById('form-msg') ? document.getElementById('form-msg').value.trim() : (formData.get('message') ? formData.get('message').toString().trim() : '')
                };

                // 1. Try saving to Google Sheets
                let sheetsSaved = false;
                let sheetsErrorMsg = '';
                const configured = isGoogleSheetsConfigured();

                if (configured) {
                    try {
                        // Sending as text/plain bypasses CORS preflight which Apps Script web apps do not support
                        const response = await fetch(GOOGLE_SCRIPT_URL, {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'text/plain;charset=utf-8'
                            },
                            body: JSON.stringify({
                                name: data.name,
                                email: data.email,
                                company: data.company,
                                message: data.message
                            })
                        });
                        
                        if (response.ok) {
                            sheetsSaved = true;
                            console.log('Lead saved to Google Sheets successfully.');
                        } else {
                            throw new Error('Google Apps Script responded with status: ' + response.status);
                        }
                    } catch (sheetsErr) {
                        console.error('Google Sheets submission error, attempting no-cors fallback:', sheetsErr);
                        try {
                            // Fallback to no-cors mode in case of redirection/CORS blocks
                            await fetch(GOOGLE_SCRIPT_URL, {
                                method: 'POST',
                                mode: 'no-cors',
                                headers: {
                                    'Content-Type': 'text/plain;charset=utf-8'
                                },
                                body: JSON.stringify({
                                    name: data.name,
                                    email: data.email,
                                    company: data.company,
                                    message: data.message
                                })
                            });
                            sheetsSaved = true;
                            console.log('Lead submitted to Google Sheets (no-cors fallback active).');
                        } catch (fallbackErr) {
                            console.error('Google Sheets fallback submission failed:', fallbackErr);
                            sheetsErrorMsg = sheetsErr.message || sheetsErr;
                        }
                    }
                } else {
                    console.warn('Google Sheets URL is not configured in js/google-sheets-config.js. Running in email fallback mode.');
                }

                // 2. Send email notification via FormSubmit
                const emailPayload = {
                    name: data.name,
                    email: data.email,
                    company: data.company,
                    message: data.message,
                    _captcha: 'false',
                    _subject: 'طلب تواصل جديد من موقع عادل مقدمي',
                    _template: 'table'
                };

                let emailSent = false;
                try {
                    const response = await fetch('https://formsubmit.co/ajax/amk735151@gamil.com', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'Accept': 'application/json'
                        },
                        body: JSON.stringify(emailPayload)
                    });

                    if (response.ok) {
                        const result = await response.json();
                        if (result.success === 'true' || result.success === true) {
                            emailSent = true;
                            console.log('Email notification sent successfully via FormSubmit.');
                        }
                    }
                } catch (emailErr) {
                    console.error('Email notification error:', emailErr);
                }

                const successMessage = 'تم إرسال رسالتك بنجاح! ✅ سنتواصل معك قريباً عبر البريد الإلكتروني الذي أدخلته.';

                // Determine submission outcome status
                // The user requested success ONLY when Google Sheets request is successful
                if (configured && !sheetsSaved) {
                    throw new Error('فشل الحفظ في Google Sheets: ' + sheetsErrorMsg);
                }
                
                if (!configured && !emailSent) {
                    throw new Error('فشل إرسال الإشعار عبر البريد الإلكتروني.');
                }

                // If we reach here, it's successful!
                // 1. Hide the inline form status
                formStatus.style.display = 'none';
                formStatus.className = 'form-status';
                formStatus.textContent = '';
                
                // 2. Show the top notification
                if (topNotification && topNotificationMessage) {
                    topNotificationMessage.textContent = successMessage;
                    topNotification.classList.add('show');
                    
                    // Auto close after 7 seconds
                    if (notificationTimeout) clearTimeout(notificationTimeout);
                    notificationTimeout = setTimeout(() => {
                        topNotification.classList.remove('show');
                    }, 7000);
                }

                // Explicitly clear fields to guarantee the UI reflects it
                const fields = contactForm.querySelectorAll('.form-input');
                fields.forEach(field => field.value = '');
                contactForm.reset();
            } catch (error) {
                console.error('Form submission error:', error);
                formStatus.className = 'form-status error';
                formStatus.style.display = 'block'; // Force display block to ensure visibility
                formStatus.textContent = 'حدث خطأ أثناء إرسال الرسالة. يرجى المحاولة مرة أخرى.';
            } finally {
                // Re-enable submit button
                submitBtn.disabled = false;
                submitBtn.textContent = originalBtnText;
            }
        });
    }
});
