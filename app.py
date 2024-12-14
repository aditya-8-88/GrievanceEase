import os
import json
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Initialize the generative AI model
genai.configure(api_key=os.getenv('API_KEY'))

model = genai.GenerativeModel(
    model_name='gemini-1.5-pro',
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', json_file='chat_history.json')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('prompt')
    json_file = request.json.get('json_file')
    if not user_input:
        return jsonify({'response': 'No input provided.'})

    try:
        response = model.generate_content(user_input)
        # response.resolve()  # Ensure the response completes iteration

        chatbot_response = response.text.strip()

        # Append the chat messages to the JSON file
        chat_history = []
        if os.path.exists(json_file):
            with open(json_file, 'r') as file:
                chat_history = json.load(file)

        chat_history.append({'user': user_input, 'bot': chatbot_response})

        with open(json_file, 'w') as file:
            json.dump(chat_history, file, indent=4)

        return jsonify({'response': chatbot_response})
    except Exception as e:
        return jsonify({'response': f'Error: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)