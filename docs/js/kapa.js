document.addEventListener("DOMContentLoaded", function () {
    const container = document.querySelector("#docsearch");
    if (!container) return;

    const btn = document.createElement("button");
    btn.id = "ask-percona-ai";

    // Use a span for the star so we can style it
    btn.innerHTML = `<span class="percona-star">✨</span> <span class="percona-text">Ask Percona AI</span>`;

    container.appendChild(btn);

    btn.addEventListener("click", function () {
        if (window.Kapa) window.Kapa.open();
    });

    // Load Kapa widget
    (function () {
        var script = document.createElement("script");
        script.src = "https://widget.kapa.ai/kapa-widget.bundle.js";
        script.setAttribute("data-website-id", "YOUR_KAPA_ID");
        script.setAttribute("data-modal-disclaimer",
            "The Percona AI Assistant helps you find simple, clear answers to your Percona questions using official documentation, resolved forum posts, and blog posts."
        );
        script.setAttribute("data-modal-override-open-selector", "#ask-percona-ai");
        script.setAttribute("data-button-hide", "true");
        document.head.appendChild(script);
    })();
});