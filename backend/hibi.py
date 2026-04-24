import os
import re
from flask import Flask, request, jsonify, render_template
from google import genai

app = Flask(__name__, template_folder="../frontend")
app.secret_key = os.environ.get("SECRET_KEY", "hibi-secret-key")


def md_to_html(text):
    lines = text.split('\n')
    html_lines = []
    in_ul = False
    in_ol = False

    for line in lines:
        # Bold
        line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)

        ol_match     = re.match(r'^\d+\.\s+(.*)', line)
        nested_match = re.match(r'^\s{2,}[\*\-]\s+(.*)', line)
        ul_match     = re.match(r'^[\*\-]\s+(.*)', line)

        if ol_match:
            if in_ul:
                html_lines.append('</ul>')
                in_ul = False
            if not in_ol:
                html_lines.append('<ol>')
                in_ol = True
            html_lines.append(f'<li>{ol_match.group(1)}</li>')

        elif nested_match:
            html_lines.append(f'<li class="nested">{nested_match.group(1)}</li>')

        elif ul_match:
            if in_ol:
                html_lines.append('</ol>')
                in_ol = False
            if not in_ul:
                html_lines.append('<ul>')
                in_ul = True
            html_lines.append(f'<li>{ul_match.group(1)}</li>')

        else:
            if in_ol:
                html_lines.append('</ol>')
                in_ol = False
            if in_ul:
                html_lines.append('</ul>')
                in_ul = False
            if line.strip():
                html_lines.append(f'<p>{line}</p>')

    if in_ol:
        html_lines.append('</ol>')
    if in_ul:
        html_lines.append('</ul>')

    return '\n'.join(html_lines)


def get_kb():
    return os.environ.get("HIBA_DETAILS", "")


def get_system_prompt():
    kb = get_kb()
    return f"""
You are Hiba's personal assistant. Your job is to provide answers to questions asked by the user.
Give important information in **bold**.
Answer in a polite and friendly tone.
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

        for msg in history[:-1]:
            if msg["role"] == "user":
                chat_session.send_message(msg["content"])

        response = chat_session.send_message(user_message)
        reply = md_to_html(response.text)
        return jsonify({"reply": reply, "status": "ok"})

    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}", "status": "error"})


if __name__ == "__main__":
    app.run(debug=True)
