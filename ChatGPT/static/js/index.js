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

function sendDataToProcessPrompt() {
    var userPrompt = document.getElementsByName("message")[0].value;
  
    var formData = new FormData();
    formData.append("message", userPrompt);
  
    var xhr = new XMLHttpRequest();
  
    xhr.open("POST", "/process/prompt/", true);
    xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
  
    // Define the callback function when the request completes
    xhr.onload = function () {
      if (xhr.status === 200) {
        console.log(xhr.responseText);
        // window.location.href = "/";
      } else {
        console.error("Error:", xhr.status);
      }
    };
  
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