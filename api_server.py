from flask import Flask, request
import requests

app = Flask(__name__)


@app.route("/api/embed", methods=["POST"])
def handle_embed():
    data = request.get_data()
    headers = dict(request.headers)
    try:
        response = requests.post(
            "http://localhost:8081/embeddings", data=data, headers=headers
        )
        return response.content, response.status_code
    except Exception as e:
        return str(e), 500


if __name__ == "__main__":
    app.run(host="localhost", port=8082)
