import os

from dotenv import load_dotenv
from ollama import Client

# Load environment variables from .env file
load_dotenv()

# Initialize the Ollama Client
client = Client(host="http://localhost:11434")

def chatbot_response(message: str, file_path: str = None) -> str:
    try:
        # Initialize file_content
        file_content = None

        # If a file path is provided, read its content
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()

        # Prepare messages for the chatbot
        messages = [{'role': 'user', 'content': message}]
        
        # If file_content is available, add it as context for the model
        if file_content:
            # Add the file content as context in the system message
            # This gives the model information about the content of the file
            messages.insert(0, {'role': 'system', 'content': f"Context: {file_content}"})

        print(messages)  # For debugging, to see how messages look

        # Now, proceed with generating the chatbot response
        chat_response = client.chat(model="llama3.2:latest", messages=messages)

        # Return the chatbot's response
        return chat_response['message']['content']

    except Exception as e:
        return f"Error: {str(e)}"

