(function() {
    function createAIButton() {
        const container = document.querySelector("#docsearch");
        if (!container || document.getElementById("ask-percona-ai")) return;

        const button = document.createElement("button");
        button.id = "ask-percona-ai";
        button.innerHTML = `<span class="percona-star">✨</span><span class="percona-text">Ask Percona AI</span>`;
        container.appendChild(button);
    }

    function loadKapa() {
        if (window.kapaWidgetLoaded) return;
        const button = document.getElementById("ask-percona-ai");
        if (!button) {
            setTimeout(loadKapa, 50);
            return;
        }

        window.kapaWidgetLoaded = true;

        const script = document.createElement("script");
        script.src = "https://widget.kapa.ai/kapa-widget.bundle.js";
        script.async = true;

        // Required config
        script.setAttribute("data-website-id", "0e0d55cf-6370-4a6d-a987-96670a7fe935");
        script.setAttribute("data-modal-override-open-selector", "#ask-percona-ai");
        script.setAttribute("data-button-hide", "true");
        script.setAttribute("data-project-name", "Percona");
        script.setAttribute("data-modal-title", "Percona AI Assistant");
        script.setAttribute("font-size", "0.875rem");

        // Modal content
        script.setAttribute(
            "data-modal-disclaimer",
            "The **Percona AI Assistant** helps you find simple, clear answers to your Percona questions using [official documentation](https://docs.percona.com/), resolved [forum posts](https://forums.percona.com/) and [blog posts](https://www.percona.com/blog/). Note, do not enter personal or confidential information. Before using Percona AI assistant, read the [Legal Notice](https://homepage-pr-245.onrender.com/new/legal-notice)."
        );

        script.setAttribute(
            "data-modal-example-questions",
            "How do I install Percona Server?, How do I get started with PMM?, Why should I use Percona Monitoring and Management (PMM)?, What free enterprise-grade features does Percona Server for MongoDB have?, What does Percona Transparent Data Encryption for PostgreSQL do?, What are Kubernetes-native Percona Operators?"
        );

        script.setAttribute(
            "data-project-logo",
            "https://homepage-pr-245.onrender.com/assets/percona-logomark-one-color-dark.png"
        );

        document.head.appendChild(script);
    }

    createAIButton();
    loadKapa();

    document.addEventListener("navigation.instant", () => {
        createAIButton();
        loadKapa();
    });
})();