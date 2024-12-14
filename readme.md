# CivicVoice.ai

CivicVoice.ai is a web application designed to assist users in drafting formal letters and providing information on child abuse and harassment. The application uses a generative AI model to generate content based on user input.

## Features

- Chat interface for user interaction
- Generates formal letters based on chat history
- Provides information on child abuse and harassment
- Responsive design for various screen sizes


## Installation

1. Clone the repository:
    ```sh
    git@github.com:aditya-8-88/GrievanceEase.git
    cd GrievanceEase
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv env
    source env/bin/activate
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirement.txt
    ```

4. Create a `.env` file and add your API key:
    ```env
    API_KEY=your_api_key_here
    ```

## Usage

1. Run the Flask application:
    ```sh
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. Interact with the chat interface to generate formal letters and get information on child abuse and harassment.

## Files

- `app.py`: Main Flask application file.
- `chat_history.json`: Stores the chat history between the user and the bot.
- `draft.py`: Script to generate a grievance letter based on chat history.
- `grievance_letter.txt`: Template for the grievance letter.
- `requirement.txt`: List of dependencies.
- `static/`: Directory containing static files (CSS, JavaScript, images).
- `templates/`: Directory containing HTML templates.

## License

This project is licensed under the MIT License.