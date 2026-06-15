from pydantic import BaseModel

class Question(BaseModel):
    user_question: str