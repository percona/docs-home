// "Ask Percona AI" button.
// The Kapa widget itself (with all its data-* config) is loaded from
// main.html as a markup <script data-osano="ESSENTIAL">, so Osano doesn't
// block it. This file only creates the button and opens the widget via
// Kapa's JS API, so it works no matter which one loads first.
(function () {
    function createAIButton() {
        const container = document.querySelector("#docsearch");
        if (!container) {
            // Algolia DocSearch may not have rendered yet - try again shortly
            setTimeout(createAIButton, 50);
            return;
        }
        if (document.getElementById("ask-percona-ai")) return;

        const button = document.createElement("button");
        button.id = "ask-percona-ai";
        button.type = "button";
        button.innerHTML = `<span class="percona-star">✨</span><span class="percona-text">Ask Percona AI</span>`;

        button.addEventListener("click", function (event) {
            event.preventDefault();
            event.stopPropagation(); // don't let the click open DocSearch
            if (window.Kapa && typeof window.Kapa.open === "function") {
                window.Kapa.open();
            } else {
                console.warn("Kapa widget not loaded yet (blocked or still loading).");
            }
        });

        container.appendChild(button);
    }

    createAIButton();
})();
