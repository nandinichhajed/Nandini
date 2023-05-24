function executePrompt(cardId) {
    event.preventDefault();
    let prompt = "";

    if (cardId === 1) {
        prompt = "Hello ChatGPT";
    } else if (cardId === 2) {
        prompt = "Hello I am nandini";
    }
    // Send a POST request to the Django API endpoint
    fetch('/hotelName/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt }),
    })
        .then(response => response.json())
        .then(data => {
            // Handle the response from the API
            console.log(data.response);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}