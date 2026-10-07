import os, uuid
from flask import Flask

app = Flask(__name__)

INSTANCE = uuid.uuid4().hex[:8]

@app.route("/")
def hello():
    message = os.environ.get("MESSAGE", "GitHub Auto Deploy")
    service = os.environ.get("K_SERVICE", "local")
    revision = os.environ.get("K_REVISION", "local")
    return (f"{message} - Hello from Cloud Run: service {service}, "
            f"revision {revision}, instance {INSTANCE}\n")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
