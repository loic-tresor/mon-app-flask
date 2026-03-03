import os
from flask import Flask, jsonify
from azure.storage.blob import BlobServiceClient

app = Flask(__name__)

# Config Azure via variables d'environnement [cite: 107]
CONN_STR = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

@app.route('/healthz') # Liveness [cite: 39]
def healthz():
    return jsonify({"status": "healthy"}), 200

@app.route('/readyz') # Readiness [cite: 41]
def readyz():
    return jsonify({"status": "ready"}), 200

@app.route('/api/events') # API demandée [cite: 32]
def events():
    # Logique pour lire events.json dans le Blob Storage [cite: 29]
    return jsonify({"items": []})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)