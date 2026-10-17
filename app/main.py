from flask import Flask, jsonify
from datetime import datetime, timezone

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify({
        "application": "Homelab Status",
        "message": "Welcome to my DevOps project!",
        "status": "running"
    })


@app.get("/health")
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
