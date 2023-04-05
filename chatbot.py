from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "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"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2000,
        temperature=0.3
    )
    return response.choices[0].text

@app.route('/api/chatbot', methods=['GET'])
def chatbot():
    message = request.args.get('message')
    response = generate_response(message)
    return jsonify({'response': response})