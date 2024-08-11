from openaiclient import OpenAIClient
from openai import OpenAI
import json

from flask import Flask, jsonify, request

from flask_cors import CORS
app = Flask(__name__)

CORS(app)

#! need rename
#@app.route("/api/chat", methods=["POST"]) 
@app.route('/hello', methods=['POST'])
def query_to_bot():
    """makes basic chat completion call to LLM

    Returns:
        json: _description_
    """
    print("got a request", request)
    user_input_data = request.get_json()
    prompt=user_input_data['content']
    messages = [
            {
                "role": "user",
                "content": prompt,
            }
        ]
    completion = OpenAIClient().chat(messages, json_mode=True)
    response = json.loads(completion)
    print("#####  response ##### \n\n", response, "\n\n")
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
