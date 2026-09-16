from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DATA_FILE = "data.txt"


@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify(status="error", message="Пустой текст"), 400

    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")

    return jsonify(status="ok", message="Данные сохранены")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)