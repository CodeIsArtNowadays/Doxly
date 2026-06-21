console.log(5)
const websocket = new WebSocket("ws://127.0.0.1:8000/5/channel");

function sendMessage(event) {
  console.log('sm')
  var input = document.getElementById("chatInput");
  var message = input.value;
  websocket.send(JSON.stringify({
    type: "message",
    content: {
      message: message,
    },
  }));
  input.value = "";
  event.preventDefault();
}

function sendAuth(event) {
  console.log('sa')
  var input = document.getElementById("authInput");
  var token = input.value;
  websocket.send(JSON.stringify({
    type: "auth",
    content: {
      token: token,
    },
  }));
  input.value = "";
  event.preventDefault();
}

websocket.onmessage = function (event) {
  console.log(event.data);
};
