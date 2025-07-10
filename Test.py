from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/run', methods=['GET'])
def run():
    return jsonify({
        "message": "Hello from Python on Render!",
        "status": "Success"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
