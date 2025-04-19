from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from src.main import react_graph

app = FastAPI()

# Serve the HTML template
@app.get("/", response_class=HTMLResponse)
async def read_form():
    with open("index.html", "r") as file:
        return file.read()

@app.post("/calculate")
async def calculate(user_input: str = Form(...)):
    result = ""
    if user_input.lower() in ["quit", "q"]:
        return "Good Bye"
    for event in react_graph.stream({'messages': ("user", user_input)}):
        for value in event.values():
            last_message = value['messages'][-1]
            result = last_message.content  # Get the assistant's response
    return {"result": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
