import os
from flask import Flask, request, jsonify, render_template
from google import genai
import markdown
import bleach

app = Flask(__name__, template_folder="../frontend")
app.secret_key = os.environ.get("SECRET_KEY", "hibi-secret-key")


# Markdown → Safe HTML
def md_to_html(text):
    html = markdown.markdown(
        text,
        extensions=[
            "extra",        # tables, lists
            "nl2br",        # line breaks
            "sane_lists"    # better lists
        ]
    )

    # Allow only safe tags
    allowed_tags = [
        "p", "strong", "em", "ul", "ol", "li",
        "br", "a", "h1", "h2", "h3", "h4"
    ]

    return bleach.clean(html, tags=allowed_tags, strip=True)


def get_kb():
    return os.environ.get("HIBA_DETAILS", "")


def get_system_prompt():
    kb = get_kb()
    return f"""
You are Hiba's personal assistant. Your job is to provide answers to questions asked by the user.

Give important information in **bold**.
Use proper bullet points and lists where needed.
Keep answers clean and readable.

If there are any questions outside the knowledge base, say you do not have that information.

Only refer to the knowledge base below and provide responses based on it.

{kb}
"""


def get_gemini_client():
    api_key = os.environ.get("GEMINI_API_KEY")
    return genai.Client(api_key=api_key)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    history = data.get("history", [])

    try:
        client = get_gemini_client()

        chat_session = client.chats.create(
            model="gemini-2.5-flash",
            config={"system_instruction": get_system_prompt()}
        )

        # Maintain history
        for msg in history[:-1]:
            if msg["role"] == "user":
                chat_session.send_message(msg["content"])

        response = chat_session.send_message(user_message)

        # Convert Markdown → HTML
        reply_html = md_to_html(response.text)

        return jsonify({"reply": reply_html, "status": "ok"})

    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}", "status": "error"})


if __name__ == "__main__":
    app.run(debug=True)
