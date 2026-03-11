(function () {
    const KAPA_ID = "YOUR_KAPA_ID";

    function insertButton() {
        const searchContainer = document.querySelector("#docsearch");
        if (!searchContainer) return;

        if (document.querySelector("#ask-percona-ai")) return;

        const btn = document.createElement("button");
        btn.id = "ask-percona-ai";
        btn.type = "button";
        btn.className = "md-button percona-ai-button";
        btn.textContent = "✨ Ask Percona AI";

        const algoliaBtn = searchContainer.querySelector(".DocSearch");
        if (algoliaBtn) {
            algoliaBtn.parentNode.insertBefore(btn, algoliaBtn.nextSibling);
        } else {
            searchContainer.appendChild(btn);
        }

        // Load Kapa script if not loaded
        if (!document.querySelector(`script[data-website-id='${KAPA_ID}']`)) {
            const script = document.createElement("script");
            script.src = "https://widget.kapa.ai/kapa-widget.bundle.js";
            script.setAttribute("data-website-id", KAPA_ID);
            script.setAttribute(
                "data-modal-disclaimer",
                "The Percona AI Assistant helps you find simple, clear answers to your Percona questions using official documentation, resolved forum posts, and blog posts."
            );
            script.setAttribute("data-modal-override-open-selector", "#ask-percona-ai");
            script.setAttribute("data-button-hide", "true");
            document.head.appendChild(script);
        }

        btn.addEventListener("click", function () {
            if (window.Kapa) {
                window.Kapa.open();
            }
        });
    }

    const observer = new MutationObserver(() => {
        insertButton();
    });

    observer.observe(document.body, { childList: true, subtree: true });

    document.addEventListener("DOMContentLoaded", insertButton);
})();