function executePrompt(cardId) {
    event.preventDefault();
    let prompt = "";

    if (cardId === 1) {
        prompt = "You are a hotel assistant for Wynn Las Vegas and answer all the queries asked by guests. Your task is to assist the guest and make their stay luxurious and memorable, while constantly asking questions before you answer to better grasp what the guest is looking for. Add a welcome letter of for the guest in every new conversation.";
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
            window.location.href = "process/";
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function redirectToPrompt() {
    window.location.href = "prompt/";
}

function sendDataToProcessPrompt(language) {
    var userPrompt = document.getElementsByName("message")[0].value;

    // Check if a language is provided and modify the prompt accordingly
    if (language) {
        userPrompt += " in " + language;
    }

    var formData = new FormData();
    formData.append("message", userPrompt);

    var xhr = new XMLHttpRequest();

    xhr.open("POST", "/process/prompt/", true);

    // Set the CSRF token in the request headers
    xhr.setRequestHeader("X-CSRFToken", getCSRFToken());

    // Define the callback function when the request completes
    xhr.onload = function () {
        if (xhr.status === 200) {
            console.log(xhr.responseText);
            window.location.reload();
        } else {
            console.error("Error:", xhr.status);
        }
    };

    // Send the request with the form data
    xhr.send(formData);
}

  
// Function to get the CSRF token from the HTML form
function getCSRFToken() {
  var csrfTokenElement = document.getElementsByName("csrfmiddlewaretoken")[0];
  return csrfTokenElement.value;
}