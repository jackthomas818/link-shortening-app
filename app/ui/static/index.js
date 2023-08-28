document.addEventListener("DOMContentLoaded", function () {
    const shortenBtn = document.getElementById("shortenButton");
    const longUrlInput = document.getElementById("longUrl");
    const shortUrlText = document.getElementById("shortUrl");

    shortenBtn.addEventListener("click", async function () {
        const longUrl = longUrlInput.value;

        if (longUrl) {
            try {
                const response = await fetch("http://localhost:5000/shorten/", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        long_url: longUrl
                    })
                });

                if (response.ok) {
                    const data = await response.json();
                    shortUrlText.textContent = `Shortened URL: ${data.short_url}`;
                } else {
                    const errorData = await response.json();
                    shortUrlText.textContent = `Error: ${errorData.error}`;
                }

            } catch (error) {
                shortUrlText.textContent = `Error: ${error.message}`;
            }

        } else {
            shortUrlText.textContent = "Please enter a long URL.";
        }
    })

});