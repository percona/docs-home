document.addEventListener("DOMContentLoaded", function() {
    console.log("DOM fully loaded");

    // 1. Remove any pre-existing matching elements immediately
    const existingElements = document.querySelectorAll('.md-nav__title.md-nav__container');
    if (existingElements.length > 0) {
        console.log("Found pre-existing elements, removing them:", existingElements);
        existingElements.forEach(function(element) {
            element.remove(); // This completely removes the element and its space
        });
        // Trigger a reflow after removing the elements to update the layout
        document.body.offsetHeight; // Accessing this forces a reflow
    }

    // 2. Use MutationObserver to watch for new elements being added dynamically
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            mutation.addedNodes.forEach(function(node) {
                if (node.nodeType === 1 && node.matches('.md-nav__title.md-nav__container')) {
                    console.log("Found new element via MutationObserver, removing it:", node);
                    node.remove(); // Remove the element as soon as it's added
                }
            });
        });
    });

    // Start observing the document body for added child nodes
    observer.observe(document.body, {
        childList: true,  // Watch for new elements being added
        subtree: true      // Watch all descendants of the body
    });
});

