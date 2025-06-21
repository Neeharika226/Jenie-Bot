function sendMessage() {
    const userInput = document.getElementById("userInput").value;
    const chatBox = document.getElementById("chat-box");

    chatBox.innerHTML += `<div class="user"><b>You:</b> ${userInput}</div>`;

    eel.get_bot_response(userInput)(function(response) {
        chatBox.innerHTML += `<div class="bot"><b>Jenie:</b> ${response}</div>`;
        document.getElementById("userInput").value = "";
        chatBox.scrollTop = chatBox.scrollHeight;
    });
}
