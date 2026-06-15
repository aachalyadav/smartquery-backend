from fastapi import APIRouter
from app.models import Question
from app.services import generate_answer

router = APIRouter()

@router.get("/")
def home():
    return {"message": "Hello! SmartQuery API is running"}

@router.post("/ask")
def ask_question(data: Question):
    answer = generate_answer(data.user_question)

    return {
        "your_question": data.user_question,
        "answer": answer
    }