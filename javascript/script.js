document.addEventListener("DOMContentLoaded", () => {
    const requestButton = document.querySelector(".request-button");
    const urlInput = document.querySelector(".url-input");
    const responseArea = document.querySelector(".response-area");
    // Select all buttons inside the list-group
    const buttons = document.querySelectorAll('.list-group .list-group-item');

    // Log the buttons to confirm selection
    // console.log(buttons);

    // You can loop through them to perform actions
    buttons.forEach((button) => {
        button.addEventListener('click', () => {
            // console.log(`You clicked on: ${button.textContent}`);
            if (button.textContent === 'About') {
                // console.log('Setting url to aboutme');
                urlInput.value = 'http://127.0.0.1:5000/aboutme';
            }
        });
    });

    requestButton.addEventListener("click", async () => {
        const url = urlInput.value;
        const method = 'GET';

        if (!url) {
            alert("Please enter a URL.");
            return;
        }

        try {
            const response = await fetch(url, { method });
            const data = await response.json();
            responseArea.textContent = JSON.stringify(data, null, 2);
        } catch (error) {
            responseArea.textContent = `Error: ${error.message}`;
        }
    });
});
