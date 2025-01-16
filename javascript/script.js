document.addEventListener("DOMContentLoaded", () => {
    const requestButton = document.querySelector(".request-button");
    const methodSelect = document.querySelector(".method-select");
    const urlInput = document.querySelector(".url-input");
    const responseArea = document.querySelector(".response-area");

    requestButton.addEventListener("click", async () => {
        const url = urlInput.value;
        const method = methodSelect.value;

        if (!url) {
            alert("Please enter a URL.");
            return;
        }

        try {
            const response = await fetch(url, { method });
            const data = await response.json();
            responseArea.value = JSON.stringify(data, null, 2);
        } catch (error) {
            responseArea.value = `Error: ${error.message}`;
        }
    });
});
