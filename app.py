from flask import Flask, jsonify, request

from llm import chatbot_response

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json['message']
    if not message:
        return jsonify({'message': 'Please provide a message!'})

    response = chatbot_response(message, "./test.txt")

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
