
async function sendMessage() {

    let message = document.getElementById("message").value;

    if (message.trim() === "") {
        return;
    }

    let chatBox = document.getElementById("chat-box");

    chatBox.innerHTML += "<p><b>You:</b> " + message + "</p>";

    document.getElementById("message").value = "";

    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: message
        })
    });

    const data = await response.json();

    chatBox.innerHTML += `
<div class="ai-msg">
    <div>
        <pre>${data.reply}</pre>
    </div>
</div>
`;

    chatBox.scrollTop = chatBox.scrollHeight;
}

document.getElementById("message").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

