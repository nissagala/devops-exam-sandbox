import os, json, base64
from flask import Flask, request, jsonify
import redis

app = Flask(__name__)

REDIS_PASSWORD = os.environ["REDIS_PASSWORD"]

r = redis.Redis(host='localhost', port=6379, password=REDIS_PASSWORD)

@app.route('/process', methods=['POST'])
def process():
    try:
        payload = request.json['payload']
        data = base64.b64decode(payload)
        obj = json.loads(data)
        
        return jsonify({"status": "processed", "result": obj})
    except Exception:
        return jsonify({"error": "invalid payload"}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)