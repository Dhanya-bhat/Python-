from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/run")
def run():
    return jsonify({"message": "Hello from Render!"})

