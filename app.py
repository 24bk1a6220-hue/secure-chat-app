from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)

key = Fernet.generate_key()
cipher = Fernet(key)
messages = []

@app.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        msg = request.form["message"]
        encrypted = cipher.encrypt(msg.encode())
        messages.append(encrypted)

    decrypted_messages = [cipher.decrypt(m).decode() for m in messages]
    return render_template("chat.html", messages=decrypted_messages)

if __name__ == "__main__":
    app.run(debug=True)
