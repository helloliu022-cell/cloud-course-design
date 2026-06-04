from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "cicd-demo")

@app.route("/")
def index():
    return jsonify({
        "service": "backend",
        "version": VERSION,
        "hostname": socket.gethostname()
    })

@app.route("/api/ping")
def ping():
    return jsonify({
        "status": "ok",
        "version": VERSION,
        "hostname": socket.gethostname()
    })

@app.route("/api/visit")
def visit():
    return jsonify({
        "message": "visit endpoint for cloud course design",
        "version": VERSION,
        "hostname": socket.gethostname()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
