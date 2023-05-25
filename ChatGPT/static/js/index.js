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
            window.location.href = "process/";
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function redirectToPrompt() {
    window.location.href = "prompt/";
}

function sendDataToProcessPrompt() {
    // Get the user input from the textarea
    var userPrompt = document.getElementsByName("message")[0].value;
  
    // Create a new form data object
    var formData = new FormData();
    formData.append("message", userPrompt);
  
    // Create a new XMLHttpRequest object
    var xhr = new XMLHttpRequest();
  
    // Set up the POST request
    xhr.open("POST", "/process/prompt/", true);
    xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
  
    // Define the callback function when the request completes
    xhr.onload = function () {
      if (xhr.status === 200) {
        // Request was successful
        console.log(xhr.responseText);
        // Redirect or handle the response as needed
        window.location.href = "/";
      } else {
        // Request failed
        console.error("Error:", xhr.status);
      }
    };
  
    // Send the form data
    xhr.send(formData);
  }
  
  // Helper function to get the CSRF token
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}