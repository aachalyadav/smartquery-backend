from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Question(BaseModel):
    user_question: str

@app.get("/")
def home():
    return {"message": "Hello! SmartQuery API is running"}

@app.post("/ask")
def ask_question(data: Question):
    question = data.user_question.lower()

    if "ai" in question:
        answer = "AI stands for Artificial Intelligence. It enables machines to think and learn."
    
    elif "python" in question:
        answer = "Python is a beginner-friendly programming language used in web development, AI, and data science."
    
    elif "hello" in question:
        answer = "Hello! Nice to meet you."
    
    else:
        answer = "Sorry, I don't know the answer yet."

    return {
        "your_question": data.user_question,
        "answer": answer
    }