function handleInput(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}
function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    if (userInput.trim() === "") return;

    let chatBox = document.getElementById("chat-box");
    let userMessage = document.createElement("div");
    userMessage.classList.add("message", "user-message");
    userMessage.textContent = "You: " + userInput;
    chatBox.appendChild(userMessage);

    document.getElementById("user-input").value = "";

    chatBox.scrollTop = chatBox.scrollHeight; 

    fetch(`/get?msg=${encodeURIComponent(userInput)}`)
        .then(response => response.json())
        .then(data => {
            let botMessage = document.createElement("div");
            botMessage.classList.add("message", "bot-message");
            botMessage.textContent = "Chatbot: " + data.response;
            chatBox.appendChild(botMessage);

            chatBox.scrollTop = chatBox.scrollHeight;
        });
}
