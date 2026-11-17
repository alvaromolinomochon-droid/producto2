from flask import Flask
import socket
app = Flask(__name__)
@app.route("/")
def home():
    return f"Hola v3 desde el pod: {socket.gethostname()}\n"
app.run(host="0.0.0.0", port=5000)
