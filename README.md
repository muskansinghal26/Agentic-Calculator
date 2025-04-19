# Calculator Assistant with Langchain and FastAPI

## Project Description
This project is an interactive calculator assistant web application built using FastAPI and the Langchain ecosystem. It leverages Langchain Groq and Langgraph libraries to create a reactive state graph that processes user input messages and performs arithmetic operations such as addition, subtraction, multiplication, and division. The application serves a simple HTML interface where users can input expressions or commands, and receive calculated results or responses streamed from the assistant.

## Features
- Interactive web interface served via FastAPI
- Supports basic arithmetic operations: add, subtract, multiply, divide
- Uses Langchain Groq and Langgraph for reactive message processing
- Streamed responses for user inputs
- Easy to extend with additional tools or capabilities

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Clone the repository
```bash
git clone <repository-url>
cd Calculator
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Environment Variables
Create a `.env` file in the project root and add your API keys:
```
GROQ_API_KEY=your_groq_api_key_here
LANGSMITH_API_KEY=your_langsmith_api_key_here
```

## Usage

### Run the FastAPI server
```bash
uvicorn app:app --reload
```

### Access the web interface
Open your browser and navigate to:
```
http://127.0.0.1:8000/
```

Enter your input in the form and submit to get calculated results or responses.

### Commands
- Type arithmetic expressions or commands
- Type `quit` or `q` to exit the interaction

## Project Structure
- `app.py`: FastAPI application serving the HTML interface and handling calculation requests
- `index.html`: HTML form for user input
- `src/main.py`: Core logic integrating Langchain Groq, Langgraph, and arithmetic tools
- `src/utils.py`: Arithmetic functions (add, subtract, multiply, divide)
- `requirements.txt`: Python dependencies

## Dependencies
- FastAPI: Web framework for serving the app
- Uvicorn: ASGI server for running FastAPI
- Langchain, Langgraph: Libraries for building reactive language model applications
- python-multipart: For handling form data in FastAPI

## License
This project is licensed under the MIT License. See the LICENSE file for details.
