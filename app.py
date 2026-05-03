from flask import Flask, jsonify, request
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import socket
import time
import uuid

app = Flask(__name__)

# simple request counter
REQUEST_COUNT = Counter("http_requests_total", "Total HTTP requests")

start_time = time.time()

# add request id and basic logging
@app.before_request
def before_request():
    request.id = str(uuid.uuid4())[:8]
    request.start_time = time.time()

@app.after_request
def after_request(response):
    duration = time.time() - request.start_time
    REQUEST_COUNT.inc()
    print(f"[{request.id}] {request.method} {request.path} {response.status_code} - {round(duration*1000,2)}ms")
    return response

# routes
@app.route("/")
def home():
    return jsonify({
        "message": "Hello from Sumit!",
        "hostname": socket.gethostname(),
        "uptime": round(time.time() - start_time, 2)
    })

@app.route("/health/live")
def live():
    return {"status": "alive"}, 200

@app.route("/health/ready")
def ready():
    return {"status": "ready"}, 200

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)