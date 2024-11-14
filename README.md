# Personalized ChatGPT

This repository contains a chatbot application that leverages the Ollama Client to generate responses based on user input and file context.

## Setup

### 1. Create and Activate Python Virtual Environment

#### Windows

First, create a virtual environment to manage your dependencies:

```bash
python -m venv gpt-env
```

Activate the virtual environment:

```bash
.\gpt-env\Scripts\activate
```

#### Linux/macOS

First, create a virtual environment to manage your dependencies:

```bash
python3 -m venv gpt-env
```

Activate the virtual environment:

```bash
source gpt-env/bin/activate
```

### 2. Install Required Packages

Install the necessary packages using pip:

```bash
pip install ollama python-dotenv flask
```

### 3. Run the Application

Start the application by running:

```bash
python app.py
```

## Usage

### Endpoint

The application exposes a POST endpoint at `localhost:5000/chat`.

### Request Body

To interact with the chatbot, send a POST request to the endpoint with a JSON body containing your message. Optionally, you can also provide a file path for additional context.

Example request body:

```json
{
  "message": "When did hari john do Master of Science in Software Engineering?",
  "file_path": "path/to/context/file.txt" // Optional
}
```

### Response

The response will contain the chatbot's reply based on the provided message and context.

Example response:

```json
{
  "response": "Hari John completed his Master of Science in Software Engineering on May 2017."
}
```

## Example

Here is an example of how to use the endpoint with `curl`:

```bash
curl -X POST localhost:5000/chat -H "Content-Type: application/json" -d '{
  "message": "When did he do Master of Science in Software Engineering?",
  "file_path": "path/to/context/file.txt"
}'
```
