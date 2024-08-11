from flask import Flask, jsonify

from flask_cors import CORS
app = Flask(__name__)

CORS(app)

@app.route('/hello', methods=['POST'])
def hello_world():
    ## include logic here to collect input and then run LLM API request
    return jsonify( {'hello': 'Hello, World!' })


if __name__ == '__main__':
    app.run(port=8080, debug=True)
