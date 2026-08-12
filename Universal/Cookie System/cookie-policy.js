document.addEventListener("DOMContentLoaded", function() {
    // 1. Inject Scroll-to-Top CSS if missing
    let basePath = "";
    const scripts = document.getElementsByTagName('script');
    for (let i = 0; i < scripts.length; i++) {
        if (scripts[i].src && scripts[i].src.includes("scroll-to-top.js")) {
            const src = scripts[i].src;
            basePath = src.substring(0, src.indexOf("scroll-to-top.js"));
            break;
        }
    }
    if (basePath) {
        const link = document.createElement("link");
        link.rel = "stylesheet";
        link.href = basePath + "../css/scroll-to-top.css";
        document.head.appendChild(link);
    }

    // 2. Inject Cookie CSS
    if (!document.getElementById("cookie-policy-styles")) {
        const styleTag = document.createElement("style");
        styleTag.id = "cookie-policy-styles";
        styleTag.textContent = `
            .cookie-widget-btn {
                position: fixed !important;
                bottom: 30px !important;
                left: 30px !important;
                width: 56px !important;
                height: 56px !important;
                background-color: #f37021 !important;
                border-radius: 50% !important;
                display: flex !important;
                justify-content: center !important;
                align-items: center !important;
                cursor: pointer !important;
                box-shadow: 0 4px 15px rgba(243, 112, 33, 0.4) !important;
                z-index: 2147483647 !important;
                transition: background-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease !important;
            }
            .cookie-widget-btn:hover {
                background-color: #ffffff !important;
                transform: scale(1.1) !important;
                box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25) !important;
            }
            .cookie-widget-btn svg {
                width: 28px !important;
                height: 28px !important;
                fill: #ffffff !important;
                transition: fill 0.3s ease !important;
            }
            .cookie-widget-btn:hover svg {
                fill: #f37021 !important;
            }
            .cookie-modal-overlay {
                position: fixed !important;
                top: 0 !important;
                left: 0 !important;
                width: 100vw !important;
                height: 100vh !important;
                background-color: rgba(0, 0, 0, 0.65) !important;
                backdrop-filter: blur(4px) !important;
                z-index: 2147483647 !important;
                display: flex !important;
                justify-content: center !important;
                align-items: center !important;
                opacity: 0 !important;
                pointer-events: none !important;
                transition: opacity 0.3s ease !important;
                padding: 16px !important;
                box-sizing: border-box !important;
            }
            .cookie-modal-overlay.active {
                opacity: 1 !important;
                pointer-events: auto !important;
            }
            .cookie-modal {
                background-color: #ffffff !important;
                border-radius: 16px !important;
                width: 90% !important;
                max-width: 480px !important;
                padding: 24px 24px 28px 24px !important;
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3) !important;
                transform: translateY(20px) !important;
                transition: transform 0.3s ease !important;
                font-family: 'Outfit', 'Inter', system-ui, -apple-system, sans-serif !important;
                color: #222222 !important;
                box-sizing: border-box !important;
            }
            .cookie-modal-overlay.active .cookie-modal {
                transform: translateY(0) !important;
            }
            .cookie-modal-header {
                display: flex !important;
                justify-content: space-between !important;
                align-items: center !important;
                margin-bottom: 12px !important;
            }
            .cookie-modal-title {
                font-size: 20px !important;
                font-weight: 700 !important;
                margin: 0 !important;
                color: #111111 !important;
            }
            .cookie-modal-close {
                background: none !important;
                border: none !important;
                font-size: 24px !important;
                cursor: pointer !important;
                color: #888888 !important;
                transition: color 0.2s ease !important;
                line-height: 1 !important;
                padding: 0 !important;
            }
            .cookie-modal-close:hover {
                color: #f37021 !important;
            }
            .cookie-modal-body {
                font-size: 13.5px !important;
                line-height: 1.5 !important;
                color: #555555 !important;
                margin-bottom: 16px !important;
            }
            .cookie-modal-body p {
                margin-top: 0 !important;
                margin-bottom: 12px !important;
            }
            .cookie-toggles {
                margin-top: 10px !important;
                margin-bottom: 10px !important;
            }
            .cookie-toggle-row {
                display: flex !important;
                justify-content: space-between !important;
                align-items: center !important;
                padding: 10px 0 !important;
                border-bottom: 1px solid #eeeeee !important;
                gap: 16px !important;
            }
            .cookie-toggle-row:last-child {
                border-bottom: none !important;
            }
            .cookie-toggle-label {
                font-weight: 600 !important;
                color: #111111 !important;
                font-size: 14px !important;
            }
            .cookie-toggle-desc {
                font-size: 11.5px !important;
                color: #777777 !important;
                margin-top: 2px !important;
            }
            .cookie-switch {
                position: relative !important;
                display: inline-block !important;
                width: 42px !important;
                height: 22px !important;
                flex-shrink: 0 !important;
            }
            .cookie-switch input {
                opacity: 0 !important;
                width: 0 !important;
                height: 0 !important;
            }
            .cookie-slider {
                position: absolute !important;
                cursor: pointer !important;
                top: 0; left: 0; right: 0; bottom: 0;
                background-color: #cccccc !important;
                transition: .4s !important;
                border-radius: 22px !important;
            }
            .cookie-slider:before {
                position: absolute !important;
                content: "" !important;
                height: 16px !important;
                width: 16px !important;
                left: 3px !important;
                bottom: 3px !important;
                background-color: white !important;
                transition: .4s !important;
                border-radius: 50% !important;
            }
            input:checked + .cookie-slider {
                background-color: #f37021 !important;
            }
            input:checked + .cookie-slider:before {
                transform: translateX(20px) !important;
            }
            input:disabled + .cookie-slider {
                background-color: #f37021 !important;
                opacity: 0.6 !important;
                cursor: not-allowed !important;
            }
            .cookie-modal-footer {
                display: flex !important;
                flex-direction: column !important;
                gap: 8px !important;
                align-items: stretch !important;
                width: 100% !important;
            }
            .cookie-btn {
                width: 100% !important;
                padding: 12px 16px !important;
                border-radius: 8px !important;
                font-weight: 600 !important;
                font-size: 14px !important;
                cursor: pointer !important;
                transition: all 0.2s ease !important;
                border: none !important;
                font-family: inherit !important;
                margin: 0 !important;
                text-align: center !important;
                box-sizing: border-box !important;
            }
            .cookie-btn-secondary {
                background-color: #f1f3f7 !important;
                color: #333333 !important;
            }
            .cookie-btn-secondary:hover {
                background-color: #e2e5ec !important;
            }
            .cookie-btn-primary {
                background-color: #f37021 !important;
                color: #ffffff !important;
            }
            .cookie-btn-primary:hover {
                background-color: #d95a10 !important;
            }
            
            @media screen and (max-width: 600px) {
                .cookie-modal-overlay {
                    align-items: center !important;
                    justify-content: center !important;
                    padding: 16px !important;
                }
                .cookie-modal {
                    width: 92% !important;
                    max-width: 400px !important;
                    border-radius: 16px !important;
                    padding: 18px 18px 22px 18px !important;
                    max-height: 94vh !important;
                    overflow-y: auto !important;
                }
                .cookie-modal-title {
                    font-size: 18px !important;
                }
                .cookie-modal-body {
                    font-size: 12.5px !important;
                    line-height: 1.45 !important;
                    margin-bottom: 12px !important;
                }
                .cookie-modal-body p {
                    margin-bottom: 8px !important;
                }
                .cookie-toggle-row {
                    padding: 8px 0 !important;
                }
                .cookie-toggle-label {
                    font-size: 13.5px !important;
                }
                .cookie-toggle-desc {
                    font-size: 11px !important;
                }
                .cookie-btn {
                    padding: 11px 14px !important;
                    font-size: 13.5px !important;
                    border-radius: 8px !important;
                }
            }
        `;
        document.head.appendChild(styleTag);
    }

    // 3. Inject Widget & Modal HTML
    if (!document.getElementById("cookieWidgetBtn")) {
        const btnContainer = document.createElement("div");
        btnContainer.innerHTML = `
            <div id="scrollToTopBtn" class="scroll-to-top-btn" title="Scroll to top">
                <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <polyline points="18 15 12 9 6 15" stroke-linecap="round" stroke-linejoin="round"></polyline>
                </svg>
            </div>

            <div class="cookie-widget-btn" id="cookieWidgetBtn" title="Cookie Preferences">
                <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path d="M21.598 11.064a1.006 1.006 0 0 0-.854-.172A2.938 2.938 0 0 1 20 11c-1.654 0-3-1.346-3-3 0-.24.03-.47.086-.69a1.005 1.005 0 0 0-1.261-1.261A2.955 2.955 0 0 1 15 6c-1.654 0-3-1.346-3-3 0-.17.016-.336.043-.5a1.004 1.004 0 0 0-1.127-1.127A9.957 9.957 0 0 0 2 12c0 5.514 4.486 10 10 10s10-4.486 10-10c0-.323-.016-.64-.047-.954a1.006 1.006 0 0 0-.355-.682zM12 20c-4.411 0-8-3.589-8-8a7.962 7.962 0 0 1 6.006-7.75A5.006 5.006 0 0 0 15 9l.101-.001a5.007 5.007 0 0 0 4.837 4C19.444 16.941 16.071 20 12 20z"/>
                    <circle cx="7.5" cy="14.5" r="1.5"/>
                    <circle cx="12" cy="11" r="1.5"/>
                    <circle cx="15.5" cy="16.5" r="1.5"/>
                    <circle cx="8" cy="9" r="1"/>
                </svg>
            </div>

            <div class="cookie-modal-overlay" id="cookieModalOverlay">
                <div class="cookie-modal">
                    <div class="cookie-modal-header">
                        <h3 class="cookie-modal-title">Cookie Preferences</h3>
                        <button class="cookie-modal-close" id="cookieModalClose">&times;</button>
                    </div>
                    <div class="cookie-modal-body">
                        <p>We use cookies to enhance your browsing experience, serve personalized ads or content, and analyze our traffic. By clicking "Accept All", you consent to our use of cookies.</p>
                        
                        <div class="cookie-toggles">
                            <div class="cookie-toggle-row">
                                <div>
                                    <div class="cookie-toggle-label">Essential Cookies</div>
                                    <div class="cookie-toggle-desc">Required for the website to function properly. Cannot be disabled.</div>
                                </div>
                                <label class="cookie-switch">
                                    <input type="checkbox" checked disabled>
                                    <span class="cookie-slider"></span>
                                </label>
                            </div>
                            <div class="cookie-toggle-row">
                                <div>
                                    <div class="cookie-toggle-label">Analytics Cookies</div>
                                    <div class="cookie-toggle-desc">Help us understand how visitors interact with the website.</div>
                                </div>
                                <label class="cookie-switch">
                                    <input type="checkbox" id="cookieAnalytics">
                                    <span class="cookie-slider"></span>
                                </label>
                            </div>
                            <div class="cookie-toggle-row">
                                <div>
                                    <div class="cookie-toggle-label">Marketing Cookies</div>
                                    <div class="cookie-toggle-desc">Used to track visitors across websites to display relevant ads.</div>
                                </div>
                                <label class="cookie-switch">
                                    <input type="checkbox" id="cookieMarketing">
                                    <span class="cookie-slider"></span>
                                </label>
                            </div>
                        </div>
                    </div>
                    
                    <div class="cookie-modal-footer">
                        <button class="cookie-btn cookie-btn-primary" id="cookieAcceptAllBtn">Accept All</button>
                        <button class="cookie-btn cookie-btn-primary" id="cookieRejectAllBtn">Reject All</button>
                        <button class="cookie-btn cookie-btn-secondary" id="cookieSaveBtn">Save Preferences</button>
                    </div>
                </div>
            </div>
        `;
        document.body.appendChild(btnContainer);
    }

    // 4. Scroll to Top Logic
    const scrollToTopBtn = document.getElementById("scrollToTopBtn");
    if (scrollToTopBtn) {
        window.addEventListener("scroll", function() {
            if (window.scrollY > 500) {
                scrollToTopBtn.classList.add("visible");
            } else {
                scrollToTopBtn.classList.remove("visible");
            }
        });
        scrollToTopBtn.addEventListener("click", function() {
            window.scrollTo({ top: 0, behavior: "smooth" });
        });
    }

    // 5. Cookie Modal Logic
    const cookieBtn = document.getElementById("cookieWidgetBtn");
    const overlay = document.getElementById("cookieModalOverlay");
    const closeBtn = document.getElementById("cookieModalClose");
    const saveBtn = document.getElementById("cookieSaveBtn");
    const acceptAllBtn = document.getElementById("cookieAcceptAllBtn");
    const rejectAllBtn = document.getElementById("cookieRejectAllBtn");
    const checkAnalytics = document.getElementById("cookieAnalytics");
    const checkMarketing = document.getElementById("cookieMarketing");

    const triggerGA4 = (analyticsGranted) => {
        if (typeof window.gtag === 'function') {
            window.gtag('consent', 'update', { 'analytics_storage': analyticsGranted ? 'granted' : 'denied' });
            if (analyticsGranted) {
                window.gtag('event', 'page_view', {
                    page_title: document.title,
                    page_location: window.location.href,
                    page_path: window.location.pathname
                });
            }
        }
    };

    const loadPreferences = () => {
        const prefs = JSON.parse(localStorage.getItem("cookiePreferences"));
        if (prefs) {
            if (checkAnalytics) checkAnalytics.checked = prefs.analytics;
            if (checkMarketing) checkMarketing.checked = prefs.marketing;
            triggerGA4(prefs.analytics);
        } else {
            // Auto open modal on first visit
            setTimeout(() => { 
                if (overlay) overlay.classList.add("active"); 
            }, 300);
            triggerGA4(true);
        }
    };

    const savePreferences = (analytics, marketing) => {
        localStorage.setItem("cookiePreferences", JSON.stringify({
            essential: true,
            analytics: analytics,
            marketing: marketing
        }));
        if (overlay) overlay.classList.remove("active");
        triggerGA4(analytics);
    };

    if (cookieBtn) {
        cookieBtn.addEventListener("click", (e) => {
            e.preventDefault();
            e.stopPropagation();
            if (overlay) overlay.classList.add("active");
        });
    }

    if (closeBtn) {
        closeBtn.addEventListener("click", (e) => {
            e.preventDefault();
            if (overlay) overlay.classList.remove("active");
        });
    }

    if (overlay) {
        overlay.addEventListener("click", (e) => {
            if (e.target === overlay) overlay.classList.remove("active");
        });
    }

    if (saveBtn) {
        saveBtn.addEventListener("click", (e) => {
            e.preventDefault();
            savePreferences(checkAnalytics ? checkAnalytics.checked : true, checkMarketing ? checkMarketing.checked : false);
        });
    }

    if (acceptAllBtn) {
        acceptAllBtn.addEventListener("click", (e) => {
            e.preventDefault();
            if (checkAnalytics) checkAnalytics.checked = true;
            if (checkMarketing) checkMarketing.checked = true;
            savePreferences(true, true);
        });
    }

    if (rejectAllBtn) {
        rejectAllBtn.addEventListener("click", (e) => {
            e.preventDefault();
            if (checkAnalytics) checkAnalytics.checked = false;
            if (checkMarketing) checkMarketing.checked = false;
            savePreferences(false, false);
        });
    }

    loadPreferences();
});
