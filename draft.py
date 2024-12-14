import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Initialize the generative AI model
genai.configure(api_key=os.getenv('API_KEY'))

model = genai.GenerativeModel(
    model_name='gemini-1.5-pro',
)

def generate_grievance_letter(json_file):
    if not os.path.exists(json_file):
        print(f"File {json_file} does not exist.")
        return

    with open(json_file, 'r') as file:
        chat_history = json.load(file)

    if not chat_history:
        print("No chat history found in the JSON file.")
        return

    # Combine all chat messages into a single string
    conversation_text = "\n".join([f"User: {entry['user']}\nBot: {entry['bot']}" for entry in chat_history])

    try:
        # Generate the formal letter using the model
        response = model.generate_content(conversation_text)
        grievance_letter = response.text.strip()

        # Save the generated letter to a new file
        output_file = 'grievance_letter.txt'
        with open(output_file, 'w') as file:
            file.write(grievance_letter)

        print(f"Grievance letter generated and saved to {output_file}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    json_file = 'chat_history.json'
    generate_grievance_letter(json_file)