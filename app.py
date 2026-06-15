from flask import Flask, render_template, request, jsonify
from google import genai

app = Flask(__name__)
import os
client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
    )

chat_history = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    message = request.json["message"]

    chat_history.append(f"User: {message}")

    prompt = "\n".join(chat_history)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
You are StudyMate AI.

Help students with:
- Study planning
- Coding help
- Career guidance
- Exam preparation

Conversation:
{prompt}
"""
    )

    ai_reply = response.text

    chat_history.append(f"AI: {ai_reply}")

    return jsonify({
        "reply": ai_reply
    })

if __name__ == "__main__":
    app.run(debug=True)