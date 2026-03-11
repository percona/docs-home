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