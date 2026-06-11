from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import os

app = Flask(__name__)
metrics = PrometheusMetrics(app)

VERSION = os.getenv("VERSION", "v1")

@app.get("/")
def index():
    return jsonify({"service": "api", "version": VERSION})

@app.get("/health")
def health():
    return jsonify({"status": "ok", "version": VERSION})

@app.get("/fail")
def fail():
    return jsonify({"error": "forced failure", "version": VERSION}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
