document.addEventListener("DOMContentLoaded", function () {
    const container = document.querySelector("#docsearch");
    if (!container) return;
  
    // Prevent duplicate button
    if (document.querySelector("#ask-percona-ai")) return;
  
    // Create button
    const btn = document.createElement("button");
    btn.id = "ask-percona-ai";
    btn.innerHTML = `<span class="percona-star">✨</span><span class="percona-text">Ask Percona AI</span>`;
    container.appendChild(btn);
  
    // Load Kapa widget
    if (!window.kapaWidgetLoaded) {
      window.kapaWidgetLoaded = true;
  
      const script = document.createElement("script");
      script.src = "https://widget.kapa.ai/kapa-widget.bundle.js";
      script.async = true;
      script.setAttribute("data-website-id", "0e0d55cf-6370-4a6d-a987-96670a7fe935");
      script.setAttribute("data-button-hide", "true");
      script.setAttribute("data-modal-override-open-selector", "#ask-percona-ai");
      script.setAttribute(
        "data-modal-disclaimer",
        "The **Percona AI Assistant** helps you find clear answers using official documentation, resolved forum posts, and blog posts. Learn more in the [Percona documentation](https://docs.percona.com)."
      );
  
      // Once the script loads, enable the button
      script.onload = () => {
        btn.addEventListener("click", () => {
          if (window.Kapa && typeof window.Kapa.open === "function") {
            window.Kapa.open();
          }
        });
      };
  
      document.head.appendChild(script);
    }
  });
  