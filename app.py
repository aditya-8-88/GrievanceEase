import os
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
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('prompt')
    if not user_input:
        return jsonify({'response': 'No input provided.'})

    try:
        response = model.generate_content(user_input)
        print(response.text)
        chatbot_response = response.text.strip()
        return jsonify({'response': chatbot_response})
    except Exception as e:
        return jsonify({'response': f'Error: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)