// ==========================================================================
// AWWWARDS-LEVEL UI/UX UPGRADE JS
// Requires: Three.js, GSAP, ScrollTrigger
// ==========================================================================

document.addEventListener("DOMContentLoaded", () => {
    
    const isMobile = window.innerWidth < 768;

    // 1. Custom Magnetic Cursor
    const cursor = document.querySelector('.custom-cursor');
    const follower = document.querySelector('.cursor-follower');
    
    let mouseX = window.innerWidth / 2;
    let mouseY = window.innerHeight / 2;
    let followerX = window.innerWidth / 2;
    let followerY = window.innerHeight / 2;

    if (!isMobile && cursor && follower) {
        document.addEventListener('mousemove', (e) => {
            mouseX = e.clientX;
            mouseY = e.clientY;
            
            // Update CSS vars for spotlight
            document.documentElement.style.setProperty('--mouse-x', `${mouseX}px`);
            document.documentElement.style.setProperty('--mouse-y', `${mouseY}px`);
            
            // Move fast cursor dot immediately
            cursor.style.left = `${mouseX}px`;
            cursor.style.top = `${mouseY}px`;
        });

        // Smooth follow loop
        const loop = () => {
            followerX += (mouseX - followerX) * 0.15;
            followerY += (mouseY - followerY) * 0.15;
            follower.style.left = `${followerX}px`;
            follower.style.top = `${followerY}px`;
            requestAnimationFrame(loop);
        };
        loop();

        // Magnetic & Hover Effects on Buttons/Links
        const interactables = document.querySelectorAll('a, button, .card, .dashboard-card, .service-card');
        interactables.forEach(el => {
            el.addEventListener('mouseenter', () => {
                cursor.classList.add('hovering');
                follower.classList.add('hovering');
            });
            el.addEventListener('mouseleave', () => {
                cursor.classList.remove('hovering');
                follower.classList.remove('hovering');
                // Reset transform in case of magnetic button
                if (el.classList.contains('btn-cta') || el.tagName.toLowerCase() === 'button') {
                    gsap.to(el, { x: 0, y: 0, duration: 0.3, ease: 'power2.out' });
                }
            });
            
            // Magnetic effect on CTAs
            if (el.classList.contains('btn-cta') || el.tagName.toLowerCase() === 'button') {
                el.addEventListener('mousemove', (e) => {
                    const rect = el.getBoundingClientRect();
                    const centerX = rect.left + rect.width / 2;
                    const centerY = rect.top + rect.height / 2;
                    const deltaX = (e.clientX - centerX) * 0.3;
                    const deltaY = (e.clientY - centerY) * 0.3;
                    gsap.to(el, { x: deltaX, y: deltaY, duration: 0.3, ease: 'power2.out' });
                });
            }
        });
    }

    // 2. Hyper-Realistic 3D Tilt for Cards
    if (!isMobile) {
        const tiltCards = document.querySelectorAll('.card, .dashboard-card, .service-card, .platform-card, .journey-step, .stat-card');
        
        tiltCards.forEach(card => {
            // Add glare element inside card
            const glare = document.createElement('div');
            glare.classList.add('glare-element');
            card.appendChild(glare);

            card.addEventListener('mousemove', (e) => {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left; // x position within the element
                const y = e.clientY - rect.top;  // y position within the element
                
                const centerX = rect.width / 2;
                const centerY = rect.height / 2;
                
                const rotateX = ((y - centerY) / centerY) * -10; // max 10 deg
                const rotateY = ((x - centerX) / centerX) * 10;
                
                // Set glare position
                glare.style.setProperty('--glare-x', `${(x / rect.width) * 100}%`);
                glare.style.setProperty('--glare-y', `${(y / rect.height) * 100}%`);
                
                gsap.to(card, {
                    rotateX: rotateX,
                    rotateY: rotateY,
                    duration: 0.1,
                    ease: "none"
                });
            });
            
            card.addEventListener('mouseleave', () => {
                gsap.to(card, {
                    rotateX: 0,
                    rotateY: 0,
                    duration: 0.5,
                    ease: "power3.out"
                });
            });
        });
    }

    // 3. Three.js WebGL Particle Background
    const canvas = document.getElementById('webgl-canvas');
    if (canvas && typeof THREE !== 'undefined' && !isMobile) {
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
        
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

        // Create particles
        const particlesGeometry = new THREE.BufferGeometry();
        const particlesCount = 2000;
        
        const posArray = new Float32Array(particlesCount * 3);
        
        for(let i=0; i < particlesCount * 3; i++){
            // Range -5 to 5
            posArray[i] = (Math.random() - 0.5) * 10;
        }
        
        particlesGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
        
        // Electric Blue / Cyan colors matching the brand
        const particlesMaterial = new THREE.PointsMaterial({
            size: 0.005,
            color: 0x06b6d4, // Cyan
            transparent: true,
            opacity: 0.8,
            blending: THREE.AdditiveBlending
        });
        
        const particlesMesh = new THREE.Points(particlesGeometry, particlesMaterial);
        scene.add(particlesMesh);
        
        camera.position.z = 2;

        let targetX = 0;
        let targetY = 0;

        document.addEventListener('mousemove', (event) => {
            targetX = (event.clientX / window.innerWidth) - 0.5;
            targetY = (event.clientY / window.innerHeight) - 0.5;
        });

        const clock = new THREE.Clock();

        const animate = () => {
            const elapsedTime = clock.getElapsedTime();
            
            // Gentle continuous rotation
            particlesMesh.rotation.y = elapsedTime * 0.05;
            particlesMesh.rotation.x = elapsedTime * 0.02;

            // Follow mouse interactively
            particlesMesh.rotation.y += 0.05 * (targetX - particlesMesh.rotation.y);
            particlesMesh.rotation.x += 0.05 * (targetY - particlesMesh.rotation.x);
            
            // Breathing effect
            particlesMesh.position.z = Math.sin(elapsedTime * 0.5) * 0.2;

            renderer.render(scene, camera);
            requestAnimationFrame(animate);
        };
        
        animate();

        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        });
    }

    // 4. GSAP ScrollTrigger Animations (Cinematic Reveal)
    if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
        gsap.registerPlugin(ScrollTrigger);

        // Sections Reveal
        const sections = document.querySelectorAll('section');
        sections.forEach(sec => {
            gsap.fromTo(sec, 
                { opacity: 0, y: 50, filter: 'blur(10px)' }, 
                { 
                    opacity: 1, 
                    y: 0, 
                    filter: 'blur(0px)', 
                    duration: 1, 
                    ease: "power3.out",
                    scrollTrigger: {
                        trigger: sec,
                        start: "top 80%",
                        toggleActions: "play none none reverse"
                    }
                }
            );
        });

        // Staggered Entrance for Cards
        const cardContainers = document.querySelectorAll('.services-grid, .platforms-grid, .dashboard-grid');
        cardContainers.forEach(container => {
            const cards = container.children;
            gsap.fromTo(cards, 
                { opacity: 0, y: 30, filter: 'blur(5px)' }, 
                {
                    opacity: 1,
                    y: 0,
                    filter: 'blur(0px)',
                    duration: 0.8,
                    stagger: 0.1,
                    ease: "power2.out",
                    scrollTrigger: {
                        trigger: container,
                        start: "top 85%"
                    }
                }
            );
        });
    }

    // 5. Alive Metrics (Counters)
    const counters = document.querySelectorAll('.stat-value, .highlight-number');
    if (counters.length > 0) {
        // Need an IntersectionObserver since we don't want to conflict heavily with GSAP generic loops
        const observer = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const el = entry.target;
                    // Try to parse the text as number (remove non-digits if needed, but preserve format)
                    const text = el.innerText;
                    // Very simple counter animation: if it contains a number
                    const numberMatch = text.match(/[\d,.]+/);
                    if (numberMatch && !el.classList.contains('counted')) {
                        const originalValue = numberMatch[0];
                        const cleanValue = parseFloat(originalValue.replace(/,/g, ''));
                        
                        if (!isNaN(cleanValue)) {
                            el.classList.add('counted');
                            let count = { val: 0 };
                            gsap.to(count, {
                                val: cleanValue,
                                duration: 2,
                                ease: "power2.out",
                                onUpdate: function() {
                                    // format appropriately (rough estimate of decimals)
                                    let isFloat = originalValue.includes('.');
                                    let currentVal = isFloat ? count.val.toFixed(2) : Math.floor(count.val);
                                    
                                    // if original had a percentage or dollar sign, replace just the number
                                    el.innerText = text.replace(originalValue, currentVal);
                                }
                            });
                        }
                    }
                    observer.unobserve(el);
                }
            });
        }, { threshold: 0.5 });

        counters.forEach(c => observer.observe(c));
    }

    // 6. Shine Sweep on Buttons
    const buttons = document.querySelectorAll('.btn-cta');
    setInterval(() => {
        buttons.forEach(btn => {
            btn.classList.add('shine-sweep');
            setTimeout(() => {
                btn.classList.remove('shine-sweep');
            }, 1000);
        });
    }, 4000); // Every 4 seconds

});
