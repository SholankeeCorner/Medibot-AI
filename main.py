from fastapi import FastAPI
from app.chatbot import get_response
from app.models import ChatRequest

app = FastAPI()

@app.post("/chat")
def chat(request: ChatRequest):
    reply = get_response(request.message)
    return {"response": reply}