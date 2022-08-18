from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

@app.route('/ping')
def ping():
    return jsonify({"message": "pong!!"})

if __name__ == '__main__':
    app.run(debug=True, port=4500)